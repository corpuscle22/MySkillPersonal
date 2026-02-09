---
name: ehr-clinical-app-doc-generator
description: Generates comprehensive, production-ready documentation packages for building healthcare applications that integrate with EHR systems such as Epic, Cerner (Oracle Health), Allscripts, Meditech, and athenahealth. Capabilities include creating clinical use case specs, evidence-based logic, user-friendly decision trees (Draw.io), system architecture diagrams (Draw.io), FHIR/HL7 integration guides, data models, and implementation roadmaps. Use when users need end-to-end documentation for clinical decision support tools, EHR apps, or healthcare interoperability projects.
---

# EHR Clinical App Documentation Generator

## 1. What This Skill Should Enable Claude to Do

Given **any clinical use case** as input (e.g., "clinical decision support for sepsis screening," "automated prior authorization for medications," "patient risk stratification for readmission," "lab result interpretation and alerting"), this skill should generate a **complete documentation package** that enables software engineering teams, solution architects, and clinical informaticists to design, build, validate, and deploy an EHR-integrated healthcare application.

The output documentation package must be comprehensive enough that:
- A software engineering team can begin development without ambiguity
- A clinical team can validate the clinical logic and evidence base
- A solution architect can design the integration architecture
- A compliance/regulatory team can assess risk and conformance
- A project manager can plan the implementation timeline

## 2. When This Skill Should Trigger

This skill should trigger whenever the user:
- Asks to generate documentation for a healthcare/clinical application
- Requests architecture or design documents for EHR integration
- Mentions building a clinical decision support (CDS) tool
- Asks for workflow documentation for EPIC, Cerner, or any EHR-integrated app
- Requests FHIR/HL7 integration specifications
- Asks for clinical logic documentation with evidence citations
- Wants decision tree or workflow diagrams for a medical use case
- Mentions CDS Hooks, SMART on FHIR, HL7v2, or EHR interoperability
- Says things like "document this clinical workflow," "create specs for an EHR app," "generate architecture for a health IT system," or "build me a clinical app design doc"
- Asks for interpretation logic, clinical algorithms, or evidence-based guideline implementation specs
- Requests any healthcare application planning, design, or specification documentation

## 3. Expected Output Format

The skill should produce a **multi-file documentation package** organized as follows. All documents should be generated as real files (`.md`, `.html`, `.json`, `.drawio`) that can be downloaded. **NO MERMAID FILES.**

### Output Directory Structure

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
│   ├── decision-tree-chart.drawio          # Editable Draw.io diagram
│   ├── decision-tree-chart.html            # Viewable HTML version
│   ├── clinical-algorithm-flowchart.drawio # Editable Draw.io diagram
│   ├── clinical-algorithm-flowchart.html   # Viewable HTML version
│   ├── edge-cases-and-exceptions.md
│   └── clinical-validation-test-cases.md
├── 03-architecture/
│   ├── system-architecture-overview.md
│   ├── system-architecture-diagram.drawio  # Editable Draw.io diagram
│   ├── system-architecture-diagram.html    # Viewable HTML version
│   ├── ehr-integration-architecture.md
│   ├── integration-sequence-diagrams.drawio # Editable Draw.io diagram
│   ├── integration-sequence-diagrams.html   # Viewable HTML version
│   ├── data-flow-diagram.drawio            # Editable Draw.io diagram
│   ├── data-flow-diagram.html              # Viewable HTML version
│   ├── api-specifications.md
│   └── security-architecture.md
├── 04-ehr-integration/
│   ├── epic-integration-guide.md
│   ├── cerner-integration-guide.md
│   ├── general-ehr-integration-guide.md
│   ├── fhir-resource-mapping.md
│   ├── hl7-interface-specification.md
│   ├── cds-hooks-specification.md
│   ├── smart-on-fhir-app-specification.md
│   └── ehr-workflow-integration-points.md
├── 05-data-specifications/
│   ├── data-model.md
│   ├── data-dictionary.md
│   ├── fhir-resource-examples.json
│   ├── terminology-valueset-definitions.md
│   └── data-validation-rules.md
├── 06-workflow-diagrams/
│   ├── clinical-workflow-current-state.drawio
│   ├── clinical-workflow-current-state.html
│   ├── clinical-workflow-future-state.drawio
│   ├── clinical-workflow-future-state.html
│   ├── user-interaction-workflow.drawio
│   ├── user-interaction-workflow.html
│   ├── alert-notification-workflow.drawio
│   └── alert-notification-workflow.html
├── 07-implementation/
│   ├── implementation-roadmap.md
│   ├── technical-requirements.md
│   ├── testing-strategy.md
│   ├── deployment-guide.md
│   └── go-live-checklist.md
└── 08-appendices/
    ├── glossary.md
    ├── references-bibliography.md
    ├── change-log-template.md
    └── stakeholder-sign-off-template.md
