# Clinical Problem Term Relationship Rules

Detailed decision rules for determining whether medical problem terms are related.

## Table of Contents
1. [Core Principle](#core-principle)
2. [Hierarchical Relationships](#hierarchical-relationships)
3. [Synonym Relationships](#synonym-relationships)
4. [Overlapping Manifestations](#overlapping-manifestations)
5. [Disease-Complication Relationships](#disease-complication-relationships)
6. [Acute vs Chronic Forms](#acute-vs-chronic-forms)
7. [Clinically Associated but Distinct (NOT RELATED)](#clinically-associated-but-distinct)
8. [Edge Cases and Exceptions](#edge-cases-and-exceptions)

---

## Core Principle

**"RELATED" = Redundant. Only one term should remain on the problem list.**

"Related" in this context does NOT mean "clinically associated" or "part of the same disease spectrum." It means the terms are **redundant** and having both provides no additional clinical value.

**The Critical Test:**
> "Would removing one of these terms from the problem list lose clinically important information needed for patient care?"
>
> - **YES** = NOT RELATED (keep both)
> - **NO** = RELATED (consolidate to one)

## Hierarchical Relationships

### Definition
One term is more general (parent) and one is more specific (child) within clinical classification systems.

### Rule: Keep the More Specific Term
When both a general and specific diagnosis exist, retain the specific diagnosis.

### Common Hierarchical Patterns

| General Term | Specific Term | Action |
|--------------|---------------|--------|
| Diabetes mellitus | Type 1 diabetes mellitus | Keep Type 1 |
| Diabetes mellitus | Type 2 diabetes mellitus | Keep Type 2 |
| Heart failure | Systolic heart failure | Keep Systolic |
| Heart failure | Heart failure with reduced ejection fraction | Keep HFrEF |
| Anemia | Iron deficiency anemia | Keep Iron deficiency |
| Anemia | Anemia of chronic disease | Keep specific type |
| Thyroid disorder | Hypothyroidism | Keep Hypothyroidism |
| Thyroid disorder | Graves disease | Keep Graves disease |
| Cancer | Breast cancer | Keep Breast cancer |
| Lung disease | COPD | Keep COPD |
| Kidney disease | Chronic kidney disease stage 3 | Keep CKD stage 3 |

### Decision Logic
```
IF term_A is_parent_of term_B:
    RETURN RELATED
    RECOMMEND keep term_B (more specific)
ELSE IF term_B is_parent_of term_A:
    RETURN RELATED  
    RECOMMEND keep term_A (more specific)
```

---

## Synonym Relationships

### Definition
Different terms that refer to the same clinical entity.

### Rule: Keep the Most Clinically Precise Term
Prefer standardized clinical terminology over abbreviations or colloquial terms.

### Common Synonym Patterns

| Term Variants | Preferred Term |
|---------------|----------------|
| HTN, Hypertension, High blood pressure | Hypertension |
| MI, Myocardial infarction, Heart attack | Myocardial infarction |
| CVA, Stroke, Cerebrovascular accident | Cerebrovascular accident |
| GERD, Gastroesophageal reflux disease, Acid reflux | Gastroesophageal reflux disease |
| CHF, Congestive heart failure, Heart failure | Heart failure |
| DM, Diabetes, Sugar diabetes | Diabetes mellitus |
| CAD, Coronary artery disease, Heart disease | Coronary artery disease |
| AFIB, A-fib, Atrial fibrillation | Atrial fibrillation |
| DVT, Deep vein thrombosis, Blood clot in leg | Deep vein thrombosis |
| PE, Pulmonary embolism, Blood clot in lung | Pulmonary embolism |
| RA, Rheumatoid arthritis | Rheumatoid arthritis |
| OA, Osteoarthritis, Degenerative joint disease | Osteoarthritis |
| COPD, Chronic obstructive pulmonary disease | Chronic obstructive pulmonary disease |
| BPH, Benign prostatic hyperplasia, Enlarged prostate | Benign prostatic hyperplasia |
| UTI, Urinary tract infection, Bladder infection | Urinary tract infection |
| URI, Upper respiratory infection, Common cold | Upper respiratory infection |

### Decision Logic
```
IF term_A synonym_of term_B:
    RETURN RELATED
    RECOMMEND keep most clinically precise term
```

---

## Overlapping Manifestations

### Definition
Terms that describe related manifestations of the same underlying disease process.

### Rule: Consolidate or Keep Most Comprehensive
When complications of the same base disease exist, evaluate for consolidation.

### Common Overlap Patterns

#### Diabetic Complications
| Term A | Term B | Relationship |
|--------|--------|--------------|
| Diabetic retinopathy | Diabetic oculopathy | Overlapping (both eye) |
| Diabetic retinopathy | Diabetic macular edema | Overlapping (both eye) |
| Diabetic nephropathy | CKD due to diabetes | Overlapping (same entity) |
| Diabetic neuropathy | Peripheral neuropathy in diabetic | Overlapping |
| DM with retinopathy | DM with oculopathy | Overlapping |

#### Cardiovascular Manifestations
| Term A | Term B | Relationship |
|--------|--------|--------------|
| Atherosclerotic heart disease | Coronary artery disease | Overlapping |
| Ischemic cardiomyopathy | CAD with reduced EF | Overlapping |
| Hypertensive heart disease | LVH due to hypertension | Overlapping |

#### Respiratory Manifestations
| Term A | Term B | Relationship |
|--------|--------|--------------|
| COPD with acute exacerbation | Acute bronchitis in COPD | Overlapping |
| Asthma exacerbation | Acute asthma attack | Overlapping |

### Decision Logic
```
IF term_A and term_B share_base_disease AND describe_same_organ_system:
    RETURN RELATED (Overlapping)
    RECOMMEND consolidate to most comprehensive term
```

---

## Disease-Complication Relationships

### Definition
Base disease and its known complication both appear on the problem list.

### Rule: Keep Complication When It Implies Base Disease
The complication inherently indicates the presence of the base condition.

### Common Disease-Complication Patterns

| Base Disease | Complication | Action |
|--------------|--------------|--------|
| Type 2 diabetes | Diabetic nephropathy | Keep Diabetic nephropathy |
| Type 2 diabetes | Diabetic retinopathy | Keep Diabetic retinopathy |
| Hypertension | Hypertensive nephropathy | Keep Hypertensive nephropathy |
| Hypertension | Hypertensive retinopathy | Keep Hypertensive retinopathy |
| Atrial fibrillation | Cardioembolic stroke | Keep both (distinct tracking) |
| Cirrhosis | Hepatic encephalopathy | Keep both (distinct tracking) |

### Special Consideration
Some base diseases should remain listed even with complications for:
- Medication management (e.g., diabetes medications)
- Screening purposes
- Care coordination

### Decision Logic
```
IF complication_term explicitly_includes base_disease_name:
    RETURN RELATED
    RECOMMEND keep complication term (implies base)
ELSE IF complication requires_separate_tracking:
    RETURN RELATED but keep both for clinical purposes
```

---

## Acute vs Chronic Forms

### Definition
Acute and chronic presentations of the same disease entity.

### Rule: Context-Dependent Consolidation

### Patterns

| Acute Form | Chronic Form | Recommendation |
|------------|--------------|----------------|
| Acute kidney injury | Chronic kidney disease | Keep both if both exist |
| Acute pancreatitis | Chronic pancreatitis | Keep current state |
| Acute hepatitis B | Chronic hepatitis B | Keep current state |
| Acute heart failure | Chronic heart failure | Keep both if applicable |
| Acute pain | Chronic pain | Keep both if different conditions |


### Decision Logic
```
IF acute and chronic forms of same condition:
    IF same underlying pathology:
        RETURN RELATED
        RECOMMEND keep current clinical state
    ELSE:
        RETURN NOT RELATED (e.g., acute injury superimposed on chronic disease)
```

---

## Clinically Associated but Distinct

### Definition
Conditions that share pathophysiology, risk factors, or disease spectrum but represent separate clinical entities requiring individual documentation and management.

### Rule: These Are NOT RELATED - Keep Both
Even though these conditions may be clinically associated, they must BOTH remain on the problem list.

### Key Examples

| Term A | Term B | Why NOT RELATED |
|--------|--------|-------------------|
| History of DVT | History of PE | Different anatomical locations (venous vs pulmonary); both inform VTE risk assessment and anticoagulation decisions |
| Diabetic retinopathy | Diabetic nephropathy | Different organ systems; each requires separate monitoring protocols (ophthalmology vs nephrology) |
| Diabetic neuropathy | Diabetic retinopathy | Different organ complications; different specialists, different monitoring |
| Right knee osteoarthritis | Left knee osteoarthritis | Different anatomical locations; may have different severity, treatment plans |
| Atrial fibrillation | History of stroke | Different conditions; stroke may be consequence but requires separate tracking |
| COPD | Pulmonary hypertension | Related but distinct; different treatments, different prognostic implications |
| Heart failure | Coronary artery disease | Often coexist but managed differently; both inform treatment |
| Chronic kidney disease | Hypertension | Often causally related but both need separate tracking |

### The VTE Example Explained

**DVT (Deep Vein Thrombosis)** and **PE (Pulmonary Embolism)**:
- Both are part of the VTE (venous thromboembolism) spectrum
- Share common risk factors and treatment (anticoagulation)
- PE often originates from DVT

**However, they are NOT RELATED because:**
1. **Different anatomical locations** - legs/pelvis vs lungs
2. **Different clinical presentations** - leg swelling vs respiratory distress
3. **Different severity implications** - PE has higher mortality risk
4. **Both inform clinical decisions** - history of both indicates higher recurrence risk
5. **Removing either loses information** - "History of VTE" alone doesn't capture the full picture

### Decision Logic
```
IF terms share disease_spectrum OR common_pathophysiology:
    IF both represent distinct anatomical locations:
        RETURN NOT RELATED (keep both)
    IF both require separate clinical monitoring:
        RETURN NOT RELATED (keep both)
    IF both inform different treatment decisions:
        RETURN NOT RELATED (keep both)
    IF removing one loses clinically important information:
        RETURN NOT RELATED (keep both)
```

---

## Edge Cases and Exceptions

### When to Keep Both Terms Despite Relationship

1. **Different anatomical locations**
   - "Type 2 DM with retinopathy" AND "Type 2 DM with nephropathy"
   - Both track different organ involvement; keep both

2. **Different stages of same disease**
   - "CKD Stage 3" vs "CKD Stage 4" 
   - Keep current stage only

3. **Historical vs active conditions**
   - "History of MI" vs "Acute MI"
   - Keep both if clinically relevant

4. **Bilateral conditions**
   - "Right knee osteoarthritis" vs "Left knee osteoarthritis"
   - May keep both for tracking or consolidate to "Bilateral knee OA"

### Terms That Are Never Related

| Category A | Category B | Always Distinct |
|------------|------------|-----------------|
| Endocrine | Surgical/Trauma | Yes |
| Cardiovascular | Infectious | Yes (usually) |
| Psychiatric | Orthopedic | Yes |
| Autoimmune | Neoplastic | Yes (usually) |

### Special Coding Considerations

When ICD-10 codes are available:
- Same first 3 characters often indicates related conditions
- Different chapters (first letter) usually indicates distinct conditions
- "With" codes (e.g., E11.65) combine base + complication

---

## Quick Reference Decision Tree

```
START with two terms

0. THE CRITICAL TEST: Would removing one term lose clinically important information?
   YES -> NOT RELATED (keep both) -> STOP
   NO -> Continue

1. Are they exact synonyms or abbreviations of each other?
   YES -> RELATED (Synonym) -> Keep more precise term
   NO -> Continue

2. Is one term a more specific version of the other?
   YES -> RELATED (Hierarchical) -> Keep more specific term
   NO -> Continue

3. Do they describe the same disease affecting the SAME organ/location?
   YES -> RELATED (Overlapping) -> Evaluate for consolidation
   NO -> Continue (different organs = NOT RELATED)

4. Is one a complication where the complication term INCLUDES the base disease name?
   YES -> RELATED (Disease-Complication) -> Keep complication term
   NO -> Continue

5. Do they represent different anatomical locations, organ systems, or require separate monitoring?
   YES -> NOT RELATED -> Keep both separately
   NO -> Continue

6. Are they completely independent clinical entities?
   YES -> NOT RELATED -> Keep both separately
```

