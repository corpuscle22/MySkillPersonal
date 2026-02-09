# Clinical Use Case: Undiagnosed Obesity Identification

## Narrative
Dr. Chen is seeing Mr. Williams (47M) for an annual wellness visit. The MA has recorded vitals: Height 5'10" (178 cm), Weight 242 lbs (110 kg). The EHR calculates BMI as 34.7 kg/m². Mr. Williams has hypertension and prediabetes on his Problem List, but "Obesity" is not documented.

As Dr. Chen opens the chart, the Obesity Identifier app runs in the background. It recognizes the calculated BMI >= 30 and the absence of an obesity diagnosis.

A non-intrusive alert appears: *"Patient BMI is 34.7 kg/m² (Class I Obesity). Obesity is not on Problem List. Click to add 'Obesity, unspecified (ICD-10 E66.9)' to Problem List."*

Dr. Chen reviews the weight trend (showing gradual increase over 3 years), agrees with the assessment, and clicks "Add". The Problem List is updated, and an automatic suggestion for "Obesity Management" (Intensive Behavioral Therapy referral, nutrition counseling) appears.

## Primary Trigger Events
| Event | Description |
|-------|-------------|
| Chart Open | Patient chart opened in ambulatory or inpatient setting |
| Vital Signs Entry | New height/weight recorded in flowsheet |
| Encounter Close | Pre-billing documentation review |
| Annual Wellness Visit | Medicare AWV or preventive visit |

## Data Requirements
| Data Element | Source | LOINC Code |
|--------------|--------|------------|
| Body Weight | Vital Signs Flowsheet | 29463-7 |
| Body Height | Vital Signs Flowsheet | 8302-2 |
| BMI (if directly recorded) | Vital Signs Flowsheet | 39156-5 |
| Date of Birth | Demographics | - |
| Sex | Demographics | - |

## BMI Calculation Logic
```
IF BMI is directly recorded in flowsheet:
    USE recorded BMI
ELSE IF Height AND Weight are available:
    CALCULATE BMI = Weight(kg) / Height(m)²

    Conversion formulas:
    - Weight: lbs × 0.453592 = kg
    - Height: inches × 0.0254 = meters
```

## Inclusion Criteria

### Adult Patients (Age >= 18)
1. Patient age >= 18 years
2. No existing active problem matching ValueSet "Obesity_All_Types"
3. Calculated or recorded BMI >= 30.0 kg/m²
4. Height and weight recorded within past 12 months

### Pediatric Patients (Age 2-17)
1. Patient age 2-17 years
2. No existing active problem matching ValueSet "Obesity_Pediatric"
3. BMI >= 95th percentile for age and sex (per CDC growth charts)
4. Height and weight recorded within past 12 months

## Exclusion Criteria
| Criterion | Rationale |
|-----------|-----------|
| Existing Obesity Diagnosis | Already documented - no action needed |
| Current Pregnancy | Weight gain expected; separate guidelines apply |
| Active Edema/Ascites | Weight may be artificially elevated |
| Limb Amputation | Standard BMI calculation unreliable |
| Age < 2 years | Infant growth charts differ |
| Height/Weight > 12 months old | Data may be stale |

## Classification Logic

### Adult BMI Classification
| BMI (kg/m²) | Classification | ICD-10 | SNOMED CT |
|-------------|----------------|--------|-----------|
| 30.0 - 34.9 | Obesity Class I | E66.9 | 414916001 |
| 35.0 - 39.9 | Obesity Class II | E66.9 | 414916001 |
| >= 40.0 | Obesity Class III (Morbid) | E66.01 | 238136002 |

### Special Cases
| Condition | Suggested Code | Notes |
|-----------|---------------|-------|
| Drug-induced obesity | E66.1 | If on known weight-gain medications |
| Obesity with alveolar hypoventilation | E66.2 | If concurrent OHS/Pickwickian |
| Overweight (BMI 25-29.9) | E66.3 | Optional - not obesity but elevated |

## User Workflow

```
[Vital Signs Recorded or Chart Opened]
        |
        v
[Calculate/Retrieve BMI]
        |
        v
[BMI >= 30? (Adult) or >= 95th %ile (Peds)]
        |
       No -----> [Check Overweight 25-29.9?]
        |              |
       Yes            Yes/No
        |              |
        v              v
[Obesity on Problem List?]  [Optional Overweight Alert]
        |
       Yes -----> [Exit Silently]
        |
       No
        |
        v
[Display Alert Banner]
   "BMI 34.7 - Obesity Class I not documented"
   [View Trend] [Add to Problem List] [Dismiss]
        |
        v
[Provider Action]
   |           |           |
   v           v           v
[View      [Add          [Dismiss]
 Weight     Condition     |
 Trend]     to EHR]       v
   |           |       [Log Reason]
   v           v
[Show      [Update Problem List]
 Graph]         |
                v
           [Suggest Order Set:
            - Nutrition Referral
            - Sleep Study (if BMI >= 35)
            - Metabolic Panel
            - Lipid Panel]
```

## Alert Display Requirements
1. **Non-Interruptive**: Banner alert, not modal popup (except for Class III)
2. **BMI Display**: Show calculated BMI with classification
3. **Trend Available**: Link to weight history graph
4. **One-Click Action**: Add diagnosis without additional navigation
5. **Severity Indication**: Color-code by obesity class
6. **Snooze Option**: "Remind me next visit" for patient discussion

## Expected Outcomes
| Metric | Target |
|--------|--------|
| Alert Sensitivity | >= 98% (simple calculation) |
| Alert Specificity | >= 95% |
| Provider Acceptance Rate | >= 60% |
| Documentation Rate Improvement | 50% increase in obesity coding |
| Time to Documentation | < 15 seconds from alert |
