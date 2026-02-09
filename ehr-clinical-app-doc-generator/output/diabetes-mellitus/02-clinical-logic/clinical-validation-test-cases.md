# Clinical Validation Test Cases: Diabetes Mellitus Identification

## Test Case Categories
1. **True Positive**: Patient should trigger DM alert
2. **True Negative**: Patient should NOT trigger alert
3. **Exclusion Logic**: Patient excluded for valid reason
4. **Edge Cases**: Boundary conditions and special scenarios
5. **Prediabetes**: Optional prediabetes detection

---

## Category 1: True Positive Cases (Should Fire Alert)

### TC-001: Classic HbA1c Confirmation (Pattern A)
| Field | Value |
|-------|-------|
| Patient | 55M, no existing DM diagnosis |
| Current HbA1c | 7.8% (2024-01-15) |
| Previous HbA1c | 7.2% (2023-10-01) |
| Problem List | Hypertension, Hyperlipidemia |
| **Expected Result** | **ALERT: Type 2 DM (E11.9)** |
| Rationale | Two HbA1c >= 6.5% on different days within 12 months |

### TC-002: Classic FPG Confirmation (Pattern B)
| Field | Value |
|-------|-------|
| Patient | 48F, no existing DM diagnosis |
| Current FPG | 142 mg/dL (2024-02-01) |
| Previous FPG | 138 mg/dL (2023-11-15) |
| Problem List | Obesity |
| **Expected Result** | **ALERT: Type 2 DM (E11.9)** |
| Rationale | Two FPG >= 126 mg/dL on different days within 12 months |

### TC-003: Mixed Confirmation - HbA1c + FPG (Pattern C)
| Field | Value |
|-------|-------|
| Patient | 62M, no existing DM diagnosis |
| Current HbA1c | 6.9% (2024-01-20) |
| Previous FPG | 134 mg/dL (2023-12-05) |
| Problem List | CAD, Heart Failure |
| **Expected Result** | **ALERT: Type 2 DM (E11.9)** |
| Rationale | HbA1c >= 6.5% and FPG >= 126 on different days |

### TC-004: Mixed Confirmation - FPG + HbA1c (Pattern C Reverse)
| Field | Value |
|-------|-------|
| Patient | 51F, no existing DM diagnosis |
| Current FPG | 156 mg/dL (2024-02-10) |
| Previous HbA1c | 6.7% (2023-09-22) |
| Problem List | PCOS |
| **Expected Result** | **ALERT: Type 2 DM (E11.9)** |
| Rationale | FPG >= 126 and HbA1c >= 6.5% on different days |

### TC-005: Symptomatic Hyperglycemia (Pattern D)
| Field | Value |
|-------|-------|
| Patient | 35M, no existing DM diagnosis |
| Random Glucose | 287 mg/dL (2024-02-15) |
| Documented Symptoms | Polyuria, unexplained weight loss |
| Problem List | None |
| **Expected Result** | **ALERT: Type 2 DM (E11.9)** |
| Rationale | Random glucose >= 200 with classic symptoms |

---

## Category 2: True Negative Cases (Should NOT Fire Alert)

### TC-101: Single Elevated HbA1c (No Confirmation)
| Field | Value |
|-------|-------|
| Patient | 58F, no existing DM diagnosis |
| Current HbA1c | 6.8% (2024-01-10) |
| Previous HbA1c | 5.9% (2023-06-15) |
| Problem List | Hypertension |
| **Expected Result** | **NO ALERT** |
| Rationale | Only one HbA1c >= 6.5%, requires confirmation |

### TC-102: Single Elevated FPG (No Confirmation)
| Field | Value |
|-------|-------|
| Patient | 45M, no existing DM diagnosis |
| Current FPG | 132 mg/dL (2024-02-01) |
| Previous FPG | 98 mg/dL (2023-08-20) |
| Problem List | Anxiety |
| **Expected Result** | **NO ALERT** |
| Rationale | Only one FPG >= 126, requires confirmation |

### TC-103: Both Tests Below Threshold
| Field | Value |
|-------|-------|
| Patient | 40F, no existing DM diagnosis |
| Current HbA1c | 5.4% (2024-01-15) |
| Current FPG | 92 mg/dL (2024-01-15) |
| Problem List | None |
| **Expected Result** | **NO ALERT** |
| Rationale | All values in normal range |

