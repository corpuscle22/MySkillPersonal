#!/usr/bin/env python3
"""
Property Search Tool - Search public property records across US counties.

Supports:
  - Socrata SODA API (data.texas.gov, Cook County, etc.)
  - County Appraisal District web scraping (Collin CAD, Dallas CAD, etc.)
  - Search by owner name, property address, or property ID

Usage:
  python property_search.py --mode owner --query "SMITH JOHN" --county collin --state TX
  python property_search.py --mode address --query "123 Main St" --county collin --state TX
  python property_search.py --mode propid --query "1234567" --county collin --state TX
  python property_search.py --mode owner --query "SMITH JOHN" --source socrata --dataset vtby-uz4n
"""

import argparse
import json
import sys
import time
import os
from datetime import datetime
from urllib.parse import quote, urlencode
from pathlib import Path

try:
    import requests
except ImportError:
    print("ERROR: 'requests' library required. Install with: pip install requests")
    sys.exit(1)

# ---------------------------------------------------------------------------
# COUNTY REGISTRY: maps (state, county) -> data source config
# ---------------------------------------------------------------------------
COUNTY_REGISTRY = {
    # ── Texas ──────────────────────────────────────────────────────────────
    ("TX", "collin"): {
        "source": "socrata",
        "domain": "data.texas.gov",
        "datasets": {
            "2022": "vtby-uz4n",
            "2023": "kfq3-t3pb",
            "preliminary": "sn6q-rxgx",
        },
        "default_dataset": "vtby-uz4n",
        "owner_field": "ownername",
        "address_field": "situsconcat",
        "address_short": "situsconcatshort",
        "propid_field": "propid",
        "display_name": "Collin Central Appraisal District",
        "web_url": "https://www.collincad.org/property-search",
    },
    ("TX", "dallas"): {
        "source": "web_search",
        "web_url": "https://www.dallascad.org/SearchAddr.aspx",
        "owner_search_url": "https://www.dallascad.org/SearchOwner.aspx",
        "display_name": "Dallas Central Appraisal District",
    },
    ("TX", "denton"): {
        "source": "web_search",
        "web_url": "https://www.dentoncad.com/",
        "display_name": "Denton Central Appraisal District",
    },
    ("TX", "tarrant"): {
        "source": "web_search",
        "web_url": "https://www.tad.org/property-search/",
        "display_name": "Tarrant Appraisal District",
    },
    ("TX", "travis"): {
        "source": "web_search",
        "web_url": "https://www.traviscad.org/property-search",
        "display_name": "Travis Central Appraisal District",
    },
    ("TX", "harris"): {
        "source": "web_search",
        "web_url": "https://public.hcad.org/records/",
        "display_name": "Harris County Appraisal District",
    },
    ("TX", "williamson"): {
        "source": "web_search",
        "web_url": "https://www.wcad.org/property-search/",
        "display_name": "Williamson Central Appraisal District",
    },
    # ── Illinois ───────────────────────────────────────────────────────────
    ("IL", "cook"): {
        "source": "socrata",
        "domain": "datacatalog.cookcountyil.gov",
        "datasets": {"assessments": "uzyt-m557"},
        "default_dataset": "uzyt-m557",
        "owner_field": "taxpayer_name",
        "address_field": "property_address",
        "propid_field": "pin",
        "display_name": "Cook County Assessor",
        "web_url": "https://www.cookcountyassessor.com/",
    },
    # ── Florida ────────────────────────────────────────────────────────────
    ("FL", "miami-dade"): {
        "source": "web_search",
        "web_url": "https://www.miamidade.gov/pa/",
        "display_name": "Miami-Dade Property Appraiser",
    },
    ("FL", "broward"): {
        "source": "web_search",
        "web_url": "https://web.bcpa.net/BcpaClient/",
        "display_name": "Broward County Property Appraiser",
    },
    # ── California ─────────────────────────────────────────────────────────
    ("CA", "los-angeles"): {
        "source": "web_search",
        "web_url": "https://portal.assessor.lacounty.gov/",
        "display_name": "Los Angeles County Assessor",
    },
    # ── Arizona ────────────────────────────────────────────────────────────
    ("AZ", "maricopa"): {
        "source": "web_search",
        "web_url": "https://mcassessor.maricopa.gov/",
        "display_name": "Maricopa County Assessor",
    },
}

