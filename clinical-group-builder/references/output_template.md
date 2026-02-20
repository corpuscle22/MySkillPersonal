# Output Template

Use this template for all group definition outputs. All six sections are required.

**Key principle:** Terminology tables list **components** (analyte concepts for labs, ingredient concepts for meds) — NOT individual LOINC codes or RxNorm dose forms. Specimen scope, property scope, and method scope are expressed as group-level criteria in the inclusion/exclusion section.

---

## Section 1: Clinical Scope Statement

A single paragraph that defines:
- The clinical intent of the group
- What is explicitly in scope
- What is explicitly out of scope
- Key clinical boundaries that make the group meaningful and usable

**Format:**

> **Clinical Scope Statement:** This group captures [what it measures/covers] used in [clinical context]. It includes [key inclusions]. It excludes [key exclusions]. The group is bounded by [key boundaries such as specimen type, population, method, or formulation constraints].

**Example (Lab):**

> **Clinical Scope Statement:** This group captures laboratory tests that measure the vitamin B family of nutrients and their functional biomarkers, used in the evaluation of nutritional deficiency, malabsorption, and hematologic workup. It includes direct measurements of vitamins B1, B2, B3, B5, B6, B7, B9 (folate), and B12 (cobalamin), as well as functional biomarkers (methylmalonic acid, homocysteine) that are routinely used to confirm deficiency states. It excludes research-only metabolite profiling, genetic assays for inborn errors of metabolism (e.g., MTHFR genotyping), and allergy antibody panels. The group is method-agnostic, property-agnostic, and includes all clinically relevant specimen types.

**Example (Medication):**

> **Clinical Scope Statement:** This group captures medications classified as oral anticoagulants used in the prevention and treatment of thromboembolic disease. It includes direct oral anticoagulants (DOACs: apixaban, rivaroxaban, edoxaban, dabigatran) and vitamin K antagonists (warfarin). It excludes parenteral anticoagulants (heparin, enoxaparin), antiplatelet agents (aspirin, clopidogrel), and thrombolytics. The group is bounded to oral formulations with FDA-approved indications for anticoagulation.

---

## Section 2: Inclusion Criteria and Exclusion Criteria

Two clearly separated tables derived from clinical best practices and real-world ordering/prescribing patterns.

**Format:**

### Inclusion Criteria

| # | Criterion | Rationale |
|---|-----------|-----------|
| 1 | Criterion text | Rationale text |
| 2 | [Nuanced rule]: Include [item] **only when** [condition] | Rationale |

### Exclusion Criteria

| # | Criterion | Rationale |
|---|-----------|-----------|
| 1 | Criterion text | Rationale text |
| 2 | [Nuanced rule]: Exclude [item] **unless** [condition] | Rationale |

**Guidelines:**
- Each criterion must have a brief rationale
- Use "Include X only when Y" or "Exclude X unless Y" for nuanced conditional rules
- Cite ordering patterns or guidelines when possible (e.g., "per ADA 2024 Standards of Care")
- **Group-level scope rules** (specimen types, properties, methods) belong HERE, not in the terminology table
  - Example: "Include all clinically relevant specimen types (serum, plasma, whole blood, RBC, urine, CSF)"
  - Example: "Property-agnostic: include mass concentration (MCnc), molar concentration (SCnc), and qualitative (PrThr)"
  - Example: "Method-agnostic: include all assay methods (immunoassay, LC-MS/MS, RIA, microbiologic)"

---

## Section 3: Recommended Group Title

A succinct, descriptive title derived from the finalized scope and criteria.

**Rules:**
- Lab groups MUST end with "laboratory result" (e.g., "Vitamin B measurement and related tests laboratory result")
- Medication groups MUST end with "medication" (e.g., "Oral anticoagulant medication")
- Use standard clinical terminology, not brand names
- Keep concise (typically 2–6 words plus the suffix)

**Format:**

### Recommended Group Title

