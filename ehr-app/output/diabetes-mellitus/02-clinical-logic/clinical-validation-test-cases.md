# Clinical Validation Test Cases: Diabetes Mellitus Identifier

## Test Case Categories
1. **True Positive - Diabetes**: Patient should trigger diabetes alert
2. **True Positive - Prediabetes**: Patient should trigger prediabetes alert
3. **True Negative**: Patient should NOT trigger alert
4. **Exclusion Logic**: Patient excluded for valid reason
5. **Edge Cases**: Boundary conditions and special populations

---

## Category 1: True Positive - Diabetes (Should Fire Alert)

### TC-001: Diabetes - HbA1c Only
| Field | Value |
|-------|-------|
| Patient | 52M |
| HbA1c | 7.2% (recorded 2 weeks ago) |
| FPG | Not available |
| Problem List | Hypertension |
| **Expected Result** | **ALERT: Diabetes Mellitus - Likely (E11.9)** |
| **Confidence** | Moderate (single criterion) |
| Rationale | HbA1c 7.2% >= 6.5% threshold |

### TC-002: Diabetes - FPG Only
| Field | Value |
|-------|-------|
| Patient | 48F |
| HbA1c | Not available |
| FPG | 142 mg/dL (recorded 1 week ago) |
| Problem List | Obesity, GERD |
| **Expected Result** | **ALERT: Diabetes Mellitus - Likely (E11.9)** |
| **Confidence** | Moderate (single criterion) |
| Rationale | FPG 142 >= 126 mg/dL threshold |

### TC-003: Diabetes - Confirmed (Two Criteria)
| Field | Value |
|-------|-------|
| Patient | 55M |
| HbA1c | 6.8% (recorded 1 month ago) |
| FPG | 134 mg/dL (recorded 1 month ago) |
| Problem List | Hypertension, Hyperlipidemia |
| **Expected Result** | **ALERT: Diabetes Mellitus - Confirmed (E11.9)** |
| **Confidence** | High (two criteria) |
| Rationale | Both HbA1c and FPG meet diabetes thresholds |

### TC-004: Diabetes - OGTT Based
| Field | Value |
|-------|-------|
| Patient | 44F |
| HbA1c | 6.3% |
| 2-hr OGTT | 218 mg/dL |
| Problem List | PCOS |
| **Expected Result** | **ALERT: Diabetes Mellitus - Likely (E11.9)** |
| **Confidence** | Moderate |
| Rationale | 2-hr OGTT >= 200 mg/dL, HbA1c in prediabetes range |

### TC-005: Diabetes - Symptomatic Hyperglycemia
| Field | Value |
|-------|-------|
| Patient | 38M |
| Random Glucose | 324 mg/dL |
| Symptoms | Polyuria, polydipsia, 15 lb weight loss |
| Problem List | None |
| **Expected Result** | **ALERT: Diabetes Mellitus - Confirmed (E11.9)** |
| **Confidence** | High |
| Rationale | Random glucose >= 200 with classic symptoms |

### TC-006: Diabetes - Very High HbA1c
| Field | Value |
|-------|-------|
| Patient | 62F |
| HbA1c | 10.4% |
| FPG | 212 mg/dL |
| Problem List | Hypertension |
| **Expected Result** | **ALERT: Diabetes Mellitus - Confirmed (E11.9)** |
| **Confidence** | High |
| **Alert Priority** | High (severely elevated values) |
| Rationale | Markedly elevated values, urgent intervention needed |

---

## Category 2: True Positive - Prediabetes (Should Fire Alert)

### TC-101: Prediabetes - HbA1c in Range
| Field | Value |
|-------|-------|
| Patient | 45M |
| HbA1c | 5.9% |
| FPG | 94 mg/dL |
| Problem List | Obesity |
| **Expected Result** | **ALERT: Prediabetes (R73.03)** |
| Rationale | HbA1c 5.9% in prediabetes range (5.7-6.4%) |

### TC-102: Prediabetes - Impaired Fasting Glucose
| Field | Value |
|-------|-------|
| Patient | 50F |
| HbA1c | 5.5% |
| FPG | 112 mg/dL |
| Problem List | Hyperlipidemia |
| **Expected Result** | **ALERT: Prediabetes - IFG (R73.01)** |
| Rationale | FPG 112 in impaired fasting glucose range (100-125) |