# Socrata SODA API settings
SODA_LIMIT = 500
SODA_TIMEOUT = 60
USER_AGENT = "PropertySearchSkill/1.0"


def socrata_search(config: dict, mode: str, query: str, dataset_key: str = None,
                   limit: int = SODA_LIMIT, app_token: str = None) -> list:
    """Query Socrata SODA API for property records."""
    domain = config["domain"]
    ds = dataset_key or config.get("default_dataset")
    dataset_id = config["datasets"].get(ds, ds)

    base_url = f"https://{domain}/resource/{dataset_id}.json"

    # Build SoQL $where clause based on search mode
    if mode == "owner":
        where = f"upper({config['owner_field']}) like upper('%{query}%')"
    elif mode == "address":
        addr_field = config.get("address_field", "situsconcat")
        addr_short = config.get("address_short")
        if addr_short:
            where = (f"upper({addr_field}) like upper('%{query}%') "
                     f"OR upper({addr_short}) like upper('%{query}%')")
        else:
            where = f"upper({addr_field}) like upper('%{query}%')"
    elif mode == "propid":
        where = f"{config['propid_field']} = '{query}'"
    else:
        raise ValueError(f"Unknown search mode: {mode}")

    params = {
        "$where": where,
        "$limit": limit,
        "$order": config.get("owner_field", "ownername") + " ASC",
    }

    headers = {"User-Agent": USER_AGENT}
    if app_token:
        headers["X-App-Token"] = app_token

    resp = requests.get(base_url, params=params, headers=headers, timeout=SODA_TIMEOUT)
    resp.raise_for_status()
    return resp.json()


def format_collin_record(rec: dict) -> dict:
    """Normalize a Collin CAD Socrata record into a standard output dict."""
    return {
        "property_id": rec.get("propid", ""),
        "geo_id": rec.get("geoid", ""),
        "property_year": rec.get("propyear", ""),
        "property_type": rec.get("proptype", ""),
        "property_subtype": rec.get("propsubtype", ""),
        "legal_description": rec.get("legaldescription", ""),
        "situs_address": rec.get("situsconcat", ""),
        "owner_name": rec.get("ownername", ""),
        "owner_address": ", ".join(filter(None, [
            rec.get("owneraddrline1", ""),
            rec.get("owneraddrcity", ""),
            rec.get("owneraddrstate", ""),
            rec.get("owneraddrzip", ""),
        ])),
        "owner_id": rec.get("ownerid", ""),
        "deed_type": rec.get("deedtypecd", ""),
        "deed_number": rec.get("deednum", ""),
        "deed_date": rec.get("deedeffdate", ""),
        "year_built": rec.get("imprvyearbuilt", ""),
        "improvement_class": rec.get("imprvclasscd", ""),
        "main_area_sqft": rec.get("imprvmainarea", ""),
        "has_pool": rec.get("imprvpoolflag", False),
        "land_size_acres": rec.get("landsizeacres", ""),
        "land_size_sqft": rec.get("landsizesqft", ""),
        "homestead_exempt": rec.get("exempthmstdflag", False),
        "exemptions": rec.get("exemptcodes", ""),
        "market_value": rec.get("currvalmarket", ""),
        "appraised_value": rec.get("currvalappraised", ""),
        "assessed_value": rec.get("currvalassessed", ""),
        "land_value": rec.get("currvalland", ""),
        "improvement_value": rec.get("currvalimprv", ""),
        "hs_cap_loss": rec.get("currvalhscaploss", ""),
        "prev_market_value": rec.get("prevvalmarket", ""),
        "prev_appraised_value": rec.get("prevvalappraised", ""),
        "school_district": rec.get("entityschoolcode", ""),
        "city_code": rec.get("entitycitycode", ""),
        "entity_codes": rec.get("entitycodes", ""),
        "neighborhood_code": rec.get("nbhdcode", ""),
        "map_id": rec.get("mapid", ""),
        "status": rec.get("propstatus", ""),
        "data_date": rec.get("datadate", ""),
    }


