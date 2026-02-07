#!/usr/bin/env python3
"""
Company Profile Fetcher

Fetches basic company information from multiple sources.

Usage:
    python company_profile.py --company "Tesla"
    python company_profile.py --company "OpenAI" --search
    python company_profile.py --ticker AAPL
"""

import argparse
import json
import sys
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from urllib.parse import quote_plus


# Configuration
CONFIG_FILE = Path.home() / ".company-intelligence" / "config.json"

FMP_BASE_URL = "https://financialmodelingprep.com/api/v3"
OPENCORPORATES_URL = "https://api.opencorporates.com/v0.4"


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
    except HTTPError as e:
        return {'error': f"HTTP Error: {e.code} - {e.reason}"}
    except URLError as e:
        return {'error': f"URL Error: {e}"}
    except json.JSONDecodeError:
        return {'error': "Invalid JSON response"}


def search_fmp(query: str, api_key: str) -> list:
    """Search for companies using FMP."""
    url = f"{FMP_BASE_URL}/search?query={quote_plus(query)}&limit=10&apikey={api_key}"
    data = fetch_json(url)
    if isinstance(data, list):
        return data
    return []


def get_fmp_profile(ticker: str, api_key: str) -> dict:
    """Get company profile from FMP."""
    url = f"{FMP_BASE_URL}/profile/{ticker}?apikey={api_key}"
    data = fetch_json(url)
    if isinstance(data, list) and data:
        return data[0]
    return data


def search_opencorporates(query: str, api_key: str = None) -> list:
    """Search for companies using OpenCorporates."""
    url = f"{OPENCORPORATES_URL}/companies/search?q={quote_plus(query)}&per_page=10"
    if api_key:
        url += f"&api_token={api_key}"
    
    data = fetch_json(url)
    if 'error' in data:
        return []
    
    results = data.get('results', {}).get('companies', [])
    return [c.get('company', {}) for c in results]


def format_opencorporates_result(company: dict) -> str:
    """Format OpenCorporates company result."""
    output = []
    output.append(f"  Name: {company.get('name', 'N/A')}")
    output.append(f"  Jurisdiction: {company.get('jurisdiction_code', 'N/A')}")
    output.append(f"  Company Number: {company.get('company_number', 'N/A')}")
    output.append(f"  Status: {company.get('current_status', 'N/A')}")
    output.append(f"  Incorporation Date: {company.get('incorporation_date', 'N/A')}")
    output.append(f"  Company Type: {company.get('company_type', 'N/A')}")
    
    address = company.get('registered_address_in_full', '')
    if address:
        output.append(f"  Address: {address}")
    
    url = company.get('opencorporates_url', '')
    if url:
        output.append(f"  Details: {url}")
    
    return "\n".join(output)


def display_profile(profile: dict):
    """Display company profile."""
    print("\n" + "=" * 70)
    print("COMPANY PROFILE")
    print("=" * 70)
    
    print(f"\nCompany Name: {profile.get('companyName', 'N/A')}")
    print(f"Symbol: {profile.get('symbol', 'N/A')}")
    print(f"Exchange: {profile.get('exchangeShortName', 'N/A')}")
    print(f"Industry: {profile.get('industry', 'N/A')}")
    print(f"Sector: {profile.get('sector', 'N/A')}")
    print(f"CEO: {profile.get('ceo', 'N/A')}")
    
    employees = profile.get('fullTimeEmployees')
    if employees:
        print(f"Employees: {int(employees):,}")
    
    print(f"Headquarters: {profile.get('city', 'N/A')}, {profile.get('state', '')}, {profile.get('country', 'N/A')}")
    print(f"Website: {profile.get('website', 'N/A')}")
    print(f"Phone: {profile.get('phone', 'N/A')}")
    print(f"IPO Date: {profile.get('ipoDate', 'N/A')}")
    
    mktcap = profile.get('mktCap')
    if mktcap:
        if mktcap >= 1e12:
            print(f"Market Cap: ${mktcap/1e12:.2f}T")
        elif mktcap >= 1e9:
            print(f"Market Cap: ${mktcap/1e9:.2f}B")
        else:
            print(f"Market Cap: ${mktcap/1e6:.2f}M")
    
    price = profile.get('price')
    if price:
        print(f"Stock Price: ${price:.2f}")
    
    beta = profile.get('beta')
    if beta:
        print(f"Beta: {beta:.2f}")
    
    print(f"\nDescription:")
    desc = profile.get('description', 'N/A')
    # Word wrap description
    words = desc.split()
    lines = []
    current_line = []
    for word in words:
        current_line.append(word)
        if len(' '.join(current_line)) > 80:
            lines.append(' '.join(current_line[:-1]))
            current_line = [word]
    if current_line:
        lines.append(' '.join(current_line))
    print('\n'.join(lines[:10]))
    if len(lines) > 10:
        print("...[truncated]")


