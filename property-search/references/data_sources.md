# Property Search Data Sources Reference

## Table of Contents
1. [Socrata SODA API](#socrata-soda-api)
2. [Collin CAD (Texas) - Primary](#collin-cad-texas)
3. [Cook County (Illinois)](#cook-county-illinois)
4. [Texas Counties Web Portals](#texas-counties-web-portals)
5. [Other State Web Portals](#other-state-web-portals)
6. [Adding New Counties](#adding-new-counties)
7. [Commercial APIs](#commercial-apis)

---

## Socrata SODA API

The Socrata Open Data API (SODA) is the primary API used by this skill. Many government entities publish property data through Socrata-powered portals.

### Base URL Pattern
```
https://{domain}/resource/{dataset_id}.json
```

### SoQL Query Reference
- `$where` - Filter clause (SQL-like): `$where=upper(ownername) like '%SMITH%'`
- `$limit` - Max records: `$limit=100`
- `$offset` - Pagination: `$offset=100`
- `$order` - Sort: `$order=ownername ASC`
- `$select` - Fields: `$select=ownername,situsconcat,currvalmarket`
- `$q` - Full-text search: `$q=smith main street`

### LIKE Operator for Partial Match
```
$where=upper(ownername) like upper('%SMITH JOHN%')
```
Use `%` as wildcard. Use `upper()` for case-insensitive search.

### App Tokens
Optional but recommended to avoid throttling. Register at https://dev.socrata.com/
Pass via header `X-App-Token` or query param `$$app_token`.

### Rate Limits
- Without token: ~67 requests/minute
- With token: higher limits

---

## Collin CAD (Texas)

**Display Name:** Collin Central Appraisal District
**Web Portal:** https://www.collincad.org/property-search
**Data Portal:** https://data.texas.gov

### Datasets on data.texas.gov
| Year | Dataset ID | Notes |
|------|-----------|-------|
| 2022 | `vtby-uz4n` | Certified values |
| 2023 | `kfq3-t3pb` | Certified values |
| Preliminary | `sn6q-rxgx` | Current year preliminary |

### Key API Fields
| Field | API Name | Description |
|-------|----------|-------------|
| Property ID | `propid` | Unique property identifier |
| Geo ID | `geoid` | Geographic identifier |
| Property Year | `propyear` | Tax year |
| Property Type | `proptype` | Real / Personal |
| Subtype | `propsubtype` | Residential / Commercial / etc. |
| Owner Name | `ownername` | Property owner (LAST FIRST format) |
| Owner ID | `ownerid` | Owner identifier |
| Owner Address Line 1 | `owneraddrline1` | Mailing address |
| Owner City | `owneraddrcity` | Mailing city |
| Owner State | `owneraddrstate` | Mailing state |
| Owner Zip | `owneraddrzip` | Mailing zip |
| Situs Address (full) | `situsconcat` | Full property address with city/zip |
| Situs Address (short) | `situsconcatshort` | Street address only |
| Situs City | `situscity` | Property city |
| Situs Zip | `situszip` | Property zip |
| Market Value | `currvalmarket` | Current market value |
| Appraised Value | `currvalappraised` | Appraised value |
| Assessed Value | `currvalassessed` | Assessed (taxable) value |
| Land Value | `currvalland` | Land only value |
| Improvement Value | `currvalimprv` | Improvements value |
| Year Built | `imprvyearbuilt` | Year structure built |
| Main Area | `imprvmainarea` | Main living area (sqft) |
| Pool | `imprvpoolflag` | Has pool (true/false) |
| Land Acres | `landsizeacres` | Land size in acres |
| Land Sqft | `landsizesqft` | Land size in square feet |
| Homestead | `exempthmstdflag` | Homestead exemption flag |
| Exemptions | `exemptcodes` | Exemption codes |
| Deed Number | `deednum` | Deed document number |
| Deed Date | `deedeffdate` | Deed effective date |
| Legal Description | `legaldescription` | Legal property description |
| School District | `entityschoolcode` | School district code |
| City Code | `entitycitycode` | City entity code |
| Neighborhood | `nbhdcode` | Neighborhood code |
| Status | `propstatus` | Certified/Preliminary |

### Example Queries
```
# Search by owner name containing "SMITH"
https://data.texas.gov/resource/vtby-uz4n.json?$where=upper(ownername) like '%SMITH%'&$limit=50

# Search by address
https://data.texas.gov/resource/vtby-uz4n.json?$where=upper(situsconcat) like '%MAIN ST%'&$limit=50

# Search by property ID
https://data.texas.gov/resource/vtby-uz4n.json?$where=propid='1234567'

# Get high-value properties
https://data.texas.gov/resource/vtby-uz4n.json?$where=currvalmarket > 1000000&$order=currvalmarket DESC&$limit=20
```

---

## Cook County (Illinois)

**Display Name:** Cook County Assessor
**Web Portal:** https://www.cookcountyassessor.com/
**Data Portal:** https://datacatalog.cookcountyil.gov

### Datasets
| Dataset | ID | Notes |
|---------|-----|-------|
| Assessments | `uzyt-m557` | Property assessments |

### Key Fields
- `pin` - Property Index Number
- `taxpayer_name` - Owner/Taxpayer name
- `property_address` - Property address

---

## Texas Counties Web Portals

These counties do not have direct SODA APIs but have web search portals:

| County | Portal URL | Search Capabilities |
|--------|-----------|-------------------|
| Dallas | dallascad.org | Owner, Address, Account# |
| Denton | dentoncad.com | Owner, Address, ID |
| Tarrant | tad.org | Owner, Address, Account# |
| Travis | traviscad.org | Owner, Address, Geo ID |
| Harris | hcad.org | Owner, Address, Account# |
| Williamson | wcad.org | Owner, Address, Prop ID |

For web-only counties, use `browser_subagent` to navigate and extract data.

---

## Other State Web Portals

| State | County | Portal URL |
|-------|--------|-----------|
| FL | Miami-Dade | miamidade.gov/pa/ |
| FL | Broward | web.bcpa.net |
| CA | Los Angeles | portal.assessor.lacounty.gov |
| AZ | Maricopa | mcassessor.maricopa.gov |

---

## Adding New Counties

### For Socrata-based sources
1. Find the dataset on the data portal (e.g., data.texas.gov, datacatalog.cookcountyil.gov)
2. Note the domain and dataset ID from the URL
3. Identify key field names: owner, address, property ID
4. Add entry to `COUNTY_REGISTRY` in `property_search.py`

### For web-only sources
1. Add entry with `"source": "web_search"` and the portal URL
2. Use `browser_subagent` to scrape results when searching

### Custom Socrata Endpoint (no registry change needed)
```bash
python property_search.py --mode owner --query "SMITH" \
  --source socrata --domain data.example.gov --dataset-id xxxx-yyyy \
  --owner-field owner_name --address-field prop_address
```

---

## Commercial APIs (for reference)
These paid services aggregate data nationally:
- **ATTOM** - 158M+ records, 3000+ counties
- **CoreLogic** - 99.99% US coverage
- **RealEstateAPI.com** - 159M properties, owner search
- **TaxNetUSA** - All TX and FL counties, Web API
- **Melissa** - Property Cloud API, address-based lookup