def format_generic_record(rec: dict, config: dict) -> dict:
    """Normalize a generic Socrata record using config field mappings."""
    result = {"_raw": rec}
    result["owner_name"] = rec.get(config.get("owner_field", ""), "")
    result["situs_address"] = rec.get(config.get("address_field", ""), "")
    result["property_id"] = rec.get(config.get("propid_field", ""), "")
    # Include all other fields
    for k, v in rec.items():
        if k not in result:
            result[k] = v
    return result


def search_property(state: str, county: str, mode: str, query: str,
                    dataset_key: str = None, limit: int = SODA_LIMIT,
                    app_token: str = None) -> dict:
    """
    Main entry point: search for properties in a given county.

    Returns dict with keys: success, source, county, results, count, query_info
    """
    key = (state.upper(), county.lower())
    config = COUNTY_REGISTRY.get(key)

    if not config:
        return {
            "success": False,
            "error": f"County '{county}' in state '{state}' not in registry. "
                     f"Available: {list(COUNTY_REGISTRY.keys())}",
            "suggestion": "Use --source socrata with --domain and --dataset for custom endpoints.",
        }

    result = {
        "success": True,
        "source": config["source"],
        "county": config["display_name"],
        "web_url": config.get("web_url", ""),
        "query_info": {"mode": mode, "query": query, "state": state, "county": county},
        "timestamp": datetime.now().isoformat(),
    }

    if config["source"] == "socrata":
        try:
            raw = socrata_search(config, mode, query, dataset_key, limit, app_token)
            # Normalize records
            if key == ("TX", "collin"):
                records = [format_collin_record(r) for r in raw]
            else:
                records = [format_generic_record(r, config) for r in raw]
            result["results"] = records
            result["count"] = len(records)
        except requests.HTTPError as e:
            result["success"] = False
            result["error"] = f"Socrata API error: {e}"
        except Exception as e:
            result["success"] = False
            result["error"] = str(e)
    elif config["source"] == "web_search":
        result["results"] = []
        result["count"] = 0
        result["note"] = (
            f"Direct API not available for {config['display_name']}. "
            f"Use the web portal: {config.get('web_url', 'N/A')}. "
            f"Alternatively, use browser_subagent to scrape results."
        )
    return result


def search_custom_socrata(domain: str, dataset_id: str, mode: str, query: str,
                          owner_field: str = "ownername",
                          address_field: str = "situsconcat",
                          propid_field: str = "propid",
                          limit: int = SODA_LIMIT,
                          app_token: str = None) -> dict:
    """
    Search any Socrata SODA API endpoint with custom field mappings.
    Useful for counties not in the registry.
    """
    config = {
        "domain": domain,
        "datasets": {"custom": dataset_id},
        "default_dataset": "custom",
        "owner_field": owner_field,
        "address_field": address_field,
        "propid_field": propid_field,
    }
    try:
        raw = socrata_search(config, mode, query, "custom", limit, app_token)
        records = [format_generic_record(r, config) for r in raw]
        return {
            "success": True,
            "source": "socrata",
            "domain": domain,
            "dataset": dataset_id,
            "results": records,
            "count": len(records),
            "timestamp": datetime.now().isoformat(),
        }
    except Exception as e:
        return {"success": False, "error": str(e)}


def list_counties():
    """Return list of supported counties."""
    counties = []
    for (state, county), config in sorted(COUNTY_REGISTRY.items()):
        counties.append({
            "state": state,
            "county": county,
            "name": config["display_name"],
            "source": config["source"],
            "web_url": config.get("web_url", ""),
        })
    return counties


