# Interpretation Logic Specification: CKD Staging

## Data Inputs
- **Current_eGFR**: Latest valid eGFR result.
- **Previous_eGFR**: Most recent eGFR result recorded > 90 days prior to Current_eGFR.
- **Current_UACR**: Latest Urine Albumin-Creatinine Ratio.
- **Previous_UACR**: Most recent UACR recorded > 90 days prior.
- **Existing_Problems**: List of active conditions on Problem List.

## Algorithm

### Step 1: Exclusion Check
IF (`Existing_Problems` contains ANY code from ValueSet "CKD_All_Stages"):
    THEN EXIT (Patient already diagnosed).

### Step 2: eGFR Evaluation (G-Stage)
IF (`Current_eGFR` is Valid AND `Previous_eGFR` is Valid):
    IF (`Current_eGFR` < 60 AND `Previous_eGFR` < 60):
        # Confirmed low GFR > 3 months
        DETERMINE `Suggested_Stage` based on `Current_eGFR`:
            - score >= 90: Stage 1 (Requires Albuminuria)
            - 60-89: Stage 2 (Requires Albuminuria)
            - 45-59: **Stage 3a**
            - 30-44: **Stage 3b**
            - 15-29: **Stage 4**
            - < 15: **Stage 5**
        GO TO Step 4.
    ELSE:
        PROCEED to Step 3 (Check Albuminuria alone).

### Step 3: Albuminuria Evaluation (A-Stage)
IF (`Current_UACR` > 30 mg/g AND `Previous_UACR` > 30 mg/g):
    IF (`Current_eGFR` >= 90):
        SET `Suggested_Stage` = **Stage 1**
    ELSE IF (`Current_eGFR` between 60-89):
        SET `Suggested_Stage` = **Stage 2**
    GO TO Step 4.

### Step 4: Logic Output
IF `Suggested_Stage` IS SET:
    RETURN Object:
        - `Alert_Type`: "Undiagnosed CKD"
        - `Suggested_Concept`: SNOMED code for `Suggested_Stage`
        - `Rationale`: "Two eGFR values < 60 separated by > 90 days: [Date1: Val1], [Date2: Val2]"
ELSE:
    EXIT (No criteria met).