```

## 4. Detailed Requirements for Each Document Section

### 4.1 Executive Summary (`00-executive-summary.md`)

Generate a 2-3 page executive summary.

### 4.2 Clinical Requirements (`01-clinical-requirements/`)
- Clinical use case spec, evidence citations, terminology mapping, regulatory checklist.

### 4.3 Clinical Logic (`02-clinical-logic/`)

#### `interpretation-logic-specification.md`
- Complete algorithm logic, thresholds, branches.

#### `decision-tree-chart.drawio` & `.html`
- **Draw.io Format Only**.
- Complete decision tree in editable Draw.io XML format.
- Every branch labeled with conditions and thresholds.
- Terminal nodes showing actions/classifications/risk levels.

#### `clinical-algorithm-flowchart.drawio` & `.html`
- **Draw.io Format Only**.
- Flowchart showing the step-by-step execution logic.

### 4.4 Architecture (`03-architecture/`)

#### `system-architecture-overview.md`
- High-level architecture, components, tech stack.

#### Technical Diagrams (Draw.io)
- **ALL diagrams must be in Draw.io format.**
- `system-architecture-diagram.drawio`
- `integration-sequence-diagrams.drawio`
- `data-flow-diagram.drawio`

#### `ehr-integration-architecture.md`
- Integration patterns for Epic, Cerner, General.

### 4.5 EHR Integration (`04-ehr-integration/`)
- Integration guides, FHIR mapping, CDS Hooks specs, SMART on FHIR specs.

### 4.6 Data Specifications (`05-data-specifications/`)
- Data model, dictionary, FHIR examples.

### 4.7 Workflow Diagrams (`06-workflow-diagrams/`)
- **ALL diagrams must be in Draw.io format.**
- `clinical-workflow-current-state.drawio`
- `clinical-workflow-future-state.drawio`
- `user-interaction-workflow.drawio`
- `alert-notification-workflow.drawio`

### 4.8 Implementation (`07-implementation/`)
- Roadmap, technical requirements, testing, deployment.

### 4.9 Appendices (`08-appendices/`)
- Glossary, bibliography, templates.

## 5. Diagram Generation Requirements

**ALL DIAGRAMS MUST BE GENERATED IN DRAW.IO FORMAT.**
**DO NOT USE MERMAID.**

**Target Files**: All decision trees, flowcharts, architecture diagrams, sequence diagrams, and workflow diagrams.

**Format**: 
1. **.drawio**: Valid XML format compatible with diagrams.net.
2. **.html**: A self-contained HTML file that embeds the XML and renders it using the Draw.io viewer library.

**HTML Pattern for Draw.io**:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Diagram</title>
    <meta charset="utf-8">
</head>
<body>
    <div class="mxgraph" style="max-width:100%;border:1px solid transparent;" data-mxgraph="{&quot;highlight&quot;:&quot;#0000ff&quot;,&quot;nav&quot;:true,&quot;resize&quot;:true,&quot;toolbar&quot;:&quot;zoom layers tags lightbox&quot;,&quot;edit&quot;:&quot;_blank&quot;,&quot;xml&quot;:&quot;[ESCAPED_XML_HERE]&quot;}"></div>
    <script type="text/javascript" src="https://viewer.diagrams.net/js/viewer-static.min.js"></script>
</body>
</html>
```

## 6. Evidence Citation Requirements

The skill MUST use PubMed tools to search for and verify clinical evidence.
1. **Search PubMed** using `search_articles`.
2. **Retrieve metadata** using `get_article_metadata`.
3. **Check for full text** using `get_full_text_article`.
4. **Cite real, verifiable references**.

## 7. Process the Skill Should Follow

1. **Parse the Input Use Case**: Extract domain, app type, EHRs, concepts.
2. **Research Clinical Evidence**: Search PubMed/web for guidelines/algorithms.
3. **Map Clinical Terminology**: Map concepts to standard codes.
4. **Design Clinical Logic**: Build decision tree, define thresholds.
5. **Design Architecture**: System/Integration architecture.
6. **Generate EHR-Specific Integration Guides**: Epic, Cerner, General.
7. **Generate Diagrams**: **Draw.io for EVERYTHING**.
8. **Generate Implementation Documentation**: Roadmap, testing, etc.
9. **Package and Present**: Organize files, generate TOC.

## 8. Key Design Principles

1. **Evidence-First**: Every decision point backed by citation.
2. **Standards-Based**: FHIR R4, HL7v2, CDS Hooks, SMART on FHIR.
3. **EHR-Agnostic with EHR-Specific Addenda**.
4. **Clinician-Readable**: All diagrams in user-friendly Draw.io format.
5. **No Mermaid**: Mermaid is forbidden.
6. **Regulation-Aware**: FDA SaMD, HIPAA.
7. **Terminology-Rich**: Map to ICD-10, SNOMED, LOINC, RxNorm.
8. **Real Citations Only**.
