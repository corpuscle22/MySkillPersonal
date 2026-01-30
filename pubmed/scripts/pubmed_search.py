#!/usr/bin/env python3
"""
PubMed Research Tool - Search and retrieve medical literature from PubMed/NCBI.
Prioritizes high-quality evidence: meta-analyses, systematic reviews, RCTs.

Usage:
    python pubmed_search.py "your medical question" [--max N] [--years N]

Environment:
    NCBI_API_KEY - Optional API key for faster queries (10 req/s vs 3 req/s)
"""

import argparse
import json
import os
import re
import sys
import time
from urllib.parse import quote_plus
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from xml.etree import ElementTree as ET
import urllib.request

# NCBI E-utilities base URL
BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

# Get API key from environment or use user-provided default
# User provided key: baff0ef3404df1265a893b3cf826c7000c08
API_KEY = os.environ.get("NCBI_API_KEY") or "baff0ef3404df1265a893b3cf826c7000c08"
# User provided email: drprasad30@gmail.com
EMAIL = "drprasad30@gmail.com"


def build_url(endpoint: str, params: dict) -> str:
    """Build E-utilities URL with parameters."""
    if API_KEY:
        params["api_key"] = API_KEY
    if EMAIL:
        params["email"] = EMAIL
    param_str = "&".join(f"{k}={quote_plus(str(v))}" for k, v in params.items())
    return f"{BASE_URL}/{endpoint}?{param_str}"


def fetch_url(url: str, retries: int = 3) -> str:
    """Fetch URL content with retries."""
    for attempt in range(retries):
        try:
            req = Request(url, headers={"User-Agent": "PubMedResearchTool/1.0"})
            with urlopen(req, timeout=30) as response:
                return response.read().decode("utf-8")
        except (HTTPError, URLError) as e:
            if attempt < retries - 1:
                time.sleep(1)
                continue
            raise RuntimeError(f"Failed to fetch {url}: {e}")
    return ""


def search_pubmed(query: str, max_results: int = 50, years: int = 10) -> list:
    """
    Search PubMed with filters for high-quality evidence.
    Returns list of PMIDs.
    """
    # Build a query that prioritizes high-quality evidence
    # Add filters for article types we want
    enhanced_query = f"({query}) AND (english[Language])"
    
    params = {
        "db": "pubmed",
        "term": enhanced_query,
        "retmax": max_results,
        "retmode": "json",
        "sort": "relevance",
        "usehistory": "y"
    }
    
    # Add date filter using reldate (days)
    if years > 0:
        params["reldate"] = years * 365
        params["datetype"] = "pdat"  # Publication date
    
    url = build_url("esearch.fcgi", params)
    response = fetch_url(url)
    data = json.loads(response)
    
    if "esearchresult" in data and "idlist" in data["esearchresult"]:
        return data["esearchresult"]["idlist"]
    return []


def fetch_article_details(pmids: list) -> list:
    """Fetch detailed article information for given PMIDs."""
    if not pmids:
        return []
    
    # Fetch in batches to avoid URL length limits
    batch_size = 20
    all_articles = []
    
    for i in range(0, len(pmids), batch_size):
        batch = pmids[i:i+batch_size]
        params = {
            "db": "pubmed",
            "id": ",".join(batch),
            "retmode": "xml"
        }
        
        url = build_url("efetch.fcgi", params)
        xml_data = fetch_url(url)
        articles = parse_pubmed_xml(xml_data)
        all_articles.extend(articles)
        
        # Rate limiting (respect API limits)
        if not API_KEY:
            time.sleep(0.4)  # ~3 requests per second without key
        else:
            time.sleep(0.15)  # ~10 requests per second with key
    
    # 2nd pass: Fetch full text for articles with PMCID
    articles_with_pmc = [a for a in all_articles if a.get("pmcid")]
    if articles_with_pmc:
        print(f"   📥 Fetching full text for {len(articles_with_pmc)} PMC articles...", file=sys.stderr)
        for article in articles_with_pmc:
            full_text = fetch_pmc_fulltext(article["pmcid"])
            if full_text:
                article["full_text"] = full_text
                article["has_full_text"] = True
            
            # Rate limit for PMC fetching
            if not API_KEY:
                time.sleep(0.4)
            else:
                time.sleep(0.15)

    return all_articles


def fetch_pmc_fulltext(pmcid: str) -> str:
    """Fetch full text from PMC using E-utilities."""
    try:
        params = {
            "db": "pmc",
            "id": pmcid,
            "retmode": "xml"  # XML is easier to parse for structure
        }
        url = build_url("efetch.fcgi", params)
        xml_data = fetch_url(url)
        
        # Simple extraction of body text
        root = ET.fromstring(xml_data)
        body = root.find(".//body")
        if body is not None:
            # Extract all text from body
            return "".join(body.itertext())
            
        return ""
    except Exception as e:
        # Silently fail for full text fetch to avoid breaking the main flow
        return ""


