# Glossary: Diabetes Mellitus Identifier

## Clinical Terms

| Term | Definition |
|------|------------|
| **Diabetes Mellitus** | A chronic metabolic disease characterized by elevated blood glucose levels resulting from defects in insulin secretion, insulin action, or both. |
| **Type 1 Diabetes** | Autoimmune destruction of pancreatic beta cells, leading to absolute insulin deficiency. Usually presents in childhood/adolescence. |
| **Type 2 Diabetes** | Progressive insulin secretory defect on the background of insulin resistance. Most common form (~90-95% of cases). |
| **Prediabetes** | Intermediate state of elevated glucose below diabetes threshold, indicating high risk for progression to diabetes. |
| **HbA1c (Hemoglobin A1c)** | Glycated hemoglobin reflecting average blood glucose over the past 2-3 months. Gold standard for diabetes diagnosis and monitoring. |
| **Fasting Plasma Glucose (FPG)** | Blood glucose measured after at least 8 hours of fasting. |
| **Oral Glucose Tolerance Test (OGTT)** | Diagnostic test measuring blood glucose after a 75g oral glucose load. |
| **Impaired Fasting Glucose (IFG)** | FPG between 100-125 mg/dL, a form of prediabetes. |
| **Impaired Glucose Tolerance (IGT)** | 2-hour OGTT glucose between 140-199 mg/dL, a form of prediabetes. |
| **Polyuria** | Excessive urination, a classic symptom of hyperglycemia. |
| **Polydipsia** | Excessive thirst, a classic symptom of hyperglycemia. |
| **Hemoglobinopathy** | Inherited disorders of hemoglobin (e.g., sickle cell disease, thalassemia) that can affect HbA1c accuracy. |

## Technical Terms

| Term | Definition |
|------|------------|
| **CDS Hooks** | HL7 standard for integrating clinical decision support services into EHR workflows via RESTful APIs. |
| **SMART on FHIR** | Standard for launching healthcare applications from within an EHR using OAuth 2.0 authorization. |
| **FHIR (Fast Healthcare Interoperability Resources)** | HL7 standard for exchanging healthcare information electronically. |
| **LOINC (Logical Observation Identifiers Names and Codes)** | Universal standard for identifying medical laboratory observations. |
| **SNOMED CT** | Comprehensive clinical terminology for clinical documentation and reporting. |
| **ICD-10-CM** | International Classification of Diseases, 10th revision, Clinical Modification. Used for diagnosis coding. |
| **RxNorm** | Normalized naming system for generic and branded drugs. |
| **US Core** | FHIR implementation guide for US healthcare, defining required profiles and data elements. |
| **OAuth 2.0** | Authorization framework for secure API access without sharing credentials. |
| **Bearer Token** | Access token passed in HTTP headers to authenticate API requests. |
| **Prefetch** | CDS Hooks mechanism where the EHR proactively queries data to include in the hook request. |
| **Card** | CDS Hooks response element containing alert information, suggestions, and links. |

## Organizational Terms

| Term | Definition |
|------|------------|
| **ADA** | American Diabetes Association, publisher of the Standards of Care in Diabetes. |
| **USPSTF** | U.S. Preventive Services Task Force, makes evidence-based preventive care recommendations. |
| **FDA** | U.S. Food and Drug Administration, regulates medical devices including software. |
| **SaMD** | Software as a Medical Device, FDA regulatory category for clinical software. |
| **HIPAA** | Health Insurance Portability and Accountability Act, establishes standards for PHI protection. |
| **ONC** | Office of the National Coordinator for Health IT, oversees health IT certification. |
| **Epic** | Major EHR vendor, common in academic medical centers and large health systems. |
| **Cerner (Oracle Health)** | Major EHR vendor acquired by Oracle in 2022. |

## Acronyms

| Acronym | Expansion |
|---------|-----------|
| A1c | Hemoglobin A1c |
| API | Application Programming Interface |
| BAA | Business Associate Agreement |
| BMI | Body Mass Index |
| CDS | Clinical Decision Support |
| DM | Diabetes Mellitus |
| DPP | Diabetes Prevention Program |
| DSME | Diabetes Self-Management Education |
| EHR | Electronic Health Record |
| FPG | Fasting Plasma Glucose |
| HIT | Health Information Technology |
| MLLP | Minimal Lower Layer Protocol (HL7v2 transport) |
| OGTT | Oral Glucose Tolerance Test |
| PHI | Protected Health Information |
| REST | Representational State Transfer |
| RTO | Recovery Time Objective |
| RPO | Recovery Point Objective |
| SLA | Service Level Agreement |
| SME | Subject Matter Expert |
| TLS | Transport Layer Security |
| UAT | User Acceptance Testing |

## References

1. American Diabetes Association. Standards of Care in Diabetes—2026. Diabetes Care. 2026;49(Suppl 1).
2. HL7 FHIR R4. https://hl7.org/fhir/R4/
3. CDS Hooks Specification. https://cds-hooks.org/
4. SMART App Launch Framework. https://hl7.org/fhir/smart-app-launch/
5. LOINC. https://loinc.org/
6. SNOMED CT. https://www.snomed.org/
