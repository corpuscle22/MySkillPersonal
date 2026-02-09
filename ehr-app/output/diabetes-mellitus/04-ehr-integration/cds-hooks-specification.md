# CDS Hooks Specification: Diabetes Mellitus Identifier

## Overview
This specification defines the CDS Hooks implementation for the Diabetes Mellitus Identifier service, enabling real-time clinical decision support for diabetes and prediabetes identification based on laboratory results.

## Service Definition

### Service Discovery Response
**Endpoint**: `GET /cds-services`

```json
{
  "services": [
    {
      "id": "diabetes-identifier",
      "hook": "patient-view",
      "title": "Diabetes Mellitus Identifier",
      "description": "Identifies patients with undiagnosed diabetes or prediabetes based on HbA1c, fasting glucose, and OGTT results per ADA 2026 guidelines",
      "prefetch": {
        "patient": "Patient/{{context.patientId}}",
        "conditions": "Condition?patient={{context.patientId}}&clinical-status=active",
        "hba1c": "Observation?patient={{context.patientId}}&code=4548-4,17856-6,59261-8&_sort=-date&_count=3",
        "glucose": "Observation?patient={{context.patientId}}&code=1558-6,2345-7,20438-8&_sort=-date&_count=5"
      }
    }
  ]
}
```

## Supported Hooks

### 1. patient-view
**Trigger**: When a clinician opens a patient's chart.
**Use Case**: Passive screening for undiagnosed diabetes at every encounter.

### 2. order-sign
**Trigger**: When a clinician signs/reviews laboratory orders or results.
**Use Case**: Alert when new lab results meet diagnostic criteria.

---

## Request Format

### Hook Request Example
```json
{
  "hookInstance": "d1577c69-dfbe-44ad-ba6d-3e05e953b2ea",
  "fhirServer": "https://ehr.example.org/fhir/R4",
  "hook": "patient-view",
  "fhirAuthorization": {
    "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "Bearer",
    "expires_in": 3600,
    "scope": "patient/*.read"
  },
  "context": {
    "userId": "Practitioner/dr-smith-123",
    "patientId": "Patient/pt-12345",
    "encounterId": "Encounter/enc-67890"
  },
  "prefetch": {
    "patient": {
      "resourceType": "Patient",
      "id": "pt-12345",
      "birthDate": "1970-05-15",
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
            },
            "clinicalStatus": {
              "coding": [{
                "system": "http://terminology.hl7.org/CodeSystem/condition-clinical",
                "code": "active"
              }]
            }
          }
        }
      ]
    },
    "hba1c": {
      "resourceType": "Bundle",
      "entry": [
        {
          "resource": {
            "resourceType": "Observation",
            "id": "obs-hba1c-001",
            "code": {
              "coding": [{
                "system": "http://loinc.org",
                "code": "4548-4",
                "display": "Hemoglobin A1c"
              }]
            },
            "effectiveDateTime": "2026-01-15",
            "valueQuantity": {
              "value": 7.2,
              "unit": "%",
              "system": "http://unitsofmeasure.org",
              "code": "%"
            }
          }
        }
      ]
    },
    "glucose": {
      "resourceType": "Bundle",
      "entry": [
        {
          "resource": {
            "resourceType": "Observation",
            "id": "obs-fpg-001",
            "code": {
              "coding": [{
                "system": "http://loinc.org",
                "code": "1558-6",
                "display": "Fasting glucose"
              }]
            },
            "effectiveDateTime": "2026-01-15",
            "valueQuantity": {
              "value": 138,
              "unit": "mg/dL",
              "system": "http://unitsofmeasure.org",
              "code": "mg/dL"
            }
          }
        }
      ]
    }
  }
}
```

---

## Response Format

