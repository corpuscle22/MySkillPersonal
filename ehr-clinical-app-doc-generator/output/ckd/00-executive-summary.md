# Executive Summary: Undiagnosed CKD Identifier & Stager

## Problem Statement
Chronic Kidney Disease (CKD) is often "silent" in its early stages. Millions of patients typically have lab results in their Electronic Health Record (EHR) indicating reduced kidney function (eGFR < 60) or kidney damage (Albuminuria) for months or years before a formal diagnosis is entered onto the Problem List. This gap leads to missed opportunities for early intervention, medication adjustment (renally cleared drugs), and care coordination.

## Proposed Solution
The **CKD Identifier** is an EHR-integrated Clinical Decision Support (CDS) application. It automatically scans patient records for longitudinal evidence of CKD based on KDIGO 2024 guidelines. When a patient meets the criteria for CKD (sustained eGFR < 60 or UACR > 30 for > 90 days) *without* an existing diagnosis, the system triggers a "Smart Alert" or "BPA" (BestPractice Alert) to the provider, suggesting the precise SNOMED CT and ICD-10 term (e.g., "Chronic kidney disease, stage 3a") to be added to the Problem List with a single click.

## Clinical Impact
- **Early Detection**: Identifies patients in Stage 3a/3b before progression to Stage 4/5.
- **Improved Coding**: Ensures accurate HCC (Hierarchical Condition Category) coding and risk adjustment.
- **Safety**: Triggers downstream checks for NSAID avoidance and medication dosing.
- **Population Health**: Populates registries for value-based care initiatives.

## Target Users
- Primary Care Providers (PCPs)
- Nephrologists
- Population Health Managers
- Clinical Documentation Improvement (CDI) Specialists

## EHR Integration Scope
- **Primary**: Epic (BestPractice Alert, Problem List Write-back), Cerner (Discern Rule, Problem List interaction).
- **Standard**: HL7 FHIR R4 (Condition, Observation resources).
