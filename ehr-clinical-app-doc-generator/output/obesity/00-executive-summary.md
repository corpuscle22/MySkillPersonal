# Executive Summary: Undiagnosed Obesity Identifier

## Problem Statement
Obesity is a chronic disease affecting over 40% of American adults, yet it remains significantly under-documented in Electronic Health Records. Studies show that only 20-30% of patients with BMI >= 30 have obesity formally coded on their Problem List. This documentation gap results in missed opportunities for evidence-based interventions (behavioral counseling, pharmacotherapy, bariatric surgery referrals), inaccurate risk adjustment for value-based care contracts, and failure to trigger appropriate preventive care protocols.

## Proposed Solution
The **Obesity Identifier** is an EHR-integrated Clinical Decision Support (CDS) application. It automatically evaluates patient vital signs (height, weight) to calculate BMI and identify patients meeting obesity criteria per **CDC/WHO guidelines**. When a patient has BMI >= 30 kg/m² *without* an existing obesity diagnosis on their Problem List, the system triggers a non-interruptive alert to the provider, suggesting the precise severity classification and ICD-10 code (e.g., "Obesity, Class II - BMI 35-39.9") to be added with a single click.

## Diagnostic Criteria (CDC/WHO)

### Adult BMI Classification (Age >= 18)
| Category | BMI Range (kg/m²) | ICD-10 Code |
|----------|-------------------|-------------|
| Underweight | < 18.5 | R63.6 |
| Normal weight | 18.5 - 24.9 | - |
| Overweight | 25.0 - 29.9 | E66.3 |
| **Obesity Class I** | **30.0 - 34.9** | **E66.9** |
| **Obesity Class II** | **35.0 - 39.9** | **E66.9** |
| **Obesity Class III (Severe)** | **>= 40.0** | **E66.01** |

### Pediatric BMI Classification (Age 2-17)
| Category | BMI Percentile |
|----------|---------------|
| Underweight | < 5th percentile |
| Normal weight | 5th - 84th percentile |
| Overweight | 85th - 94th percentile |
| **Obesity** | **>= 95th percentile** |
| **Severe Obesity** | **>= 120% of 95th percentile** |

## Clinical Impact
- **Early Intervention**: Identifies patients eligible for intensive behavioral therapy (IBT), covered by Medicare.
- **Pharmacotherapy Triggers**: Flags patients who may benefit from FDA-approved anti-obesity medications.
- **Bariatric Surgery Eligibility**: Identifies Class II/III obesity for surgical referral consideration.
- **Improved Coding**: Ensures accurate HCC coding and RAF scores for value-based care.
- **Comorbidity Screening**: Triggers screening for obesity-related conditions (T2DM, OSA, NAFLD, HTN).
- **Population Health**: Enables obesity registry for care management programs.

## Target Users
- Primary Care Providers (PCPs)
- Endocrinologists
- Bariatric Surgery Programs
- Population Health Managers
- Clinical Documentation Improvement (CDI) Specialists
- Pediatricians

## EHR Integration Scope
- **Primary**: Epic (BestPractice Alert, Problem List Write-back), Cerner (Discern Rule).
- **Standard**: HL7 FHIR R4 (Condition, Observation resources), CDS Hooks.
- **Data Source**: Vital Signs (height, weight) from flowsheets.

## Key Differentiators
1. **Automatic BMI Calculation**: Derives BMI from height/weight if not directly documented.
2. **Severity Classification**: Distinguishes Class I, II, and III obesity for appropriate interventions.
3. **Pediatric Support**: Uses age/sex-specific BMI percentiles for patients 2-17 years.
4. **Trend Awareness**: Can identify weight trajectory for early intervention.
5. **Exclusion Logic**: Accounts for pregnancy, edema, amputations affecting weight interpretation.
