# Executive Summary: Diabetes Mellitus Identifier

## Problem Statement
Approximately 38.4 million Americans have diabetes, yet an estimated 8.7 million (22.8%) remain undiagnosed. Many patients with qualifying laboratory values (HbA1c, fasting glucose, or OGTT) in their EHR do not have diabetes formally documented on their problem list, leading to missed opportunities for intervention, incomplete billing capture, and suboptimal care coordination.

## Proposed Solution
The Diabetes Mellitus Identifier is a clinical decision support (CDS) application that analyzes laboratory results in the EHR to identify patients meeting ADA diagnostic criteria for diabetes or prediabetes who lack a corresponding diagnosis on their active problem list. The system fires real-time alerts to clinicians, providing suggested ICD-10 codes and recommended next steps.

## Clinical Impact
- **Earlier Diagnosis**: Reduce time from qualifying lab result to formal diagnosis
- **Improved Documentation**: Ensure proper ICD-10 coding for quality measures and billing
- **Care Gap Closure**: Trigger appropriate follow-up testing, referrals, and education
- **Population Health**: Enable registry-based tracking of diabetic patients
- **Complication Prevention**: Earlier intervention reduces microvascular/macrovascular complications

## Target Users
| Role | Primary Use |
|------|-------------|
| Primary Care Physicians | Review alerts during patient encounters, confirm diagnoses |
| Endocrinologists | Receive referrals for complex cases |
| Nurses/Care Coordinators | Follow up on pending diagnoses, schedule education |
| Quality/Population Health Teams | Monitor screening rates and care gaps |

## EHR Integration Scope
- **Primary EHRs**: Epic, Cerner (Oracle Health)
- **Integration Method**: CDS Hooks (patient-view, order-sign), SMART on FHIR
- **Data Sources**: Laboratory results (HbA1c, glucose), Problem List, Demographics
- **Deployment Model**: Cloud-hosted with on-premise FHIR gateway

## Key Evidence
1. **ADA Standards of Care 2026**: HbA1c >= 6.5%, FPG >= 126 mg/dL, or 2-hr OGTT >= 200 mg/dL confirms diabetes ([ADA Guidelines](https://diabetesjournals.org/care/article/49/Supplement_1/S27/163926/2-Diagnosis-and-Classification-of-Diabetes))
2. **USPSTF 2021**: Screen adults 35-70 with overweight/obesity every 3 years ([USPSTF](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/screening-for-prediabetes-and-type-2-diabetes))
3. **CDC Data**: 22.8% of diabetics are undiagnosed, representing 8.7 million Americans

## Implementation Timeline (Estimated)
| Phase | Duration | Key Activities |
|-------|----------|----------------|
| Design & Architecture | 4 weeks | Requirements, clinical logic validation, architecture design |
| Core Development | 6 weeks | CDS service, clinical rules engine, FHIR client |
| EHR Integration | 4 weeks | Epic/Cerner sandbox testing, BPA configuration |
| Clinical Validation | 3 weeks | Retrospective chart review, sensitivity/specificity analysis |
| Pilot | 4 weeks | Single clinic deployment, user feedback |
| Go-Live | 2 weeks | Enterprise rollout, hypercare support |

## Risk Summary
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Alert fatigue | Medium | High | Limit to high-confidence cases, allow snoozing |
| False positives (hemoglobinopathies) | Low | Medium | Document exclusion logic, provide override reasons |
| EHR integration delays | Medium | Medium | Early engagement with Epic/Cerner teams |
| Clinician adoption | Medium | High | Training, workflow integration, champion network |

## Regulatory Considerations
- **FDA**: Meets CDS exemption criteria under 21st Century Cures Act (displays information, supports clinical judgment, clinician can independently review basis)
- **HIPAA**: Minimum necessary PHI access, audit logging, BAA with hosting provider
- **Quality Measures**: Supports HEDIS Comprehensive Diabetes Care measures
