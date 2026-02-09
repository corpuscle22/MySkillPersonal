# Clinical Validation Test Cases: Obesity Identification

## Test Case Categories
1. **True Positive**: Patient should trigger obesity alert
2. **True Negative**: Patient should NOT trigger alert
3. **Exclusion Logic**: Patient excluded for valid reason
4. **Edge Cases**: Boundary conditions
5. **Pediatric Cases**: Age-specific percentile logic

---

## Category 1: True Positive Cases (Should Fire Alert)

### TC-001: Obesity Class I (BMI 30-34.9)
| Field | Value |
|-------|-------|
| Patient | 45M |
| Height | 5'10" (178 cm) |
| Weight | 210 lbs (95.3 kg) |
| Calculated BMI | 30.1 kg/m² |
| Problem List | Hypertension |
| **Expected Result** | **ALERT: Obesity Class I (E66.9)** |
| Rationale | BMI 30.1 >= 30.0 threshold |

### TC-002: Obesity Class II (BMI 35-39.9)
| Field | Value |
|-------|-------|
| Patient | 52F |
| Height | 5'4" (163 cm) |
| Weight | 215 lbs (97.5 kg) |
| Calculated BMI | 36.7 kg/m² |
| Problem List | Hyperlipidemia, GERD |
| **Expected Result** | **ALERT: Obesity Class II (E66.9)** |
| Rationale | BMI 36.7 in Class II range |

### TC-003: Obesity Class III / Morbid Obesity (BMI >= 40)
| Field | Value |
|-------|-------|
| Patient | 38M |
| Height | 5'11" (180 cm) |
| Weight | 310 lbs (140.6 kg) |
| Calculated BMI | 43.4 kg/m² |
| Problem List | Sleep Apnea, Hypertension |
| **Expected Result** | **ALERT: Obesity Class III/Morbid (E66.01)** |
| Rationale | BMI 43.4 >= 40.0, severe obesity |

### TC-004: Super Obesity (BMI >= 50)
| Field | Value |
|-------|-------|
| Patient | 42F |
| Height | 5'5" (165 cm) |
| Weight | 340 lbs (154.2 kg) |
| Calculated BMI | 56.6 kg/m² |
| Problem List | Type 2 DM, OSA |
| **Expected Result** | **ALERT: Obesity Class III/Morbid (E66.01), BMI Z68.43** |
| Rationale | BMI 56.6, super obesity range |

---

## Category 2: True Negative Cases (Should NOT Fire Alert)

### TC-101: Normal BMI
| Field | Value |
|-------|-------|
| Patient | 35F |
| Height | 5'6" (168 cm) |
| Weight | 145 lbs (65.8 kg) |
| Calculated BMI | 23.4 kg/m² |
| Problem List | None |
| **Expected Result** | **NO ALERT** |
| Rationale | BMI 23.4 in normal range |

### TC-102: Overweight but Not Obese
| Field | Value |
|-------|-------|
| Patient | 48M |
| Height | 6'0" (183 cm) |
| Weight | 195 lbs (88.5 kg) |
| Calculated BMI | 26.4 kg/m² |
| Problem List | Hypertension |
| **Expected Result** | **NO ALERT** (or optional overweight alert) |
| Rationale | BMI 26.4 is overweight, not obese |

### TC-103: BMI Just Under Threshold
| Field | Value |
|-------|-------|
| Patient | 55F |
| Height | 5'3" (160 cm) |
| Weight | 168 lbs (76.2 kg) |
| Calculated BMI | 29.8 kg/m² |
| Problem List | Prediabetes |
| **Expected Result** | **NO ALERT** (or optional overweight alert) |
| Rationale | BMI 29.8 < 30.0 threshold |

---

## Category 3: Exclusion Logic Cases

### TC-201: Existing Obesity Diagnosis
| Field | Value |
|-------|-------|
| Patient | 50M |
| Height | 5'9" (175 cm) |
| Weight | 250 lbs (113.4 kg) |
| Calculated BMI | 36.9 kg/m² |
| Problem List | **Obesity (E66.9)**, Type 2 DM |
| **Expected Result** | **EXIT: Already Diagnosed** |
| Rationale | Obesity already on problem list |

