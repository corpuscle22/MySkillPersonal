#!/usr/bin/env python3
"""
RxNorm SCD (Semantic Clinical Drug) Lookup Script

Queries the RxNorm REST API to find SCD codes for medications,
filtered to pediatric-appropriate formulations.

Usage:
    python rxnorm_scd_lookup.py <drug_name> [--pediatric-only]

Examples:
    python rxnorm_scd_lookup.py amoxicillin
    python rxnorm_scd_lookup.py ibuprofen --pediatric-only
"""

import sys
import json
import urllib.request
import urllib.parse
from typing import Optional

RXNORM_BASE_URL = "https://rxnav.nlm.nih.gov/REST"

# Pediatric-friendly formulation keywords
PEDIATRIC_FORMULATIONS = [
    "oral suspension",
    "oral solution",
    "chewable",
    "drops",
    "syrup",
    "elixir",
    "disintegrating",
    "dispersible",
    "powder for",
    "granules",
]


def fetch_json(url: str) -> Optional[dict]:
    """Fetch JSON from URL."""
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            return json.loads(response.read().decode('utf-8'))
    except Exception as e:
        print(f"Error fetching {url}: {e}", file=sys.stderr)
        return None


def get_drugs(drug_name: str) -> list[dict]:
    """
    Get drug concepts from RxNorm API.
    Returns list of concept properties with rxcui, name, and tty.
    """
    encoded_name = urllib.parse.quote(drug_name)
    url = f"{RXNORM_BASE_URL}/drugs.json?name={encoded_name}"
    
    data = fetch_json(url)
    if not data or 'drugGroup' not in data:
        return []
    
    concepts = []
    drug_group = data['drugGroup']
    
    if 'conceptGroup' not in drug_group:
        return []
    
    for group in drug_group['conceptGroup']:
        tty = group.get('tty', '')
        if tty != 'SCD':  # Filter to SCD only
            continue
        
        if 'conceptProperties' not in group:
            continue
        
        for prop in group['conceptProperties']:
            concepts.append({
                'rxcui': prop.get('rxcui', ''),
                'name': prop.get('name', ''),
                'tty': prop.get('tty', ''),
            })
    
    return concepts


def filter_pediatric_formulations(concepts: list[dict]) -> list[dict]:
    """Filter concepts to pediatric-appropriate formulations."""
    pediatric = []
    for concept in concepts:
        name_lower = concept['name'].lower()
        for formulation in PEDIATRIC_FORMULATIONS:
            if formulation in name_lower:
                pediatric.append(concept)
                break
    return pediatric


def format_output(concepts: list[dict]) -> str:
    """Format concepts for display."""
    if not concepts:
        return "No SCD codes found."
    
    lines = []
    lines.append(f"Found {len(concepts)} SCD code(s):\n")
    
    for c in concepts:
        lines.append(f"  RxCUI: {c['rxcui']}")
        lines.append(f"  Name:  {c['name']}")
        lines.append(f"  TTY:   {c['tty']}")
        lines.append("")
    
    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print("Usage: rxnorm_scd_lookup.py <drug_name> [--pediatric-only]")
        print("\nExamples:")
        print("  python rxnorm_scd_lookup.py amoxicillin")
        print("  python rxnorm_scd_lookup.py ibuprofen --pediatric-only")
        sys.exit(1)
    
    drug_name = sys.argv[1]
    pediatric_only = "--pediatric-only" in sys.argv
    
    print(f"Searching RxNorm for: {drug_name}")
    if pediatric_only:
        print("Filtering to pediatric formulations only\n")
    else:
        print("")
    
    concepts = get_drugs(drug_name)
    
    if pediatric_only:
        concepts = filter_pediatric_formulations(concepts)
    
    print(format_output(concepts))
    
    # Also output as JSON for programmatic use
    if concepts:
        print("\nJSON Output:")
        print(json.dumps(concepts, indent=2))


if __name__ == "__main__":
    main()
