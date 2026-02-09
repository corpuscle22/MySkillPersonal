# Clinical Logic Patterns

## Table of Contents
1. [Interpretation Logic Specification Template](#interpretation-logic-specification-template)
2. [Decision Tree Patterns](#decision-tree-patterns)
3. [Clinical Scoring Systems](#clinical-scoring-systems)
4. [Edge Case Handling](#edge-case-handling)
5. [Test Case Templates](#test-case-templates)

---

## Interpretation Logic Specification Template

### Standard Algorithm Structure

```markdown
## Data Inputs
- **[Input_Name]**: Description (LOINC: [code], units, normal range)

## Algorithm

### Step 1: Exclusion Check
IF (condition that should exclude patient):
    THEN EXIT (reason)

### Step 2: Data Validation
IF (required data is NULL or stale):
    THEN EXIT (Insufficient data)

### Step 3: Primary Calculation
SET [variable] = [formula or logic]

### Step 4: Classification
IF ([threshold condition]):
    SET Classification = "[Category]"
    SET Suggested_ICD10 = "[Code]"
    SET Suggested_SNOMED = [Code]
    SET Alert_Priority = "High|Medium|Low"
ELSE IF ([next condition]):
    ...

### Step 5: Logic Output
RETURN Object:
    - Alert_Type: "[Type]"
    - Classification: Classification
    - Calculated_Value: [Value]
    - Suggested_SNOMED: [Code]
    - Suggested_ICD10: "[Code]"
    - Rationale: "[Explanation with values]"
    - Priority: Alert_Priority
    - Suggested_Actions: [Array of actions]
```

---

## Decision Tree Patterns

### Standard Decision Node Structure
```
[Start Node]
    |
    v
[Exclusion Check] --YES--> [EXIT: Reason]
    |NO
    v
[Data Available?] --NO--> [EXIT: Insufficient Data]
    |YES
    v
[Calculate Value]
    |
    v
[Threshold Check] --Condition A--> [Classification A]
    |
    |--Condition B--> [Classification B]
    |
    |--Condition C--> [Classification C]
    |
    v
[Exit: No Criteria Met]
```

### Classification Thresholds Table
```markdown
| Value Range | Classification | ICD-10 | SNOMED | Priority |
|-------------|----------------|--------|--------|----------|
| >= X | Severe | [Code] | [Code] | High |
| Y - X | Moderate | [Code] | [Code] | Medium |
| Z - Y | Mild | [Code] | [Code] | Low |
| < Z | Normal | - | - | None |
```

---

## Clinical Scoring Systems

### Scoring System Template
```markdown
## [Score Name] Calculation

### Components
| Component | Criteria | Points |
|-----------|----------|--------|
| [Component 1] | [Condition] | [0-N] |
| [Component 2] | [Condition] | [0-N] |
...

### Score Interpretation
| Score Range | Risk Category | Action |
|-------------|---------------|--------|
| 0-X | Low | [Action] |
| X-Y | Moderate | [Action] |
| >= Y | High | [Action] |

### Evidence Base
- Primary Citation: [Author et al., Journal, Year]
- Validation Studies: [Citations]
```

### Common Scoring Patterns

#### Binary Component
```
IF (condition present):
    ADD 1 point
ELSE:
    ADD 0 points
```

#### Graded Component
```
IF (value >= high_threshold):
    ADD 3 points
ELSE IF (value >= medium_threshold):
    ADD 2 points
ELSE IF (value >= low_threshold):
    ADD 1 point
ELSE:
    ADD 0 points
```

---

## Edge Case Handling

### Standard Exclusion Criteria
```markdown
### Clinical Exclusions
- Pregnancy (different reference ranges apply)
- Pediatric patients (age-specific criteria)
- Recent surgery/procedure (transient abnormalities)
- Active dialysis (different targets)
- Transplant recipients (immunosuppression effects)
- Terminal illness/hospice (goals of care)

### Data Quality Exclusions
- Missing required data elements
- Data older than [X] days/months
- Implausible values (negative, extreme outliers)
- Conflicting data from multiple sources
```

### Override Handling
```markdown
## Override Reasons
| Code | Display | Description |
|------|---------|-------------|
| [code] | [display] | [when to use] |

## Override Documentation
When alert is overridden:
1. Capture override reason code
2. Record overriding clinician
3. Timestamp the override
4. Log for audit trail
```

---

## Test Case Templates

### Test Case Table Format
```markdown
| TC-ID | Patient | Input Values | Expected Output | Rationale |
|-------|---------|--------------|-----------------|-----------|
| TC-001 | 45M | [values] | ALERT: [type] | [why] |
| TC-002 | 52F | [values] | NO ALERT | [why] |
```

### Test Case Categories

#### 1. True Positive Cases (Should Fire Alert)
- Cases meeting all criteria
- Boundary cases (exactly at threshold)
- Severe/urgent cases

#### 2. True Negative Cases (Should NOT Fire Alert)
- Normal values
- Values just below threshold
- Previously diagnosed (exclusion)

#### 3. Exclusion Logic Cases
- Already diagnosed
- Pregnancy
- Pediatric age
- Missing data
- Stale data

#### 4. Edge Cases
- Exact threshold values
- Unit conversions (metric/imperial)
- Multiple qualifying criteria
- Conflicting inputs

#### 5. Population-Specific Cases
- Pediatric with age-specific criteria
- Geriatric considerations
- Race/ethnicity adjustments if applicable

### Minimum Test Case Requirements
- 15-20 test cases minimum per clinical rule
- Cover all branches of decision tree
- Include at least 3 edge cases per threshold
- Document expected behavior for null/missing data
