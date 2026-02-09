# CDS Hooks Specification: Obesity Identifier

## Overview
This specification defines the CDS Hooks implementation for the Obesity Identifier service, enabling real-time clinical decision support for obesity identification based on vital signs data.

## Service Definition

### Service Discovery Response
```json
{
  "services": [
    {
      "id": "obesity-identifier",
      "hook": "patient-view",
      "title": "Obesity Identifier",
      "description": "Identifies patients with undiagnosed obesity based on BMI calculated from vital signs per CDC/WHO guidelines",
      "prefetch": {
        "patient": "Patient/{{context.patientId}}",
        "conditions": "Condition?patient={{context.patientId}}&clinical-status=active",
        "weight": "Observation?patient={{context.patientId}}&code=29463-7&_sort=-date&_count=5",
        "height": "Observation?patient={{context.patientId}}&code=8302-2&_sort=-date&_count=5",
        "bmi": "Observation?patient={{context.patientId}}&code=39156-5&_sort=-date&_count=5"
      }
    }
  ]
}
```

## Supported Hooks

### 1. patient-view
**Trigger**: When a clinician opens a patient's chart.

### 2. encounter-start
**Trigger**: When a new encounter begins.

### 3. order-sign (vital signs)
**Trigger**: When vital signs are recorded/signed.

---

## Request Format

### Hook Request Example
```json
{
  "hookInstance": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "fhirServer": "https://ehr.example.org/fhir",
  "hook": "patient-view",
  "fhirAuthorization": {
    "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "Bearer",
    "expires_in": 3600,
    "scope": "patient/*.read"
  },
  "context": {
    "userId": "Practitioner/12345",
    "patientId": "Patient/67890",
    "encounterId": "Encounter/11111"
  },
  "prefetch": {
    "patient": {
      "resourceType": "Patient",
      "id": "67890",
      "birthDate": "1975-03-15",
      "gender": "male"
    },
    "conditions": {
      "resourceType": "Bundle",
      "entry": [
        {
          "resource": {
            "resourceType": "Condition",
            "code": {
              "coding": [{
                "system": "http://hl7.org/fhir/sid/icd-10-cm",
                "code": "I10",
                "display": "Essential hypertension"
              }]
            }
          }
        }
      ]
    },
    "weight": {
      "resourceType": "Bundle",
      "entry": [
        {
          "resource": {
            "resourceType": "Observation",
            "code": {
              "coding": [{"system": "http://loinc.org", "code": "29463-7"}]
            },
            "effectiveDateTime": "2024-02-08",
            "valueQuantity": {"value": 110, "unit": "kg"}
          }
        }
      ]
    },
    "height": {
      "resourceType": "Bundle",
      "entry": [
        {
          "resource": {
            "resourceType": "Observation",
            "code": {
              "coding": [{"system": "http://loinc.org", "code": "8302-2"}]
            },
            "effectiveDateTime": "2024-01-15",
            "valueQuantity": {"value": 178, "unit": "cm"}
          }
        }
      ]
    },
    "bmi": {
      "resourceType": "Bundle",
      "entry": []
    }
  }
}
```

---

## Response Format

