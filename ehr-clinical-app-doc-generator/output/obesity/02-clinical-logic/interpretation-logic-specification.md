# Interpretation Logic Specification: Obesity Identification

## Data Inputs
- **Current_Weight**: Latest body weight from vital signs (LOINC: 29463-7).
- **Current_Height**: Latest body height from vital signs (LOINC: 8302-2).
- **Recorded_BMI**: Directly recorded BMI if available (LOINC: 39156-5).
- **Date_of_Birth**: Patient date of birth for age calculation.
- **Sex**: Patient biological sex (for pediatric percentile calculation).
- **Existing_Problems**: List of active conditions on Problem List.

## Algorithm

### Step 1: Exclusion Check
IF (`Existing_Problems` contains ANY code from ValueSet "Obesity_All_Types"):
    THEN EXIT (Patient already diagnosed with obesity).

IF (`Existing_Problems` contains ANY code from ValueSet "Pregnancy_Status"):
    THEN EXIT (Pregnant patient - separate guidelines apply).

IF (`Existing_Problems` contains "Edema" OR "Ascites" OR "Anasarca"):
    THEN SET `Weight_Unreliable` = TRUE.
    THEN EXIT (Weight may be artificially elevated).

IF (`Existing_Problems` contains ANY code from ValueSet "Limb_Amputation"):
    THEN SET `BMI_Unreliable` = TRUE.
    # Consider adjusted BMI formulas or exit.

### Step 2: Data Validation
IF (`Current_Weight` is NULL OR `Current_Weight` recorded > 12 months ago):
    THEN EXIT (Insufficient data - weight required).

IF (`Current_Height` is NULL OR `Current_Height` recorded > 24 months ago):
    # Height changes slowly in adults; allow 24-month window
    IF (Patient age >= 18):
        THEN EXIT (Insufficient data - height required).

### Step 3: BMI Calculation
IF (`Recorded_BMI` is available AND recent):
    SET `BMI` = `Recorded_BMI`
ELSE:
    # Convert units if necessary
    SET `Weight_kg` = Convert(`Current_Weight`, "kg")
    SET `Height_m` = Convert(`Current_Height`, "m")

    # Calculate BMI
    SET `BMI` = `Weight_kg` / (`Height_m` * `Height_m`)
    SET `BMI` = ROUND(`BMI`, 1)  # Round to 1 decimal place

### Step 4: Age-Based Classification

#### Step 4a: Adult Classification (Age >= 18)
IF (Patient age >= 18):
    IF (`BMI` >= 40.0):
        SET `Classification` = "Obesity Class III (Severe/Morbid)"
        SET `Suggested_ICD10` = "E66.01"
        SET `Suggested_SNOMED` = 238136002
        SET `Alert_Priority` = "High"
    ELSE IF (`BMI` >= 35.0 AND `BMI` < 40.0):
        SET `Classification` = "Obesity Class II"
        SET `Suggested_ICD10` = "E66.9"
        SET `Suggested_SNOMED` = 414916001
        SET `Alert_Priority` = "Medium"
    ELSE IF (`BMI` >= 30.0 AND `BMI` < 35.0):
        SET `Classification` = "Obesity Class I"
        SET `Suggested_ICD10` = "E66.9"
        SET `Suggested_SNOMED` = 414916001
        SET `Alert_Priority` = "Medium"
    ELSE IF (`BMI` >= 25.0 AND `BMI` < 30.0):
        SET `Classification` = "Overweight"
        SET `Suggested_ICD10` = "E66.3"
        SET `Suggested_SNOMED` = 238131007
        SET `Alert_Priority` = "Low"
        # Optional: May not fire alert for overweight
    ELSE:
        EXIT (BMI in normal or underweight range).