> **[Title] laboratory result** or **[Title] medication**

---

## Section 4: Terminology Mapping Table (Component Level)

A structured table mapping each included **component** (analyte concept for labs, ingredient concept for meds) to its clinical category and grouping rationale.

**For Laboratory Result Groups (LOINC Components):**

| # | Component | Vitamin / Category | Clinical Role | Specimen Types | Grouping Rationale |
|---|-----------|--------------------|---------------|----------------|--------------------|
| 1 | Thiamine | B1 | Direct measurement | Ser/Plas, Bld | Core analyte |
| 2 | Thiamine pyrophosphate | B1 | Active metabolite | Ser, Bld | Biologically active form |
| 3 | Methylmalonate | Functional biomarker | B12 confirmatory | Ser/Plas, Ur | Elevated in B12 deficiency |

**Column definitions:**
- **Component**: The LOINC Component name (analyte concept). This is the grouping level.
- **Vitamin / Category**: Which vitamin or functional category the component belongs to.
- **Clinical Role**: Direct measurement, active metabolite, functional biomarker, interpretive, transport protein, autoantibody, etc.
- **Specimen Types**: Which specimen types are relevant for this component (group-level criteria apply; this column indicates typical specimens).
- **Grouping Rationale**: Why this component is included in the group.

**For Medication Groups (RxNorm Ingredients):**

| # | Ingredient | Drug Class | RxCUI | Therapeutic Role | Grouping Rationale |
|---|------------|------------|-------|------------------|--------------------|
| 1 | Warfarin | Vitamin K antagonist | 11289 | Core anticoagulant | Standard of care |
| 2 | Apixaban | Direct Factor Xa inhibitor | 1364430 | Core anticoagulant | First-line DOAC |

**Column definitions:**
- **Ingredient**: RxNorm Ingredient (IN) or Multiple Ingredient (MIN) name.
- **Drug Class**: Pharmacologic/therapeutic class.
- **RxCUI**: RxNorm Concept Unique Identifier at the IN/MIN level.
- **Therapeutic Role**: First-line, alternative, adjunctive, etc.
- **Grouping Rationale**: Why this ingredient is included.

**Guidelines:**
- Order by clinical importance or logical grouping (not alphabetically)
- For lab groups: list at the **LOINC Component** level — not individual LOINC codes
- For medication groups: list at the **Ingredient (IN)** level — not individual dose forms
- Specimen type and property scope for labs are captured in Section 2 (Inclusion Criteria), not repeated per-component
- Each component/ingredient should appear **once**, regardless of how many individual codes it corresponds to

---

## Section 5: Relevant Clinical Specialties

Identify which clinical specialties are most likely to find this group relevant, with a brief note on why.

**Format:**

### Relevant Clinical Specialties

| Specialty | Relevance |
|-----------|-----------|
| Primary Care | Routine screening and monitoring |
| Endocrinology | Diagnostic workup of [condition] |
| Hematology | Evaluation of [condition] |

---

## Section 6: JIRA-Ready Summary

A bullet-point summary suitable for direct copy-paste into a JIRA ticket.

**Format:**

### JIRA-Ready Summary

```
**Intent:** [One-line statement of what this group captures and its clinical purpose]

**Inclusions:**
• [Component/category 1] — [rationale]
• [Component/category 2] — [rationale]
• [Group-level scope]: [specimen types / properties / methods]
• [Nuanced rule if applicable]

**Exclusions:**
• [Component/category 1] — [rationale]
• [Component/category 2] — [rationale]
• [Nuanced rule if applicable]

**Recommended Group Title:** [Title]

**Terminology Standard:** [LOINC Components / RxNorm Ingredients]
**Number of Components/Ingredients:** [count]

**Applicable Specialties:** [comma-separated list]

**Assumptions & Limitations:**
• [Assumption 1]
• [Known limitation 1]

**Expected Clinical Applicability:** [Brief statement on how/where this group will be used in clinical workflows]
```
