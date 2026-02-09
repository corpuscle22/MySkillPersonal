# Clinical Use Case: Undiagnosed CKD Identification

## Narrative
Dr. Smith is seeing Mr. Jones (58M) for a diabetes follow-up. Mr. Jones has had an eGFR of 52 and 55 on his last two metabolic panels (6 months apart), but "Chromic Kidney Disease" is missing from his Problem List.
As Dr. Smith opens the chart, the CKD Identifier app runs in the background. It recognizes the persistent eGFR < 60 and absence of diagnosis.
A non-intrusive alert appears: *"Clinical evidence suggests CKD Stage 3a. Click to add 'Chronic kidney disease, stage 3a (ICD-10 N18.31)' to Problem List."*
Dr. Smith reviews the trend line presented in the alert, agrees, and clicks "Add". The Problem List is updated, and an automatic order set for "CKD Stage 3 Management" (ACEi/ARB, Urine Microalbumin) is suggested.

## Triggers
- **Event**: Chart Open (Patient View) OR Result Verification (New Lab Result).
- **Condition**: 
  1. No existing active problem on Problem List matching ValueSet "Chronic Kidney Disease".
  2. Last eGFR < 60 mL/min/1.73m².
  3. Historical eGFR < 60 mL/min/1.73m² recorded > 90 days prior.
  4. OR: Persistent Albuminuria (UACR > 30 mg/g) > 90 days.

## Exclusion Criteria
- Patients with regular dialysis or kidney transplant (ESRD status).
- Acute Kidney Injury (AKI) diagnosis in active encounter (relative exclusion, context dependent).
- Patients < 18 years old (Pediatric logic differs).
