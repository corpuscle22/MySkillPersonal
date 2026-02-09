# Clinical Use Case Specification: Diabetes Mellitus Identifier

## Narrative Description
When a clinician opens a patient's chart or reviews laboratory results, the Diabetes Mellitus Identifier automatically evaluates the patient's recent HbA1c, fasting plasma glucose (FPG), and oral glucose tolerance test (OGTT) results against ADA diagnostic criteria. If qualifying values are present and diabetes/prediabetes is not already documented on the active problem list, the system generates a clinical decision support alert recommending that the clinician add the appropriate diagnosis.

The alert provides:
- The qualifying laboratory value(s) with dates
- Suggested ICD-10 and SNOMED CT codes
- One-click actions to add the diagnosis to the problem list
- Links to order follow-up tests or referrals
- Override options with documented reasons

## Patient Population

### Inclusion Criteria
- Age >= 18 years (adult criteria)
- Age 10-17 years (pediatric/adolescent screening per ADA)
- Has at least one qualifying laboratory result within the past 12 months:
  - HbA1c >= 5.7% (prediabetes) or >= 6.5% (diabetes)
  - Fasting Plasma Glucose >= 100 mg/dL (prediabetes) or >= 126 mg/dL (diabetes)
  - 2-hour OGTT >= 140 mg/dL (prediabetes) or >= 200 mg/dL (diabetes)
  - Random glucose >= 200 mg/dL with symptoms

### Exclusion Criteria
- Existing diagnosis of diabetes mellitus (any type) on active problem list
- Existing diagnosis of prediabetes (for prediabetes alerts only)
- Current pregnancy (gestational diabetes has different criteria)
- Known hemoglobinopathy affecting HbA1c reliability (sickle cell, thalassemia)
- Recent blood transfusion within 90 days (affects HbA1c)
- End-stage renal disease on dialysis (affects HbA1c)
- Age < 10 years (different pediatric criteria apply)

## Clinical Triggers
| Trigger | Hook | Event | Data Source |
|---------|------|-------|-------------|
| Chart Open | patient-view | Clinician opens patient chart | FHIR Patient context |
| Lab Result Review | order-sign | Clinician reviews/signs lab results | FHIR Observation (lab) |
| New Lab Result | ORU^R01 | Laboratory result interface message | HL7v2 ORU |

## User Stories

### US-001: Identify Undiagnosed Diabetes
**As a** primary care physician
**I want** to be alerted when a patient has qualifying lab values for diabetes without a documented diagnosis
**So that** I can add diabetes to the problem list and initiate appropriate management

**Acceptance Criteria:**
- [ ] Alert fires when HbA1c >= 6.5% and no diabetes on problem list
- [ ] Alert fires when FPG >= 126 mg/dL (confirmed on 2 occasions) and no diabetes on problem list
- [ ] Alert displays the qualifying lab value(s) with dates
- [ ] Alert provides one-click action to add E11.9 to problem list
- [ ] Alert can be dismissed with documented reason

### US-002: Identify Prediabetes
**As a** primary care physician
**I want** to be alerted when a patient has lab values indicating prediabetes
**So that** I can document the diagnosis and initiate lifestyle counseling

**Acceptance Criteria:**
- [ ] Alert fires when HbA1c 5.7-6.4% and no prediabetes/diabetes on problem list
- [ ] Alert fires when FPG 100-125 mg/dL and no prediabetes/diabetes on problem list
- [ ] Alert provides one-click action to add R73.03 to problem list
- [ ] Alert includes link to order nutrition counseling referral

### US-003: Avoid Alert Fatigue
**As a** clinician
**I want** alerts to be relevant and actionable
**So that** I don't become desensitized to clinical decision support

**Acceptance Criteria:**
- [ ] Alert does not fire if diabetes/prediabetes already on problem list
- [ ] Alert does not fire for pregnant patients
- [ ] Alert can be snoozed for 30 days with documented reason
- [ ] Alert severity is appropriate (warning, not critical)

### US-004: Document Override Reason
**As a** clinician
**I want** to document why I'm declining to add a diabetes diagnosis
**So that** there is a clear audit trail and the alert doesn't repeatedly fire

**Acceptance Criteria:**
- [ ] Override reasons include: "Hemoglobinopathy affecting A1c", "Stress hyperglycemia", "Will recheck in 3 months", "Patient declined diagnosis"
- [ ] Override reason is logged to audit database
- [ ] Override suppresses alert for configurable period (default 90 days)

## Expected Outcomes
| Metric | Current State | Target | Measurement |
|--------|---------------|--------|-------------|
| Undiagnosed diabetes rate | ~23% | <10% | Problem list vs. qualifying labs |
| Time to diagnosis | Unknown | <30 days from qualifying lab | Lab date to problem list date |
| Alert acceptance rate | N/A | >60% | Accepted / (Accepted + Overridden) |
| Alert override rate | N/A | <40% | Overridden / Total alerts |

## Clinical Performance Requirements
| Metric | Target | Rationale |
|--------|--------|-----------|
| Sensitivity | >= 95% | Capture nearly all patients with qualifying labs |
| Specificity | >= 85% | Minimize false positives from transient elevations |
| Positive Predictive Value | >= 80% | High confidence when alert fires |
| Alert Response Time | < 500ms | Real-time workflow integration |
