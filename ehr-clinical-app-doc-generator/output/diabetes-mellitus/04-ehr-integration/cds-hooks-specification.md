# CDS Hooks Specification: Diabetes Mellitus Identifier

## Overview
This specification defines the CDS Hooks implementation for the Diabetes Mellitus Identifier service, enabling real-time clinical decision support within EHR workflows.

## Service Definition

### Service Discovery Response
```json
{
  "services": [
    {
      "id": "diabetes-mellitus-identifier",
      "hook": "patient-view",
      "title": "Diabetes Mellitus Identifier",
      "description": "Identifies patients with undiagnosed diabetes mellitus based on laboratory evidence per ADA 2024 guidelines",
      "prefetch": {
        "patient": "Patient/{{context.patientId}}",
        "conditions": "Condition?patient={{context.patientId}}&clinical-status=active",
        "hba1c_results": "Observation?patient={{context.patientId}}&code=4548-4,17856-6,4549-2,59261-8&_sort=-date&_count=10",
        "glucose_results": "Observation?patient={{context.patientId}}&code=1558-6,2345-7,2339-0&_sort=-date&_count=10",
        "medications": "MedicationRequest?patient={{context.patientId}}&status=active"
      }
    }
  ]
}
```

## Supported Hooks

### 1. patient-view
**Trigger**: When a clinician opens a patient's chart.

**Purpose**: Evaluate for undiagnosed diabetes mellitus based on historical lab data.

### 2. order-sign (Optional)
**Trigger**: When a clinician signs a lab order for HbA1c or glucose.

**Purpose**: Pre-emptive check before new labs are ordered.

---

## Request Format

### Hook Request Example
```json
{
  "hookInstance": "d1577c69-dfbe-44ad-ba6d-3e05e953b2ea",
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
      "birthDate": "1970-05-15",
      "gender": "female"
    },
    "conditions": {
      "resourceType": "Bundle",
      "entry": [
        {
          "resource": {
            "resourceType": "Condition",
            "code": {
              "coding": [
                {
                  "system": "http://hl7.org/fhir/sid/icd-10-cm",
                  "code": "I10",
                  "display": "Essential hypertension"
                }
              ]
            }
          }
        }
      ]
    },
    "hba1c_results": {
      "resourceType": "Bundle",
      "entry": [
        {
          "resource": {
            "resourceType": "Observation",
            "code": {
              "coding": [{"system": "http://loinc.org", "code": "4548-4"}]
            },
            "effectiveDateTime": "2024-01-15",
            "valueQuantity": {"value": 7.2, "unit": "%"}
          }
        },
        {
          "resource": {
            "resourceType": "Observation",
            "code": {
              "coding": [{"system": "http://loinc.org", "code": "4548-4"}]
            },
            "effectiveDateTime": "2023-10-01",
            "valueQuantity": {"value": 6.8, "unit": "%"}
          }
        }
      ]
    },
    "glucose_results": {
      "resourceType": "Bundle",
      "entry": []
    },
    "medications": {
      "resourceType": "Bundle",
      "entry": []
    }
  }
}
```

---

## Response Format

