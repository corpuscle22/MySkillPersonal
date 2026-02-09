# Interpretation Logic Specification: Diabetes Mellitus Identifier

## Data Inputs
- **HbA1c**: Latest HbA1c result (LOINC: 4548-4, 17856-6, 59261-8), units: %, recorded within 12 months
- **FPG**: Fasting plasma glucose (LOINC: 1558-6), units: mg/dL, recorded within 12 months
- **OGTT_2hr**: 2-hour glucose from OGTT (LOINC: 20438-8), units: mg/dL, recorded within 12 months
- **Random_Glucose**: Random plasma glucose (LOINC: 2345-7), units: mg/dL
- **Date_of_Birth**: Patient date of birth for age calculation
- **Existing_Problems**: List of active conditions on Problem List
- **Pregnancy_Status**: Active pregnancy condition if present
- **Hemoglobinopathy**: Documented hemoglobin variant (sickle cell, thalassemia)

## Algorithm

### Step 1: Exclusion Check

```
IF (Existing_Problems contains ANY code from ValueSet "Diabetes_All_Types"):
    THEN EXIT (Patient already diagnosed with diabetes)

IF (Existing_Problems contains code from ValueSet "Pregnancy_Status"):
    THEN EXIT (Pregnant patient - gestational diabetes criteria apply)

IF (Existing_Problems contains "Sickle Cell Disease" OR "Thalassemia"):
    THEN SET HbA1c_Reliable = FALSE
    # Continue but exclude HbA1c-based diagnosis

IF (Existing_Problems contains "ESRD" OR "Dialysis Dependence"):
    THEN SET HbA1c_Reliable = FALSE

IF (Patient has blood transfusion within 90 days):
    THEN SET HbA1c_Reliable = FALSE

IF (Patient age < 10 years):
    THEN EXIT (Pediatric criteria not implemented)
```

### Step 2: Data Validation

```
SET Has_HbA1c = (HbA1c is NOT NULL AND HbA1c recorded within 12 months)
SET Has_FPG = (FPG is NOT NULL AND FPG recorded within 12 months)
SET Has_OGTT = (OGTT_2hr is NOT NULL AND OGTT_2hr recorded within 12 months)
SET Has_Random = (Random_Glucose is NOT NULL)

IF (Has_HbA1c = FALSE AND Has_FPG = FALSE AND Has_OGTT = FALSE):
    THEN EXIT (Insufficient laboratory data)
```

### Step 3: Diabetes Evaluation - Pattern A (HbA1c-Based)

```
IF (HbA1c_Reliable = TRUE AND Has_HbA1c = TRUE):
    IF (HbA1c >= 6.5):
        SET Pattern_A = "DIABETES"
        SET A1c_Class = "Diabetes"
    ELSE IF (HbA1c >= 5.7 AND HbA1c < 6.5):
        SET Pattern_A = "PREDIABETES"
        SET A1c_Class = "Prediabetes"
    ELSE:
        SET Pattern_A = "NORMAL"
        SET A1c_Class = "Normal"
ELSE:
    SET Pattern_A = "NOT_EVALUABLE"
```

### Step 4: Diabetes Evaluation - Pattern B (FPG-Based)

```
IF (Has_FPG = TRUE):
    IF (FPG >= 126):
        SET Pattern_B = "DIABETES"
        SET FPG_Class = "Diabetes"
    ELSE IF (FPG >= 100 AND FPG < 126):
        SET Pattern_B = "PREDIABETES"
        SET FPG_Class = "Impaired Fasting Glucose"
    ELSE:
        SET Pattern_B = "NORMAL"
        SET FPG_Class = "Normal"
ELSE:
    SET Pattern_B = "NOT_EVALUABLE"
```

### Step 5: Diabetes Evaluation - Pattern C (OGTT-Based)

```
IF (Has_OGTT = TRUE):
    IF (OGTT_2hr >= 200):
        SET Pattern_C = "DIABETES"
        SET OGTT_Class = "Diabetes"
    ELSE IF (OGTT_2hr >= 140 AND OGTT_2hr < 200):
        SET Pattern_C = "PREDIABETES"
        SET OGTT_Class = "Impaired Glucose Tolerance"
    ELSE:
        SET Pattern_C = "NORMAL"
        SET OGTT_Class = "Normal"
ELSE:
    SET Pattern_C = "NOT_EVALUABLE"
```

### Step 6: Diabetes Evaluation - Pattern D (Symptomatic Hyperglycemia)

```
IF (Has_Random = TRUE AND Random_Glucose >= 200):
    IF (Patient has symptoms: polyuria, polydipsia, unexplained weight loss):
        SET Pattern_D = "DIABETES"
        SET Random_Class = "Symptomatic Hyperglycemia"
    ELSE:
        SET Pattern_D = "NEEDS_CONFIRMATION"
ELSE:
    SET Pattern_D = "NOT_EVALUABLE"
```

### Step 7: Classification Logic

