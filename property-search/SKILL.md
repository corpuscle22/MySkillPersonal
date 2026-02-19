---
name: property-search
description: Search public property records across US counties to find property information by owner name, address, or property ID. Use when the user asks to (1) find properties owned by a person, (2) look up property details by address, (3) find someone's address from their name using property records, (4) get property tax/appraisal values, (5) search county appraisal district records, or (6) look up ownership and deed information. Triggers include "property search", "find property", "who owns", "property owner", "find address for", "appraisal district", "property records", "property tax lookup", "CAD search", "county assessor search", or any request to find real estate ownership information from public databases.
---

# Property Search

Search public property records across US counties using Socrata SODA APIs and county appraisal district web portals.

## Capabilities

- **Owner Search**: Find all properties owned by a person (search by last name, full name, or partial name)
- **Address Search**: Lookup property details by street address
- **Property ID Search**: Lookup by property ID, parcel number, or PIN
- **Reverse Lookup**: Find a person's address by searching property records with their name

## Workflow

1. Determine search parameters from user request
   - **Search mode**: `owner` (name), `address` (street address), or `propid` (ID)
   - **State & County**: Identify from user context (default: TX/collin)
   - **Query**: The search term

2. Determine the data source
   - **Socrata API counties** (preferred): Run `scripts/property_search.py`
   - **Web-only counties**: Use `browser_subagent` to scrape the county portal
   - **Unknown county**: Search web for county's open data portal; if Socrata-based, use custom endpoint

3. Execute the search
   - For Socrata: `python scripts/property_search.py --mode owner --query "SMITH JOHN" --state TX --county collin`
   - For web portals: Use `browser_subagent` to navigate the county's property search page

4. Format and present results
   - Save detailed results to `outputs/` directory
   - Present a summary table to user with key fields

## Script Usage

```bash
# Search by owner name (Collin County, TX - default)
python scripts/property_search.py --mode owner --query "SMITH JOHN" --state TX --county collin

# Search by address
python scripts/property_search.py --mode address --query "123 MAIN ST" --state TX --county collin

# Search by property ID
python scripts/property_search.py --mode propid --query "1234567" --state TX --county collin

# Use different dataset year
python scripts/property_search.py --mode owner --query "JONES" --dataset 2023

# Output as JSON
python scripts/property_search.py --mode owner --query "JONES" --format json

# Save results to file
python scripts/property_search.py --mode owner --query "JONES" --output outputs/jones_search.txt

# List supported counties
python scripts/property_search.py --list-counties

# Custom Socrata endpoint (any county with SODA API)
python scripts/property_search.py --mode owner --query "SMITH" \
  --source socrata --domain data.example.gov --dataset-id xxxx-yyyy \
  --owner-field owner_name --address-field prop_address
```

## Supported Counties

| State | County | Source | Has API |
|-------|--------|--------|---------|
| TX | Collin | Socrata (data.texas.gov) | Yes |
| TX | Dallas | Web (dallascad.org) | No - use browser |
| TX | Denton | Web (dentoncad.com) | No - use browser |
| TX | Tarrant | Web (tad.org) | No - use browser |
| TX | Travis | Web (traviscad.org) | No - use browser |
| TX | Harris | Web (hcad.org) | No - use browser |
| TX | Williamson | Web (wcad.org) | No - use browser |
| IL | Cook | Socrata (cookcountyil.gov) | Yes |
| FL | Miami-Dade | Web (miamidade.gov) | No - use browser |
| FL | Broward | Web (bcpa.net) | No - use browser |
| CA | Los Angeles | Web (lacounty.gov) | No - use browser |
| AZ | Maricopa | Web (maricopa.gov) | No - use browser |

## Web Portal Scraping (for non-API counties)

When the county has no API, use `browser_subagent` to search:

1. Navigate to the county's property search URL
2. Enter the search query in the appropriate field (owner name / address)
3. Submit the form and wait for results
4. Extract property data from the results table
5. If detailed records needed, click into individual property pages

## Key Search Tips

- **Owner names** are typically stored as `LAST FIRST` (e.g., "SMITH JOHN")
- Use partial names for broader matches (e.g., just "SMITH" instead of "SMITH JOHN")
- When searching for a person's address, search by owner name and look at `situs_address`
- The `owner_address` is the mailing address (may differ from property location)
- Homestead exemption (`exempthmstdflag`) indicates primary residence

## Output Fields (Collin CAD)

Key fields returned from Collin County searches:
- `owner_name` - Property owner (LAST FIRST format)
- `situs_address` - Physical property address
- `owner_address` - Owner's mailing address
- `market_value` - Current market value
- `appraised_value` - Appraised value
- `assessed_value` - Assessed (taxable) value
- `year_built` - Year structure built
- `main_area_sqft` - Living area square feet
- `legal_description` - Legal description
- `deed_number` / `deed_date` - Deed information

For full field reference, see `references/data_sources.md`.

## Adding New Counties

To add a new county:
1. Check if the county publishes data on a Socrata portal
2. If yes, add to `COUNTY_REGISTRY` in `scripts/property_search.py`
3. If no, add as `web_search` source with portal URL
4. See `references/data_sources.md` for details