def format_report(results: dict, output_format: str = "text") -> str:
    """Format search results for display."""
    if output_format == "json":
        return json.dumps(results, indent=2, default=str)

    lines = []
    lines.append("=" * 80)
    lines.append(f"PROPERTY SEARCH RESULTS")
    lines.append(f"County: {results.get('county', 'Unknown')}")
    lines.append(f"Source: {results.get('source', 'Unknown')}")
    qi = results.get("query_info", {})
    lines.append(f"Search: {qi.get('mode', '')} = '{qi.get('query', '')}'")
    lines.append(f"Time: {results.get('timestamp', '')}")
    lines.append(f"Results: {results.get('count', 0)}")
    lines.append("=" * 80)

    if results.get("note"):
        lines.append(f"\nNOTE: {results['note']}")

    if not results.get("success"):
        lines.append(f"\nERROR: {results.get('error', 'Unknown error')}")
        return "\n".join(lines)

    for i, rec in enumerate(results.get("results", []), 1):
        lines.append(f"\n--- Record {i} ---")
        # Prioritize key fields
        priority_fields = [
            "owner_name", "situs_address", "owner_address", "property_id",
            "market_value", "appraised_value", "assessed_value",
            "year_built", "main_area_sqft", "land_size_sqft",
            "legal_description", "deed_number", "deed_date",
        ]
        for field in priority_fields:
            val = rec.get(field)
            if val and val != "" and val != "0":
                label = field.replace("_", " ").title()
                if "value" in field.lower():
                    try:
                        val = f"${int(val):,}"
                    except (ValueError, TypeError):
                        pass
                lines.append(f"  {label}: {val}")
        # Show remaining fields
        shown = set(priority_fields) | {"_raw"}
        for k, v in rec.items():
            if k not in shown and v and v != "" and v != "0" and v is not False:
                label = k.replace("_", " ").title()
                lines.append(f"  {label}: {v}")

    lines.append("\n" + "=" * 80)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Search public property records")
    parser.add_argument("--mode", choices=["owner", "address", "propid"],
                        default=None, help="Search mode")
    parser.add_argument("--query", default=None, help="Search query")
    parser.add_argument("--state", default="TX", help="State (default: TX)")
    parser.add_argument("--county", default="collin", help="County (default: collin)")
    parser.add_argument("--dataset", default=None, help="Dataset key (e.g., 2022, 2023, preliminary)")
    parser.add_argument("--limit", type=int, default=50, help="Max results (default: 50)")
    parser.add_argument("--format", choices=["text", "json"], default="text", help="Output format")
    parser.add_argument("--token", default=None, help="Socrata app token (optional)")
    parser.add_argument("--list-counties", action="store_true", help="List supported counties")
    # Custom Socrata endpoint
    parser.add_argument("--source", default=None, help="Data source: socrata")
    parser.add_argument("--domain", default=None, help="Socrata domain for custom search")
    parser.add_argument("--dataset-id", default=None, help="Socrata dataset ID for custom search")
    parser.add_argument("--owner-field", default="ownername", help="Owner field name")
    parser.add_argument("--address-field", default="situsconcat", help="Address field name")
    parser.add_argument("--propid-field", default="propid", help="Property ID field name")
    # Output to file
    parser.add_argument("--output", default=None, help="Save output to file")

    args = parser.parse_args()

    if args.list_counties:
        counties = list_counties()
        print(f"\nSupported Counties ({len(counties)}):\n")
        for c in counties:
            api_tag = " [API]" if c["source"] == "socrata" else " [Web]"
            print(f"  {c['state']}/{c['county']}: {c['name']}{api_tag}")
            print(f"    {c['web_url']}")
        return

    if not args.mode or not args.query:
        parser.error("--mode and --query are required for searches")

    # Custom Socrata endpoint
    if args.source == "socrata" and args.domain and args.dataset_id:
        results = search_custom_socrata(
            domain=args.domain,
            dataset_id=args.dataset_id,
            mode=args.mode,
            query=args.query,
            owner_field=args.owner_field,
            address_field=args.address_field,
            propid_field=args.propid_field,
            limit=args.limit,
            app_token=args.token,
        )
    else:
        results = search_property(
            state=args.state,
            county=args.county,
            mode=args.mode,
            query=args.query,
            dataset_key=args.dataset,
            limit=args.limit,
            app_token=args.token,
        )

    output = format_report(results, args.format)
    print(output)

    # Save to file if requested
    if args.output:
        outpath = Path(args.output)
        outpath.parent.mkdir(parents=True, exist_ok=True)
        outpath.write_text(output, encoding="utf-8")
        print(f"\nResults saved to: {outpath}")


if __name__ == "__main__":
    main()