```
# Count diabetes-level criteria met
SET Diabetes_Criteria_Count = 0
IF (Pattern_A = "DIABETES"): Diabetes_Criteria_Count += 1
IF (Pattern_B = "DIABETES"): Diabetes_Criteria_Count += 1
IF (Pattern_C = "DIABETES"): Diabetes_Criteria_Count += 1
IF (Pattern_D = "DIABETES"): Diabetes_Criteria_Count += 1

# Determine final classification
IF (Diabetes_Criteria_Count >= 2):
    SET Classification = "Diabetes Mellitus - Confirmed"
    SET Suggested_ICD10 = "E11.9"
    SET Suggested_SNOMED = 44054006
    SET Alert_Priority = "High"
    SET Confidence = "High"

ELSE IF (Diabetes_Criteria_Count = 1):
    SET Classification = "Diabetes Mellitus - Likely (Confirm with 2nd test)"
    SET Suggested_ICD10 = "E11.9"
    SET Suggested_SNOMED = 44054006
    SET Alert_Priority = "Medium"
    SET Confidence = "Moderate"

ELSE IF (Pattern_A = "PREDIABETES" OR Pattern_B = "PREDIABETES" OR Pattern_C = "PREDIABETES"):
    # Check if prediabetes already on problem list
    IF (Existing_Problems contains code from ValueSet "Prediabetes"):
        THEN EXIT (Prediabetes already diagnosed)
    SET Classification = "Prediabetes"
    SET Suggested_ICD10 = "R73.03"
    SET Suggested_SNOMED = 714628002
    SET Alert_Priority = "Low"
    SET Confidence = "High"

ELSE:
    EXIT (No diabetes or prediabetes criteria met)
```

### Step 8: Logic Output

```
IF Classification IS SET:
    RETURN Object:
        - Alert_Type: "Undiagnosed Diabetes/Prediabetes"
        - Classification: Classification
        - Qualifying_Labs: [
            {Test: "HbA1c", Value: HbA1c, Date: HbA1c_Date, Threshold: ">=6.5%"},
            {Test: "FPG", Value: FPG, Date: FPG_Date, Threshold: ">=126 mg/dL"},
            {Test: "2-hr OGTT", Value: OGTT_2hr, Date: OGTT_Date, Threshold: ">=200 mg/dL"}
        ]
        - Suggested_SNOMED: Suggested_SNOMED
        - Suggested_ICD10: Suggested_ICD10
        - Rationale: "Patient has [qualifying values] meeting ADA criteria for [Classification]"
        - Priority: Alert_Priority
        - Confidence: Confidence
        - Suggested_Actions: [
            "Add diagnosis to Problem List",
            "Order follow-up HbA1c in 3 months",
            "Refer to diabetes education",
            "Order comprehensive metabolic panel",
            "Refer to ophthalmology for retinal exam"
        ]
ELSE:
    EXIT (No criteria met)
```

---

## Classification Summary

### Diabetes Diagnosis (Adults)
| Test | Diabetes Threshold | Prediabetes Range | Normal |
|------|-------------------|-------------------|--------|
| HbA1c | >= 6.5% | 5.7 - 6.4% | < 5.7% |
| Fasting Plasma Glucose | >= 126 mg/dL | 100 - 125 mg/dL | < 100 mg/dL |
| 2-hr OGTT | >= 200 mg/dL | 140 - 199 mg/dL | < 140 mg/dL |
| Random Glucose + Symptoms | >= 200 mg/dL | N/A | N/A |

### Confirmation Requirements
| Scenario | Confirmation Needed |
|----------|---------------------|
| 2+ criteria from different tests | No (confirmed) |
| 1 criterion, asymptomatic | Yes (repeat same test or different test) |
| 1 criterion, symptomatic | No (classic symptoms with random glucose >= 200) |

---

## Unit Conversion Formulas

### HbA1c
```
HbA1c (IFCC mmol/mol) = (HbA1c% - 2.15) × 10.929
HbA1c% = (HbA1c mmol/mol / 10.929) + 2.15
```

### Glucose
```
Glucose (mmol/L) = Glucose (mg/dL) / 18.018
Glucose (mg/dL) = Glucose (mmol/L) × 18.018
```

---

## Special Population Considerations

### Hemoglobinopathies
If HbA1c is unreliable, use glucose-based criteria only:
- Fasting glucose >= 126 mg/dL on two occasions
- 2-hr OGTT >= 200 mg/dL
- Fructosamine or glycated albumin as alternatives

### Elderly (>= 65 years)
- Same diagnostic criteria apply
- Consider less stringent treatment targets (HbA1c < 8% may be acceptable)

### Adolescents (10-17 years)
- Same diagnostic criteria as adults
- Higher index of suspicion for Type 1 vs Type 2
- Consider C-peptide and GAD65 antibodies if unclear

---

## References
- American Diabetes Association. Standards of Care in Diabetes—2026. Diabetes Care. 2026;49(Suppl 1):S27-S42.
- International Expert Committee Report 2009. Diabetes Care. 2009;32(7):1327-1334.
