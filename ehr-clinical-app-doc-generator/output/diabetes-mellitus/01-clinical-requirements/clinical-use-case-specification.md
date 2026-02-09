# Clinical Use Case: Undiagnosed Diabetes Mellitus Identification

## Narrative
Dr. Martinez is seeing Mrs. Thompson (52F) for a routine wellness visit. Mrs. Thompson has had an HbA1c of 7.2% three months ago and a fasting glucose of 142 mg/dL at today's visit, but "Diabetes Mellitus" is missing from her Problem List.

As Dr. Martinez opens the chart, the Diabetes Mellitus Identifier app runs in the background. It recognizes two confirmatory tests meeting diagnostic thresholds and the absence of a diabetes diagnosis.

A non-intrusive alert appears: *"Clinical evidence suggests Type 2 Diabetes Mellitus. HbA1c 7.2% (3 months ago) and FPG 142 mg/dL (today) meet ADA diagnostic criteria. Click to add 'Type 2 diabetes mellitus without complications (ICD-10 E11.9)' to Problem List."*

Dr. Martinez reviews the lab trend presented in the alert, agrees, and clicks "Add". The Problem List is updated, and an automatic order set for "New Diabetes Management" (A1c q3 months, lipid panel, urine microalbumin, retinal exam referral) is suggested.

## Primary Trigger Events
| Event | Description |
|-------|-------------|
| Chart Open | Patient chart opened in ambulatory or inpatient setting |
| Result Verification | New lab result (HbA1c, Glucose) is finalized |
| Order Placement | Provider places lab order for glucose or HbA1c |
| Encounter Close | Pre-billing documentation review |

## Inclusion Criteria (ALL must be met)
1. Patient age >= 18 years
2. No existing active problem matching ValueSet "Diabetes_Mellitus_All_Types"
3. Laboratory evidence meeting ONE of the following patterns:

### Pattern A: HbA1c-Based Diagnosis
- Current HbA1c >= 6.5% AND
- Historical HbA1c >= 6.5% recorded on a different day (any time in past 12 months)

### Pattern B: Fasting Glucose-Based Diagnosis
- Current Fasting Plasma Glucose >= 126 mg/dL AND
- Historical Fasting Plasma Glucose >= 126 mg/dL recorded on a different day (within 12 months)

### Pattern C: Mixed Confirmation
- Current HbA1c >= 6.5% AND Historical FPG >= 126 mg/dL (or vice versa)
- Tests on different days within 12 months

### Pattern D: Symptomatic with Random Glucose
- Random Plasma Glucose >= 200 mg/dL AND
- Documented symptoms (polyuria, polydipsia, unexplained weight loss) in problem list or note text

## Exclusion Criteria
| Criterion | Rationale |
|-----------|-----------|
| Existing Diabetes Diagnosis | Already documented - no action needed |
| Gestational Diabetes (current pregnancy) | Different management pathway |
| Active Steroid Use (>7 days) | Steroid-induced hyperglycemia is transient |
| Acute Illness (ICU admission) | Stress hyperglycemia not diagnostic |
| Age < 18 years | Pediatric criteria differ |
| Hemoglobinopathy on Problem List | May affect HbA1c accuracy |
| Recent Blood Transfusion (<90 days) | Affects HbA1c reliability |

## Optional: Prediabetes Identification
If diabetes criteria not met, check for prediabetes:
- HbA1c 5.7% - 6.4% (confirmed on two tests)
- FPG 100-125 mg/dL (confirmed on two tests)

Alert text: *"Patient meets criteria for Prediabetes. Consider adding to Problem List and lifestyle counseling."*

## User Workflow

```
[Patient Chart Opened]
        |
        v
[Background Logic Executes]
        |
        v
[Criteria Met?]---No---> [Exit Silently]
        |
       Yes
        v
[Display Alert Banner]
   "Evidence suggests Diabetes Mellitus"
   [View Details] [Add to Problem List] [Dismiss]
        |
        v
[Provider Action]
   |           |           |
   v           v           v
[View]     [Add]      [Dismiss]
   |           |           |
   v           v           v
[Show     [Write      [Log
 Lab       Condition   Dismissal
 Trend]    to EHR]     Reason]
```

## Alert Display Requirements
1. **Non-Interruptive**: Banner alert, not modal popup
2. **Evidence Summary**: Show triggering lab values with dates
3. **One-Click Action**: Add diagnosis without additional navigation
4. **Snooze Option**: "Remind me next visit" for uncertain cases
5. **Audit Trail**: Log all alert presentations and responses

## Expected Outcomes
| Metric | Target |
|--------|--------|
| Alert Sensitivity | >= 95% |
| Alert Specificity | >= 90% |
| Provider Acceptance Rate | >= 70% |
| Time to Documentation | < 30 seconds from alert |
| Problem List Accuracy | 100% correct ICD-10/SNOMED code |