### TC-103: Prediabetes - Impaired Glucose Tolerance
| Field | Value |
|-------|-------|
| Patient | 42F |
| HbA1c | 5.6% |
| 2-hr OGTT | 158 mg/dL |
| Problem List | Family history of DM |
| **Expected Result** | **ALERT: Prediabetes - IGT (R73.02)** |
| Rationale | 2-hr OGTT in IGT range (140-199 mg/dL) |

### TC-104: Prediabetes - Multiple Markers
| Field | Value |
|-------|-------|
| Patient | 58M |
| HbA1c | 6.1% |
| FPG | 108 mg/dL |
| Problem List | Obesity, Sleep Apnea |
| **Expected Result** | **ALERT: Prediabetes (R73.03)** |
| **Confidence** | High (multiple markers) |
| Rationale | Both HbA1c and FPG in prediabetes ranges |

---

## Category 3: True Negative (Should NOT Fire Alert)

### TC-201: Normal Values
| Field | Value |
|-------|-------|
| Patient | 35F |
| HbA1c | 5.2% |
| FPG | 88 mg/dL |
| Problem List | None |
| **Expected Result** | **NO ALERT** |
| Rationale | All values in normal range |

### TC-202: Borderline Normal HbA1c
| Field | Value |
|-------|-------|
| Patient | 40M |
| HbA1c | 5.6% |
| FPG | 96 mg/dL |
| Problem List | Hypertension |
| **Expected Result** | **NO ALERT** |
| Rationale | HbA1c 5.6% just below prediabetes threshold |

### TC-203: Existing Diabetes Diagnosis
| Field | Value |
|-------|-------|
| Patient | 60M |
| HbA1c | 7.8% |
| FPG | 156 mg/dL |
| Problem List | **Type 2 Diabetes (E11.9)**, Hypertension |
| **Expected Result** | **NO ALERT (Already Diagnosed)** |
| Rationale | Diabetes already on problem list |

### TC-204: Existing Prediabetes Diagnosis
| Field | Value |
|-------|-------|
| Patient | 48F |
| HbA1c | 6.0% |
| FPG | 104 mg/dL |
| Problem List | **Prediabetes (R73.03)** |
| **Expected Result** | **NO ALERT (Already Diagnosed)** |
| Rationale | Prediabetes already on problem list |

---

## Category 4: Exclusion Logic Cases

### TC-301: Pregnancy Exclusion
| Field | Value |
|-------|-------|
| Patient | 32F, 24 weeks pregnant |
| HbA1c | 6.2% |
| FPG | 118 mg/dL |
| Problem List | Pregnancy (Z33.1) |
| **Expected Result** | **EXIT: Pregnancy (GDM criteria apply)** |
| Rationale | Gestational diabetes has different diagnostic criteria |

### TC-302: Sickle Cell Disease
| Field | Value |
|-------|-------|
| Patient | 28F |
| HbA1c | 5.8% |
| FPG | 132 mg/dL |
| Problem List | Sickle Cell Disease (D57.1) |
| **Expected Result** | **ALERT based on FPG only** |
| Note | HbA1c excluded from evaluation |
| Rationale | HbA1c unreliable with hemoglobinopathy |

### TC-303: ESRD on Dialysis
| Field | Value |
|-------|-------|
| Patient | 65M |
| HbA1c | 5.4% |
| FPG | 138 mg/dL |
| Problem List | ESRD (N18.6), Dialysis (Z99.2) |
| **Expected Result** | **ALERT based on FPG only** |
| Note | HbA1c excluded from evaluation |
| Rationale | HbA1c unreliable in ESRD |

### TC-304: Recent Blood Transfusion
| Field | Value |
|-------|-------|
| Patient | 55F |
| HbA1c | 6.0% |
| Transfusion Date | 6 weeks ago |
| Problem List | Anemia |
| **Expected Result** | **HbA1c not used; evaluate by glucose only** |
| Rationale | HbA1c unreliable within 90 days of transfusion |

### TC-305: Missing Lab Data
| Field | Value |
|-------|-------|
| Patient | 45M |
| HbA1c | Not available |
| FPG | Not available |
| OGTT | Not available |
| Problem List | Hypertension |
| **Expected Result** | **EXIT: Insufficient Data** |
| Rationale | No qualifying labs available |

