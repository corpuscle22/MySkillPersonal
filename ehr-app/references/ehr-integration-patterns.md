# EHR Integration Patterns

## Table of Contents
1. [FHIR R4 Integration](#fhir-r4-integration)
2. [CDS Hooks Specification](#cds-hooks-specification)
3. [SMART on FHIR](#smart-on-fhir)
4. [Epic Integration](#epic-integration)
5. [Cerner Integration](#cerner-integration)
6. [HL7v2 Interfaces](#hl7v2-interfaces)
7. [Security Patterns](#security-patterns)

---

## FHIR R4 Integration

### Base Specification
- **FHIR Version**: R4 (4.0.1)
- **Profile Set**: US Core IG v6.1+
- **Base URL Pattern**: `https://{ehr-server}/fhir/R4`

### Common Resources

#### Patient
```json
{
  "resourceType": "Patient",
  "id": "example",
  "identifier": [{
    "system": "http://hospital.org/mrn",
    "value": "12345"
  }],
  "name": [{"family": "Smith", "given": ["John"]}],
  "gender": "male",
  "birthDate": "1970-01-01"
}
```

#### Observation (Vital/Lab)
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
  "subject": {"reference": "Patient/example"},
  "effectiveDateTime": "2024-01-15",
  "valueQuantity": {
    "value": 85,
    "unit": "kg",
    "system": "http://unitsofmeasure.org",
    "code": "kg"
  }
}
```

#### Condition (Diagnosis)
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
    "coding": [{
      "system": "http://snomed.info/sct",
      "code": "414916001",
      "display": "Obesity"
    }]
  },
  "subject": {"reference": "Patient/example"}
}
```

### Search Parameters
| Resource | Common Searches |
|----------|-----------------|
| Patient | identifier, name, birthdate, gender |
| Observation | patient, code, date, category |
| Condition | patient, clinical-status, code |
| MedicationRequest | patient, status, authoredon |
| Encounter | patient, date, status |

---

## CDS Hooks Specification

### Service Discovery
**Endpoint**: `GET /cds-services`

```json
{
  "services": [{
    "id": "example-service",
    "hook": "patient-view",
    "title": "Example Clinical Decision Support",
    "description": "Provides alerts for [condition]",
    "prefetch": {
      "patient": "Patient/{{context.patientId}}",
      "conditions": "Condition?patient={{context.patientId}}&clinical-status=active",
      "observations": "Observation?patient={{context.patientId}}&code=[LOINC]&_sort=-date&_count=5"
    }
  }]
}
```

### Standard Hooks
| Hook | Trigger | Use Case |
|------|---------|----------|
| patient-view | Chart opened | Passive alerts, reminders |
| encounter-start | Encounter begins | Admission screening |
| order-select | Order being selected | Order guidance |
| order-sign | Order being signed | Final safety checks |
| medication-prescribe | Rx being written | Drug interaction alerts |

### Hook Request
```json
{
  "hookInstance": "uuid",
  "fhirServer": "https://ehr.example.org/fhir",
  "hook": "patient-view",
  "context": {
    "userId": "Practitioner/123",
    "patientId": "Patient/456",
    "encounterId": "Encounter/789"
  },
  "fhirAuthorization": {
    "access_token": "...",
    "token_type": "Bearer",
    "expires_in": 3600,
    "scope": "patient/*.read"
  },
  "prefetch": { /* prefetched resources */ }
}
```

### Card Response
```json
{
  "cards": [{
    "uuid": "alert-uuid",
    "summary": "Alert headline (< 140 chars)",
    "detail": "Detailed markdown explanation",
    "indicator": "warning",
    "source": {
      "label": "Service Name",
      "url": "https://cds.example.org"
    },
    "suggestions": [{
      "label": "Suggested Action",
      "uuid": "suggestion-uuid",
      "isRecommended": true,
      "actions": [{
        "type": "create",
        "description": "Create resource",
        "resource": { /* FHIR resource */ }
      }]
    }],
    "links": [{
      "label": "Learn More",
      "url": "https://example.org/info",
      "type": "absolute"
    }],
    "overrideReasons": [{
      "code": {
        "coding": [{
          "system": "http://example.org/override-reasons",
          "code": "reason-code",
          "display": "Override reason"
        }]
      }
    }]
  }]
}
```

### Indicator Levels
| Indicator | Color | Use Case |
|-----------|-------|----------|
| info | Blue | Informational |
| warning | Yellow/Orange | Attention needed |
| critical | Red | Urgent action required |

---

## SMART on FHIR

### Launch Sequence (EHR Launch)
1. EHR redirects to: `{app-launch-url}?iss={fhir-base}&launch={launch-token}`
2. App requests authorization: `{authorize-url}?response_type=code&client_id=...&scope=...&launch=...&redirect_uri=...&state=...&aud={fhir-base}`
3. User authorizes (if needed)
4. EHR redirects to: `{redirect-uri}?code={auth-code}&state=...`
5. App exchanges code for token: `POST {token-url}`
6. App receives: access_token, patient context, encounter context

### Required Scopes
```
launch
patient/Patient.read
patient/Observation.read
patient/Condition.read
patient/MedicationRequest.read
```

### Token Response
```json
{
  "access_token": "...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "scope": "launch patient/*.read",
  "patient": "Patient/123",
  "encounter": "Encounter/456"
}
```

---

## Epic Integration

### App Orchard / Showroom
- **Sandbox**: https://open.epic.com
- **Registration**: Epic App Orchard submission required
- **Review Process**: Clinical and technical review

### Epic FHIR Endpoints
| Environment | Base URL Pattern |
|-------------|------------------|
| Sandbox | https://fhir.epic.com/interconnect-fhir-oauth/api/FHIR/R4 |
| Production | https://{customer-subdomain}/api/FHIR/R4 |

### Epic-Specific Considerations
- **BestPractice Alerts (BPAs)**: Epic's native CDS alerting
- **SmartData Elements (SDEs)**: For writing back discrete data
- **MyChart Integration**: Patient-facing app integration
- **Epic Interconnect**: Middleware for API access

### Epic Backend Services
For system-to-system integration (no user context):
- JWT-based authentication
- Requires Epic Backend Services app registration

---

## Cerner Integration

### Cerner Code Program
- **Sandbox**: https://code.cerner.com
- **Registration**: Cerner Code developer account
- **Certification**: Cerner Code certification process

### Cerner FHIR Endpoints
| Environment | Base URL Pattern |
|-------------|------------------|
| Sandbox | https://fhir-myrecord.cerner.com/r4/{tenant-id} |
| Production | https://fhir-{region}.cerner.com/r4/{tenant-id} |

### Cerner-Specific Considerations
- **Millennium APIs**: Native Cerner APIs
- **PowerChart Integration**: Provider-facing workflow
- **MPages**: Custom workflow pages
- **HealtheIntent**: Population health platform

---

## HL7v2 Interfaces

### Common Message Types
| Message | Trigger | Use Case |
|---------|---------|----------|
| ADT^A01 | Admit | Patient admission |
| ADT^A08 | Update | Patient update |
| ORM^O01 | Order | New order |
| ORU^R01 | Result | Lab/clinical result |
| RDE^O11 | Pharmacy | Medication order |

### ORU^R01 Structure (Lab Result)
```
MSH|^~\&|LAB|HOSP|CDS|HOSP|20240115120000||ORU^R01|MSG001|P|2.5.1
PID|1||12345^^^MRN||Smith^John||19700101|M
OBR|1||ORD001|2160-0^Creatinine^LN|||20240115080000
OBX|1|NM|2160-0^Creatinine^LN||1.2|mg/dL|0.7-1.3|N|||F
```

### Integration Middleware
- **Mirth Connect**: Open source
- **Rhapsody**: Commercial
- **Microsoft Azure FHIR**: Cloud-based
- **HAPI FHIR**: Java-based server

---

## Security Patterns

### Authentication
| Pattern | Use Case |
|---------|----------|
| OAuth 2.0 + SMART | User-authorized access |
| Backend Services JWT | System-to-system |
| Client Credentials | Service accounts |

### Required Security Controls
- TLS 1.2+ for all connections
- Token-based authentication (no API keys)
- Audit logging (who, what, when)
- Role-based access control
- PHI encryption at rest and in transit

### SMART Scopes
| Scope | Access |
|-------|--------|
| patient/*.read | Read all resources for patient |
| patient/*.write | Write all resources for patient |
| user/*.read | Read based on user's access |
| launch | EHR launch context |
| openid fhirUser | User identity |

### Audit Requirements
Log all access events:
- User/system identity
- Patient accessed
- Resources accessed
- Timestamp
- Action (read/write/delete)
- Success/failure