def parse_pubmed_xml(xml_data: str) -> list:
    """Parse PubMed XML response into article dictionaries."""
    articles = []
    try:
        root = ET.fromstring(xml_data)
        for article in root.findall(".//PubmedArticle"):
            parsed = parse_article(article)
            if parsed:
                articles.append(parsed)
    except ET.ParseError:
        pass
    return articles


def parse_article(article_elem) -> dict:
    """Parse a single PubmedArticle element."""
    try:
        medline = article_elem.find(".//MedlineCitation")
        article = medline.find(".//Article")
        
        # Get PMID
        pmid = medline.find("PMID").text if medline.find("PMID") is not None else ""
        
        # Get title
        title_elem = article.find(".//ArticleTitle")
        title = "".join(title_elem.itertext()) if title_elem is not None else "No title"
        
        # Get abstract
        abstract_parts = []
        abstract_elem = article.find(".//Abstract")
        if abstract_elem is not None:
            for text in abstract_elem.findall(".//AbstractText"):
                label = text.get("Label", "")
                content = "".join(text.itertext())
                if label:
                    abstract_parts.append(f"**{label}**: {content}")
                else:
                    abstract_parts.append(content)
        abstract = " ".join(abstract_parts) if abstract_parts else "No abstract available."
        
        # Get authors
        authors = []
        author_list = article.find(".//AuthorList")
        if author_list is not None:
            for author in author_list.findall("Author"):
                last = author.find("LastName")
                fore = author.find("ForeName")
                if last is not None:
                    name = last.text
                    if fore is not None:
                        name = f"{last.text} {fore.text[0]}"
                    authors.append(name)
        
        # Get journal info
        journal = article.find(".//Journal/Title")
        journal_name = journal.text if journal is not None else "Unknown Journal"
        
        # Get publication date
        pub_date = article.find(".//PubDate")
        year = ""
        if pub_date is not None:
            year_elem = pub_date.find("Year")
            if year_elem is not None:
                year = year_elem.text
        
        # Get publication type(s)
        pub_types = []
        for pt in article.findall(".//PublicationTypeList/PublicationType"):
            pub_types.append(pt.text)
        
        # Get DOI and PMCID
        doi = ""
        pmcid = ""
        
        # Check ArticleIdList
        id_list = medline.find("ArticleIdList") # Usually in PubmedData or MedlineCitation... actually usually PubmedData
        # Let's check PubmedData which is a sibling of MedlineCitation in PubmedArticle
        # But EFetch XML structure can vary. Let's look for it relative to PubmedArticle root
        # PubmedArticle/PubmedData/ArticleIdList/ArticleId
        
        pubmed_data = article_elem.find("PubmedData")
        if pubmed_data is not None:
             id_list = pubmed_data.find("ArticleIdList")
             if id_list is not None:
                for id_node in id_list.findall("ArticleId"):
                    id_type = id_node.get("IdType")
                    if id_type == "doi":
                        doi = id_node.text
                    elif id_type == "pmc":
                        pmcid = id_node.text
        
        # Calculate evidence score based on publication type
        evidence_score = calculate_evidence_score(pub_types, title, abstract)
        
        return {
            "pmid": pmid,
            "pmcid": pmcid,
            "doi": doi,
            "title": title,
            "abstract": abstract,
            "authors": authors[:3],  # First 3 authors
            "journal": journal_name,
            "year": year,
            "pub_types": pub_types,
            "evidence_score": evidence_score,
            "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
            "has_full_text": False
        }
    except Exception:
        return None


def calculate_evidence_score(pub_types: list, title: str, abstract: str) -> int:
    """
    Calculate evidence quality score (1-10).
    Higher score = higher quality evidence.
    """
    score = 5  # Base score
    
    # Check publication types (highest weight)
    pub_types_lower = [pt.lower() for pt in pub_types]
    title_lower = title.lower()
    abstract_lower = abstract.lower()
    
    # Meta-analysis and systematic reviews (highest quality)
    if "meta-analysis" in pub_types_lower or "meta-analysis" in title_lower:
        score = 10
    elif "systematic review" in pub_types_lower or "systematic review" in title_lower:
        score = 9
    # Randomized controlled trials
    elif "randomized controlled trial" in pub_types_lower or "rct" in title_lower:
        score = 8
    # Clinical trials
    elif "clinical trial" in pub_types_lower:
        score = 7
    # Practice guidelines
    elif "practice guideline" in pub_types_lower or "guideline" in pub_types_lower:
        score = 8
    # Cohort/observational studies
    elif any(term in abstract_lower for term in ["cohort study", "prospective study", "longitudinal study"]):
        score = 6
    # Case-control studies
    elif "case-control" in abstract_lower:
        score = 5
    # Case reports/series (lower quality)
    elif "case report" in pub_types_lower or "case series" in abstract_lower:
        score = 3
    # Reviews (non-systematic)
    elif "review" in pub_types_lower and "systematic" not in str(pub_types_lower):
        score = 4
    
    return score