### TC-104: Elevated Random Glucose Without Symptoms
| Field | Value |
|-------|-------|
| Patient | 60M, no existing DM diagnosis |
| Random Glucose | 215 mg/dL (2024-02-10) |
| Documented Symptoms | None |
| Problem List | Hypertension |
| **Expected Result** | **NO ALERT** |
| Rationale | Random glucose >= 200 requires symptoms for diagnosis |

### TC-105: Confirmatory Tests Too Far Apart (>12 months)
| Field | Value |
|-------|-------|
| Patient | 52F, no existing DM diagnosis |
| Current HbA1c | 7.1% (2024-02-01) |
| Previous HbA1c | 6.9% (2022-06-15) |
| Problem List | Hypothyroidism |
| **Expected Result** | **NO ALERT** |
| Rationale | Previous test > 12 months ago, need recent confirmation |

---

## Category 3: Exclusion Logic Cases

### TC-201: Existing DM Diagnosis on Problem List
| Field | Value |
|-------|-------|
| Patient | 65M |
| Current HbA1c | 8.2% (2024-01-20) |
| Previous HbA1c | 7.8% (2023-10-15) |
| Problem List | **Type 2 diabetes mellitus (E11.9)**, Hypertension |
| **Expected Result** | **EXIT: Already Diagnosed** |
| Rationale | DM already on problem list |

### TC-202: Pediatric Patient (Age < 18)
| Field | Value |
|-------|-------|
| Patient | 15F |
| Current HbA1c | 7.5% (2024-02-01) |
| Previous HbA1c | 7.2% (2023-11-10) |
| Problem List | Obesity |
| **Expected Result** | **EXIT: Pediatric Patient** |
| Rationale | Age < 18, pediatric criteria differ |

### TC-203: Active Steroid Use
| Field | Value |
|-------|-------|
| Patient | 55M, no existing DM diagnosis |
| Current HbA1c | 7.3% (2024-01-25) |
| Previous HbA1c | 6.8% (2023-10-20) |
| Active Medications | Prednisone 40mg daily x 14 days |
| Problem List | COPD Exacerbation |
| **Expected Result** | **EXIT: Steroid-Induced Hyperglycemia** |
| Rationale | Active high-dose steroid use > 7 days |

### TC-204: Hemoglobinopathy (HbA1c Unreliable)
| Field | Value |
|-------|-------|
| Patient | 42F, no existing DM diagnosis |
| Current HbA1c | 6.8% (2024-02-05) |
| Previous HbA1c | 6.6% (2023-11-12) |
| Problem List | Sickle Cell Trait (D57.3) |
| **Expected Result** | **ALERT suppressed for HbA1c path** |
| Rationale | HbA1c unreliable in hemoglobinopathy; require FPG confirmation |

### TC-205: Current Pregnancy with Gestational DM
| Field | Value |
|-------|-------|
| Patient | 32F, currently pregnant |
| Current HbA1c | 6.9% (2024-01-30) |
| Previous FPG | 142 mg/dL (2023-12-15) |
| Problem List | Gestational diabetes (O24.4) |
| **Expected Result** | **EXIT: Gestational DM** |
| Rationale | Gestational DM managed separately |

---

## Category 4: Edge Cases

### TC-301: HbA1c Exactly at Threshold (6.5%)
| Field | Value |
|-------|-------|
| Patient | 50M, no existing DM diagnosis |
| Current HbA1c | 6.5% (2024-02-01) |
| Previous HbA1c | 6.5% (2023-09-15) |
| Problem List | Prediabetes |
| **Expected Result** | **ALERT: Type 2 DM (E11.9)** |
| Rationale | 6.5% meets threshold (>= 6.5%) |

### TC-302: FPG Exactly at Threshold (126 mg/dL)
| Field | Value |
|-------|-------|
| Patient | 47F, no existing DM diagnosis |
| Current FPG | 126 mg/dL (2024-01-20) |
| Previous FPG | 126 mg/dL (2023-10-10) |
| Problem List | Hypertension |
| **Expected Result** | **ALERT: Type 2 DM (E11.9)** |
| Rationale | 126 meets threshold (>= 126) |

