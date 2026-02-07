---
name: problem-list-analyzer
description: "Analyze clinical documentation to generate appropriate problem list entries. Use when given clinical notes (history, physical examination, objective findings, assessments) to extract and organize diagnoses into three categories. (1) Confirmed Diagnoses for long-term or clinically important problems appropriate for problem list documentation. (2) Documented Uncertain Diagnoses for problems explicitly noted as possible, suspected, or uncertain in the documentation. (3) Inferred Differential Diagnosis for most likely diagnoses inferred from symptoms, findings, demographics, and clinical context using evidence-based medical reasoning."
---

# Problem List Analyzer

Analyze clinical documentation to generate comprehensive, appropriate problem list entries organized by certainty level.

## Overview

This skill examines clinical notes to extract and categorize medical problems for documentation on a patient's problem list. It distinguishes between confirmed long-term conditions, explicitly uncertain diagnoses, and inferred differential diagnoses based on the complete clinical picture.

## Clinical Analysis Framework

### Step 1: Extract Patient Demographics and Context

From the clinical documentation, identify:
- **Age and sex** - Critical for age/sex-specific differential diagnoses
- **Risk factors** - Documented conditions that predispose to other diseases
- **Social history** - Smoking, alcohol, occupation, living situation
- **Family history** - Hereditary conditions and familial patterns
- **Past medical history** - Pre-existing conditions affecting current assessment

### Step 2: Analyze Clinical Findings

Extract and organize:
- **Chief complaint** - Primary reason for encounter
- **History of present illness (HPI)** - Symptom timeline, characteristics, associated features
- **Review of systems (ROS)** - Positive and pertinent negative findings
- **Physical examination** - Objective findings on examination
- **Laboratory/imaging results** - Diagnostic test results
- **Assessment/Plan** - Provider's documented clinical impression

### Step 3: Categorize Problems

**CRITICAL REDUNDANCY RULE:** Before including ANY symptom or finding as a problem, verify it is NOT already explained by a confirmed diagnosis. Symptoms that are expected manifestations of a confirmed diagnosis must be EXCLUDED from all output categories to avoid redundancy.

Apply the following categorization criteria:

#### Confirmed Diagnoses (For Problem List)

Include problems that meet ALL of these criteria:
1. **Clearly documented** - Explicitly stated as diagnosis (not suspected/possible)
2. **Long-term OR clinically significant** - Either:
   - Chronic conditions (lasting > 3 months or lifelong)
   - Conditions requiring ongoing management
   - Conditions affecting future clinical decisions (surgical history, allergies)
   - Serious conditions even if acute (malignancy, MI, stroke)

**EXCLUDE** from Confirmed Diagnoses:
- Acute minor self-limiting conditions (common cold, minor laceration)
- Transient symptoms without underlying diagnosis (sore throat, mild headache)
- **Symptoms attributable to confirmed diagnoses** (see Symptom Redundancy Rule below)
- Unless documentation indicates chronicity (e.g., "chronic migraine" is included)

#### Documented Uncertain Diagnoses

Include problems where documentation explicitly indicates uncertainty:
- "Possible [condition]"
- "Suspected [condition]"
- "Rule out [condition]"
- "Probable [condition]"
- "[Condition]?" or "[Condition] vs [other]"
- "Cannot exclude [condition]"
- "Concerning for [condition]"

These represent the clinician's documented differential when not yet confirmed.

#### Inferred Differential Diagnosis

Apply clinical reasoning to infer the MOST LIKELY diagnosis from:
- Documented symptoms and signs not yet attributed to a diagnosis
- Pattern recognition from demographics + clinical presentation
- Risk factor analysis suggesting specific conditions
- Laboratory/imaging abnormalities without documented interpretation

**Reference authentic medical sources** for evidence-based differential generation:
- Consider disease prevalence for patient demographics
- Match symptom clusters to known disease presentations
- Apply clinical decision rules where applicable

See `references/differential_reasoning.md` for detailed inference methodology.

## Output Format

```
## Problem List Analysis

### Patient Context
- Age/Sex: [extracted demographics]
- Key Risk Factors: [relevant risk factors]
- Clinical Setting: [inpatient/outpatient/ED]

---

### Confirmed Diagnoses
Problems appropriate for problem list documentation (long-term or clinically important):

| # | Problem | Supporting Evidence | Rationale for Inclusion |
|---|---------|---------------------|------------------------|
| 1 | [Diagnosis] | [Key findings] | [Why this belongs on problem list] |

---

### Documented Uncertain Diagnoses
Problems explicitly documented as uncertain in clinical notes:

| # | Uncertain Problem | Documentation Language | Clinical Context |
|---|-------------------|----------------------|------------------|
| 1 | [Condition] | "[exact wording used]" | [Supporting context] |

---

### Inferred Differential Diagnosis
Most likely diagnosis inferred from symptoms, findings, and clinical context:

| # | Inferred Diagnosis | Supporting Evidence | Clinical Reasoning |
|---|-------------------|---------------------|-------------------|
| 1 | [Condition] | [Symptoms/signs/labs] | [Why this is most likely] |

---

### Summary
- Confirmed Diagnoses: [count] problem(s) recommended for problem list
- Uncertain Diagnoses: [count] requiring further workup
- Inferred Diagnoses: [count] to consider based on clinical picture
```

## Inclusion/Exclusion Criteria

### Problems TO INCLUDE on Problem List (Confirmed)

**Chronic conditions:**
- Diabetes mellitus (any type)
- Hypertension
- Chronic kidney disease
- Heart failure
- COPD/Asthma
- Coronary artery disease
- Chronic pain syndromes
- Mental health conditions (depression, anxiety, bipolar, schizophrenia)
- Autoimmune diseases
- Cancer (active or history of)
- HIV/AIDS
- Hepatitis B/C
- Epilepsy
- Dementia
- Parkinson's disease

