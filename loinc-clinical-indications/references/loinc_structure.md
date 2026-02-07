# LOINC Code Structure and Terminology

## LOINC Code Format

LOINC codes use the format: `NNNNN-N` where NNNNN is a numeric identifier and the final N is a check digit.

**Examples:**
- `2345-7` - Glucose in Serum/Plasma
- `718-7` - Hemoglobin in Blood
- `4548-4` - Hemoglobin A1c in Blood

## LOINC Part Codes

Part codes are prefixed with `LP` and represent individual components of the 6-axis structure.

**Format:** `LPNNNNN-N`

**Examples:**
- `LP14559-6` - Glucose (Component)
- `LP7057-5` - Serum or Plasma (System)


## The 6-Axis Structure

Each LOINC code is defined by 6 axes ("Parts"):

| Axis | Description | Example |
|------|-------------|---------|
| **Component** | What is measured/observed | Glucose, Hemoglobin, Sodium |
| **Property** | Characteristic being measured | Mass concentration, Number concentration |
| **Time** | Point in time or time interval | Pt (point in time), 24H (24-hour collection) |
| **System** | Specimen or body site | Blood, Serum, Urine, CSF |
| **Scale** | Type of value | Qn (quantitative), Ord (ordinal), Nom (nominal) |
| **Method** | How measurement is made (optional) | Hexokinase, Manual count, Automated |


## LOINC Classes

Major classes of LOINC codes:

| Class | Description |
|-------|-------------|
| **CHEM** | Chemistry tests |
| **HEM/BC** | Hematology/Blood cell counts |
| **SERO** | Serology/Immunology |
| **MICRO** | Microbiology |
| **UA** | Urinalysis |
| **COAG** | Coagulation |
| **DRUG/TOX** | Drug/Toxicology |
| **PANEL.CHEM** | Chemistry panels |
| **PANEL.UA** | Urinalysis panels |


## Common Abbreviations

| Abbreviation | Meaning |
|--------------|---------|
| MCnc | Mass concentration |
| NCnc | Number concentration |
| CCnc | Catalytic concentration |
| ACnc | Arbitrary concentration |
| Pt | Point in time |
| Qn | Quantitative |
| Ord | Ordinal |
| Nom | Nominal |
| Ser/Plas | Serum or Plasma |
| Bld | Blood |
| CSF | Cerebrospinal fluid |
