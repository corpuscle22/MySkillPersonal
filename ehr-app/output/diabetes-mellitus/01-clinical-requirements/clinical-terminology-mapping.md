# Clinical Terminology Mapping: Diabetes Mellitus Identifier

## ICD-10-CM Diagnosis Codes

### Diabetes Mellitus
| Clinical Concept | ICD-10 Code | Display Name | Notes |
|-----------------|-------------|--------------|-------|
| Type 2 Diabetes, unspecified | E11.9 | Type 2 diabetes mellitus without complications | Default for new diagnoses |
| Type 2 Diabetes with CKD | E11.22 | Type 2 diabetes mellitus with diabetic chronic kidney disease | If CKD present |
| Type 2 Diabetes with neuropathy | E11.40 | Type 2 diabetes mellitus with diabetic neuropathy, unspecified | If neuropathy present |
| Type 2 Diabetes with retinopathy | E11.319 | Type 2 diabetes mellitus with unspecified diabetic retinopathy without macular edema | If retinopathy present |
| Type 1 Diabetes | E10.9 | Type 1 diabetes mellitus without complications | If Type 1 suspected |
| Other specified diabetes | E13.9 | Other specified diabetes mellitus without complications | Secondary causes |
| Drug-induced diabetes | E09.9 | Drug or chemical induced diabetes mellitus without complications | Steroid-induced, etc. |

### Prediabetes
| Clinical Concept | ICD-10 Code | Display Name | Notes |
|-----------------|-------------|--------------|-------|
| Prediabetes | R73.03 | Prediabetes | Preferred code |
| Impaired fasting glucose | R73.01 | Impaired fasting glucose | FPG 100-125 |
| Impaired glucose tolerance | R73.02 | Abnormal glucose tolerance test | OGTT 140-199 |
| Elevated HbA1c | R73.09 | Other abnormal glucose | Alternative for A1c 5.7-6.4% |

### Exclusion Conditions
| Clinical Concept | ICD-10 Code | Display Name | Exclusion Reason |
|-----------------|-------------|--------------|------------------|
| Pregnancy | Z33.1 | Pregnant state | Different criteria (GDM) |
| Gestational diabetes | O24.4* | Gestational diabetes mellitus | Separate condition |
| Sickle cell disease | D57.* | Sickle-cell disorders | Affects HbA1c |
| Thalassemia | D56.* | Thalassemia | Affects HbA1c |
| ESRD on dialysis | N18.6, Z99.2 | End stage renal disease, Dependence on renal dialysis | Affects HbA1c |

---

## SNOMED CT Concepts

### Diabetes Mellitus
| Clinical Concept | SNOMED Code | Display Name | Semantic Tag |
|-----------------|-------------|--------------|--------------|
| Type 2 diabetes | 44054006 | Diabetes mellitus type 2 | disorder |
| Type 1 diabetes | 46635009 | Diabetes mellitus type 1 | disorder |
| Diabetes mellitus | 73211009 | Diabetes mellitus | disorder |
| Secondary diabetes | 8801005 | Secondary diabetes mellitus | disorder |
| Steroid-induced diabetes | 190416008 | Steroid-induced diabetes mellitus | disorder |

### Prediabetes
| Clinical Concept | SNOMED Code | Display Name | Semantic Tag |
|-----------------|-------------|--------------|--------------|
| Prediabetes | 714628002 | Prediabetes | finding |
| Impaired fasting glucose | 9414007 | Impaired fasting glucose | finding |
| Impaired glucose tolerance | 267384006 | Impaired glucose tolerance | finding |
| At risk for diabetes | 310505005 | Impaired glucose regulation | finding |

---

## LOINC Codes (Laboratory)

### Hemoglobin A1c
| Measurement | LOINC Code | Long Name | Units | Normal Range |
|-------------|------------|-----------|-------|--------------|
| HbA1c (NGSP) | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | % | < 5.7% |
| HbA1c (IFCC) | 59261-8 | Hemoglobin A1c/Hemoglobin.total in Blood by IFCC protocol | mmol/mol | < 39 |
| HbA1c (DCCT) | 17856-6 | Hemoglobin A1c/Hemoglobin.total in Blood by HPLC | % | < 5.7% |

### Glucose
| Measurement | LOINC Code | Long Name | Units | Diabetes Threshold |
|-------------|------------|-----------|-------|--------------------|
| Fasting glucose | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | mg/dL | >= 126 |
| Fasting glucose (mmol) | 14771-0 | Fasting glucose [Moles/volume] in Serum or Plasma | mmol/L | >= 7.0 |
| Random glucose | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | mg/dL | >= 200 (symptomatic) |
| 2-hr OGTT glucose | 20438-8 | Glucose [Mass/volume] in Serum or Plasma --2 hours post 75g glucose PO | mg/dL | >= 200 |
| 1-hr OGTT glucose | 20437-0 | Glucose [Mass/volume] in Serum or Plasma --1 hour post 75g glucose PO | mg/dL | (not diagnostic) |

