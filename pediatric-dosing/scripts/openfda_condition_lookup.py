#!/usr/bin/env python3
"""
openFDA Drug Label Lookup Script

Queries the openFDA Drug Label API to find medications for a given condition,
with pediatric use information and dosing.

Usage:
    python openfda_condition_lookup.py <condition>
    python openfda_condition_lookup.py <condition> --pediatric-only

Examples:
    python openfda_condition_lookup.py "atopic dermatitis"
    python openfda_condition_lookup.py "asthma" --pediatric-only
    python openfda_condition_lookup.py "otitis media"
"""

import sys
import json
import urllib.request
import urllib.parse
from typing import Optional

OPENFDA_BASE_URL = "https://api.fda.gov/drug/label.json"


def fetch_json(url: str) -> Optional[dict]:
    """Fetch JSON from URL."""
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            return json.loads(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        print(f"HTTP Error {e.code}: {e.reason}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Error fetching {url}: {e}", file=sys.stderr)
        return None


def search_by_condition(condition: str, pediatric_only: bool = False, limit: int = 10) -> list[dict]:
    """
    Search openFDA for drugs indicated for a condition.
    
    Args:
        condition: Clinical condition to search for
        pediatric_only: If True, filter to drugs with pediatric_use section
        limit: Maximum number of results
    
    Returns:
        List of drug label results with relevant fields
    """
    # Build search query - search in indications_and_usage
    encoded_condition = urllib.parse.quote(condition)
    
    # Search in indications field
    search_query = f'indications_and_usage:"{encoded_condition}"'
    
    # If pediatric only, also require pediatric_use field exists
    if pediatric_only:
        search_query += '+AND+_exists_:pediatric_use'
    
    url = f"{OPENFDA_BASE_URL}?search={search_query}&limit={limit}"
    
    data = fetch_json(url)
    if not data or 'results' not in data:
        return []
    
    results = []
    for item in data['results']:
        result = {
            'brand_name': None,
            'generic_name': None,
            'indications': None,
            'pediatric_use': None,
            'dosage_and_administration': None,
            'rxcui': None,
        }
        
        # Extract openFDA fields
        openfda = item.get('openfda', {})
        if openfda.get('brand_name'):
            result['brand_name'] = openfda['brand_name'][0]
        if openfda.get('generic_name'):
            result['generic_name'] = openfda['generic_name'][0]
        if openfda.get('rxcui'):
            result['rxcui'] = openfda['rxcui']
        
        # Extract label sections
        if item.get('indications_and_usage'):
            result['indications'] = item['indications_and_usage'][0][:500] + '...' if len(item['indications_and_usage'][0]) > 500 else item['indications_and_usage'][0]
        
        if item.get('pediatric_use'):
            result['pediatric_use'] = item['pediatric_use'][0][:500] + '...' if len(item['pediatric_use'][0]) > 500 else item['pediatric_use'][0]
        
        if item.get('dosage_and_administration'):
            result['dosage_and_administration'] = item['dosage_and_administration'][0][:800] + '...' if len(item['dosage_and_administration'][0]) > 800 else item['dosage_and_administration'][0]
        
        # Only include if we have a drug name
        if result['generic_name'] or result['brand_name']:
            results.append(result)
    
    return results


def format_output(results: list[dict], condition: str) -> str:
    """Format results for display."""
    if not results:
        return f"No FDA-approved drugs found for condition: {condition}"
    
    lines = []
    lines.append(f"Found {len(results)} FDA-approved drug(s) for: {condition}")
    lines.append(f"Source: openFDA Drug Label API")
    lines.append("=" * 60)
    
    for i, r in enumerate(results, 1):
        lines.append(f"\n[{i}] {r['generic_name'] or r['brand_name'] or 'Unknown'}")
        if r['brand_name'] and r['generic_name']:
            lines.append(f"    Brand: {r['brand_name']}")
        
        if r['rxcui']:
            lines.append(f"    RxCUI: {', '.join(r['rxcui'][:3])}")
        
        if r['indications']:
            lines.append(f"\n    INDICATION:")
            # Wrap text
            for line in r['indications'].split('\n')[:3]:
                lines.append(f"    {line[:100]}")
        
        if r['pediatric_use']:
            lines.append(f"\n    PEDIATRIC USE:")
            for line in r['pediatric_use'].split('\n')[:3]:
                lines.append(f"    {line[:100]}")
        
        if r['dosage_and_administration']:
            lines.append(f"\n    DOSAGE:")
            for line in r['dosage_and_administration'].split('\n')[:5]:
                lines.append(f"    {line[:100]}")
        
        lines.append("-" * 60)
    
    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print("Usage: openfda_condition_lookup.py <condition> [--pediatric-only]")
        print("\nSearches FDA drug labels for medications indicated for a condition.")
        print("\nExamples:")
        print('  python openfda_condition_lookup.py "atopic dermatitis"')
        print('  python openfda_condition_lookup.py "asthma" --pediatric-only')
        print('  python openfda_condition_lookup.py "otitis media"')
        sys.exit(1)
    
    condition = sys.argv[1]
    pediatric_only = "--pediatric-only" in sys.argv
    
    print(f"Searching openFDA for: {condition}")
    if pediatric_only:
        print("Filtering to drugs with pediatric labeling\n")
    else:
        print("")
    
    results = search_by_condition(condition, pediatric_only)
    print(format_output(results, condition))
    
    # Also output as JSON for programmatic use
    if results:
        print("\n\nJSON Output (first result):")
        print(json.dumps(results[0], indent=2))


if __name__ == "__main__":
    main()