def main():
    parser = argparse.ArgumentParser(
        description="Fetch company profile information",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python company_profile.py --ticker AAPL
    python company_profile.py --company "Tesla" --search
    python company_profile.py --company "OpenAI" --registry
        """
    )
    
    parser.add_argument('--company', '-c', help='Company name to search for')
    parser.add_argument('--ticker', '-t', help='Stock ticker symbol')
    parser.add_argument('--search', '-s', action='store_true', help='Search for matching companies')
    parser.add_argument('--registry', '-r', action='store_true', help='Search company registries (OpenCorporates)')
    parser.add_argument('--json', '-j', action='store_true', help='Output as JSON')
    
    args = parser.parse_args()
    
    if not args.company and not args.ticker:
        parser.error("Either --company or --ticker is required")
    
    config = load_config()
    fmp_key = config.get('fmp_api_key')
    oc_key = config.get('opencorporates_api_key')
    
    # If ticker provided, get profile directly
    if args.ticker:
        if not fmp_key:
            print("Error: FMP API key required for ticker lookup.")
            print("Run 'python setup_apis.py' to configure.")
            sys.exit(1)
        
        print(f"Fetching profile for: {args.ticker.upper()}")
        profile = get_fmp_profile(args.ticker.upper(), fmp_key)
        
        if args.json:
            print(json.dumps(profile, indent=2))
        elif 'error' in profile:
            print(f"Error: {profile['error']}")
        else:
            display_profile(profile)
        return
    
    # Search by company name
    company_name = args.company
    print(f"Searching for: {company_name}")
    
    results = {'fmp_matches': [], 'registry_matches': []}
    
    # Search FMP if API key available
    if fmp_key and (args.search or not args.registry):
        print("\nSearching financial databases...")
        fmp_results = search_fmp(company_name, fmp_key)
        results['fmp_matches'] = fmp_results
        
        if not args.json:
            if fmp_results:
                print(f"\nFound {len(fmp_results)} match(es) in financial databases:")
                print("-" * 50)
                for i, match in enumerate(fmp_results[:5], 1):
                    print(f"{i}. {match.get('name')} ({match.get('symbol')})")
                    print(f"   Exchange: {match.get('stockExchange', 'N/A')}")
                
                # If only one match, show full profile
                if len(fmp_results) == 1:
                    profile = get_fmp_profile(fmp_results[0]['symbol'], fmp_key)
                    display_profile(profile)
            else:
                print("No matches found in financial databases.")
    
    # Search OpenCorporates if requested
    if args.registry:
        print("\nSearching company registries...")
        oc_results = search_opencorporates(company_name, oc_key)
        results['registry_matches'] = oc_results
        
        if not args.json:
            if oc_results:
                print(f"\nFound {len(oc_results)} match(es) in company registries:")
                print("-" * 50)
                for i, company in enumerate(oc_results[:5], 1):
                    print(f"\n{i}.")
                    print(format_opencorporates_result(company))
            else:
                print("No matches found in company registries.")
    
    if args.json:
        print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
