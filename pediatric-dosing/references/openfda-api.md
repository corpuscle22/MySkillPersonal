# openFDA API Reference

Reference guide for querying the openFDA Drug Label API for condition-based medication lookup.

## API Overview

- **Base URL**: `https://api.fda.gov/drug/label.json`
- **Format**: JSON
- **No authentication required** (limited to 240 requests/minute without API key)

## Key Endpoints

### Search Drug Labels

```
GET https://api.fda.gov/drug/label.json?search=<query>&limit=<n>
```

### Useful Search Fields

| Field | Description |
|-------|-------------|
| `indications_and_usage` | FDA-approved indications |
| `pediatric_use` | Pediatric-specific information |
| `dosage_and_administration` | Dosing guidance |
| `warnings` | Safety warnings |
| `contraindications` | Contraindications |

## Example Queries

**Search by condition:**
```
?search=indications_and_usage:"asthma"&limit=10
```

**Filter to drugs with pediatric labeling:**
```
?search=indications_and_usage:"asthma"+AND+_exists_:pediatric_use&limit=10
```

**Search by generic name:**
```
?search=openfda.generic_name:"amoxicillin"&limit=5
```

## Response Structure

```json
{
  "results": [
    {
      "openfda": {
        "brand_name": ["AMOXIL"],
        "generic_name": ["AMOXICILLIN"],
        "rxcui": ["308182", "308183"]
      },
      "indications_and_usage": ["..."],
      "pediatric_use": ["..."],
      "dosage_and_administration": ["..."]
    }
  ]
}
```

## Pediatric-Relevant Fields

- `pediatric_use` - Specific pediatric safety/efficacy data
- `dosage_and_administration` - Often includes pediatric dosing
- `use_in_specific_populations` - May include pediatric info

## Rate Limits

- Without API key: 240 requests/minute, 120,000/day
- With API key: 240 requests/minute, unlimited daily
