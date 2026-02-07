---
name: pediatric-dosing
description: Calculate weight-based pediatric medication dosing and retrieve RxNorm SCD codes. Use when the user needs to (1) identify appropriate medications for a pediatric clinical condition, (2) calculate weight-based dosing for a child, (3) find RxNorm Semantic Clinical Drug (SCD) codes for pediatric formulations, or (4) determine appropriate formulations for a child's age/weight. Only returns SCD term types (excludes SBD and other RxNorm types). Focuses on pediatric-appropriate formulations like oral suspensions, chewables, and drops.
---

# Pediatric Medication Dosing

Calculate pediatric medication doses and retrieve RxNorm SCD codes for appropriate formulations.

## Workflow

1. **Look up condition** → Query openFDA or check static references
2. **Select medication** → Use FDA-approved drug with pediatric labeling
3. **Calculate dose** → Apply weight-based formula
4. **Select formulation** → Choose age-appropriate form
5. **Get RxNorm SCD** → Query for SCD codes

## Step 1: Condition → Medication Lookup

### Option A: Dynamic Lookup (Scalable)
Query openFDA for any condition:

```bash
python scripts/openfda_condition_lookup.py "<condition>" --pediatric-only
```

Returns FDA-approved drugs with:
- Generic/brand name
- Indications
- Pediatric use information
- Dosage guidance
- RxCUI identifiers

### Option B: Static Reference (Common Conditions)
For guidelines-based recommendations, see [condition-medications.md](references/condition-medications.md).

## Step 2-3: Weight-Based Dosing

```
Dose (mg) = Weight (kg) × Dose (mg/kg)
Volume (mL) = Dose (mg) ÷ Concentration (mg/mL)
```

See [dosing-guidelines.md](references/dosing-guidelines.md) for common medications.

## Step 4: Formulation Selection by Age

| Age | Preferred Formulation |
|-----|----------------------|
| 0-12 months | Drops, concentrated suspension |
| 6 months - 6 years | Oral suspension |
| 2-12 years | Chewable tablets, suspension |
| 6+ years | Orally disintegrating tablets |
| 8+ years | Standard tablets/capsules |

## Step 5: RxNorm SCD Lookup

```bash
python scripts/rxnorm_scd_lookup.py <drug_name> --pediatric-only
```

Returns **SCD codes only** (excludes SBD). See [rxnorm-api.md](references/rxnorm-api.md).

## Output Format

```
CONDITION: [Clinical condition]
SOURCE: [openFDA / Guideline citation]

MEDICATION: [Drug name]
INDICATION: [FDA-approved indication]
PEDIATRIC USE: [Pediatric labeling summary]
DOSE: [Calculated dose with formula]
FORMULATION: [Age-appropriate form]

RxNorm SCD:
  RxCUI: [identifier]
  Name: [full SCD name]
  TTY: SCD
```

## Data Sources

| Data | Source |
|------|--------|
| Condition → Medication (dynamic) | openFDA Drug Label API |
| Condition → Medication (static) | AAP, NASPGHAN, GINA, IDSA guidelines |
| Dosing | Published pediatric references |
| RxNorm SCD codes | NIH RxNorm API |