### Positive Response (Diabetes Identified)
```json
{
  "cards": [
    {
      "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      "summary": "Undiagnosed Type 2 Diabetes Mellitus Detected",
      "detail": "Patient has two HbA1c values >= 6.5% on different days:\n- 2024-01-15: 7.2%\n- 2023-10-01: 6.8%\n\nThis meets ADA 2024 diagnostic criteria for Type 2 Diabetes Mellitus.",
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
          "label": "Add Type 2 Diabetes Mellitus to Problem List",
          "uuid": "suggestion-add-dm",
          "isRecommended": true,
          "actions": [
            {
              "type": "create",
              "description": "Add Condition: Type 2 diabetes mellitus without complications",
              "resource": {
                "resourceType": "Condition",
                "clinicalStatus": {
                  "coding": [
                    {
                      "system": "http://terminology.hl7.org/CodeSystem/condition-clinical",
                      "code": "active"
                    }
                  ]
                },
                "verificationStatus": {
                  "coding": [
                    {
                      "system": "http://terminology.hl7.org/CodeSystem/condition-ver-status",
                      "code": "confirmed"
                    }
                  ]
                },
                "category": [
                  {
                    "coding": [
                      {
                        "system": "http://terminology.hl7.org/CodeSystem/condition-category",
                        "code": "problem-list-item"
                      }
                    ]
                  }
                ],
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
                  "reference": "Patient/67890"
                },
                "onsetDateTime": "2023-10-01"
              }
            }
          ]
        },
        {
          "label": "Order Diabetes Management Labs",
          "uuid": "suggestion-order-labs",
          "actions": [
            {
              "type": "create",
              "description": "Order: HbA1c, Lipid Panel, Urine Microalbumin, BMP",
              "resource": {
                "resourceType": "ServiceRequest",
                "status": "draft",
                "intent": "order",
                "code": {
                  "coding": [
                    {
                      "system": "http://loinc.org",
                      "code": "4548-4",
                      "display": "Hemoglobin A1c"
                    }
                  ]
                },
                "subject": {
                  "reference": "Patient/67890"
                }
              }
            }
          ]
        }
      ],
      "links": [
        {
          "label": "View Lab Trend",
          "url": "https://ehr.example.org/patient/67890/labs/hba1c-trend",
          "type": "smart"
        },
        {
          "label": "ADA Standards of Care 2024",
          "url": "https://diabetesjournals.org/care/issue/47/Supplement_1",
          "type": "absolute"
        }
      ],
      "overrideReasons": [
        {
          "code": {
            "coding": [
              {
                "system": "http://cds.example.org/override-reasons",
                "code": "stress-hyperglycemia",
                "display": "Values likely due to acute illness/stress"
              }
            ]
          }
        },
        {
          "code": {
            "coding": [
              {
                "system": "http://cds.example.org/override-reasons",
                "code": "already-aware",
                "display": "Clinician already aware, managing separately"
              }
            ]
          }
        },
        {
          "code": {
            "coding": [
              {
                "system": "http://cds.example.org/override-reasons",
                "code": "patient-declined",
                "display": "Patient declined documentation"
              }
            ]
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
      "uuid": "b2c3d4e5-f6a7-8901-bcde-f23456789012",
      "summary": "Prediabetes Identified",
      "detail": "Patient has two HbA1c values in the prediabetes range (5.7-6.4%):\n- 2024-01-15: 6.1%\n- 2023-09-20: 5.9%\n\nConsider adding Prediabetes to Problem List and counseling on lifestyle modifications.",
      "indicator": "info",
      "source": {
        "label": "Diabetes Mellitus Identifier",
        "url": "https://cds.example.org/diabetes-identifier"
      },
      "suggestions": [
        {
          "label": "Add Prediabetes to Problem List",
          "uuid": "suggestion-add-prediabetes",
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
                "subject": {
                  "reference": "Patient/67890"
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

### No Alert Response (Criteria Not Met)
```json
{
  "cards": []
}
```

---

## Error Handling

### Missing Prefetch Data
```json
{
  "cards": [
    {
      "summary": "Unable to evaluate for diabetes - missing lab data",
      "indicator": "info",
      "source": {
        "label": "Diabetes Mellitus Identifier"
      }
    }
  ]
}
```

---

## Feedback Endpoint

### POST /cds-services/diabetes-mellitus-identifier/feedback
```json
{
  "card": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "outcome": "accepted",
  "acceptedSuggestions": ["suggestion-add-dm"],
  "overrideReason": null
}
```

---

## Security Requirements

1. **OAuth 2.0**: All requests must include valid Bearer token
2. **SMART Scopes**: Requires `patient/*.read` scope minimum
3. **Audit Logging**: All alert presentations and responses logged
4. **PHI Handling**: No PHI stored in CDS service; stateless evaluation

---

## Performance Requirements

| Metric | Requirement |
|--------|-------------|
| Response Time | < 500ms (95th percentile) |
| Availability | 99.9% uptime |
| Concurrent Requests | 100 requests/second |
| Prefetch Timeout | 2 seconds max |
