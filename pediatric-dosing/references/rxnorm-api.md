# RxNorm API Reference

Reference guide for querying the RxNorm REST API to retrieve Semantic Clinical Drug (SCD) codes.

## API Overview

- **Base URL**: `https://rxnav.nlm.nih.gov/REST`
- **Format**: JSON or XML (append `.json` to endpoints for JSON)
- **No authentication required**

## Key Term Types (TTY)

| TTY | Description | Use Case |
|-----|-------------|----------|
| **SCD** | Semantic Clinical Drug | Generic drug with ingredient + strength + dose form |
| SBD | Semantic Branded Drug | Brand name version (exclude per requirements) |
| IN | Ingredient | Active ingredient only |
| SCDC | Semantic Clinical Drug Component | Ingredient + strength |
| SCDF | Semantic Clinical Dose Form | Ingredient + dose form |

**Important**: This skill uses SCD only. Exclude all other term types.

## Primary Endpoints

### getDrugs
Get drug products by name.

```
GET /REST/drugs.json?name={drugName}
```

**Response structure:**
```json
{
  "drugGroup": {
    "conceptGroup": [
      {
        "tty": "SCD",
        "conceptProperties": [
          {
            "rxcui": "308182",
            "name": "amoxicillin 250 MG/5ML Oral Suspension",
            "tty": "SCD"
          }
        ]
      }
    ]
  }
}
```

### getRelatedByType
Get related concepts filtered by term type.

```
GET /REST/rxcui/{rxcui}/related.json?tty=SCD
```

### getRxConceptProperties
Get properties for a specific RxCUI.

```
GET /REST/rxcui/{rxcui}/properties.json
```

## Filtering to SCD

When parsing API responses, filter `conceptGroup` entries where `tty == "SCD"`. Each matching group contains `conceptProperties` with:

- `rxcui` - RxNorm Concept Unique Identifier
- `name` - Full drug name (ingredient + strength + dose form)
- `tty` - Term type (will be "SCD")

## Common Pediatric Formulation Keywords

Filter SCD names containing these keywords for pediatric-appropriate forms:

- `Oral Suspension`
- `Oral Solution`
- `Chewable Tablet`
- `Oral Drops`
- `Syrup`
- `Elixir`
- `Disintegrating Tablet`
- `Powder for`
- `Granules`

## Example Queries

**Amoxicillin suspensions:**
```
https://rxnav.nlm.nih.gov/REST/drugs.json?name=amoxicillin
```
Filter response to SCD entries containing "Oral Suspension"

**Ibuprofen pediatric forms:**
```
https://rxnav.nlm.nih.gov/REST/drugs.json?name=ibuprofen
```
Filter to SCD entries with suspension/chewable keywords
