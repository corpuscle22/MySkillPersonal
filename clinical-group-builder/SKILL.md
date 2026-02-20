---
name: clinical-group-builder
description: >-
  Generate clinically sound group definitions for laboratory result or medication groups from a
  proposed group title or free-text clinical intent. Use when the user provides a group name
  (e.g., "Vitamin B laboratory result," "Anticoagulant medication," "Liver function laboratory
  result," "Opioid medication") and needs a structured clinical scope statement, inclusion/exclusion
  criteria, LOINC or RxNorm component-level terminology mapping, and a JIRA-ready summary. Supports both
  "laboratory result" groups (mapped to LOINC components) and "medication" groups (mapped to RxNorm
  ingredients). Triggers on requests involving: defining a clinical group, building a value set,
  scoping a lab or medication panel, creating inclusion/exclusion criteria for clinical content,
  or producing JIRA-ready group definitions.
---

# Clinical Group Builder

Generate clinically rigorous group definitions from a proposed group title or free-text clinical intent, with component-level terminology mapping and JIRA-ready output.

## Overview

This skill accepts a group title or clinical intent (e.g., "Thyroid function laboratory result" or "NSAID medication") and produces:

1. A **Clinical Scope Statement** defining what is in/out of scope
2. **Inclusion and Exclusion Criteria** grounded in clinical best practices
3. A **Recommended Group Title** conforming to naming conventions
4. **Component-Level Terminology Mapping** (LOINC components for labs, RxNorm ingredients for medications) — **not** individual LOINC codes; the grouping operates at the analyte/concept level
5. **Relevant Clinical Specialties**
6. A **JIRA-Ready Summary** for direct copy-paste

## Key Design Principle: Component-Level Grouping

**Group definitions operate at the LOINC component (analyte/concept) level, not at the individual LOINC code level.**

- For **lab groups**: List the *components* (e.g., "Thiamine," "Folate," "Methylmalonate") that should be included or excluded, not every individual LOINC code variant for specimen type, property, or method.
- For **medication groups**: List the *ingredients* (e.g., "Warfarin," "Apixaban") at the RxNorm IN/MIN level, not every dose form or branded product.
- This approach is more maintainable, clinically intuitive, and avoids bloating the definition with hundreds of individual codes.
- When specimen type, property, or method distinctions matter, capture them as **inclusion/exclusion criteria** rather than per-code entries.

## Workflow

### Step 1: Classify the Group Type

Determine whether the input describes a **laboratory result** group or a **medication** group.

**Laboratory result indicators:** test names, analytes, biomarkers, panels, specimen types, "lab," "assay," "measurement," "level"
**Medication indicators:** drug names, drug classes, therapeutic categories, "medication," "drug," "prescription," "therapy"

If ambiguous, ask the user:
> "Should this group cover laboratory results (mapped to LOINC) or medications (mapped to RxNorm)?"

### Step 2: Clarify Clinical Intent

Before generating the group definition, ask **targeted** clarifying questions when the input is ambiguous or scope-dependent. The goal is to establish:

- **Clinical use case** — screening, diagnostic confirmation, monitoring, prescribing, history review, exposure surveillance, contraindication screening
- **Population** — general, pediatric, neonatal, pregnant, geriatric
- **Setting** — primary care, specialty, inpatient, ED, reference lab
- **Scope boundaries** — See `references/clarification_patterns.md` for domain-specific question templates

**Rules for clarifying questions:**
- Ask at most 3 questions per round to avoid overwhelming the user
- Lead with the highest-impact question (the one that most changes the resulting scope)
- If the user's intent is clear and unambiguous, proceed without asking (e.g., "CBC laboratory result" needs no clarification)
- Offer sensible defaults: "Unless you specify otherwise, I'll assume a general adult population in a hospital or outpatient setting."

### Step 3: Research Using Sibling Skills

Before performing the clinical assessment, **leverage other available skills** to build a comprehensive evidence base. This ensures the group definition is grounded in current clinical practice, not just terminology lookups.

#### 3a. Use `POF` (Point of Care Evidence) for Clinical Context

When you need to understand **which tests or medications are recommended for a clinical condition** (the "why" behind the group), invoke the POF skill's research workflow:

```
# Use POF's research strategy to identify what tests/medications are clinically recommended
# Reference: ../POF/SKILL.md -> Step 1 (Research Current Evidence)
```

**When to use POF:**
- When the group intent maps to a clinical condition (e.g., "B12 deficiency workup" informs "Vitamin B laboratory result")
- When you need evidence grading or guideline support for inclusion/exclusion decisions
- When you need to identify reference lab panel compositions and ordering conventions
- When you need to research confirmatory/reflex testing pathways

**POF resources to reference:**
- `../POF/references/trusted_sources.md` — Tiered source hierarchy for evidence quality
- `../POF/references/guideline_organizations.md` — US guideline bodies by specialty
- `../POF/references/reference_labs_and_panels.md` — Major US reference lab catalogs and panel compositions

#### 3b. Use `loinc-clinical-indications` for LOINC Lookups

For laboratory result groups, use the LOINC lookup script to **discover relevant LOINC components** and verify analyte names:

```bash
python ../loinc-clinical-indications/scripts/loinc_lookup.py "<analyte name>"
```

**Purpose in this skill:** Use the lookup results to identify the correct LOINC **component names** for the terminology mapping table — you do NOT need to enumerate every individual LOINC code. Instead, note the component names returned and group them logically.

**When to use:**
- To verify correct LOINC component names for each analyte
- To discover related analytes you may have missed (e.g., searching "thiamine" reveals both "Thiamine" and "Thiamine pyrophosphate" components)
- To confirm specimen types available for an analyte
- To identify deprecated or unexpected codes to add to exclusion criteria

#### 3c. Use `medication-query` for Medication Intelligence

For medication groups, use the medication-query skill to enrich medication data:

```bash
python ../medication-query/scripts/lookup.py "<drug name or RxCUI>"
```

**Purpose in this skill:** Retrieve RxCUI, drug class, mechanism of action, and FDA-approved indications to inform:
- Whether a medication belongs in the group (clinical intent alignment)
- Drug class categorization for the terminology table
- Distinguishing FDA-approved vs. off-label use when relevant to inclusion criteria

**When to use:**
- To verify drug names, RxCUIs, and drug classes for medication groups
- To understand the therapeutic role of borderline-inclusion medications
- To identify combination products, prodrugs, or related agents

### Step 4: Perform Clinical Assessment

This is the **clinical reasoning** phase — identify what tests or medications are clinically appropriate for the stated intent, informed by the research from Step 3.

#### For Laboratory Result Groups

1. **Identify core analytes/components** that directly fulfill the clinical intent
2. **Consider related components** — metabolites, functional biomarkers, confirmatory tests, reflex tests
3. **Check common commercial panels** — Reference ordering conventions from major US labs (Quest, LabCorp, ARUP, Mayo) to inform practical scope boundaries. See `references/lab_panel_conventions.md` and `../POF/references/reference_labs_and_panels.md`
4. **Assess specimen types** — Determine whether to scope to a single specimen or include multiple (serum, urine, CSF, etc.) — express this as inclusion/exclusion criteria, not as separate entries per specimen
5. **Evaluate properties** — Mass concentration vs. molar concentration vs. enzymatic activity, quantitative vs. qualitative — the group should be property-agnostic by default
6. **Flag edge cases** — Research-only assays, obsolete tests, calculated results, ratios, point-of-care vs. central lab

#### For Medication Groups

1. **Identify core drug classes and agents** that directly fulfill the clinical intent
2. **Consider related agents** — combination products, prodrugs, biosimilars, OTC equivalents
3. **Assess formulation scope** — oral, injectable, topical, ophthalmic, etc.
4. **Evaluate ingredient level vs. clinical drug** — Default to Ingredient (IN) level; use SCD/SBD only when formulation specificity is clinically necessary
5. **Flag edge cases** — Investigational drugs, compounded preparations, herbal/supplement equivalents, veterinary-only agents

### Step 5: Map to Terminology Standards (Component Level)

After the clinical assessment, map the identified items to their **component-level** terminology codes.

#### Laboratory Result Groups → LOINC Components

For each identified analyte:
1. Run `loinc_lookup.py` to confirm the correct LOINC **component name** (e.g., "Thiamine," "Thiamine pyrophosphate," "Folate")
2. Record the component name, its clinical category within the group, and the grouping rationale
3. Note specimen scope and property scope as **group-level criteria**, not per-component entries
4. Do **NOT** enumerate individual LOINC codes — the table lists components (analyte concepts)

```bash
python ../loinc-clinical-indications/scripts/loinc_lookup.py "<analyte>"
```

#### Medication Groups → RxNorm Ingredients

For each identified medication:
1. Run the medication-query lookup to confirm the correct RxNorm ingredient name and RxCUI
2. Record at the **IN** (Ingredient) or **MIN** (Multiple Ingredients) level
3. Note formulation scope as a **group-level criterion**, not per-ingredient

```bash
python ../medication-query/scripts/lookup.py "<drug name>"
```

### Step 6: Compose the Output

Generate the full output using the template in `references/output_template.md`. The output must include all six sections in order.

**Critical output rules:**
- All clinical assertions must cite authoritative sources (Tier 1–3 per `references/trusted_sources.md` or `../POF/references/trusted_sources.md`)
- The Clinical Scope Statement must be a single paragraph
- The Recommended Group Title must end with "laboratory result" (for lab groups) or "medication" (for medication groups)
- The JIRA-Ready Summary must be directly copy-pasteable
- The terminology table lists **components/ingredients**, not individual codes
- Specimen, property, and method scope are expressed as group-level criteria in the inclusion/exclusion section

### Step 7: Save Output

Save the completed group definition to the `output/` directory:

```
output/<group-title-slug>_group_definition.md
```

Use lowercase, hyphenated slug derived from the recommended group title (e.g., `vitamin-b-measurement-and-related-tests-laboratory-result_group_definition.md`).

## Resources

### Sibling Skills (used during research)
- `../loinc-clinical-indications/` — LOINC code lookup and clinical indications research (scripts/loinc_lookup.py)
- `../medication-query/` — Medication information, RxCUI lookup, drug class, and indications (scripts/lookup.py)
- `../POF/` — Evidence-based clinical research, guideline synthesis, reference lab panel compositions, trusted source hierarchy

### references/
- `output_template.md` — Required output structure and formatting template (component-level)
- `clarification_patterns.md` — Domain-specific clarifying question templates
- `lab_panel_conventions.md` — Common US commercial lab panel compositions for scope reference
- `trusted_sources.md` — Tiered list of authoritative medical reference sources
