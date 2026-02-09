# Clinical Terminology Mapping Standards

## Table of Contents
1. [ICD-10-CM/PCS Codes](#icd-10-cmpcs-codes)
2. [SNOMED CT Concepts](#snomed-ct-concepts)
3. [LOINC Codes](#loinc-codes)
4. [RxNorm Codes](#rxnorm-codes)
5. [CPT/HCPCS Codes](#cpthcpcs-codes)
6. [Value Set Definitions](#value-set-definitions)
7. [FHIR Terminology Bindings](#fhir-terminology-bindings)

---

## ICD-10-CM/PCS Codes

**System URI**: `http://hl7.org/fhir/sid/icd-10-cm`

### Mapping Table Format
```markdown
| Clinical Concept | ICD-10 Code | Display Name | Notes |
|-----------------|-------------|--------------|-------|
| [Concept] | [Code] | [Display] | [Context] |
```

### Common Patterns
- Diagnosis codes: Use ICD-10-CM (Clinical Modification)
- Procedure codes: Use ICD-10-PCS (Procedure Coding System)
- Include all applicable specificity (4th, 5th, 6th, 7th characters)
- Document unspecified codes for fallback scenarios

### Example Mappings
```json
{
  "coding": [{
    "system": "http://hl7.org/fhir/sid/icd-10-cm",
    "code": "N18.3",
    "display": "Chronic kidney disease, stage 3 (moderate)"
  }]
}
```

---

## SNOMED CT Concepts

**System URI**: `http://snomed.info/sct`

### Mapping Table Format
```markdown
| Clinical Concept | SNOMED Code | Display Name | Semantic Tag |
|-----------------|-------------|--------------|--------------|
| [Concept] | [Code] | [Display] | [finding/disorder/etc] |
```

### Hierarchy Considerations
- Use most specific concept available
- Document parent concepts for broader queries
- Include both pre-coordinated and post-coordinated expressions where needed

### Common Clinical Findings
| Category | Example Code | Display |
|----------|--------------|---------|
| Vital Signs | 271649006 | Systolic blood pressure |
| Lab Results | 395123003 | Glomerular filtration rate finding |
| Diagnoses | 414916001 | Obesity |
| Procedures | 108241001 | Dialysis procedure |

---

## LOINC Codes

**System URI**: `http://loinc.org`

### Mapping Table Format
```markdown
| Measurement | LOINC Code | Long Name | Component | Property | Units |
|-------------|------------|-----------|-----------|----------|-------|
| [Test] | [Code] | [Name] | [Component] | [Prop] | [Units] |
```

### Common Laboratory Tests
| Category | LOINC | Display | Units |
|----------|-------|---------|-------|
| Renal Function | 33914-3 | eGFR CKD-EPI | mL/min/1.73m2 |
| Renal Function | 2160-0 | Creatinine, serum | mg/dL |
| Diabetes | 4548-4 | Hemoglobin A1c | % |
| Diabetes | 1558-6 | Fasting glucose | mg/dL |
| Lipids | 2093-3 | Total cholesterol | mg/dL |
| CBC | 718-7 | Hemoglobin | g/dL |

### Common Vital Signs
| Vital Sign | LOINC | Display | Units |
|------------|-------|---------|-------|
| Weight | 29463-7 | Body weight | kg |
| Height | 8302-2 | Body height | cm |
| BMI | 39156-5 | Body mass index | kg/m2 |
| BP Systolic | 8480-6 | Systolic BP | mm[Hg] |
| BP Diastolic | 8462-4 | Diastolic BP | mm[Hg] |
| Heart Rate | 8867-4 | Heart rate | /min |
| Resp Rate | 9279-1 | Respiratory rate | /min |
| Temperature | 8310-5 | Body temperature | Cel |
| SpO2 | 2708-6 | Oxygen saturation | % |

---

## RxNorm Codes

**System URI**: `http://www.nlm.nih.gov/research/umls/rxnorm`

### Mapping Table Format
```markdown
| Medication | RxCUI | Term Type | Display | Ingredient |
|------------|-------|-----------|---------|------------|
| [Drug] | [CUI] | [TTY] | [Name] | [Ingredient] |
```

### Term Types (TTY)
- **IN**: Ingredient
- **SCD**: Semantic Clinical Drug (ingredient + strength + form)
- **SBD**: Semantic Branded Drug
- **GPCK**: Generic Pack
- **BPCK**: Branded Pack

### Example Mapping
```json
{
  "coding": [{
    "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
    "code": "860975",
    "display": "Metformin hydrochloride 500 MG Oral Tablet"
  }]
}
```

---

## CPT/HCPCS Codes

**CPT System URI**: `http://www.ama-assn.org/go/cpt`
**HCPCS System URI**: `urn:oid:2.16.840.1.113883.6.285`

### Mapping Table Format
```markdown
| Service | CPT/HCPCS | Description | Category |
|---------|-----------|-------------|----------|
| [Service] | [Code] | [Desc] | [E&M/Procedure/etc] |
```

---

## Value Set Definitions

### Creating Value Sets
```json
{
  "resourceType": "ValueSet",
  "id": "example-valueset",
  "url": "http://example.org/fhir/ValueSet/example",
  "name": "ExampleValueSet",
  "status": "active",
  "compose": {
    "include": [{
      "system": "http://snomed.info/sct",
      "concept": [
        {"code": "123456", "display": "Concept 1"},
        {"code": "789012", "display": "Concept 2"}
      ]
    }]
  }
}
```

### Standard Value Set OIDs
| Value Set | OID | Description |
|-----------|-----|-------------|
| US Core Vital Signs | 2.16.840.1.113762.1.4.1222.18 | Vital sign observations |
| Problem List | 2.16.840.1.113883.3.88.12.3221.7.4 | Condition codes |

---

## FHIR Terminology Bindings

### Binding Strengths
- **required**: Must use code from value set
- **extensible**: Should use code from value set; can extend
- **preferred**: Recommended to use
- **example**: Illustrative only

### Common Bindings
| Element | Binding | Value Set |
|---------|---------|-----------|
| Condition.code | extensible | US Core Condition Codes |
| Observation.code | extensible | LOINC codes |
| MedicationRequest.medication | extensible | RxNorm |
| Encounter.type | extensible | US Core Encounter Type |

### US Core Profile Bindings
Always reference US Core IG v6.1+ for required terminology bindings:
- https://www.hl7.org/fhir/us/core/