### Positive Response (Obesity Identified)
```json
{
  "cards": [
    {
      "uuid": "obesity-alert-12345",
      "summary": "Undiagnosed Obesity Class II Detected (BMI 34.7)",
      "detail": "Patient BMI is **34.7 kg/m²** (Class II Obesity).\n\n**Calculation:**\n- Weight: 110 kg (2024-02-08)\n- Height: 178 cm (2024-01-15)\n- BMI = 110 / (1.78)² = 34.7\n\nObesity is not currently on the Problem List.",
      "indicator": "warning",
      "source": {
        "label": "Obesity Identifier",
        "url": "https://cds.example.org/obesity-identifier",
        "topic": {
          "coding": [
            {
              "system": "http://snomed.info/sct",
              "code": "414916001",
              "display": "Obesity"
            }
          ]
        }
      },
      "suggestions": [
        {
          "label": "Add Obesity to Problem List",
          "uuid": "suggestion-add-obesity",
          "isRecommended": true,
          "actions": [
            {
              "type": "create",
              "description": "Add Condition: Obesity, unspecified",
              "resource": {
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
                "subject": {"reference": "Patient/67890"},
                "onsetDateTime": "2024-02-08",
                "evidence": [{
                  "detail": [{"reference": "Observation/bmi-calculated"}]
                }]
              }
            },
            {
              "type": "create",
              "description": "Add BMI documentation code",
              "resource": {
                "resourceType": "Condition",
                "code": {
                  "coding": [{
                    "system": "http://hl7.org/fhir/sid/icd-10-cm",
                    "code": "Z68.34",
                    "display": "Body mass index (BMI) 34.0-34.9, adult"
                  }]
                },
                "subject": {"reference": "Patient/67890"}
              }
            }
          ]
        },
        {
          "label": "Refer to Nutrition Counseling",
          "uuid": "suggestion-nutrition",
          "actions": [
            {
              "type": "create",
              "description": "Order: Nutrition Counseling Referral",
              "resource": {
                "resourceType": "ServiceRequest",
                "status": "draft",
                "intent": "order",
                "code": {
                  "coding": [{
                    "system": "http://snomed.info/sct",
                    "code": "11816003",
                    "display": "Diet education"
                  }]
                },
                "subject": {"reference": "Patient/67890"}
              }
            }
          ]
        },
        {
          "label": "Order Metabolic Labs",
          "uuid": "suggestion-labs",
          "actions": [
            {
              "type": "create",
              "description": "Order: Lipid Panel, HbA1c, CMP",
              "resource": {
                "resourceType": "ServiceRequest",
                "status": "draft",
                "intent": "order",
                "code": {
                  "coding": [{
                    "system": "http://loinc.org",
                    "code": "24331-1",
                    "display": "Lipid panel"
                  }]
                },
                "subject": {"reference": "Patient/67890"}
              }
            }
          ]
        }
      ],
      "links": [
        {
          "label": "View Weight Trend",
          "url": "https://ehr.example.org/patient/67890/vitals/weight-trend",
          "type": "smart"
        },
        {
          "label": "Intensive Behavioral Therapy (Medicare)",
          "url": "https://www.cms.gov/medicare-coverage-database/view/ncd.aspx?NCDId=353",
          "type": "absolute"
        }
      ],
      "overrideReasons": [
        {
          "code": {
            "coding": [{
              "system": "http://cds.example.org/override-reasons",
              "code": "fluid-retention",
              "display": "Weight elevated due to fluid retention/edema"
            }]
          }
        },
        {
          "code": {
            "coding": [{
              "system": "http://cds.example.org/override-reasons",
              "code": "athlete",
              "display": "Patient is muscular athlete (BMI misleading)"
            }]
          }
        },
        {
          "code": {
            "coding": [{
              "system": "http://cds.example.org/override-reasons",
              "code": "patient-declined",
              "display": "Patient declined obesity documentation"
            }]
          }
        }
      ]
    }
  ]
}
```

### Class III (Morbid) Obesity Response - Higher Priority
```json
{
  "cards": [
    {
      "uuid": "obesity-alert-morbid-12345",
      "summary": "Morbid Obesity Detected (BMI 43.4) - Consider Bariatric Referral",
      "detail": "Patient BMI is **43.4 kg/m²** (Class III / Morbid Obesity).\n\nThis patient may be eligible for:\n- Intensive Behavioral Therapy (IBT)\n- FDA-approved anti-obesity medications\n- Bariatric surgery evaluation",
      "indicator": "critical",
      "source": {
        "label": "Obesity Identifier"
      },
      "suggestions": [
        {
          "label": "Add Morbid Obesity to Problem List",
          "uuid": "suggestion-add-morbid-obesity",
          "isRecommended": true,
          "actions": [
            {
              "type": "create",
              "description": "Add Condition: Morbid (severe) obesity",
              "resource": {
                "resourceType": "Condition",
                "code": {
                  "coding": [
                    {
                      "system": "http://snomed.info/sct",
                      "code": "238136002",
                      "display": "Morbid obesity"
                    },
                    {
                      "system": "http://hl7.org/fhir/sid/icd-10-cm",
                      "code": "E66.01",
                      "display": "Morbid (severe) obesity due to excess calories"
                    }
                  ]
                },
                "subject": {"reference": "Patient/67890"}
              }
            }
          ]
        },
        {
          "label": "Refer to Bariatric Surgery",
          "uuid": "suggestion-bariatric",
          "actions": [
            {
              "type": "create",
              "description": "Referral: Bariatric Surgery Consultation",
              "resource": {
                "resourceType": "ServiceRequest",
                "status": "draft",
                "intent": "order",
                "code": {
                  "coding": [{
                    "system": "http://snomed.info/sct",
                    "code": "305353004",
                    "display": "Referral to bariatric surgery service"
                  }]
                },
                "subject": {"reference": "Patient/67890"}
              }
            }
          ]
        }
      ]
    }
  ]
}
```

### No Alert Response
```json
{
  "cards": []
}
```

---

## Indicator Levels by BMI Class

| BMI Classification | Indicator | Color |
|-------------------|-----------|-------|
| Class I (30-34.9) | warning | Yellow |
| Class II (35-39.9) | warning | Orange |
| Class III (>= 40) | critical | Red |
| Pediatric Obesity | warning | Yellow |
| Pediatric Severe | critical | Red |

---

## Security & Performance

| Requirement | Value |
|-------------|-------|
| Authentication | OAuth 2.0 Bearer Token |
| SMART Scopes | patient/*.read |
| Response Time | < 300ms (simple calculation) |
| Availability | 99.9% uptime |
| Audit Logging | All presentations logged |
