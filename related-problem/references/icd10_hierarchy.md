# ICD-10 Category Relationships and Hierarchies

Reference for understanding ICD-10 code structure to determine problem term relationships.

## Table of Contents
1. [ICD-10 Structure Overview](#icd-10-structure-overview)
2. [Chapter Categories](#chapter-categories)
3. [Common Hierarchical Patterns](#common-hierarchical-patterns)
4. [Diabetes Mellitus Hierarchy (E08-E13)](#diabetes-mellitus-hierarchy)
5. [Cardiovascular Hierarchy (I00-I99)](#cardiovascular-hierarchy)
6. [Respiratory Hierarchy (J00-J99)](#respiratory-hierarchy)
7. [Using ICD-10 for Relationship Detection](#using-icd-10-for-relationship-detection)

---

## ICD-10 Structure Overview

ICD-10-CM codes follow a hierarchical structure:

```
[Letter][2 digits].[1-4 digits]
   |        |           |
Category  Etiology   Specificity
          /Site      /Laterality
```

### Relationship Indicators
- **Same first 3 characters**: Often related conditions
- **Same chapter (first letter)**: Same body system/category
- **Different chapters**: Usually distinct conditions

---

## Chapter Categories

| Chapter | Codes | Description | Examples |
|---------|-------|-------------|----------|
| A00-B99 | Infectious | Infectious/parasitic diseases | HIV, TB, Hepatitis |
| C00-D49 | Neoplasms | Cancers and tumors | Breast cancer, Leukemia |
| D50-D89 | Blood | Blood disorders | Anemia, Coagulation disorders |
| E00-E89 | Endocrine | Metabolic/endocrine | Diabetes, Thyroid, Obesity |
| F01-F99 | Mental | Mental/behavioral | Depression, Anxiety, Dementia |
| G00-G99 | Nervous | Nervous system | Epilepsy, Parkinson, Neuropathy |
| H00-H59 | Eye | Eye and adnexa | Cataracts, Glaucoma, Retinopathy |
| H60-H95 | Ear | Ear and mastoid | Hearing loss, Otitis |
| I00-I99 | Circulatory | Cardiovascular | HTN, CHF, CAD, Arrhythmias |
| J00-J99 | Respiratory | Respiratory system | COPD, Asthma, Pneumonia |
| K00-K95 | Digestive | Digestive system | GERD, Cirrhosis, IBD |
| L00-L99 | Skin | Skin/subcutaneous | Psoriasis, Dermatitis |
| M00-M99 | Musculoskeletal | Bones/joints/muscles | Arthritis, Osteoporosis |
| N00-N99 | Genitourinary | GU system | CKD, BPH, UTI |
| R00-R99 | Symptoms | Signs/symptoms | Chest pain, Fatigue |
| S00-T88 | Injury | Trauma/poisoning | Fractures, Burns |
| Z00-Z99 | Factors | Health status factors | Screening, History of |

### Cross-Chapter Relationships
Terms from different chapters are typically NOT RELATED, with exceptions:
- E11 (T2DM) related to H36.0 (Diabetic retinopathy)
- I10 (HTN) related to I12 (Hypertensive CKD)

---

## Common Hierarchical Patterns

### Pattern: Base Condition with "With" Combinations

ICD-10 uses combination codes for disease + manifestation:

```
E11     Type 2 diabetes mellitus (base)
E11.2x  Type 2 DM with kidney complications
E11.3x  Type 2 DM with ophthalmic complications
E11.4x  Type 2 DM with neurological complications
E11.5x  Type 2 DM with circulatory complications
E11.6x  Type 2 DM with other specified complications
```

**Rule**: Combination code (E11.3x) is RELATED to base code (E11) - Hierarchical

---

## Diabetes Mellitus Hierarchy

### E08-E13 Diabetes Categories

| Code Range | Description | Related To |
|------------|-------------|------------|
| E08 | DM due to underlying condition | All other DM types (hierarchical sibling) |
| E09 | Drug/chemical induced DM | All other DM types |
| E10 | Type 1 DM | E08-E13 (sibling); parent of E10.x complications |
| E11 | Type 2 DM | E08-E13 (sibling); parent of E11.x complications |
| E13 | Other specified DM | All other DM types |

### E11 Type 2 DM Subcategories (Hierarchical)

```
E11     Type 2 diabetes mellitus
├── E11.0   With hyperosmolarity
├── E11.1   With ketoacidosis
├── E11.2   With kidney complications
│   ├── E11.21  With diabetic nephropathy
│   ├── E11.22  With diabetic CKD
│   └── E11.29  With other kidney complication
├── E11.3   With ophthalmic complications
│   ├── E11.31  With unspecified retinopathy
│   ├── E11.32  With mild NPDR
│   ├── E11.33  With moderate NPDR
│   ├── E11.34  With severe NPDR
│   ├── E11.35  With PDR
│   ├── E11.36  With diabetic cataract
│   ├── E11.37  With diabetic macular edema
│   └── E11.39  With other ophthalmic complication
├── E11.4   With neurological complications
│   ├── E11.40  With diabetic neuropathy, unspecified
│   ├── E11.41  With diabetic mononeuropathy
│   ├── E11.42  With diabetic polyneuropathy
│   ├── E11.43  With diabetic autonomic neuropathy
│   └── E11.44  With diabetic amyotrophy
├── E11.5   With circulatory complications
│   ├── E11.51  With diabetic peripheral angiopathy
│   └── E11.52  With diabetic peripheral angiopathy with gangrene
├── E11.6   With other specified complications
│   ├── E11.61  With diabetic arthropathy
│   ├── E11.62  With skin complications
│   ├── E11.63  With oral complications
│   ├── E11.64  With hypoglycemia
│   └── E11.65  With hyperglycemia
└── E11.9   Without complications
```

### Relationship Examples

| Term A (Code) | Term B (Code) | Relationship |
|---------------|---------------|--------------|
| Type 2 DM (E11.9) | Type 2 DM with retinopathy (E11.319) | RELATED - Hierarchical |
| Type 2 DM with retinopathy (E11.31x) | Type 2 DM with macular edema (E11.37x) | RELATED - Overlapping |
| Type 1 DM (E10) | Type 2 DM (E11) | NOT RELATED - Distinct types |
| Diabetic nephropathy (E11.21) | CKD (N18) | RELATED - Same entity, prefer E11.21 |

---

## Cardiovascular Hierarchy

### I00-I99 Major Categories

```
I10-I16   Hypertensive diseases
├── I10     Essential hypertension
├── I11     Hypertensive heart disease
├── I12     Hypertensive CKD
├── I13     Hypertensive heart and CKD
└── I16     Hypertensive crisis

I20-I25   Ischemic heart diseases
├── I20     Angina pectoris
├── I21     Acute MI
├── I22     Subsequent MI
├── I23     Complications of MI
├── I24     Other acute ischemic
└── I25     Chronic ischemic heart disease

I26-I28   Pulmonary heart disease
├── I26     Pulmonary embolism
├── I27     Other pulmonary heart
└── I28     Other pulmonary vessel

I30-I52   Other heart diseases
├── I48     Atrial fibrillation/flutter
├── I50     Heart failure
│   ├── I50.1   Left ventricular failure
│   ├── I50.2   Systolic heart failure
│   ├── I50.3   Diastolic heart failure
│   ├── I50.4   Combined systolic/diastolic
│   └── I50.9   Heart failure, unspecified
```

### Relationship Examples

| Term A | Term B | Relationship |
|--------|--------|--------------|
| HTN (I10) | Hypertensive heart disease (I11) | RELATED - HHD implies HTN |
| HTN (I10) | Hypertensive CKD (I12) | RELATED - I12 implies HTN |
| Heart failure (I50.9) | Systolic HF (I50.2) | RELATED - Hierarchical |
| CAD (I25.10) | Acute MI (I21) | RELATED - Same disease spectrum |
| HTN (I10) | Atrial fibrillation (I48) | NOT RELATED - Distinct conditions |

---

## Respiratory Hierarchy

### J00-J99 Major Categories

```
J00-J06   Acute upper respiratory infections
J09-J18   Influenza and pneumonia
J20-J22   Other acute lower respiratory infections
J30-J39   Other diseases of upper respiratory tract

J40-J47   Chronic lower respiratory diseases
├── J40     Bronchitis NOS
├── J41     Simple chronic bronchitis
├── J42     Unspecified chronic bronchitis
├── J43     Emphysema
├── J44     COPD
│   ├── J44.0   COPD with acute lower respiratory infection
│   ├── J44.1   COPD with acute exacerbation
│   └── J44.9   COPD, unspecified
├── J45     Asthma
│   ├── J45.2   Mild intermittent asthma
│   ├── J45.3   Mild persistent asthma
│   ├── J45.4   Moderate persistent asthma
│   ├── J45.5   Severe persistent asthma
│   └── J45.9   Asthma, unspecified
└── J47     Bronchiectasis
```

### Relationship Examples

| Term A | Term B | Relationship |
|--------|--------|--------------|
| COPD (J44.9) | COPD with exacerbation (J44.1) | RELATED - Hierarchical |
| COPD (J44) | Emphysema (J43) | RELATED - Often overlapping |
| Asthma (J45.9) | Moderate persistent asthma (J45.4) | RELATED - Hierarchical |
| COPD (J44) | Asthma (J45) | Context-dependent - may overlap or be distinct |

---

## Using ICD-10 for Relationship Detection

### Quick Rules

1. **Same 3-character category (e.g., E11.x)**: Likely RELATED
2. **Same subcategory within chapter**: Likely RELATED
3. **Different chapters**: Usually NOT RELATED
4. **"With" codes**: RELATED to base condition

### Code Analysis Algorithm

```
FUNCTION analyze_icd10_relationship(code_A, code_B):
    
    # Extract components
    chapter_A = code_A[0]
    chapter_B = code_B[0]
    category_A = code_A[0:3]
    category_B = code_B[0:3]
    
    # Different chapters - usually unrelated
    IF chapter_A != chapter_B:
        # Check for known cross-chapter relationships
        IF is_known_cross_chapter_pair(code_A, code_B):
            RETURN RELATED
        ELSE:
            RETURN NOT_RELATED
    
    # Same category - likely related
    IF category_A == category_B:
        IF one_is_more_specific(code_A, code_B):
            RETURN RELATED (Hierarchical)
        ELSE:
            RETURN RELATED (Overlapping/Same level)
    
    # Same chapter, different category
    IF is_known_related_category_pair(category_A, category_B):
        RETURN RELATED
    ELSE:
        RETURN evaluate_clinical_relationship()
```

### Known Cross-Chapter Relationships

| Primary Code | Related Code | Explanation |
|--------------|--------------|-------------|
| E08-E13 (DM) | H36 (Diabetic retinopathy) | Use combination when available |
| E08-E13 (DM) | N08 (Glomerular disorders in DM) | Use combination when available |
| I10 (HTN) | N18 (CKD) | I12 exists for combination |
| I25 (CAD) | I50 (HF) | Can be causally related |
