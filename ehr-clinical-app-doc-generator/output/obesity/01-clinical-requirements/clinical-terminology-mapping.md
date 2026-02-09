# Clinical Terminology Mapping: Obesity Identification

## Diagnosis Codes

### SNOMED CT Concepts
| Concept | SNOMED CT Code | Description |
|---------|----------------|-------------|
| Obesity | 414916001 | Obesity (disorder) |
| Morbid obesity | 238136002 | Morbid obesity (disorder) |
| Overweight | 238131007 | Overweight (finding) |
| Obesity in childhood | 190966007 | Childhood obesity |
| Drug-induced obesity | 235598007 | Drug-induced obesity |
| Central obesity | 248311001 | Central obesity |

### ICD-10-CM Codes
| Code | Description | BMI Range | Typical Use |
|------|-------------|-----------|-------------|
| E66.01 | Morbid (severe) obesity due to excess calories | >= 40 | Class III obesity |
| E66.09 | Other obesity due to excess calories | 30-39.9 | Class I/II with caloric etiology |
| E66.1 | Drug-induced obesity | Any | Medication-related weight gain |
| E66.2 | Morbid obesity with alveolar hypoventilation | >= 40 | OHS/Pickwickian syndrome |
| E66.3 | Overweight | 25-29.9 | Overweight documentation |
| E66.8 | Other obesity | Any | Specified other causes |
| E66.9 | Obesity, unspecified | >= 30 | Default obesity code |
| Z68.30 | BMI 30.0-30.9, adult | 30.0-30.9 | BMI documentation |
| Z68.31 | BMI 31.0-31.9, adult | 31.0-31.9 | BMI documentation |
| Z68.32 | BMI 32.0-32.9, adult | 32.0-32.9 | BMI documentation |
| Z68.33 | BMI 33.0-33.9, adult | 33.0-33.9 | BMI documentation |
| Z68.34 | BMI 34.0-34.9, adult | 34.0-34.9 | BMI documentation |
| Z68.35 | BMI 35.0-35.9, adult | 35.0-35.9 | BMI documentation |
| Z68.36 | BMI 36.0-36.9, adult | 36.0-36.9 | BMI documentation |
| Z68.37 | BMI 37.0-37.9, adult | 37.0-37.9 | BMI documentation |
| Z68.38 | BMI 38.0-38.9, adult | 38.0-38.9 | BMI documentation |
| Z68.39 | BMI 39.0-39.9, adult | 39.0-39.9 | BMI documentation |
| Z68.41 | BMI 40.0-44.9, adult | 40.0-44.9 | BMI documentation |
| Z68.42 | BMI 45.0-49.9, adult | 45.0-49.9 | BMI documentation |
| Z68.43 | BMI 50.0-59.9, adult | 50.0-59.9 | BMI documentation |
| Z68.44 | BMI 60.0-69.9, adult | 60.0-69.9 | BMI documentation |
| Z68.45 | BMI >= 70.0, adult | >= 70 | BMI documentation |

### Pediatric ICD-10-CM Codes
| Code | Description | Percentile |
|------|-------------|------------|
| Z68.52 | BMI pediatric, 5th to <85th percentile | Normal |
| Z68.53 | BMI pediatric, 85th to <95th percentile | Overweight |
| Z68.54 | BMI pediatric, >= 95th percentile | Obesity |

### ValueSet: Obesity_All_Types (Exclusion Check)
```
OID: 2.16.840.1.113762.1.4.1222.2001 (example)

Includes:
- E66.* (All obesity codes)
- SNOMED CT: 414916001 and all descendants
- SNOMED CT: 238136002 (Morbid obesity)
```

---

## Vital Signs / Measurements (LOINC)

### Body Measurements
| LOINC Code | Component | Unit | Description |
|------------|-----------|------|-------------|
| 29463-7 | Body weight | kg, lb | Measured weight |
| 3141-9 | Body weight (stated) | kg, lb | Self-reported weight |
| 8302-2 | Body height | cm, in | Measured height |
| 8301-4 | Body height (stated) | cm, in | Self-reported height |
| 39156-5 | Body mass index (BMI) | kg/m² | Calculated or measured BMI |
| 59574-4 | BMI percentile | % | Pediatric BMI percentile |
| 8280-0 | Waist circumference | cm, in | Abdominal obesity marker |
| 56115-9 | Waist-to-hip ratio | ratio | Central obesity marker |

**ValueSet: Body_Weight_Measurements**
```
OID: 2.16.840.1.113762.1.4.1222.2002 (example)
Includes: 29463-7, 3141-9
```

