---
name: ehr-app
description: Generate comprehensive, production-ready documentation packages for EHR-integrated healthcare applications. Use when users ask to (1) generate documentation for healthcare/clinical applications, (2) create architecture or design docs for EHR integration with Epic, Cerner, or other systems, (3) build clinical decision support (CDS) tools, (4) document FHIR/HL7/CDS Hooks integration specifications, (5) create clinical logic with decision trees and evidence citations, (6) design workflow diagrams for medical use cases, or (7) implement SMART on FHIR apps. Triggers on phrases like "document clinical workflow", "create EHR app specs", "generate health IT architecture", "build clinical app design doc", or any clinical workflow that would benefit from EHR integration documentation.
---

# EHR Application Documentation Generator

Generate complete documentation packages for EHR-integrated healthcare applications.

## Output Structure

All documentation is generated in an `output/` directory:

```
output/
├── 00-executive-summary.md
├── 01-clinical-requirements/
│   ├── clinical-use-case-specification.md
│   ├── clinical-evidence-citations.md
│   ├── clinical-terminology-mapping.md
│   └── regulatory-compliance-checklist.md
├── 02-clinical-logic/
│   ├── interpretation-logic-specification.md
│   ├── decision-tree-chart.html
│   ├── clinical-validation-test-cases.md
│   └── edge-cases-and-exceptions.md
├── 03-architecture/
│   ├── system-architecture-overview.md
│   ├── system-architecture-diagram.html
│   ├── ehr-integration-architecture.md
│   ├── integration-sequence-diagrams.html
│   ├── api-specifications.md
│   └── security-architecture.md
├── 04-ehr-integration/
│   ├── epic-integration-guide.md
│   ├── cerner-integration-guide.md
│   ├── fhir-resource-mapping.md
│   ├── cds-hooks-specification.md
│   └── smart-on-fhir-app-specification.md
├── 05-data-specifications/
│   ├── data-model.md
│   ├── data-dictionary.md
│   └── fhir-resource-examples.json
├── 06-workflow-diagrams/
│   ├── clinical-workflow-current-state.html
│   ├── clinical-workflow-future-state.html
│   └── alert-notification-workflow.html
├── 07-implementation/
│   ├── implementation-roadmap.md
│   ├── testing-strategy.md
│   └── deployment-guide.md
└── 08-appendices/
    ├── glossary.md
    └── references-bibliography.md
```

## Execution Workflow

### Step 1: Parse Input Use Case

Extract from user request:
- Clinical domain (cardiology, infectious disease, oncology, etc.)
- Application type (CDS alert, risk score, order set, patient-facing app)
- Target EHR systems (Epic, Cerner, general FHIR)
- Key clinical concepts, lab values, medications, diagnoses

If ambiguous, ask clarifying questions:
- "Should this be provider-facing or patient-facing?"
- "Which EHR systems are in scope?"
- "What clinical triggers should initiate the application?"

### Step 2: Research Clinical Evidence

Use WebSearch and PubMed tools to find:
- Clinical practice guidelines (AHA, ACC, IDSA, ACS, USPSTF, etc.)
- Systematic reviews and meta-analyses
- Landmark clinical trials
- Validation studies for scoring systems

For each citation, retrieve:
- Full citation with DOI
- PubMed URL: `https://pubmed.ncbi.nlm.nih.gov/{PMID}/`
- Level of evidence (Oxford CEBM or GRADE)
- Key findings relevant to the use case

**Never fabricate citations** - use actual search results only.

### Step 3: Map Clinical Terminology

Map all clinical concepts to standard terminologies. See [references/terminology-standards.md](references/terminology-standards.md) for complete mapping guidance.

| System | Use For |
|--------|---------|
| ICD-10-CM/PCS | Diagnoses, procedures |
| SNOMED CT | Clinical findings |
| LOINC | Lab tests, observations |
| RxNorm | Medications |
| CPT/HCPCS | Billing codes |

### Step 4: Design Clinical Logic

Build evidence-based clinical algorithm:
- Document all thresholds, conditions, branches
- Cite evidence for each decision point
- Handle null/missing data gracefully
- Create validation test cases (minimum 15-20)

See [references/clinical-logic-patterns.md](references/clinical-logic-patterns.md) for templates.

### Step 5: Design Architecture

Design EHR integration architecture:
- FHIR R4 resources and US Core profiles
- CDS Hooks (patient-view, order-select, order-sign)
- SMART on FHIR launch sequences
- HL7v2 interfaces if needed

See [references/ehr-integration-patterns.md](references/ehr-integration-patterns.md) for EHR-specific guidance.

### Step 6: Generate Diagrams

Generate all diagrams using Draw.io XML format embedded in HTML. See [assets/diagram-templates/](assets/diagram-templates/) for templates.

Required diagrams:
- Decision tree / clinical algorithm flowchart
- System architecture diagram
- Integration sequence diagrams
- Clinical workflow diagrams (current/future state)

### Step 7: Generate Documentation

Generate all documents following templates in [references/document-templates.md](references/document-templates.md).

## Key Design Principles

1. **Evidence-First**: Every clinical decision must have a verifiable citation
2. **Standards-Based**: Use FHIR R4, HL7v2, CDS Hooks, SMART on FHIR, US Core v6.1
3. **EHR-Agnostic Core**: Vendor-neutral specs with EHR-specific addenda
4. **Clinician-Readable**: Logic understandable by non-technical clinicians
5. **Developer-Actionable**: Specs detailed enough to begin implementation
6. **Regulation-Aware**: Assess FDA SaMD, HIPAA, ONC requirements
7. **Real Citations Only**: Never fabricate DOIs, PMIDs, or URLs

## Regulatory Considerations

Always assess:
- **FDA SaMD Classification**: Does this meet CDS exemption under 21st Century Cures Act?
- **HIPAA Compliance**: PHI handling, minimum necessary, BAA requirements
- **ONC Certification**: Health IT certification requirements if applicable
- **State Regulations**: State-specific healthcare IT requirements

## Modular Generation

If user requests subset of documentation:
- "Just clinical logic" → Generate 02-clinical-logic/ only
- "Just Epic integration" → Generate epic-integration-guide.md only
- "Architecture only" → Generate 03-architecture/ only

For complex use cases, prioritize critical documents first and offer to generate additional sections in follow-up turns.