### Positive Response - Diabetes Identified (High Confidence)
```json
{
  "cards": [
    {
      "uuid": "dm-alert-12345",
      "summary": "Undiagnosed Diabetes Mellitus Detected (HbA1c 7.2%, FPG 138)",
      "detail": "Patient meets **ADA criteria for Type 2 Diabetes Mellitus**.\n\n**Qualifying Results:**\n- HbA1c: **7.2%** (2026-01-15) — Threshold: ≥6.5%\n- Fasting Glucose: **138 mg/dL** (2026-01-15) — Threshold: ≥126 mg/dL\n\n**Confidence:** High (2 criteria met)\n\nDiabetes is not currently documented on the Problem List.",
      "indicator": "warning",
      "source": {
        "label": "Diabetes Mellitus Identifier",
        "url": "https://cds.example.org/diabetes-identifier",
        "topic": {
          "coding": [
            {
              "system": "http://snomed.info/sct",
              "code": "44054006",
              "display": "Diabetes mellitus type 2"
            }
          ]
        }
      },
      "suggestions": [
        {
          "label": "Add Type 2 Diabetes to Problem List",
          "uuid": "suggestion-add-dm",
          "isRecommended": true,
          "actions": [
            {
              "type": "create",
              "description": "Add Condition: Type 2 diabetes mellitus without complications",
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
                "subject": {"reference": "Patient/pt-12345"},
                "onsetDateTime": "2026-01-15",
                "evidence": [{
                  "detail": [
                    {"reference": "Observation/obs-hba1c-001"},
                    {"reference": "Observation/obs-fpg-001"}
                  ]
                }]
              }
            }
          ]
        },
        {
          "label": "Order HbA1c in 3 Months",
          "uuid": "suggestion-followup-a1c",
          "actions": [
            {
              "type": "create",
              "description": "Order: Hemoglobin A1c (3-month follow-up)",
              "resource": {
                "resourceType": "ServiceRequest",
                "status": "draft",
                "intent": "order",
                "code": {
                  "coding": [{
                    "system": "http://loinc.org",
                    "code": "4548-4",
                    "display": "Hemoglobin A1c"
                  }]
                },
                "subject": {"reference": "Patient/pt-12345"},
                "occurrenceDateTime": "2026-04-15"
              }
            }
          ]
        },
        {
          "label": "Refer to Diabetes Education",
          "uuid": "suggestion-dsme",
          "actions": [
            {
              "type": "create",
              "description": "Referral: Diabetes Self-Management Education",
              "resource": {
                "resourceType": "ServiceRequest",
                "status": "draft",
                "intent": "order",
                "code": {
                  "coding": [{
                    "system": "http://snomed.info/sct",
                    "code": "6143009",
                    "display": "Diabetic education"
                  }]
                },
                "subject": {"reference": "Patient/pt-12345"}
              }
            }
          ]
        },
        {
          "label": "Order Comprehensive Metabolic Panel",
          "uuid": "suggestion-cmp",
          "actions": [
            {
              "type": "create",
              "description": "Order: Comprehensive Metabolic Panel",
              "resource": {
                "resourceType": "ServiceRequest",
                "status": "draft",
                "intent": "order",
                "code": {
                  "coding": [{
                    "system": "http://loinc.org",
                    "code": "24323-8",
                    "display": "Comprehensive metabolic panel"
                  }]
                },
                "subject": {"reference": "Patient/pt-12345"}
              }
            }
          ]
        }
      ],
      "links": [
        {
          "label": "ADA Standards of Care 2026",
          "url": "https://diabetesjournals.org/care/article/49/Supplement_1/S27/163926",
          "type": "absolute"
        },
        {
          "label": "View Lab Trend",
          "url": "https://ehr.example.org/patient/pt-12345/labs/glucose-trend",
          "type": "smart"
        }
      ],
      "overrideReasons": [
        {
          "code": {
            "coding": [{
              "system": "http://cds.example.org/override-reasons",
              "code": "hemoglobinopathy",
              "display": "Patient has hemoglobinopathy affecting HbA1c"
            }]
          }
        },
        {
          "code": {
            "coding": [{
              "system": "http://cds.example.org/override-reasons",
              "code": "stress-hyperglycemia",
              "display": "Stress hyperglycemia (acute illness)"
            }]
          }
        },
        {
          "code": {
            "coding": [{
              "system": "http://cds.example.org/override-reasons",
              "code": "will-retest",
              "display": "Will recheck in 3 months"
            }]
          }
        },
        {
          "code": {
            "coding": [{
              "system": "http://cds.example.org/override-reasons",
              "code": "patient-declined",
              "display": "Patient declined diagnosis documentation"
            }]
          }
        }
      ]
    }
  ]
}
```

