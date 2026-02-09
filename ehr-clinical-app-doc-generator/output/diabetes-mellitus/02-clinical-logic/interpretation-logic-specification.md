# Interpretation Logic Specification: Diabetes Mellitus Identification

## Data Inputs
- **Current_HbA1c**: Latest valid HbA1c result (LOINC: 4548-4 or related).
- **Previous_HbA1c**: Most recent HbA1c recorded on a different day within 12 months.
- **Current_FPG**: Latest Fasting Plasma Glucose result (LOINC: 1558-6).
- **Previous_FPG**: Most recent FPG recorded on a different day within 12 months.
- **Current_RPG**: Latest Random Plasma Glucose result (LOINC: 2345-7).
- **Existing_Problems**: List of active conditions on Problem List.
- **Active_Medications**: Current medication list (for steroid exclusion).
- **Documented_Symptoms**: Presence of polyuria, polydipsia, weight loss in recent notes.

## Algorithm

### Step 1: Exclusion Check
IF (`Existing_Problems` contains ANY code from ValueSet "Diabetes_Mellitus_All_Types"):
    THEN EXIT (Patient already diagnosed with diabetes).

IF (`Existing_Problems` contains ANY code from ValueSet "Hemoglobinopathy"):
    THEN SET `HbA1c_Unreliable` = TRUE.

IF (`Active_Medications` contains systemic corticosteroid for > 7 days):
    THEN SET `Steroid_Exclusion` = TRUE.

IF (Patient age < 18):
    THEN EXIT (Pediatric patient - different criteria apply).

IF (`Existing_Problems` contains "Gestational Diabetes" AND patient is currently pregnant):
    THEN EXIT (Gestational diabetes managed separately).

### Step 2: HbA1c-Based Diagnosis (Pattern A)
IF (`HbA1c_Unreliable` = FALSE):
    IF (`Current_HbA1c` >= 6.5% AND `Previous_HbA1c` >= 6.5%):
        IF (dates are different AND within 12 months of each other):
            SET `Diagnosis_Confirmed` = TRUE
            SET `Diagnosis_Type` = "Type 2 Diabetes Mellitus"
            SET `Evidence` = "Two HbA1c values >= 6.5%: [Date1: Val1], [Date2: Val2]"
            GO TO Step 6.

### Step 3: Fasting Glucose-Based Diagnosis (Pattern B)
IF (`Current_FPG` >= 126 mg/dL AND `Previous_FPG` >= 126 mg/dL):
    IF (dates are different AND within 12 months of each other):
        SET `Diagnosis_Confirmed` = TRUE
        SET `Diagnosis_Type` = "Type 2 Diabetes Mellitus"
        SET `Evidence` = "Two FPG values >= 126 mg/dL: [Date1: Val1], [Date2: Val2]"
        GO TO Step 6.

### Step 4: Mixed Confirmation (Pattern C)
IF (`Current_HbA1c` >= 6.5% AND `Previous_FPG` >= 126 mg/dL):
    IF (dates are different AND within 12 months of each other):
        SET `Diagnosis_Confirmed` = TRUE
        SET `Diagnosis_Type` = "Type 2 Diabetes Mellitus"
        SET `Evidence` = "HbA1c >= 6.5% [Date1: Val1] and FPG >= 126 [Date2: Val2]"
        GO TO Step 6.

IF (`Current_FPG` >= 126 mg/dL AND `Previous_HbA1c` >= 6.5%):
    IF (dates are different AND within 12 months of each other):
        SET `Diagnosis_Confirmed` = TRUE
        SET `Diagnosis_Type` = "Type 2 Diabetes Mellitus"
        SET `Evidence` = "FPG >= 126 [Date1: Val1] and HbA1c >= 6.5% [Date2: Val2]"
        GO TO Step 6.

### Step 5: Symptomatic Hyperglycemia (Pattern D)
IF (`Current_RPG` >= 200 mg/dL):
    IF (`Documented_Symptoms` contains polyuria OR polydipsia OR unexplained_weight_loss):
        SET `Diagnosis_Confirmed` = TRUE
        SET `Diagnosis_Type` = "Type 2 Diabetes Mellitus"
        SET `Evidence` = "Random glucose >= 200 mg/dL with classic symptoms"
        GO TO Step 6.

### Step 5b: Prediabetes Check (Optional Path)
IF (`Diagnosis_Confirmed` = FALSE):
    IF (`Current_HbA1c` between 5.7% and 6.4% AND `Previous_HbA1c` between 5.7% and 6.4%):
        SET `Prediabetes_Identified` = TRUE
        SET `Evidence` = "Two HbA1c values in prediabetes range: [Date1: Val1], [Date2: Val2]"
    ELSE IF (`Current_FPG` between 100-125 mg/dL AND `Previous_FPG` between 100-125 mg/dL):
        SET `Prediabetes_Identified` = TRUE
        SET `Evidence` = "Two FPG values in prediabetes range: [Date1: Val1], [Date2: Val2]"

### Step 6: Logic Output
IF `Diagnosis_Confirmed` = TRUE:
    RETURN Object:
        - `Alert_Type`: "Undiagnosed Diabetes Mellitus"
        - `Suggested_Diagnosis`: `Diagnosis_Type`
        - `Suggested_SNOMED`: 44054006 (Type 2 DM)
        - `Suggested_ICD10`: "E11.9"
        - `Rationale`: `Evidence`
        - `Confidence`: "High" (two confirmatory tests)

ELSE IF `Prediabetes_Identified` = TRUE:
    RETURN Object:
        - `Alert_Type`: "Prediabetes Identified"
        - `Suggested_Diagnosis`: "Prediabetes"
        - `Suggested_SNOMED`: 714628002
        - `Suggested_ICD10`: "R73.03"
        - `Rationale`: `Evidence`
        - `Confidence`: "Moderate"

ELSE:
    EXIT (No criteria met).

---

## Diagnostic Thresholds Summary

| Test | Diabetes Threshold | Prediabetes Range | Normal |
|------|-------------------|-------------------|--------|
| HbA1c | >= 6.5% | 5.7% - 6.4% | < 5.7% |
| Fasting Plasma Glucose | >= 126 mg/dL | 100 - 125 mg/dL | < 100 mg/dL |
| 2-Hour OGTT | >= 200 mg/dL | 140 - 199 mg/dL | < 140 mg/dL |
| Random Glucose + Symptoms | >= 200 mg/dL | N/A | N/A |

## Type 1 vs Type 2 Inference (Advanced)
If age < 40 AND BMI < 25 AND rapid onset symptoms:
    Consider `Diagnosis_Type` = "Type 1 Diabetes Mellitus" (SNOMED: 46635009, ICD-10: E10.9)
    Recommend: C-peptide, GAD65 antibodies, islet cell antibodies

Default assumption for adults >= 40 OR BMI >= 25: Type 2 Diabetes Mellitus.

## References
- American Diabetes Association. Standards of Care in Diabetes - 2024. Diabetes Care 2024;47(Suppl 1):S1-S321.
- KDIGO 2024 Clinical Practice Guideline for Diabetes Management in Chronic Kidney Disease.
