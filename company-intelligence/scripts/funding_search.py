#!/usr/bin/env python3
"""
Funding Search

Searches for company funding information using multiple sources.
For private companies, uses web-based research patterns.

Usage:
    python funding_search.py --company "OpenAI"
    python funding_search.py --company "Stripe" --detailed
    python funding_search.py --ticker TSLA
"""

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from urllib.parse import quote_plus


# Configuration
CONFIG_FILE = Path.home() / ".company-intelligence" / "config.json"


def load_config():
    """Load API configuration."""
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {}


def fetch_json(url: str, headers: dict = None) -> dict:
    """Fetch JSON data from URL."""
    if headers is None:
        headers = {"User-Agent": "CompanyIntelligence/1.0"}
    try:
        req = Request(url, headers=headers)
        with urlopen(req, timeout=30) as response:
            return json.loads(response.read())
    except (HTTPError, URLError, json.JSONDecodeError) as e:
        return {'error': str(e)}


def get_sec_ipo_info(ticker: str) -> dict:
    """Get IPO information from SEC for public companies."""
    from sec_edgar import get_cik_from_ticker, get_company_filings
    
    cik = get_cik_from_ticker(ticker)
    if not cik:
        return None
    
    filings = get_company_filings(cik, 'S-1', 5)
    return filings


def generate_search_queries(company_name: str) -> list:
    """Generate search queries for funding information."""
    queries = [
        f'"{company_name}" funding round',
        f'"{company_name}" series A OR series B OR series C',
        f'"{company_name}" raises OR raised million OR billion',
        f'"{company_name}" valuation investors',
        f'"{company_name}" venture capital investment',
        f'site:crunchbase.com "{company_name}"',
        f'site:pitchbook.com "{company_name}"',
        f'site:techcrunch.com "{company_name}" funding',
    ]
    return queries