### TC-303: Same-Day Tests (Invalid for Confirmation)
| Field | Value |
|-------|-------|
| Patient | 55M, no existing DM diagnosis |
| Current HbA1c | 7.2% (2024-02-10) |
| Current FPG | 145 mg/dL (2024-02-10) |
| Previous Tests | None in past 12 months |
| **Expected Result** | **NO ALERT** |
| Rationale | Both tests on same day; need different day confirmation |

### TC-304: Random Glucose at Threshold (200 mg/dL) with Symptoms
| Field | Value |
|-------|-------|
| Patient | 38F, no existing DM diagnosis |
| Random Glucose | 200 mg/dL (2024-02-12) |
| Documented Symptoms | Polydipsia |
| Problem List | None |
| **Expected Result** | **ALERT: Type 2 DM (E11.9)** |
| Rationale | 200 mg/dL meets threshold with symptoms |

### TC-305: Type 1 vs Type 2 Inference (Young, Thin, Rapid Onset)
| Field | Value |
|-------|-------|
| Patient | 28M, BMI 21, no existing DM diagnosis |
| Current HbA1c | 9.5% (2024-02-01) |
| Random Glucose | 342 mg/dL (2024-02-01) |
| Documented Symptoms | Polyuria, polydipsia, 15 lb weight loss in 3 weeks |
| Problem List | None |
| **Expected Result** | **ALERT: Consider Type 1 DM (E10.9)** |
| Rationale | Age < 40, low BMI, rapid onset suggests T1DM |

---

## Category 5: Prediabetes Cases

### TC-401: Prediabetes by HbA1c
| Field | Value |
|-------|-------|
| Patient | 52F, no existing DM or prediabetes diagnosis |
| Current HbA1c | 6.1% (2024-01-15) |
| Previous HbA1c | 5.9% (2023-08-20) |
| Problem List | Obesity |
| **Expected Result** | **ALERT: Prediabetes (R73.03)** |
| Rationale | Two HbA1c values in 5.7-6.4% range |

### TC-402: Prediabetes by FPG
| Field | Value |
|-------|-------|
| Patient | 48M, no existing DM or prediabetes diagnosis |
| Current FPG | 118 mg/dL (2024-02-01) |
| Previous FPG | 112 mg/dL (2023-11-10) |
| Problem List | Hypertension |
| **Expected Result** | **ALERT: Prediabetes (R73.03)** |
| Rationale | Two FPG values in 100-125 mg/dL range |

### TC-403: One DM, One Prediabetes Value
| Field | Value |
|-------|-------|
| Patient | 55F, no existing DM diagnosis |
| Current HbA1c | 6.8% (2024-01-20) |
| Previous HbA1c | 6.2% (2023-09-15) |
| Problem List | None |
| **Expected Result** | **NO ALERT for DM; Possible prediabetes flag** |
| Rationale | Only one value >= 6.5%; does not confirm DM |

---

## Summary Matrix

| Test Case | Pattern | Expected Outcome | Alert Type |
|-----------|---------|-----------------|------------|
| TC-001 | A (HbA1c x2) | Alert | Type 2 DM |
| TC-002 | B (FPG x2) | Alert | Type 2 DM |
| TC-003 | C (HbA1c + FPG) | Alert | Type 2 DM |
| TC-004 | C (FPG + HbA1c) | Alert | Type 2 DM |
| TC-005 | D (Symptomatic) | Alert | Type 2 DM |
| TC-101 | - | No Alert | - |
| TC-102 | - | No Alert | - |
| TC-103 | - | No Alert | - |
| TC-104 | - | No Alert | - |
| TC-105 | - | No Alert | - |
| TC-201 | Exclusion | Exit | Already Diagnosed |
| TC-202 | Exclusion | Exit | Pediatric |
| TC-203 | Exclusion | Exit | Steroid Use |
| TC-204 | Exclusion | Suppress HbA1c | Hemoglobinopathy |
| TC-205 | Exclusion | Exit | Gestational DM |
| TC-301 | Edge | Alert | Type 2 DM |
| TC-302 | Edge | Alert | Type 2 DM |
| TC-303 | Edge | No Alert | Same-day tests |
| TC-304 | Edge | Alert | Type 2 DM |
| TC-305 | Edge | Alert | Consider Type 1 DM |
| TC-401 | Prediabetes | Alert | Prediabetes |
| TC-402 | Prediabetes | Alert | Prediabetes |
| TC-403 | Prediabetes | Partial | Prediabetes possible |