#### Step 4b: Pediatric Classification (Age 2-17)
IF (Patient age >= 2 AND Patient age < 18):
    # Look up BMI percentile from CDC growth charts
    SET `BMI_Percentile` = LookupPercentile(`BMI`, Patient age, Patient sex)

    IF (`BMI_Percentile` >= 120% of 95th percentile):
        SET `Classification` = "Severe Obesity (Pediatric)"
        SET `Suggested_ICD10` = "E66.01"
        SET `Suggested_SNOMED` = 238136002
        SET `Alert_Priority` = "High"
    ELSE IF (`BMI_Percentile` >= 95th percentile):
        SET `Classification` = "Obesity (Pediatric)"
        SET `Suggested_ICD10` = "E66.9"
        SET `Suggested_SNOMED` = 414916001
        SET `Alert_Priority` = "Medium"
    ELSE IF (`BMI_Percentile` >= 85th percentile):
        SET `Classification` = "Overweight (Pediatric)"
        SET `Suggested_ICD10` = "E66.3"
        SET `Alert_Priority` = "Low"
    ELSE:
        EXIT (BMI percentile in normal range).

IF (Patient age < 2):
    EXIT (Infant - different growth chart criteria apply).

### Step 5: BMI Z-Code Selection
# Select appropriate Z68.* code for BMI documentation
IF (Patient age >= 18):
    SET `BMI_ZCode` = SelectZCode(`BMI`)
    # Z68.30-Z68.39 for BMI 30-39.9
    # Z68.41-Z68.45 for BMI >= 40

### Step 6: Logic Output
IF `Classification` IS SET:
    RETURN Object:
        - `Alert_Type`: "Undiagnosed Obesity"
        - `Classification`: `Classification`
        - `Calculated_BMI`: `BMI`
        - `Suggested_SNOMED`: `Suggested_SNOMED`
        - `Suggested_ICD10`: `Suggested_ICD10`
        - `BMI_ZCode`: `BMI_ZCode`
        - `Rationale`: "BMI [Value] kg/m² calculated from Ht [Height] and Wt [Weight] on [Date]"
        - `Priority`: `Alert_Priority`
        - `Suggested_Actions`: [
            "Add obesity to Problem List",
            "Order metabolic panel",
            "Refer to nutrition counseling"
        ]

ELSE:
    EXIT (No criteria met).

---

## BMI Classification Summary

### Adults (Age >= 18)
| BMI (kg/m²) | Classification | ICD-10 | Alert |
|-------------|----------------|--------|-------|
| < 18.5 | Underweight | R63.6 | Optional |
| 18.5 - 24.9 | Normal | - | No |
| 25.0 - 29.9 | Overweight | E66.3 | Optional |
| 30.0 - 34.9 | Obesity Class I | E66.9 | Yes |
| 35.0 - 39.9 | Obesity Class II | E66.9 | Yes |
| >= 40.0 | Obesity Class III | E66.01 | Yes (High) |

### Pediatric (Age 2-17)
| BMI Percentile | Classification | ICD-10 | Alert |
|----------------|----------------|--------|-------|
| < 5th | Underweight | R63.6 | Optional |
| 5th - 84th | Normal | - | No |
| 85th - 94th | Overweight | E66.3 | Optional |
| >= 95th | Obesity | E66.9 | Yes |
| >= 120% of 95th | Severe Obesity | E66.01 | Yes (High) |

---

## Unit Conversion Formulas

### Weight Conversion
```
Weight (kg) = Weight (lbs) × 0.453592
Weight (lbs) = Weight (kg) × 2.20462
```

### Height Conversion
```
Height (m) = Height (cm) / 100
Height (m) = Height (inches) × 0.0254
Height (cm) = Height (inches) × 2.54
```

### BMI Formula
```
BMI (kg/m²) = Weight (kg) / [Height (m)]²
```

---

## Adjusted BMI for Amputations (Advanced)

If amputation is present, adjust weight before BMI calculation:

| Amputation | Weight Adjustment |
|------------|------------------|
| Hand | +0.7% |
| Forearm (including hand) | +2.3% |
| Entire arm | +5.0% |
| Foot | +1.5% |
| Below-knee (including foot) | +5.9% |
| Above-knee (entire leg) | +16.0% |

Adjusted Weight = Measured Weight / (1 - Amputation Percentage)

---

## References
- CDC. About Adult BMI. 2024. https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/
- CDC. BMI Percentile Calculator for Child and Teen. 2024.
- WHO. Obesity and Overweight. 2024.
- CMS. Intensive Behavioral Therapy (IBT) for Obesity. Medicare Coverage.
