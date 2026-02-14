"""
Generate systematic investigation search queries for the Truth skill.

Usage:
    python generate_investigation_queries.py "<entity>" ["<claim keywords>"] ["<location>"] ["<date range>"]

Examples:
    python generate_investigation_queries.py "Acme Corp"
    python generate_investigation_queries.py "Acme Corp" "fraud settlement" "Texas" "2024-2025"
    python generate_investigation_queries.py "John Doe" "bribery corruption"
"""

import sys
from datetime import datetime


def generate_queries(entity, claim_keywords=None, location=None, date_range=None):
    entity_q = f'"{entity}"'
    keywords = claim_keywords.split() if claim_keywords else []
    queries = {}

    # ---- 1. Primary Document Searches ----
    queries["PRIMARY DOCUMENTS"] = []

    # Court & Legal
    queries["PRIMARY DOCUMENTS"].append(f'site:courtlistener.com {entity_q}')
    queries["PRIMARY DOCUMENTS"].append(f'{entity_q} docket number filetype:pdf')
    queries["PRIMARY DOCUMENTS"].append(f'site:justice.gov {entity_q}')
    queries["PRIMARY DOCUMENTS"].append(f'{entity_q} complaint OR indictment OR settlement filetype:pdf')
    for kw in keywords:
        queries["PRIMARY DOCUMENTS"].append(f'{entity_q} {kw} court filing OR docket')

    # SEC / Financial
    queries["PRIMARY DOCUMENTS"].append(f'site:sec.gov {entity_q}')
    queries["PRIMARY DOCUMENTS"].append(f'site:sec.gov/litigation {entity_q}')
    queries["PRIMARY DOCUMENTS"].append(f'{entity_q} 10-K OR 10-Q OR 8-K site:sec.gov')

    # ---- 2. Official Statements ----
    queries["OFFICIAL STATEMENTS"] = []
    queries["OFFICIAL STATEMENTS"].append(f'{entity_q} "press release" OR "official statement"')
    queries["OFFICIAL STATEMENTS"].append(f'{entity_q} site:whitehouse.gov OR site:congress.gov')
    queries["OFFICIAL STATEMENTS"].append(f'{entity_q} site:gao.gov')
    queries["OFFICIAL STATEMENTS"].append(f'{entity_q} "we have" OR "our position" OR "in response"')

    # Try to find official website
    queries["OFFICIAL STATEMENTS"].append(f'{entity_q} official site OR official website')

    # ---- 3. Government Databases ----
    queries["GOVERNMENT DATABASES"] = []
    queries["GOVERNMENT DATABASES"].append(f'site:federalregister.gov {entity_q}')
    queries["GOVERNMENT DATABASES"].append(f'site:congress.gov {entity_q}')
    queries["GOVERNMENT DATABASES"].append(f'site:govinfo.gov {entity_q}')
    queries["GOVERNMENT DATABASES"].append(f'{entity_q} site:fec.gov OR site:opensecrets.org')
    queries["GOVERNMENT DATABASES"].append(f'{entity_q} site:fara.gov')
    queries["GOVERNMENT DATABASES"].append(f'{entity_q} site:projects.propublica.org/nonprofits')

    if location:
        loc_q = f'"{location}"'
        queries["GOVERNMENT DATABASES"].append(f'{entity_q} {loc_q} court records')
        queries["GOVERNMENT DATABASES"].append(f'{entity_q} {loc_q} property records')
        queries["GOVERNMENT DATABASES"].append(f'{entity_q} secretary of state {location}')

    # ---- 4. FOIA & Archives ----
    queries["FOIA & ARCHIVES"] = []
    queries["FOIA & ARCHIVES"].append(f'site:vault.fbi.gov {entity_q}')
    queries["FOIA & ARCHIVES"].append(f'site:cia.gov/readingroom {entity_q}')
    queries["FOIA & ARCHIVES"].append(f'site:muckrock.com {entity_q}')
    queries["FOIA & ARCHIVES"].append(f'site:web.archive.org {entity_q}')
    queries["FOIA & ARCHIVES"].append(f'{entity_q} FOIA OR declassified')

    # ---- 5. Investigative & News ----
    queries["NEWS & INVESTIGATIONS"] = []
    queries["NEWS & INVESTIGATIONS"].append(f'{entity_q} investigation OR investigative')
    queries["NEWS & INVESTIGATIONS"].append(f'{entity_q} site:reuters.com')
    queries["NEWS & INVESTIGATIONS"].append(f'{entity_q} site:apnews.com')
    queries["NEWS & INVESTIGATIONS"].append(f'{entity_q} site:propublica.org')
    queries["NEWS & INVESTIGATIONS"].append(f'{entity_q} site:bbc.com OR site:bbc.co.uk')
    for kw in keywords:
        queries["NEWS & INVESTIGATIONS"].append(f'{entity_q} {kw}')
        queries["NEWS & INVESTIGATIONS"].append(f'{entity_q} {kw} fact check')

    # ---- 6. Document Discovery ----
    queries["DOCUMENT DISCOVERY"] = []
    filetypes = ["pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx"]
    for ft in filetypes:
        query = f'filetype:{ft} {entity_q}'
        if keywords:
            query += f' {keywords[0]}'
        queries["DOCUMENT DISCOVERY"].append(query)

    # ---- 7. Concerning / Negative ----
    queries["RED FLAGS"] = []
    red_flag_terms = [
        "fraud", "scam", "lawsuit", "scandal", "investigation",
        "indictment", "convicted", "settlement", "violation",
        "whistleblower", "misconduct", "penalty", "fine",
        "bankruptcy", "sanctions", "allegations", "accused"
    ]
    for term in red_flag_terms:
        queries["RED FLAGS"].append(f'{entity_q} {term}')

    # ---- 8. Social Media (leads only) ----
    queries["SOCIAL MEDIA (LEADS ONLY)"] = []
    social_sites = [
        "twitter.com", "x.com", "linkedin.com", "facebook.com",
        "reddit.com", "youtube.com"
    ]
    for site in social_sites:
        queries["SOCIAL MEDIA (LEADS ONLY)"].append(f'site:{site} {entity_q}')

    # ---- 9. Date-scoped queries ----
    if date_range:
        queries["DATE-SCOPED"] = []
        queries["DATE-SCOPED"].append(f'{entity_q} {date_range}')
        for kw in keywords:
            queries["DATE-SCOPED"].append(f'{entity_q} {kw} {date_range}')
        queries["DATE-SCOPED"].append(f'{entity_q} after:{date_range.split("-")[0]}' if "-" in date_range else f'{entity_q} {date_range}')

    # ---- 10. International ----
    queries["INTERNATIONAL"] = []
    queries["INTERNATIONAL"].append(f'site:indiankanoon.org {entity_q}')
    queries["INTERNATIONAL"].append(f'site:canlii.org {entity_q}')
    queries["INTERNATIONAL"].append(f'site:find-and-update.company-information.service.gov.uk {entity_q}')
    queries["INTERNATIONAL"].append(f'{entity_q} site:interpol.int')
    queries["INTERNATIONAL"].append(f'{entity_q} site:un.org OR site:who.int')

    return queries


def print_queries(queries):
    total = 0
    print("\n" + "=" * 70)
    print("  TRUTH INVESTIGATION — SYSTEMATIC SEARCH QUERIES")
    print("=" * 70)
    print(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    for category, query_list in queries.items():
        print(f"\n--- {category} ({len(query_list)} queries) ---")
        for i, q in enumerate(query_list, 1):
            print(f"  {i:2d}. {q}")
            total += 1

    print(f"\n{'=' * 70}")
    print(f"  TOTAL: {total} queries across {len(queries)} categories")
    print(f"{'=' * 70}\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python generate_investigation_queries.py "<entity>" ["<claim keywords>"] ["<location>"] ["<date range>"]')
        print('Example: python generate_investigation_queries.py "Acme Corp" "fraud settlement" "Texas" "2024-2025"')
        sys.exit(1)

    entity = sys.argv[1]
    claim_kw = sys.argv[2] if len(sys.argv) > 2 else None
    location = sys.argv[3] if len(sys.argv) > 3 else None
    date_range = sys.argv[4] if len(sys.argv) > 4 else None

    queries = generate_queries(entity, claim_kw, location, date_range)
    print_queries(queries)
