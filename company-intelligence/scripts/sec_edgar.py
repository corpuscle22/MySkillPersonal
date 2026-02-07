#!/usr/bin/env python3
"""
SEC EDGAR Filing Fetcher

Fetches company filings from the SEC EDGAR database.
No API key required - this is a free public API.

Usage:
    python sec_edgar.py --ticker AAPL --filing-type 10-K
    python sec_edgar.py --ticker TSLA --filing-type 10-Q --count 5
    python sec_edgar.py --cik 0000320193 --filing-type 8-K
"""

import argparse
import json
import re
import sys
from datetime import datetime
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError


# SEC requires a User-Agent header
USER_AGENT = "CompanyIntelligence research@example.com"
SEC_BASE_URL = "https://data.sec.gov"
SEC_SEARCH_URL = "https://efts.sec.gov/LATEST/search-index"


def get_cik_from_ticker(ticker: str) -> str:
    """Convert stock ticker to SEC CIK number."""
    url = f"{SEC_BASE_URL}/submissions/CIK{ticker.upper()}.json"
    
    # First try direct lookup
    try:
        req = Request(url, headers={"User-Agent": USER_AGENT})
        with urlopen(req) as response:
            data = json.loads(response.read())
            return data.get('cik', '').zfill(10)
    except HTTPError:
        pass
    
    # Try company tickers mapping
    try:
        tickers_url = "https://www.sec.gov/files/company_tickers.json"
        req = Request(tickers_url, headers={"User-Agent": USER_AGENT})
        with urlopen(req) as response:
            tickers_data = json.loads(response.read())
            for entry in tickers_data.values():
                if entry.get('ticker', '').upper() == ticker.upper():
                    return str(entry.get('cik_str', '')).zfill(10)
    except Exception:
        pass
    
    return None


def get_company_filings(cik: str, filing_type: str = None, count: int = 10) -> dict:
    """Fetch company filing history from SEC EDGAR."""
    cik = cik.zfill(10)
    url = f"{SEC_BASE_URL}/submissions/CIK{cik}.json"
    
    try:
        req = Request(url, headers={"User-Agent": USER_AGENT})
        with urlopen(req) as response:
            data = json.loads(response.read())
    except HTTPError as e:
        print(f"Error fetching data: {e}")
        return None
    except URLError as e:
        print(f"Network error: {e}")
        return None
    
    company_info = {
        'name': data.get('name', 'Unknown'),
        'cik': cik,
        'sic': data.get('sic', ''),
        'sic_description': data.get('sicDescription', ''),
        'state': data.get('stateOfIncorporation', ''),
        'fiscal_year_end': data.get('fiscalYearEnd', ''),
        'filings': []
    }
    
    # Get recent filings
    recent = data.get('filings', {}).get('recent', {})
    if not recent:
        return company_info
    
    forms = recent.get('form', [])
    dates = recent.get('filingDate', [])
    accessions = recent.get('accessionNumber', [])
    primary_docs = recent.get('primaryDocument', [])
    descriptions = recent.get('primaryDocDescription', [])
    
    for i in range(min(len(forms), 100)):  # Limit to 100 filings
        form = forms[i]
        
        # Filter by filing type if specified
        if filing_type and form.upper() != filing_type.upper():
            continue
        
        filing = {
            'form': form,
            'date': dates[i] if i < len(dates) else '',
            'accession': accessions[i] if i < len(accessions) else '',
            'document': primary_docs[i] if i < len(primary_docs) else '',
            'description': descriptions[i] if i < len(descriptions) else ''
        }
        
        # Build document URL
        if filing['accession'] and filing['document']:
            acc_no = filing['accession'].replace('-', '')
            filing['url'] = f"{SEC_BASE_URL}/Archives/edgar/data/{cik}/{acc_no}/{filing['document']}"
        
        company_info['filings'].append(filing)
        
        if len(company_info['filings']) >= count:
            break
    
    return company_info


