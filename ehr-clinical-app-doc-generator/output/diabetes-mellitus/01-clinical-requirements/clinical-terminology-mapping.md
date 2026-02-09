# Clinical Terminology Mapping: Diabetes Mellitus Identification

## Diagnosis Codes

### SNOMED CT Concepts
| Concept | SNOMED CT Code | Description |
|---------|----------------|-------------|
| Type 2 Diabetes Mellitus | 44054006 | Diabetes mellitus type 2 |
| Type 1 Diabetes Mellitus | 46635009 | Diabetes mellitus type 1 |
| Prediabetes | 714628002 | Prediabetes |
| Impaired Fasting Glucose | 9414007 | Impaired fasting glucose |
| Impaired Glucose Tolerance | 25907005 | Impaired glucose tolerance |
| Diabetes Mellitus (unspecified) | 73211009 | Diabetes mellitus |

### ICD-10-CM Codes
| Code | Description | Typical Use |
|------|-------------|-------------|
| E11.9 | Type 2 diabetes mellitus without complications | Default for new T2DM diagnosis |
| E11.65 | Type 2 diabetes mellitus with hyperglycemia | When glucose significantly elevated |
| E10.9 | Type 1 diabetes mellitus without complications | Default for new T1DM diagnosis |
| E13.9 | Other specified diabetes mellitus without complications | MODY, secondary causes |
| R73.03 | Prediabetes | Prediabetes documentation |
| R73.01 | Impaired fasting glucose | IFG documentation |
| R73.02 | Impaired glucose tolerance | IGT documentation |

### ValueSet: Diabetes_Mellitus_All_Types (Exclusion Check)
```
OID: 2.16.840.1.113762.1.4.1222.1234 (example)

Includes:
- E10.* (Type 1 diabetes mellitus, all)
- E11.* (Type 2 diabetes mellitus, all)
- E13.* (Other specified diabetes mellitus, all)
- O24.0* - O24.3* (Gestational diabetes, for pregnancy exclusion)
- SNOMED CT: 73211009 and all descendants
```

---

## Laboratory Codes (LOINC)

### HbA1c Tests
| LOINC Code | Component | Method |
|------------|-----------|--------|
| 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | Any method |
| 17856-6 | Hemoglobin A1c/Hemoglobin.total in Blood by HPLC | HPLC |
| 4549-2 | Hemoglobin A1c/Hemoglobin.total in Blood by Electrophoresis | Electrophoresis |
| 59261-8 | Hemoglobin A1c/Hemoglobin.total in Blood by IFCC protocol | IFCC standardized |

**ValueSet: HbA1c_Tests**
```
OID: 2.16.840.1.113762.1.4.1222.5678 (example)
Includes: 4548-4, 17856-6, 4549-2, 59261-8
```

### Glucose Tests
| LOINC Code | Component | Specimen/Timing |
|------------|-----------|-----------------|
| 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | Fasting |
| 1556-0 | Fasting glucose [Mass/volume] in Capillary blood | Fasting, POC |
| 2345-7 | Glucose [Mass/volume] in Serum or Plasma | Random/Non-fasting |
| 2339-0 | Glucose [Mass/volume] in Blood | Random/Non-fasting |
| 20438-8 | Glucose [Mass/volume] in Serum or Plasma --2 hours post meal | OGTT 2-hour |

**ValueSet: Fasting_Glucose_Tests**
```
OID: 2.16.840.1.113762.1.4.1222.5679 (example)
Includes: 1558-6, 1556-0
```

**ValueSet: Random_Glucose_Tests**
```
OID: 2.16.840.1.113762.1.4.1222.5680 (example)
Includes: 2345-7, 2339-0
```

**ValueSet: OGTT_2Hour_Tests**
```
OID: 2.16.840.1.113762.1.4.1222.5681 (example)
Includes: 20438-8
```

---

## Symptom Codes (for Pattern D: Symptomatic Hyperglycemia)

### SNOMED CT Symptom Concepts
| Symptom | SNOMED CT Code |
|---------|----------------|
| Polyuria | 28442001 |
| Polydipsia | 17173007 |
| Unexplained weight loss | 448765001 |
| Fatigue | 84229001 |
| Blurred vision | 246636008 |

### ICD-10-CM Symptom Codes
| Code | Description |
|------|-------------|
| R35.8 | Other polyuria |
| R63.1 | Polydipsia |
| R63.4 | Abnormal weight loss |

---

## Exclusion Condition Codes

### Gestational Diabetes (Pregnancy Exclusion)
| Code System | Code | Description |
|-------------|------|-------------|
| ICD-10-CM | O24.4* | Gestational diabetes mellitus |
| SNOMED CT | 11687002 | Gestational diabetes mellitus |

### Hemoglobinopathies (HbA1c Unreliability)
| Code System | Code | Description |
|-------------|------|-------------|
| ICD-10-CM | D57.* | Sickle-cell disorders |
| ICD-10-CM | D58.* | Other hereditary hemolytic anemias |
| ICD-10-CM | D56.* | Thalassemia |
| SNOMED CT | 127040003 | Sickle cell-hemoglobin C disease |
| SNOMED CT | 35434009 | Sickle cell anemia |

### Active Steroid Use (Relative Exclusion)
| Code System | Code | Description |
|-------------|------|-------------|
| RxNorm | 8640 | Prednisone |
| RxNorm | 6902 | Methylprednisolone |
| RxNorm | 3264 | Dexamethasone |
| RxNorm | 5492 | Hydrocortisone |

---

## FHIR Resource Mappings

### Observation (Lab Results)
```json
{
  "resourceType": "Observation",
  "status": "final",
  "category": [{
    "coding": [{
      "system": "http://terminology.hl7.org/CodeSystem/observation-category",
      "code": "laboratory"
    }]
  }],
  "code": {
    "coding": [{
      "system": "http://loinc.org",
      "code": "4548-4",
      "display": "Hemoglobin A1c/Hemoglobin.total in Blood"
    }]
  },
  "valueQuantity": {
    "value": 7.2,
    "unit": "%",
    "system": "http://unitsofmeasure.org",
    "code": "%"
  }
}
```

### Condition (Diagnosis Output)
```json
{
  "resourceType": "Condition",
  "clinicalStatus": {
    "coding": [{
      "system": "http://terminology.hl7.org/CodeSystem/condition-clinical",
      "code": "active"
    }]
  },
  "verificationStatus": {
    "coding": [{
      "system": "http://terminology.hl7.org/CodeSystem/condition-ver-status",
      "code": "confirmed"
    }]
  },
  "category": [{
    "coding": [{
      "system": "http://terminology.hl7.org/CodeSystem/condition-category",
      "code": "problem-list-item"
    }]
  }],
  "code": {
    "coding": [
      {
        "system": "http://snomed.info/sct",
        "code": "44054006",
        "display": "Diabetes mellitus type 2"
      },
      {
        "system": "http://hl7.org/fhir/sid/icd-10-cm",
        "code": "E11.9",
        "display": "Type 2 diabetes mellitus without complications"
      }
    ]
  },
  "subject": {
    "reference": "Patient/12345"
  },
  "onsetDateTime": "2024-01-15"
}
```
