# Executive Summary: Undiagnosed Diabetes Mellitus Identifier

## Problem Statement
Diabetes Mellitus (DM) affects over 37 million Americans, with an estimated 8.5 million (23%) remaining undiagnosed. Many patients have laboratory evidence of diabetes in their Electronic Health Record (EHR) - elevated HbA1c, fasting glucose, or random glucose values meeting diagnostic criteria - yet lack a formal diagnosis on their Problem List. This documentation gap leads to missed opportunities for early intervention, appropriate medication management, preventive care (retinal exams, foot exams, nephropathy screening), and accurate risk adjustment coding.

## Proposed Solution
The **Diabetes Mellitus Identifier** is an EHR-integrated Clinical Decision Support (CDS) application. It automatically scans patient records for laboratory evidence of diabetes based on **ADA 2024 Standards of Care** diagnostic criteria. When a patient meets the criteria for diabetes (confirmed on two separate occasions) *without* an existing diagnosis, the system triggers a "Smart Alert" or "BPA" (BestPractice Alert) to the provider, suggesting the precise SNOMED CT and ICD-10 term (e.g., "Type 2 diabetes mellitus without complications") to be added to the Problem List with a single click.

## Diagnostic Criteria (ADA 2024)
Any ONE of the following criteria, confirmed on a separate day:
| Criterion | Threshold |
|-----------|-----------|
| HbA1c | >= 6.5% |
| Fasting Plasma Glucose (FPG) | >= 126 mg/dL |
| 2-Hour Plasma Glucose (OGTT) | >= 200 mg/dL |
| Random Plasma Glucose | >= 200 mg/dL with classic symptoms |

## Clinical Impact
- **Early Detection**: Identifies patients with undiagnosed diabetes before complications develop.
- **Improved Coding**: Ensures accurate HCC (Hierarchical Condition Category) coding and risk adjustment.
- **Preventive Care**: Triggers downstream orders for A1c monitoring, lipid panels, renal function, eye exams.
- **Medication Safety**: Alerts for metformin contraindications, SGLT2 eligibility, insulin needs.
- **Population Health**: Populates diabetes registries for value-based care initiatives.

## Target Users
- Primary Care Providers (PCPs)
- Endocrinologists
- Population Health Managers
- Clinical Documentation Improvement (CDI) Specialists
- Care Coordinators

## EHR Integration Scope
- **Primary**: Epic (BestPractice Alert, Problem List Write-back), Cerner (Discern Rule, Problem List interaction).
- **Standard**: HL7 FHIR R4 (Condition, Observation resources), CDS Hooks.

## Key Differentiators
1. **Two-Test Confirmation**: Requires confirmatory testing per ADA guidelines to avoid false positives.
2. **Prediabetes Awareness**: Optionally identifies patients with prediabetes (HbA1c 5.7-6.4%) for lifestyle intervention.
3. **Type Inference**: Suggests Type 1 vs Type 2 based on clinical context (age, BMI, C-peptide if available).
4. **Exclusion Logic**: Excludes patients with gestational diabetes, steroid-induced hyperglycemia, or known diabetes.