### TC-202: Current Pregnancy
| Field | Value |
|-------|-------|
| Patient | 32F, currently pregnant |
| Height | 5'5" (165 cm) |
| Weight | 195 lbs (88.5 kg) |
| Calculated BMI | 32.5 kg/m² |
| Problem List | Pregnancy (Z33.1) |
| **Expected Result** | **EXIT: Pregnancy** |
| Rationale | Weight gain expected during pregnancy |

### TC-203: Significant Edema
| Field | Value |
|-------|-------|
| Patient | 68M |
| Height | 5'10" (178 cm) |
| Weight | 235 lbs (106.6 kg) |
| Calculated BMI | 33.7 kg/m² |
| Problem List | Heart Failure, Edema (R60.0) |
| **Expected Result** | **EXIT: Edema Present** |
| Rationale | Weight artificially elevated by fluid retention |

### TC-204: Limb Amputation
| Field | Value |
|-------|-------|
| Patient | 62M |
| Height | 5'8" (173 cm) |
| Weight | 165 lbs (74.8 kg) |
| Calculated BMI | 25.0 kg/m² |
| Problem List | Below-knee amputation (Z89.51) |
| **Expected Result** | **EXIT or Adjusted BMI** |
| Rationale | Standard BMI unreliable with amputation |

### TC-205: Missing Height Data
| Field | Value |
|-------|-------|
| Patient | 45F |
| Height | Not recorded |
| Weight | 200 lbs (90.7 kg) |
| Calculated BMI | Cannot calculate |
| **Expected Result** | **EXIT: Insufficient Data** |
| Rationale | Cannot calculate BMI without height |

### TC-206: Stale Weight Data (>12 months)
| Field | Value |
|-------|-------|
| Patient | 55M |
| Height | 6'0" (183 cm), recorded 6 months ago |
| Weight | 240 lbs (108.9 kg), recorded 14 months ago |
| Problem List | Hypertension |
| **Expected Result** | **EXIT: Stale Data** |
| Rationale | Weight data > 12 months old |

---

## Category 4: Edge Cases

### TC-301: BMI Exactly at Class I Threshold (30.0)
| Field | Value |
|-------|-------|
| Patient | 40M |
| Height | 5'9" (175.3 cm) |
| Weight | 203 lbs (92.1 kg) |
| Calculated BMI | 30.0 kg/m² |
| Problem List | None |
| **Expected Result** | **ALERT: Obesity Class I (E66.9)** |
| Rationale | 30.0 meets threshold (>= 30.0) |

### TC-302: BMI Exactly at Class II Threshold (35.0)
| Field | Value |
|-------|-------|
| Patient | 48F |
| Height | 5'4" (162.6 cm) |
| Weight | 204 lbs (92.5 kg) |
| Calculated BMI | 35.0 kg/m² |
| Problem List | Prediabetes |
| **Expected Result** | **ALERT: Obesity Class II (E66.9)** |
| Rationale | 35.0 meets Class II threshold |

### TC-303: BMI Exactly at Class III Threshold (40.0)
| Field | Value |
|-------|-------|
| Patient | 55M |
| Height | 5'10" (177.8 cm) |
| Weight | 278 lbs (126.1 kg) |
| Calculated BMI | 40.0 kg/m² |
| Problem List | Sleep Apnea |
| **Expected Result** | **ALERT: Obesity Class III (E66.01)** |
| Rationale | 40.0 meets morbid obesity threshold |

### TC-304: Unit Conversion - Metric Input
| Field | Value |
|-------|-------|
| Patient | 42F |
| Height | 165 cm |
| Weight | 95 kg |
| Calculated BMI | 34.9 kg/m² |
| Problem List | Hypertension |
| **Expected Result** | **ALERT: Obesity Class I (E66.9)** |
| Rationale | Metric units processed correctly |

### TC-305: Unit Conversion - Imperial Input
| Field | Value |
|-------|-------|
| Patient | 50M |
| Height | 70 inches |
| Weight | 245 lbs |
| Calculated BMI | 35.2 kg/m² |
| Problem List | GERD |
| **Expected Result** | **ALERT: Obesity Class II (E66.9)** |
| Rationale | Imperial units converted correctly |

