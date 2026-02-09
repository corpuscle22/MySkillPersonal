# Clinical Validation Test Cases: Undiagnosed CKD Identifier

## Overview
These test cases are designed to validate the core logic: specifically that the system identifies **persistent** CKD (values separated by > 90 days) and **ignores** transient drops (AKI) or already diagnosed patients.

| Test Case | Scenario Description | Inputs (Date: Value) | Problem List | Expected Output | Rationale |
|---|---|---|---|---|---|
| **TC-01** | **Classic New Diagnosis (Stage 3a)** | Today: eGFR 55<br>T-100d: eGFR 58 | Empty | **Alert: Suggest CKD Stage 3a** | persistent (>90d) low GFR, no dx. |
| **TC-02** | **Already Diagnosed** | Today: eGFR 40<br>T-120d: eGFR 38 | "Chronic kidney disease (disorder)" | **No Alert** | Patient already has diagnosis code. |
| **TC-03** | **Transient Drop (Potential AKI)** | Today: eGFR 45<br>T-100d: eGFR 95 | Empty | **No Alert** | Only one value < 60. Need confirmation > 3 months. |
| **TC-04** | **Insufficient Time Gap** | Today: eGFR 50<br>T-30d: eGFR 48<br>T-100d: eGFR 92 | Empty | **No Alert** | Two low values exist, but are only 30 days apart. Need > 90 days persistence. |
| **TC-05** | **Stage 3b w/ Albuminuria** | Today: eGFR 40, UACR 400<br>T-150d: eGFR 42 | Empty | **Alert: Suggest CKD Stage 3b** | Meets GFR criteria. UACR reinforces risk. |
| **TC-06** | **Albuminuria Only (Stage 1)** | Today: eGFR 100, UACR 350<br>T-100d: eGFR 102, UACR 400 | Empty | **Alert: Suggest CKD Stage 1** | eGFR normal, but persistent Albuminuria > 30 signifies kidney damage. |
| **TC-07** | **New Patient (No History)** | Today: eGFR 45 | Empty | **No Alert** | Cannot confirm chronicity with single value. |
| **TC-08** | **Inconsistent Data** | Today: eGFR 55<br>T-60d: eGFR 95<br>T-120d: eGFR 58 | Empty | **Alert: Suggest CKD Stage 3a** | Today(55) and T-120d(58) are > 90d apart and both < 60. T-60d is irrelevant outlier or recovery. |
| **TC-09** | **Borderline Case** | Today: eGFR 59<br>T-95d: eGFR 59 | Empty | **Alert: Suggest CKD Stage 3a** | Technically meets criteria (< 60), though clinical judgment may vary. System should alert. |
| **TC-10** | **Pediatric Exclusion** | Age: 12, eGFR: 50 | Empty | **No Alert** | App logic excludes < 18 years (different formulas/criteria). |