### Prediabetes Response
```json
{
  "cards": [
    {
      "uuid": "prediabetes-alert-67890",
      "summary": "Prediabetes Identified (HbA1c 5.9%)",
      "detail": "Patient meets criteria for **Prediabetes**.\n\n**Qualifying Results:**\n- HbA1c: **5.9%** (2026-01-20) — Range: 5.7-6.4%\n\nPrediabetes is not currently on the Problem List. Lifestyle intervention can reduce diabetes risk by 58%.",
      "indicator": "info",
      "source": {
        "label": "Diabetes Mellitus Identifier"
      },
      "suggestions": [
        {
          "label": "Add Prediabetes to Problem List",
          "uuid": "suggestion-add-prediabetes",
          "isRecommended": true,
          "actions": [
            {
              "type": "create",
              "description": "Add Condition: Prediabetes",
              "resource": {
                "resourceType": "Condition",
                "code": {
                  "coding": [
                    {
                      "system": "http://snomed.info/sct",
                      "code": "714628002",
                      "display": "Prediabetes"
                    },
                    {
                      "system": "http://hl7.org/fhir/sid/icd-10-cm",
                      "code": "R73.03",
                      "display": "Prediabetes"
                    }
                  ]
                },
                "subject": {"reference": "Patient/pt-12345"}
              }
            }
          ]
        },
        {
          "label": "Refer to Diabetes Prevention Program",
          "uuid": "suggestion-dpp",
          "actions": [
            {
              "type": "create",
              "description": "Referral: CDC Diabetes Prevention Program",
              "resource": {
                "resourceType": "ServiceRequest",
                "status": "draft",
                "intent": "order",
                "code": {
                  "coding": [{
                    "system": "http://snomed.info/sct",
                    "code": "410177006",
                    "display": "Lifestyle education"
                  }]
                },
                "subject": {"reference": "Patient/pt-12345"}
              }
            }
          ]
        }
      ],
      "links": [
        {
          "label": "CDC Diabetes Prevention Program",
          "url": "https://www.cdc.gov/diabetes/prevention/",
          "type": "absolute"
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

## Indicator Levels by Classification

| Classification | Indicator | Color | Use Case |
|----------------|-----------|-------|----------|
| Diabetes - Confirmed (2+ criteria) | warning | Orange | High confidence, immediate action |
| Diabetes - Likely (1 criterion) | warning | Yellow | Recommend confirmation |
| Prediabetes | info | Blue | Lower urgency, lifestyle focus |

---

## Security & Performance

| Requirement | Value |
|-------------|-------|
| Authentication | OAuth 2.0 Bearer Token |
| SMART Scopes | patient/*.read |
| Response Time | < 300ms (p95) |
| Availability | 99.9% uptime |
| Audit Logging | All hook invocations logged |
| PHI Handling | Minimum necessary, encrypted |

---

## Error Handling

### Insufficient Data Response
```json
{
  "cards": [
    {
      "uuid": "info-no-labs",
      "summary": "Unable to evaluate diabetes status - no recent labs",
      "detail": "No HbA1c or glucose results found within the past 12 months. Consider ordering screening labs if patient has risk factors.",
      "indicator": "info",
      "source": {"label": "Diabetes Mellitus Identifier"},
      "suggestions": [
        {
          "label": "Order Diabetes Screening Panel",
          "uuid": "suggestion-screening",
          "actions": [
            {
              "type": "create",
              "description": "Order: HbA1c + Fasting Glucose",
              "resource": {
                "resourceType": "ServiceRequest",
                "status": "draft",
                "intent": "order",
                "code": {
                  "coding": [
                    {"system": "http://loinc.org", "code": "4548-4"},
                    {"system": "http://loinc.org", "code": "1558-6"}
                  ]
                },
                "subject": {"reference": "Patient/pt-12345"}
              }
            }
          ]
        }
      ]
    }
  ]
}
```