def get_filing_content(url: str, max_chars: int = 50000) -> str:
    """Fetch and extract text content from a filing."""
    try:
        req = Request(url, headers={"User-Agent": USER_AGENT})
        with urlopen(req) as response:
            content = response.read().decode('utf-8', errors='ignore')
        
        # Remove HTML tags for basic text extraction
        text = re.sub(r'<[^>]+>', ' ', content)
        text = re.sub(r'\s+', ' ', text)
        
        return text[:max_chars]
    except Exception as e:
        return f"Error fetching content: {e}"


def format_output(company_info: dict) -> str:
    """Format company filing information for display."""
    output = []
    output.append("=" * 70)
    output.append(f"SEC EDGAR FILINGS: {company_info['name']}")
    output.append("=" * 70)
    output.append(f"CIK: {company_info['cik']}")
    output.append(f"Industry: {company_info['sic_description']} (SIC: {company_info['sic']})")
    output.append(f"State of Incorporation: {company_info['state']}")
    output.append(f"Fiscal Year End: {company_info['fiscal_year_end']}")
    output.append("")
    
    if company_info['filings']:
        output.append(f"Found {len(company_info['filings'])} filing(s):")
        output.append("-" * 70)
        
        for filing in company_info['filings']:
            output.append(f"Form: {filing['form']}")
            output.append(f"Date: {filing['date']}")
            output.append(f"Description: {filing['description']}")
            output.append(f"URL: {filing.get('url', 'N/A')}")
            output.append("-" * 70)
    else:
        output.append("No filings found matching criteria.")
    
    return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(
        description="Fetch SEC EDGAR filings for a company",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python sec_edgar.py --ticker AAPL --filing-type 10-K
    python sec_edgar.py --ticker TSLA --filing-type 10-Q --count 5
    python sec_edgar.py --cik 0000320193 --filing-type 8-K

Common filing types:
    10-K    Annual report
    10-Q    Quarterly report
    8-K     Current report (material events)
    DEF 14A Proxy statement
    S-1     Registration statement (IPO)
        """
    )
    
    parser.add_argument('--ticker', '-t', help='Stock ticker symbol (e.g., AAPL)')
    parser.add_argument('--cik', '-c', help='SEC CIK number (e.g., 0000320193)')
    parser.add_argument('--filing-type', '-f', help='Filing type filter (e.g., 10-K, 10-Q, 8-K)')
    parser.add_argument('--count', '-n', type=int, default=10, help='Number of filings to return (default: 10)')
    parser.add_argument('--json', '-j', action='store_true', help='Output as JSON')
    parser.add_argument('--fetch-content', action='store_true', help='Fetch content of first filing')
    
    args = parser.parse_args()
    
    if not args.ticker and not args.cik:
        parser.error("Either --ticker or --cik is required")
    
    # Get CIK if ticker provided
    if args.ticker:
        print(f"Looking up ticker: {args.ticker}...")
        cik = get_cik_from_ticker(args.ticker)
        if not cik:
            print(f"Error: Could not find CIK for ticker '{args.ticker}'")
            sys.exit(1)
        print(f"Found CIK: {cik}")
    else:
        cik = args.cik
    
    # Fetch filings
    print(f"Fetching filings...")
    company_info = get_company_filings(cik, args.filing_type, args.count)
    
    if not company_info:
        print("Error: Could not fetch company information")
        sys.exit(1)
    
    # Output results
    if args.json:
        print(json.dumps(company_info, indent=2))
    else:
        print(format_output(company_info))
    
    # Optionally fetch content of first filing
    if args.fetch_content and company_info['filings']:
        first_filing = company_info['filings'][0]
        if 'url' in first_filing:
            print("\n" + "=" * 70)
            print(f"FILING CONTENT PREVIEW: {first_filing['form']} ({first_filing['date']})")
            print("=" * 70)
            content = get_filing_content(first_filing['url'])
            print(content[:5000] + "\n...[truncated]" if len(content) > 5000 else content)


if __name__ == "__main__":
    main()
