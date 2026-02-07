---
name: loinc-clinical-indications
description: Identify clinical indications (diseases and conditions) for a given LOINC code, LOINC code title, LOINC part code, or LOINC part title. Use when a user needs to find what diseases, conditions, or clinical scenarios a laboratory test or clinical observation is used to diagnose. Supports both full LOINC codes (e.g., 2345-7) and LOINC part codes (LP-prefixed, e.g., LP14559-6).
---

# LOINC Clinical Indications

Identify clinical indications (diseases and conditions) for a given LOINC code or LOINC part code, with cited medical reference sources.

## Overview

This skill helps identify which diseases and conditions a LOINC-coded test or observation is used to diagnose. Given a LOINC code, part code, or search term, it returns a list of clinical indications with authoritative source citations and URLs.

## Workflow

### Step 1: Identify the LOINC Code

If the user provides:
- **LOINC code number** (e.g., `2345-7`): Use directly
- **LOINC part code** (LP-prefixed, e.g., `LP14559-6`): Use directly (treat same as full codes)
- **Test name or description**: Run `scripts/loinc_lookup.py` to find the LOINC code

```bash
python scripts/loinc_lookup.py "glucose blood"
python scripts/loinc_lookup.py 2345-7
```

### Step 2: Get LOINC Code Details

Run the lookup script to retrieve full LOINC information:

```bash
python scripts/loinc_lookup.py <code-or-search-term>
```

This returns:
- LOINC code number
- Long common name
- Component (what's being measured)
- System (specimen type)
- Related codes (if applicable)

### Step 3: Research Clinical Indications with Trusted Sources

Perform web searches prioritizing authoritative medical sources. Reference `references/trusted_sources.md` for approved sources.

**Search strategy:**
1. Search: `site:medscape.com [test name] indications`
2. Search: `site:merckmanuals.com [test name] diagnosis`
3. Search: `site:pubmed.ncbi.nlm.nih.gov [test name] clinical indications`
4. General search: `"[component name] test" clinical indications diagnosis`

**Source priority (use Tier 1 first):**
- **Tier 1:** Medscape, Merck Manual, UpToDate, PubMed, Mayo Clinic, Cleveland Clinic
- **Tier 2:** NIH, CDC, MedlinePlus, FDA, WHO
- **Tier 3:** ARUP Consult, Lab Tests Online, specialty societies (ACR, AHA, etc.)

**Avoid:** Wikipedia, health blogs, commercial lab marketing, non-peer-reviewed sources.

### Step 4: Return Indications with Source Citations

Format output as a list with source name and URL for each indication.

### Step 5: Research and Comment on US Clinical Utilization

Research and include a comment about whether the test is frequently done in US clinical care. This helps users understand how commonly the test is ordered in routine practice.

**Research strategy:**
1. Search: `"[test name]" common laboratory test ordering frequency`
2. Search: `"[test name]" routine clinical practice guidelines`
3. Check if test is part of standard panels (BMP, CMP, CBC, lipid panel, etc.)
4. Look for information from major reference labs (Quest, LabCorp, ARUP, Mayo)

**Classification categories:**
- **Very Common (Routine):** Part of standard panels, ordered daily in most clinical settings (e.g., glucose, CBC, BMP components)
- **Common:** Frequently ordered for specific clinical scenarios, available at most hospitals (e.g., TSH, HbA1c, lipid panel)
- **Moderately Common:** Ordered regularly for specific conditions, available at most reference labs (e.g., autoimmune panels, vitamin levels)
- **Uncommon/Specialized:** Ordered for rare conditions, may require specialized reference labs (e.g., rare metabolic disorders, obscure autoantibodies)
- **Rare/Research:** Primarily research use, limited clinical availability, may only be available at academic centers

**Include in output:**
- A brief statement on US clinical utilization frequency
- Note if test requires specialized reference laboratory
- Mention if test is part of common panels or reflex testing

**Example for LOINC 2345-7 (Glucose [Mass/volume] in Serum or Plasma):**

## LOINC 2345-7: Glucose [Mass/volume] in Serum or Plasma

**Component:** Glucose  
**Specimen:** Serum or Plasma

### US Clinical Utilization:
> **Very Common (Routine)** — Glucose is one of the most frequently ordered laboratory tests in US clinical care. It is included in both the Basic Metabolic Panel (BMP) and Comprehensive Metabolic Panel (CMP), which are standard tests ordered millions of times annually. Available at all clinical laboratories.

### Clinical Indications:

- Diabetes mellitus (Type 1 and Type 2) — [Medscape](https://emedicine.medscape.com/article/117739-workup)
- Prediabetes / Impaired glucose tolerance — [CDC](https://www.cdc.gov/diabetes/basics/prediabetes.html)
- Hypoglycemia — [Merck Manual](https://www.merckmanuals.com/professional/endocrine-and-metabolic-disorders/hypoglycemia)
- Gestational diabetes — [ACOG](https://www.acog.org/clinical/clinical-guidance/practice-bulletin/articles/2018/02/gestational-diabetes-mellitus)
- Diabetic ketoacidosis (DKA) — [PubMed](https://pubmed.ncbi.nlm.nih.gov/...)
- Metabolic syndrome — [Mayo Clinic](https://www.mayoclinic.org/diseases-conditions/metabolic-syndrome)

## Resources

### scripts/
- `loinc_lookup.py` - Query NIH Clinical Tables API for LOINC code information

### references/
- `loinc_structure.md` - LOINC code structure and terminology
- `clinical_categories.md` - Clinical indication patterns by test category
- `trusted_sources.md` - Authoritative medical reference sources for citations