---

## Category 5: Pediatric Cases

### TC-401: Pediatric Obesity (>= 95th Percentile)
| Field | Value |
|-------|-------|
| Patient | 10-year-old Male |
| Height | 54 inches (137 cm) |
| Weight | 110 lbs (49.9 kg) |
| Calculated BMI | 26.5 kg/m² |
| BMI Percentile | 97th percentile |
| Problem List | None |
| **Expected Result** | **ALERT: Pediatric Obesity (E66.9)** |
| Rationale | BMI >= 95th percentile for age/sex |

### TC-402: Pediatric Severe Obesity (>= 120% of 95th)
| Field | Value |
|-------|-------|
| Patient | 12-year-old Female |
| Height | 58 inches (147 cm) |
| Weight | 165 lbs (74.8 kg) |
| Calculated BMI | 34.5 kg/m² |
| BMI Percentile | >> 95th (exceeds 120% of 95th) |
| Problem List | Prediabetes |
| **Expected Result** | **ALERT: Pediatric Severe Obesity (E66.01)** |
| Rationale | BMI >= 120% of 95th percentile |

### TC-403: Pediatric Overweight (85th-94th Percentile)
| Field | Value |
|-------|-------|
| Patient | 8-year-old Male |
| Height | 50 inches (127 cm) |
| Weight | 72 lbs (32.7 kg) |
| Calculated BMI | 20.2 kg/m² |
| BMI Percentile | 90th percentile |
| Problem List | None |
| **Expected Result** | **NO ALERT** (or optional overweight) |
| Rationale | 90th percentile < 95th threshold |

### TC-404: Pediatric Normal Weight
| Field | Value |
|-------|-------|
| Patient | 6-year-old Female |
| Height | 45 inches (114 cm) |
| Weight | 45 lbs (20.4 kg) |
| Calculated BMI | 15.7 kg/m² |
| BMI Percentile | 50th percentile |
| Problem List | None |
| **Expected Result** | **NO ALERT** |
| Rationale | BMI at 50th percentile (normal) |

### TC-405: Infant (Age < 2 years)
| Field | Value |
|-------|-------|
| Patient | 18-month-old Male |
| Height | 32 inches (81 cm) |
| Weight | 28 lbs (12.7 kg) |
| Problem List | None |
| **Expected Result** | **EXIT: Infant (Age < 2)** |
| Rationale | Different growth chart criteria for infants |

---

## Summary Matrix

| Test Case | BMI/Percentile | Expected Outcome | Classification |
|-----------|---------------|------------------|----------------|
| TC-001 | 30.1 | Alert | Class I |
| TC-002 | 36.7 | Alert | Class II |
| TC-003 | 43.4 | Alert | Class III |
| TC-004 | 56.6 | Alert | Class III (Super) |
| TC-101 | 23.4 | No Alert | Normal |
| TC-102 | 26.4 | No Alert | Overweight |
| TC-103 | 29.8 | No Alert | Overweight |
| TC-201 | 36.9 | Exit | Already Diagnosed |
| TC-202 | 32.5 | Exit | Pregnancy |
| TC-203 | 33.7 | Exit | Edema |
| TC-204 | 25.0* | Exit | Amputation |
| TC-205 | N/A | Exit | No Height |
| TC-206 | N/A | Exit | Stale Data |
| TC-301 | 30.0 | Alert | Class I (Edge) |
| TC-302 | 35.0 | Alert | Class II (Edge) |
| TC-303 | 40.0 | Alert | Class III (Edge) |
| TC-304 | 34.9 | Alert | Class I (Metric) |
| TC-305 | 35.2 | Alert | Class II (Imperial) |
| TC-401 | 97th %ile | Alert | Pediatric Obesity |
| TC-402 | >120% of 95th | Alert | Pediatric Severe |
| TC-403 | 90th %ile | No Alert | Pediatric Overweight |
| TC-404 | 50th %ile | No Alert | Pediatric Normal |
| TC-405 | N/A | Exit | Infant |