### Related Labs
| Measurement | LOINC Code | Long Name | Units | Notes |
|-------------|------------|-----------|-------|-------|
| C-peptide | 1986-9 | C peptide [Mass/volume] in Serum or Plasma | ng/mL | Type 1 vs 2 |
| GAD65 antibody | 56540-8 | GAD65 Ab [Units/volume] in Serum | U/mL | Type 1 marker |
| Insulin | 2484-4 | Insulin [Units/volume] in Serum or Plasma | uIU/mL | Insulin resistance |

---

## RxNorm Codes (Medications)

### Oral Antidiabetics
| Medication Class | RxCUI | Display | Notes |
|-----------------|-------|---------|-------|
| Metformin 500mg | 860975 | Metformin hydrochloride 500 MG Oral Tablet | First-line |
| Metformin 1000mg | 861007 | Metformin hydrochloride 1000 MG Oral Tablet | First-line |
| Metformin ER 500mg | 860995 | Metformin hydrochloride 500 MG Extended Release Oral Tablet | First-line |
| Glipizide 5mg | 310488 | Glipizide 5 MG Oral Tablet | Sulfonylurea |
| Sitagliptin 100mg | 593411 | Sitagliptin 100 MG Oral Tablet | DPP-4 inhibitor |
| Empagliflozin 10mg | 1545653 | Empagliflozin 10 MG Oral Tablet | SGLT2 inhibitor |

### Insulins
| Medication | RxCUI | Display | Notes |
|------------|-------|---------|-------|
| Insulin glargine | 274783 | Insulin Glargine | Basal insulin |
| Insulin lispro | 86009 | Insulin Lispro | Rapid-acting |
| Insulin regular | 5856 | Insulin, Regular, Human | Short-acting |

---

## CPT/HCPCS Codes

| Service | Code | Description | Category |
|---------|------|-------------|----------|
| HbA1c test | 83036 | Hemoglobin; glycosylated (A1c) | Lab |
| Glucose, fasting | 82947 | Glucose; quantitative, blood | Lab |
| OGTT (2-hr) | 82951 | Glucose; tolerance test (GTT), 3 specimens | Lab |
| Diabetes education | G0108 | Diabetes outpatient self-management training services, individual | E&M |
| Diabetes education group | G0109 | Diabetes self-management training services, group session | E&M |
| Medical nutrition therapy | 97802 | Medical nutrition therapy; initial assessment | E&M |

---

## Value Set Definitions

### Diabetes All Types Value Set
**OID**: 2.16.840.1.113883.3.464.1003.103.12.1001
```json
{
  "resourceType": "ValueSet",
  "id": "diabetes-all-types",
  "url": "http://example.org/fhir/ValueSet/diabetes-all-types",
  "name": "DiabetesAllTypes",
  "status": "active",
  "compose": {
    "include": [
      {
        "system": "http://hl7.org/fhir/sid/icd-10-cm",
        "filter": [{"property": "concept", "op": "is-a", "value": "E08"}]
      },
      {
        "system": "http://hl7.org/fhir/sid/icd-10-cm",
        "filter": [{"property": "concept", "op": "is-a", "value": "E09"}]
      },
      {
        "system": "http://hl7.org/fhir/sid/icd-10-cm",
        "filter": [{"property": "concept", "op": "is-a", "value": "E10"}]
      },
      {
        "system": "http://hl7.org/fhir/sid/icd-10-cm",
        "filter": [{"property": "concept", "op": "is-a", "value": "E11"}]
      },
      {
        "system": "http://hl7.org/fhir/sid/icd-10-cm",
        "filter": [{"property": "concept", "op": "is-a", "value": "E13"}]
      }
    ]
  }
}
```

### Prediabetes Value Set
```json
{
  "resourceType": "ValueSet",
  "id": "prediabetes",
  "url": "http://example.org/fhir/ValueSet/prediabetes",
  "name": "Prediabetes",
  "status": "active",
  "compose": {
    "include": [
      {
        "system": "http://hl7.org/fhir/sid/icd-10-cm",
        "concept": [
          {"code": "R73.01", "display": "Impaired fasting glucose"},
          {"code": "R73.02", "display": "Impaired glucose tolerance"},
          {"code": "R73.03", "display": "Prediabetes"},
          {"code": "R73.09", "display": "Other abnormal glucose"}
        ]
      }
    ]
  }
}
```

### HbA1c LOINC Codes Value Set
```json
{
  "resourceType": "ValueSet",
  "id": "hba1c-loinc",
  "url": "http://example.org/fhir/ValueSet/hba1c-loinc",
  "name": "HbA1cLOINC",
  "status": "active",
  "compose": {
    "include": [
      {
        "system": "http://loinc.org",
        "concept": [
          {"code": "4548-4", "display": "Hemoglobin A1c/Hemoglobin.total in Blood"},
          {"code": "17856-6", "display": "Hemoglobin A1c/Hemoglobin.total in Blood by HPLC"},
          {"code": "59261-8", "display": "Hemoglobin A1c/Hemoglobin.total in Blood by IFCC protocol"},
          {"code": "4549-2", "display": "Hemoglobin A1c/Hemoglobin.total in Blood by Electrophoresis"}
        ]
      }
    ]
  }
}
```