**ValueSet: Body_Height_Measurements**
```
OID: 2.16.840.1.113762.1.4.1222.2003 (example)
Includes: 8302-2, 8301-4
```

**ValueSet: BMI_Measurements**
```
OID: 2.16.840.1.113762.1.4.1222.2004 (example)
Includes: 39156-5, 59574-4
```

---

## Exclusion Condition Codes

### Pregnancy (Exclusion)
| Code System | Code | Description |
|-------------|------|-------------|
| ICD-10-CM | O00-O9A | Pregnancy, childbirth, puerperium |
| ICD-10-CM | Z33.1 | Pregnant state, incidental |
| SNOMED CT | 77386006 | Pregnancy |

### Edema/Fluid Retention
| Code System | Code | Description |
|-------------|------|-------------|
| ICD-10-CM | R60.* | Edema |
| ICD-10-CM | R18.* | Ascites |
| SNOMED CT | 267038008 | Edema |

### Limb Amputation
| Code System | Code | Description |
|-------------|------|-------------|
| ICD-10-CM | Z89.* | Acquired absence of limb |
| SNOMED CT | 371166003 | Amputation status |

---

## FHIR Resource Mappings

### Observation: Body Weight
```json
{
  "resourceType": "Observation",
  "status": "final",
  "category": [{
    "coding": [{
      "system": "http://terminology.hl7.org/CodeSystem/observation-category",
      "code": "vital-signs"
    }]
  }],
  "code": {
    "coding": [{
      "system": "http://loinc.org",
      "code": "29463-7",
      "display": "Body weight"
    }]
  },
  "effectiveDateTime": "2024-02-08",
  "valueQuantity": {
    "value": 110,
    "unit": "kg",
    "system": "http://unitsofmeasure.org",
    "code": "kg"
  }
}
```

### Observation: Body Height
```json
{
  "resourceType": "Observation",
  "status": "final",
  "category": [{
    "coding": [{
      "system": "http://terminology.hl7.org/CodeSystem/observation-category",
      "code": "vital-signs"
    }]
  }],
  "code": {
    "coding": [{
      "system": "http://loinc.org",
      "code": "8302-2",
      "display": "Body height"
    }]
  },
  "effectiveDateTime": "2024-02-08",
  "valueQuantity": {
    "value": 178,
    "unit": "cm",
    "system": "http://unitsofmeasure.org",
    "code": "cm"
  }
}
```

### Observation: BMI
```json
{
  "resourceType": "Observation",
  "status": "final",
  "category": [{
    "coding": [{
      "system": "http://terminology.hl7.org/CodeSystem/observation-category",
      "code": "vital-signs"
    }]
  }],
  "code": {
    "coding": [{
      "system": "http://loinc.org",
      "code": "39156-5",
      "display": "Body mass index (BMI)"
    }]
  },
  "effectiveDateTime": "2024-02-08",
  "valueQuantity": {
    "value": 34.7,
    "unit": "kg/m2",
    "system": "http://unitsofmeasure.org",
    "code": "kg/m2"
  },
  "derivedFrom": [
    {"reference": "Observation/weight-12345"},
    {"reference": "Observation/height-12345"}
  ]
}
```

### Condition: Obesity Diagnosis
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
  "severity": {
    "coding": [{
      "system": "http://snomed.info/sct",
      "code": "6736007",
      "display": "Moderate"
    }]
  },
  "code": {
    "coding": [
      {
        "system": "http://snomed.info/sct",
        "code": "414916001",
        "display": "Obesity"
      },
      {
        "system": "http://hl7.org/fhir/sid/icd-10-cm",
        "code": "E66.9",
        "display": "Obesity, unspecified"
      }
    ]
  },
  "subject": {
    "reference": "Patient/12345"
  },
  "onsetDateTime": "2024-02-08",
  "evidence": [{
    "detail": [
      {"reference": "Observation/bmi-12345"}
    ]
  }]
}
```

---

## CDC Pediatric BMI Percentile Reference

### Boys BMI-for-Age (Selected Values)
| Age | 85th %ile | 95th %ile | 120% of 95th |
|-----|-----------|-----------|--------------|
| 5 years | 17.0 | 18.3 | 22.0 |
| 10 years | 20.5 | 23.5 | 28.2 |
| 15 years | 24.5 | 28.2 | 33.8 |

### Girls BMI-for-Age (Selected Values)
| Age | 85th %ile | 95th %ile | 120% of 95th |
|-----|-----------|-----------|--------------|
| 5 years | 17.2 | 18.6 | 22.3 |
| 10 years | 21.0 | 24.5 | 29.4 |
| 15 years | 25.5 | 30.0 | 36.0 |

*Full CDC growth chart data tables should be implemented for precise percentile calculations.*
