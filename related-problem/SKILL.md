---
name: related-problem
description: Determine whether medical problem terms are related enough that only one should remain on a patient's problem list. Use when given two or more medical conditions/diagnoses to evaluate for redundancy, hierarchy, or overlap. Identifies when terms represent the same clinical issue (e.g., "Type 1 diabetes mellitus" and "Diabetes mellitus"), one is a more specific version of another, or they describe overlapping clinical concepts that should be consolidated. Also identifies when terms are distinct and unrelated (e.g., "Diabetes mellitus" and "Appendicitis").
---

# Related Problem

Evaluate medical problem terms to determine if they are sufficiently related that only one should remain on a patient's problem list, reducing clinical redundancy.

## Overview

This skill analyzes sets of medical problem terms to identify:
- **Related (redundant) terms**: Terms where only ONE should remain on the problem list - same clinical issue, hierarchical relationship, or true duplicates
- **Not related terms**: Distinct conditions that should BOTH remain as separate entries

## Critical Principle

**"RELATED" = Redundant. Only flag terms as RELATED if one should be REMOVED from the problem list.**

If both terms represent clinically distinct conditions that warrant separate tracking, monitoring, or treatment, they are **NOT RELATED** even if they:
- Share common risk factors
- Are part of the same disease spectrum
- Have similar pathophysiology
- Often occur together

**The test:** "Would removing one of these terms lose clinically important information?" If YES, they are NOT RELATED.

## Workflow

### Step 1: Receive Input Terms

Accept a set of medical problem terms from the user. Terms may include:
- ICD-10 coded diagnoses
- SNOMED CT concepts
- Free-text clinical problem descriptions
- Mixed format combinations

### Step 2: Analyze Relationships

For each pair of terms, evaluate using these relationship categories:

#### Hierarchical Relationships (RELATED)
One term is a parent/child of the other in clinical classification:
- "Diabetes mellitus" <-> "Type 1 diabetes mellitus" (parent-child)
- "Heart failure" <-> "Acute systolic heart failure" (general-specific)
- "Anemia" <-> "Iron deficiency anemia" (category-subtype)

#### Same Clinical Concept (RELATED)
Terms describe the same underlying condition differently:
- "HTN" <-> "Hypertension" <-> "High blood pressure" (synonyms)
- "MI" <-> "Myocardial infarction" <-> "Heart attack" (abbreviations)
- "GERD" <-> "Gastroesophageal reflux disease" (acronyms)

#### Overlapping Manifestations (RELATED)
Terms describe related manifestations of a single disease process:
- "Type 1 diabetes mellitus with retinopathy" <-> "Type 1 diabetes mellitus with oculopathy"
- "Diabetic nephropathy" <-> "Chronic kidney disease due to diabetes"
- "COPD with acute exacerbation" <-> "Acute bronchitis in COPD patient"

#### Distinct Conditions (NOT RELATED)
Conditions that are clinically independent OR represent separate anatomical/clinical entities requiring individual tracking:
- "Type 1 diabetes mellitus" vs "Appendicitis" (unrelated systems)
- "Hypertension" vs "Osteoarthritis" (unrelated systems)
- "Asthma" vs "Hypothyroidism" (unrelated systems)
- "History of DVT" vs "History of PE" (both VTE spectrum, but distinct anatomical locations requiring separate documentation)
- "Diabetic retinopathy" vs "Diabetic nephropathy" (different organ complications of same base disease)

### Step 3: Apply Decision Logic

Reference `references/relationship_rules.md` for detailed clinical decision rules.

**Key principles:**
1. **Specificity rule**: When a general term and specific term coexist, keep the more specific term
2. **Complication rule**: When a base disease and its complication coexist, keep the complication (implies the base)
3. **Synonym rule**: When synonyms coexist, keep the most clinically precise term
4. **Independence rule**: Unrelated conditions always remain separate
5. **Distinct tracking rule**: If both conditions require separate clinical tracking (different anatomy, different monitoring, different treatment), they are NOT RELATED even if clinically associated

### Step 4: Return Analysis Results

For each term pair or group analyzed, return:

1. **Relationship status**: RELATED or NOT RELATED
2. **Relationship type** (if related): Hierarchical, Synonym, or Overlapping
3. **Recommended action**: Which term(s) to keep or consolidate
4. **Clinical rationale**: Brief explanation of the relationship

## Output Format

```
## Problem Term Analysis

### Input Terms:
- Term A: [first term]
- Term B: [second term]
(additional terms as applicable)

### Analysis:

| Term A | Term B | Relationship | Type | Recommendation |
|--------|--------|--------------|------|----------------|
| Type 1 diabetes mellitus | Diabetes mellitus | RELATED | Hierarchical (specific-general) | Keep "Type 1 diabetes mellitus" |
| Type 1 diabetes mellitus | Appendicitis | NOT RELATED | Distinct conditions | Keep both separately |

### Rationale:
[Clinical explanation for each determination]

### Consolidated Problem List:
[Recommended final list after removing redundancies]
```

## Examples

### Example 1: Hierarchical Relationship
**Input:** "Type 1 diabetes mellitus", "Diabetes mellitus"
**Result:** RELATED - Hierarchical
**Recommendation:** Keep "Type 1 diabetes mellitus" (more specific)

### Example 2: Overlapping Manifestations
**Input:** "Type 1 diabetes mellitus with retinopathy", "Type 1 diabetes mellitus with oculopathy"
**Result:** RELATED - Overlapping
**Recommendation:** Keep one or consolidate to "Type 1 diabetes mellitus with diabetic eye disease"

### Example 3: Distinct Conditions
**Input:** "Type 1 diabetes mellitus", "Appendicitis"
**Result:** NOT RELATED - Distinct
**Recommendation:** Keep both as separate entries

### Example 4: Same Disease Spectrum but Distinct (NOT RELATED)
**Input:** "History of DVT", "History of PE"
**Result:** NOT RELATED - Distinct anatomical conditions
**Recommendation:** Keep both - DVT (venous) and PE (pulmonary) are separate clinical events at different anatomical locations; both require documentation for risk stratification and treatment decisions

### Example 5: Different Organ Complications (NOT RELATED)
**Input:** "Diabetic retinopathy", "Diabetic nephropathy"
**Result:** NOT RELATED - Different organ systems
**Recommendation:** Keep both - each represents a distinct organ complication requiring separate monitoring and management

## Resources

### references/
- `relationship_rules.md` - Detailed clinical rules for determining problem term relationships
- `icd10_hierarchy.md` - ICD-10 category relationships and hierarchies
- `clinical_synonyms.md` - Common clinical term synonyms and abbreviations
