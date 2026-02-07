#!/usr/bin/env python3
"""
LOINC Lookup Script - Query NIH Clinical Tables API for LOINC code information

Usage:
    python loinc_lookup.py <code-or-search-term>

Examples:
    python loinc_lookup.py 2345-7           # Look up by LOINC code
    python loinc_lookup.py LP14559-6        # Look up by LOINC part code
    python loinc_lookup.py "glucose blood"  # Search by text
"""

import sys
import json
import urllib.request
import urllib.parse
import urllib.error


def search_loinc(query: str, max_results: int = 10) -> dict:
    """
    Search LOINC codes using the NIH Clinical Tables API.
    
    Args:
        query: LOINC code, part code, or search term
        max_results: Maximum number of results to return
        
    Returns:
        Dictionary with search results
    """
    base_url = "https://clinicaltables.nlm.nih.gov/api/loinc_items/v3/search"
    
    params = {
        "terms": query,
        "maxList": str(max_results),
        "df": "LOINC_NUM,LONG_COMMON_NAME,COMPONENT,PROPERTY,TIME_ASPCT,SYSTEM,SCALE_TYP,METHOD_TYP,CLASS,STATUS",
        "type": "question"
    }
    
    url = f"{base_url}?{urllib.parse.urlencode(params)}"
    
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            data = json.loads(response.read().decode('utf-8'))
            return parse_loinc_response(data)
    except urllib.error.URLError as e:
        return {"error": f"Network error: {e.reason}"}
    except json.JSONDecodeError as e:
        return {"error": f"JSON parse error: {e}"}


def parse_loinc_response(data: list) -> dict:
    """
    Parse the NIH Clinical Tables API response.
    
    Args:
        data: Raw API response (list format)
        
    Returns:
        Parsed dictionary with results
    """
    if not data or len(data) < 4:
        return {"error": "Invalid API response format", "raw": data}
    
    total_count = data[0]
    codes = data[1]  # List of LOINC codes
    extra_data = data[2] if len(data) > 2 else None
    details = data[3] if len(data) > 3 else []
    
    results = []
    for i, code in enumerate(codes):
        detail = details[i] if i < len(details) else []
        result = {
            "loinc_code": detail[0] if len(detail) > 0 else code,
            "long_common_name": detail[1] if len(detail) > 1 else "",
            "component": detail[2] if len(detail) > 2 else "",
            "property": detail[3] if len(detail) > 3 else "",
            "time_aspect": detail[4] if len(detail) > 4 else "",
            "system": detail[5] if len(detail) > 5 else "",
            "scale_type": detail[6] if len(detail) > 6 else "",
            "method_type": detail[7] if len(detail) > 7 else "",
            "class": detail[8] if len(detail) > 8 else "",
            "status": detail[9] if len(detail) > 9 else ""
        }
        results.append(result)
    
    return {
        "total_count": total_count,
        "results": results
    }


def format_result(result: dict) -> str:
    """Format a single LOINC result for display."""
    lines = [
        f"LOINC Code: {result.get('loinc_code', 'N/A')}",
        f"Name: {result.get('long_common_name', 'N/A')}",
        f"Component: {result.get('component', 'N/A')}",
        f"Property: {result.get('property', 'N/A')}",
        f"Time Aspect: {result.get('time_aspect', 'N/A')}",
        f"System (Specimen): {result.get('system', 'N/A')}",
        f"Scale Type: {result.get('scale_type', 'N/A')}",
        f"Method: {result.get('method_type', 'N/A') or 'Not specified'}",
        f"Class: {result.get('class', 'N/A')}",
        f"Status: {result.get('status', 'N/A')}"
    ]
    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print("Usage: python loinc_lookup.py <code-or-search-term>")
        print("\nExamples:")
        print('  python loinc_lookup.py 2345-7')
        print('  python loinc_lookup.py LP14559-6')
        print('  python loinc_lookup.py "glucose blood"')
        sys.exit(1)
    
    query = " ".join(sys.argv[1:])
    print(f"Searching LOINC for: {query}\n")
    
    results = search_loinc(query)
    
    if "error" in results:
        print(f"Error: {results['error']}")
        sys.exit(1)
    
    if not results.get("results"):
        print("No results found.")
        sys.exit(0)
    
    print(f"Found {results['total_count']} total results (showing up to 10):\n")
    print("=" * 60)
    
    for i, result in enumerate(results["results"], 1):
        print(f"\n[Result {i}]")
        print(format_result(result))
        print("-" * 60)
    
    # Also output JSON for programmatic use
    print("\n\nJSON Output:")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
