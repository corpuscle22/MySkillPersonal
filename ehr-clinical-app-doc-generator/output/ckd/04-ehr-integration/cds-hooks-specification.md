# CDS Hooks Specification

## Hook: patient-view
Triggered when the user opens a patient chart.

## Prefetch Template
To minimize API calls, the EHR fetches necessary data before calling the service.

```json
{
  "existingConditions": "Condition?patient={{context.patientId}}&category=problem-list-item",
  "recentLabs": "Observation?patient={{context.patientId}}&code=98979-8,45066-8,32294-1&_sort=-date&_count=20"
}
```

## Response (Card)
If CKD criteria are met:

```json
{
  "cards": [
    {
      "summary": "Undiagnosed CKD Stage 3b Detected",
      "indicator": "warning",
      "source": {
        "label": "CKD Logic Engine",
        "url": "https://kdigo.org/guidelines"
      },
      "detail": "**Action Required**: Patient has sustained eGFR < 45 for > 90 days. KDIGO guidelines recommend adding CKD Stage 3b to Problem List.",
      "suggestions": [
        {
          "label": "Add 'CKD Stage 3b' to Problem List",
          "uuid": "1234-unique-id",
          "actions": [
            {
              "type": "create",
              "description": "Create Problem List Item",
              "resource": {
                "resourceType": "Condition",
                "clinicalStatus": { "coding": [{ "system": "http://terminology.hl7.org/CodeSystem/condition-clinical", "code": "active" }] },
                "verificationStatus": { "coding": [{ "system": "http://terminology.hl7.org/CodeSystem/condition-ver-status", "code": "confirmed" }] },
                "category": [{ "coding": [{ "system": "http://terminology.hl7.org/CodeSystem/condition-category", "code": "problem-list-item" }] }],
                "code": {
                  "coding": [
                    { "system": "http://snomed.info/sct", "code": "700379002", "display": "Chronic kidney disease stage 3B" },
                    { "system": "http://hl7.org/fhir/sid/icd-10-cm", "code": "N18.32", "display": "Chronic kidney disease, stage 3b" }
                  ]
                },
                "subject": { "reference": "Patient/{{context.patientId}}" }
              }
            }
          ]
        }
      ]
    }
  ]
}
```