### TC-306: Stale Lab Data (>12 months)
| Field | Value |
|-------|-------|
| Patient | 52F |
| HbA1c | 6.6% (recorded 14 months ago) |
| FPG | Not available |
| Problem List | Obesity |
| **Expected Result** | **EXIT: Stale Data** |
| Rationale | Lab data >12 months old |

---

## Category 5: Edge Cases

### TC-401: Exact HbA1c Threshold (6.5%)
| Field | Value |
|-------|-------|
| Patient | 50M |
| HbA1c | 6.5% |
| Problem List | None |
| **Expected Result** | **ALERT: Diabetes Mellitus - Likely** |
| Rationale | 6.5% meets threshold (>= 6.5) |

### TC-402: Just Below HbA1c Threshold (6.4%)
| Field | Value |
|-------|-------|
| Patient | 50M |
| HbA1c | 6.4% |
| Problem List | None |
| **Expected Result** | **ALERT: Prediabetes** |
| Rationale | 6.4% is prediabetes, not diabetes |

### TC-403: Exact FPG Threshold (126 mg/dL)
| Field | Value |
|-------|-------|
| Patient | 48F |
| FPG | 126 mg/dL |
| Problem List | None |
| **Expected Result** | **ALERT: Diabetes Mellitus - Likely** |
| Rationale | 126 meets threshold (>= 126) |

### TC-404: Discordant Results (HbA1c vs FPG)
| Field | Value |
|-------|-------|
| Patient | 55M |
| HbA1c | 5.8% (prediabetes) |
| FPG | 128 mg/dL (diabetes) |
| Problem List | None |
| **Expected Result** | **ALERT: Diabetes Mellitus - Likely** |
| Rationale | FPG meets diabetes threshold; recommend confirmation |

### TC-405: Adolescent Patient
| Field | Value |
|-------|-------|
| Patient | 15F |
| HbA1c | 6.8% |
| BMI Percentile | 95th |
| Problem List | Obesity |
| **Expected Result** | **ALERT: Diabetes Mellitus - Likely** |
| Note | Recommend C-peptide, GAD65 Ab to differentiate Type 1 vs 2 |
| Rationale | Same criteria apply to adolescents |

### TC-406: Pediatric (<10 years)
| Field | Value |
|-------|-------|
| Patient | 8M |
| HbA1c | 7.1% |
| Problem List | None |
| **Expected Result** | **EXIT: Age < 10 years** |
| Rationale | Different pediatric criteria apply |

---

## Summary Matrix

| Test Case | HbA1c | FPG | Expected Outcome | Classification |
|-----------|-------|-----|------------------|----------------|
| TC-001 | 7.2% | N/A | Alert | DM Likely |
| TC-002 | N/A | 142 | Alert | DM Likely |
| TC-003 | 6.8% | 134 | Alert | DM Confirmed |
| TC-004 | 6.3% | OGTT 218 | Alert | DM Likely |
| TC-005 | N/A | RG 324 | Alert | DM Confirmed |
| TC-006 | 10.4% | 212 | Alert | DM Confirmed (High) |
| TC-101 | 5.9% | 94 | Alert | Prediabetes |
| TC-102 | 5.5% | 112 | Alert | Prediabetes-IFG |
| TC-103 | 5.6% | OGTT 158 | Alert | Prediabetes-IGT |
| TC-104 | 6.1% | 108 | Alert | Prediabetes |
| TC-201 | 5.2% | 88 | No Alert | Normal |
| TC-202 | 5.6% | 96 | No Alert | Normal |
| TC-203 | 7.8% | 156 | No Alert | Already Diagnosed |
| TC-204 | 6.0% | 104 | No Alert | Already Diagnosed |
| TC-301 | 6.2% | 118 | Exit | Pregnancy |
| TC-302 | 5.8% | 132 | Alert (FPG only) | DM Likely |
| TC-303 | 5.4% | 138 | Alert (FPG only) | DM Likely |
| TC-401 | 6.5% | N/A | Alert | DM Likely (edge) |
| TC-402 | 6.4% | N/A | Alert | Prediabetes (edge) |
| TC-403 | N/A | 126 | Alert | DM Likely (edge) |
| TC-404 | 5.8% | 128 | Alert | DM Likely (discordant) |