def parse_funding_amount(text: str) -> dict:
    """Parse funding amount from text."""
    patterns = [
        r'\$(\d+(?:\.\d+)?)\s*(billion|B)\b',
        r'\$(\d+(?:\.\d+)?)\s*(million|M)\b',
        r'raised\s+\$(\d+(?:\.\d+)?)\s*(billion|million|B|M)',
        r'\$(\d+(?:\.\d+)?)(B|M)\s+(?:round|funding|investment)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            amount = float(match.group(1))
            unit = match.group(2).upper()
            if unit in ['BILLION', 'B']:
                return {'amount': amount * 1e9, 'display': f'${amount}B'}
            else:
                return {'amount': amount * 1e6, 'display': f'${amount}M'}
    
    return None


def find_investors(text: str) -> list:
    """Extract investor names from text."""
    # Common VC patterns
    vc_patterns = [
        r"led by\s+([A-Z][A-Za-z\s&]+?)(?:,|\.|and|with)",
        r"from\s+([A-Z][A-Za-z\s&,]+?)(?:\.|participated)",
        r"investors?\s+(?:include|including)\s+([A-Z][A-Za-z\s&,]+?)(?:\.|and)",
    ]
    
    investors = set()
    for pattern in vc_patterns:
        matches = re.findall(pattern, text)
        for match in matches:
            # Clean up and split
            names = re.split(r',\s*|\s+and\s+', match)
            for name in names:
                name = name.strip()
                if len(name) > 3 and len(name) < 50:
                    investors.add(name)
    
    return list(investors)


def display_funding_guidance(company_name: str):
    """Display guidance for researching funding information."""
    print("\n" + "=" * 70)
    print(f"FUNDING RESEARCH GUIDANCE: {company_name}")
    print("=" * 70)
    
    print("\n## Recommended Research Steps:")
    print("\n### 1. Crunchbase (Primary Source)")
    print(f"   Visit: https://www.crunchbase.com/organization/{company_name.lower().replace(' ', '-')}")
    print("   Look for: Funding Rounds, Total Funding, Lead Investors")
    
    print("\n### 2. PitchBook (Detailed Data)")
    print(f"   Search: https://pitchbook.com/")
    print("   Provides: Detailed funding history, valuations, cap table")
    
    print("\n### 3. News Sources")
    queries = generate_search_queries(company_name)
    print("   Recommended searches:")
    for i, query in enumerate(queries[:4], 1):
        print(f"   {i}. {query}")
    
    print("\n### 4. Company Website")
    print("   Check: Press releases, About page, Newsroom")
    print("   Often announces major funding rounds")
    
    print("\n### 5. SEC Filings (if public)")
    print("   Check S-1 for IPO history, 10-K for investor info")
    
    print("\n## Key Data Points to Gather:")
    print("""
    | Data Point        | Source Priority                    |
    |-------------------|-----------------------------------|
    | Total Funding     | Crunchbase, PitchBook             |
    | Funding Rounds    | Crunchbase, News                  |
    | Lead Investors    | Crunchbase, PitchBook             |
    | Valuation         | PitchBook (often paywalled)       |
    | Round Dates       | Crunchbase, News articles         |
    """)


def display_public_company_funding(company_info: dict):
    """Display funding info for public companies."""
    print("\n" + "=" * 70)
    print("PUBLIC COMPANY IPO INFORMATION")
    print("=" * 70)
    
    if company_info and company_info.get('filings'):
        for filing in company_info['filings']:
            if 'S-1' in filing['form']:
                print(f"\nIPO Registration: {filing['form']}")
                print(f"Filing Date: {filing['date']}")
                print(f"Document: {filing.get('url', 'N/A')}")
    else:
        print("\nNo S-1 filing found (may not have IPO'd through traditional registration)")


def create_funding_template(company_name: str) -> str:
    """Create a template for funding information."""
    template = f"""
## Funding History: {company_name}

### Total Funding Raised: $[AMOUNT]
### Latest Valuation: $[AMOUNT] (as of [DATE])
### Status: [Private/Public]

### Funding Rounds

| Date | Round | Amount | Lead Investor(s) | Valuation |
|------|-------|--------|------------------|-----------|
| YYYY-MM | Seed | $XM | | |
| YYYY-MM | Series A | $XM | | |
| YYYY-MM | Series B | $XM | | |
| YYYY-MM | Series C | $XM | | |

### Notable Investors
- [Investor 1] - [Background/portfolio companies]
- [Investor 2] - [Background/portfolio companies]

### Key Funding Details
- [Notable terms, strategic investors, etc.]

### Sources
- [ ] Crunchbase profile checked
- [ ] PitchBook data reviewed
- [ ] News articles searched
- [ ] Company press releases reviewed
"""
    return template


def main():
    parser = argparse.ArgumentParser(
        description="Search for company funding information",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python funding_search.py --company "OpenAI"
    python funding_search.py --company "Stripe" --template
    python funding_search.py --ticker TSLA
        """
    )
    
    parser.add_argument('--company', '-c', help='Company name to research')
    parser.add_argument('--ticker', '-t', help='Stock ticker (for public companies)')
    parser.add_argument('--template', action='store_true', help='Output a template for gathering funding info')
    parser.add_argument('--json', '-j', action='store_true', help='Output as JSON')
    
    args = parser.parse_args()
    
    if not args.company and not args.ticker:
        parser.error("Either --company or --ticker is required")
    
    config = load_config()
    
    company_name = args.company or args.ticker
    
    if args.template:
        print(create_funding_template(company_name))
        return
    
    # For public companies with ticker
    if args.ticker:
        print(f"Researching public company: {args.ticker}")
        
        # Try to get S-1/IPO info
        try:
            ipo_info = get_sec_ipo_info(args.ticker)
            display_public_company_funding(ipo_info)
        except Exception as e:
            print(f"Note: Could not fetch SEC data: {e}")
        
        # Also provide general guidance
        display_funding_guidance(args.ticker)
    else:
        # For private companies or name search
        display_funding_guidance(company_name)
    
    if args.json:
        result = {
            'company': company_name,
            'search_queries': generate_search_queries(company_name),
            'data_sources': {
                'crunchbase': f"https://www.crunchbase.com/organization/{company_name.lower().replace(' ', '-')}",
                'pitchbook': 'https://pitchbook.com/',
            },
            'template': create_funding_template(company_name)
        }
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