**Clinically significant acute conditions:**
- Myocardial infarction
- Stroke/TIA
- Pulmonary embolism
- Deep vein thrombosis
- Sepsis
- Acute kidney injury
- Pneumonia requiring hospitalization

**Surgical history (when clinically relevant):**
- Appendectomy, cholecystectomy, etc.
- Cardiac procedures (CABG, stent placement)
- Joint replacements
- Organ transplant

### Problems TO EXCLUDE (Minor/Transient)

**Acute minor conditions (unless documented as chronic):**
- Common cold/URI
- Acute pharyngitis (sore throat)
- Simple headache (not migraine)
- Minor cuts/abrasions
- Insect bites
- Muscle strain
- Acute gastroenteritis
- Seasonal allergies (unless documented as chronic allergic rhinitis)

### Symptom Redundancy Rule (CRITICAL)

**DO NOT include symptoms as separate problems if they are expected manifestations of a confirmed diagnosis.**

This prevents redundant documentation. Before adding any symptom or finding to the output, ask: "Is this symptom explained by a diagnosis already in my Confirmed Diagnoses list?"

**Common Examples of Symptom-Diagnosis Relationships:**

| Confirmed Diagnosis | Exclude These Symptoms (Redundant) |
|---------------------|------------------------------------|
| Diabetes mellitus | Polyuria, polydipsia, polyphagia, fatigue, blurred vision, weight changes |
| Heart failure | Dyspnea, orthopnea, PND, peripheral edema, fatigue |
| COPD | Dyspnea, chronic cough, wheezing |
| Hypothyroidism | Fatigue, cold intolerance, weight gain, constipation, dry skin |
| Hyperthyroidism | Palpitations, weight loss, heat intolerance, tremor, anxiety |
| Anemia | Fatigue, pallor, dyspnea on exertion, tachycardia |
| Depression | Fatigue, insomnia, appetite changes, difficulty concentrating |
| Anxiety disorder | Palpitations, tremor, restlessness, insomnia |
| GERD | Heartburn, regurgitation, chronic cough, dysphagia |
| Chronic kidney disease | Fatigue, nausea, peripheral edema, pruritus |
| Cirrhosis | Fatigue, jaundice, ascites, peripheral edema |
| Migraine | Headache, photophobia, phonophobia, nausea |
| Peripheral neuropathy | Numbness, tingling, burning sensation in extremities |
| Benign prostatic hyperplasia | Urinary frequency, urgency, nocturia, weak stream |
| Urinary tract infection | Dysuria, urinary frequency, urgency |

**Application:**
1. First, compile the list of Confirmed Diagnoses
2. For each potential symptom entry, check if it maps to any confirmed diagnosis
3. If the symptom is a known manifestation of a confirmed diagnosis, DO NOT include it
4. Only include unexplained symptoms that require separate clinical attention

## Examples

### Example 1: Complex Chronic Patient

**Input excerpt:**
> 65-year-old male with history of type 2 diabetes, hypertension, and CAD s/p stent 2019. Presents with 3-day history of productive cough, fever to 101F. Chest X-ray shows RLL infiltrate. Possible community-acquired pneumonia. Patient also complains of occasional burning on urination. Will rule out UTI.

**Output:**

**Confirmed Diagnoses:**
| # | Problem | Supporting Evidence | Rationale |
|---|---------|---------------------|-----------|
| 1 | Type 2 diabetes mellitus | Documented in history | Chronic, requires ongoing management |
| 2 | Hypertension | Documented in history | Chronic cardiovascular risk factor |
| 3 | Coronary artery disease | History + prior stent | Chronic, significant cardiac comorbidity |
| 4 | Status post coronary stent (2019) | Documented surgical history | Affects antiplatelet therapy decisions |

**Documented Uncertain Diagnoses:**
| # | Uncertain Problem | Documentation Language | Clinical Context |
|---|-------------------|----------------------|------------------|
| 1 | Community-acquired pneumonia | "Possible community-acquired pneumonia" | RLL infiltrate on CXR with fever, cough |
| 2 | Urinary tract infection | "Will rule out UTI" | Dysuria symptoms |

**Inferred Differential Diagnosis:**
| # | Inferred Diagnosis | Supporting Evidence | Clinical Reasoning |
|---|-------------------|---------------------|-------------------|
| 1 | COPD or chronic bronchitis | 65yo male with productive cough, smoker status not documented | Age + sex + recurrent respiratory symptoms warrant screening |

### Example 2: Pediatric Acute Visit

**Input excerpt:**
> 4-year-old female with 2-day history of sore throat, fever, and decreased appetite. No cough. Exam shows tonsillar exudates, tender anterior cervical lymphadenopathy. Rapid strep positive.

**Output:**

**Confirmed Diagnoses:**
| # | Problem | Supporting Evidence | Rationale |
|---|---------|---------------------|-----------|
| 1 | Streptococcal pharyngitis | Positive rapid strep, tonsillar exudates | Although acute, bacterial infection requiring treatment - document for tracking |

**Documented Uncertain Diagnoses:**
*None documented*

**Inferred Differential Diagnosis:**
*None - definitive diagnosis established*

**Note:** Simple sore throat would be excluded, but positive strep throat warrants documentation for treatment completion tracking.

## Resources

### references/
- `differential_reasoning.md` - Methodology for evidence-based differential diagnosis inference
- `problem_list_criteria.md` - Detailed inclusion/exclusion criteria for problem list entries
- `clinical_terminology.md` - Standard terminology and abbreviation reference