def format_citation(article: dict, index: int) -> str:
    """Format a single citation."""
    authors_str = ", ".join(article["authors"])
    if len(article["authors"]) > 0:
        authors_str += " et al." if len(article["authors"]) >= 3 else ""
    
    evidence_labels = {
        10: "⭐ META-ANALYSIS",
        9: "⭐ SYSTEMATIC REVIEW",
        8: "⭐ RCT/GUIDELINE",
        7: "CLINICAL TRIAL",
        6: "COHORT STUDY",
        5: "OBSERVATIONAL",
        4: "REVIEW",
        3: "CASE REPORT",
    }
    evidence_label = evidence_labels.get(article["evidence_score"], "")
    
    return f"""
[{index}] {article["title"]}
    {authors_str}. {article["journal"]}. {article["year"]}
    Evidence: {evidence_label} (Score: {article["evidence_score"]}/10)
    PMID: {article["pmid"]} | {article["url"]}
    {f"PMCID: {article['pmcid']} (Full Text Available)" if article.get('pmcid') else ""}
    {f"DOI: {article['doi']}" if article.get('doi') else ""}"""


def format_summary(articles: list, query: str) -> str:
    """Generate a summary formatted for the AI to synthesize."""
    if not articles:
        return f"No articles found for query: {query}"
    
    # Sort by evidence score (highest first)
    sorted_articles = sorted(articles, key=lambda x: x["evidence_score"], reverse=True)
    
    output = []
    output.append("=" * 80)
    output.append(f"PUBMED RESEARCH RESULTS: {query}")
    output.append(f"Total articles found: {len(sorted_articles)}")
    output.append("=" * 80)
    
    # Count by evidence level
    high_quality = sum(1 for a in sorted_articles if a["evidence_score"] >= 8)
    output.append(f"\n📊 Evidence Quality Summary:")
    output.append(f"   High quality (Meta-analyses, SRs, RCTs, Guidelines): {high_quality}")
    output.append(f"   Medium quality (Cohort, Observational): {sum(1 for a in sorted_articles if 5 <= a['evidence_score'] < 8)}")
    output.append(f"   Lower quality (Case reports, Reviews): {sum(1 for a in sorted_articles if a['evidence_score'] < 5)}")
    
    # Show citations with abstracts
    output.append("\n" + "=" * 80)
    output.append("ARTICLES (sorted by evidence quality)")
    output.append("=" * 80)
    
    for i, article in enumerate(sorted_articles, 1):
        output.append(format_citation(article, i))
        output.append(f"\n    ABSTRACT: {article['abstract'][:800]}...")
        output.append("-" * 40)
        
        if article.get("has_full_text"):
             output.append(f"    📄 FULL TEXT EXCERPT (PMC):")
             output.append(f"    {article['full_text'][:2000]}...") # First 2000 chars of full text
             output.append(f"    [...full text continues...]")
             output.append("-" * 40)
    
    # Machine-readable JSON for AI processing
    output.append("\n" + "=" * 80)
    output.append("STRUCTURED DATA (JSON)")
    output.append("=" * 80)
    
    # Create simplified JSON for AI consumption
    simplified = []
    for article in sorted_articles:
        simplified.append({
            "pmid": article["pmid"],
            "title": article["title"],
            "year": article["year"],
            "evidence_score": article["evidence_score"],
            "pub_types": article["pub_types"],
            "abstract_excerpt": article["abstract"][:500],
            "url": article["url"]
        })
    
    output.append(json.dumps(simplified, indent=2))
    
    return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(
        description="Search PubMed for medical literature, prioritizing high-quality evidence."
    )
    parser.add_argument("query", help="Medical question or topic to research")
    parser.add_argument("--max", type=int, default=30, help="Maximum number of results (default: 30)")
    parser.add_argument("--years", type=int, default=10, help="Limit to last N years (default: 10, 0 for all time)")
    parser.add_argument("--json", action="store_true", help="Output JSON only")
    
    args = parser.parse_args()
    
    print(f"🔍 Searching PubMed for: {args.query}", file=sys.stderr)
    print(f"   Max results: {args.max}, Years: {args.years}", file=sys.stderr)
    
    if API_KEY:
        print("   ✓ Using API key for faster queries", file=sys.stderr)
    else:
        print("   ⚠ No API key (set NCBI_API_KEY for 10 req/s vs 3 req/s)", file=sys.stderr)
    
    # Search PubMed
    pmids = search_pubmed(args.query, max_results=args.max, years=args.years)
    
    if not pmids:
        print(f"\n❌ No results found for: {args.query}")
        sys.exit(1)
    
    print(f"   Found {len(pmids)} articles, fetching details...", file=sys.stderr)
    
    # Fetch article details
    articles = fetch_article_details(pmids)
    
    # Output results
    if args.json:
        print(json.dumps(articles, indent=2))
    else:
        print(format_summary(articles, args.query))


if __name__ == "__main__":
    main()
