import os

base_dir = r"c:\Users\drpra\OneDrive\Documents\antigravity\RANDOM\.agent\skills\ehr-clinical-app-doc-generator\output\ckd"

def write_file(path, content):
    full_path = os.path.join(base_dir, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created {path}")

# Helper to escape XML special characters
def escape_xml(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

# Helper to generate simple Draw.io XML
def generate_drawio_xml(title, nodes, edges):
    xml_header = f"""<mxfile host="app.diagrams.net" modified="2024-05-22T00:00:00.000Z" agent="Agent" version="21.0.0" type="device">
  <diagram name="{title}" id="diagram_1">
    <mxGraphModel dx="0" dy="0" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />"""
    
    xml_body = ""
    
    # Generate nodes
    # nodes is a list of dicts: {'id': 'id', 'label': 'text', 'x': 0, 'y': 0, 'type': 'process'|'decision'|'terminator'|'component'}
    for node in nodes:
        style = ""
        if node['type'] == 'decision':
            style = "rhombus;whiteSpace=wrap;html=1;"
            width, height = 120, 80
        elif node['type'] == 'terminator':
            style = "rounded=1;whiteSpace=wrap;html=1;arcSize=50;fillColor=#f8cecc;strokeColor=#b85450;"
            width, height = 120, 40
        elif node['type'] == 'component':
            style = "shape=module;jettyWidth=8;jettyHeight=4;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;"
            width, height = 140, 60
        elif node['type'] == 'db':
            style = "shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#e1d5e7;strokeColor=#9673a6;"
            width, height = 60, 80
        else: # process
            style = "rounded=0;whiteSpace=wrap;html=1;"
            width, height = 120, 60
            
        escaped_label = escape_xml(node['label'])
        xml_body += f"""
        <mxCell id="{node['id']}" value="{escaped_label}" style="{style}" vertex="1" parent="1">
          <mxGeometry x="{node['x']}" y="{node['y']}" width="{width}" height="{height}" as="geometry" />
        </mxCell>"""

    # Generate edges
    # edges is a list of dicts: {'source': 'id', 'target': 'id', 'label': 'text'}
    edge_id_counter = 100
    for edge in edges:
        edge_id = f"edge_{edge_id_counter}"
        edge_id_counter += 1
        label = escape_xml(edge.get('label', ''))
        style = "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;"
        
        xml_body += f"""
        <mxCell id="{edge_id}" value="{label}" style="{style}" edge="1" parent="1" source="{edge['source']}" target="{edge['target']}">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>"""

    xml_footer = """
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>"""
    
    return xml_header + xml_body + xml_footer

import json

# Generate HTML file that embeds the Draw.io XML
def generate_drawio_html(title, xml_content):
    # Create the config object
    config = {
        "highlight": "#0000ff",
        "nav": True,
        "resize": True,
        "toolbar": "zoom layers tags lightbox",
        "edit": "_blank",
        "xml": xml_content
    }
    
    # Serialize to JSON
    json_data = json.dumps(config)
    
    # Escape for HTML attribute (replace " with &quot;)
    attribute_value = json_data.replace('"', '&quot;')
    
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    <meta charset="utf-8">
</head>
<body>
    <h1>{title}</h1>
    <div class="mxgraph" style="max-width:100%;border:1px solid transparent;" data-mxgraph="{attribute_value}"></div>
    <script type="text/javascript" src="https://viewer.diagrams.net/js/viewer-static.min.js"></script>
</body>
</html>"""
    return html_content

# --- 1. Decision Tree (Clinical Logic) ---
dt_nodes = [
    {'id': 'A', 'label': 'Start: Patient Chart Open', 'x': 340, 'y': 20, 'type': 'process'},
    {'id': 'B', 'label': 'Existing CKD?', 'x': 340, 'y': 120, 'type': 'decision'},
    {'id': 'C', 'label': 'Stop: Already Diagnosed', 'x': 540, 'y': 140, 'type': 'terminator'},
    {'id': 'D', 'label': 'Current eGFR exists?', 'x': 340, 'y': 240, 'type': 'decision'},
    {'id': 'E', 'label': 'Stop: Insufficient Data', 'x': 540, 'y': 260, 'type': 'terminator'},
    {'id': 'F', 'label': 'Current eGFR < 60?', 'x': 340, 'y': 360, 'type': 'decision'},
    {'id': 'G', 'label': 'History < 60 >90d ago?', 'x': 140, 'y': 480, 'type': 'decision'},
    {'id': 'M', 'label': 'Stop: Not Chronic', 'x': 10, 'y': 480, 'type': 'terminator'},
    {'id': 'H', 'label': 'Check eGFR Value', 'x': 140, 'y': 620, 'type': 'process'},
    {'id': 'I', 'label': 'Suggest Stage 3a', 'x': 20, 'y': 740, 'type': 'terminator'},
    {'id': 'J', 'label': 'Suggest Stage 3b', 'x': 160, 'y': 740, 'type': 'terminator'},
    {'id': 'K', 'label': 'Suggest Stage 4', 'x': 300, 'y': 740, 'type': 'terminator'},
    {'id': 'L', 'label': 'Suggest Stage 5', 'x': 440, 'y': 740, 'type': 'terminator'},
    {'id': 'N', 'label': 'Current UACR > 30?', 'x': 500, 'y': 480, 'type': 'decision'},
    {'id': 'O', 'label': 'History > 30 >90d ago?', 'x': 500, 'y': 600, 'type': 'decision'},
    {'id': 'P', 'label': 'Check eGFR Value', 'x': 500, 'y': 720, 'type': 'process'},
    {'id': 'Q', 'label': 'Suggest Stage 1', 'x': 400, 'y': 840, 'type': 'terminator'},
    {'id': 'R', 'label': 'Suggest Stage 2', 'x': 600, 'y': 840, 'type': 'terminator'}
]

dt_edges = [
    {'source': 'A', 'target': 'B', 'label': ''},
    {'source': 'B', 'target': 'C', 'label': 'Yes'},
    {'source': 'B', 'target': 'D', 'label': 'No'},
    {'source': 'D', 'target': 'E', 'label': 'No'},
    {'source': 'D', 'target': 'F', 'label': 'Yes'},
    {'source': 'F', 'target': 'G', 'label': 'Yes'},
    {'source': 'F', 'target': 'N', 'label': 'No'},
    {'source': 'G', 'target': 'M', 'label': 'No'},
    {'source': 'G', 'target': 'H', 'label': 'Yes'},
    {'source': 'H', 'target': 'I', 'label': '45-59'},
    {'source': 'H', 'target': 'J', 'label': '30-44'},
    {'source': 'H', 'target': 'K', 'label': '15-29'},
    {'source': 'H', 'target': 'L', 'label': '<15'},
    {'source': 'N', 'target': 'M', 'label': 'No'},
    {'source': 'N', 'target': 'O', 'label': 'Yes'},
    {'source': 'O', 'target': 'M', 'label': 'No'},
    {'source': 'O', 'target': 'P', 'label': 'Yes'},
    {'source': 'P', 'target': 'Q', 'label': '>=90'},
    {'source': 'P', 'target': 'R', 'label': '60-89'},
    {'source': 'P', 'target': 'H', 'label': '<60'}
]

dt_xml = generate_drawio_xml("CKD Decision Tree", dt_nodes, dt_edges)
write_file("02-clinical-logic/decision-tree-chart.drawio", dt_xml)
write_file("02-clinical-logic/decision-tree-chart.html", generate_drawio_html("CKD Decision Tree", dt_xml))


# --- 2. System Architecture Diagram ---
arch_nodes = [
    {'id': 'EHR', 'label': 'EHR System (Epic/Cerner)', 'x': 50, 'y': 150, 'type': 'component'},
    {'id': 'Client', 'label': 'EHR Client (Hyperspace)', 'x': 50, 'y': 50, 'type': 'component'},
    {'id': 'Middleware', 'label': 'CDS Service (Python)', 'x': 300, 'y': 100, 'type': 'component'},
    {'id': 'DB', 'label': 'EHR Database (FHIR)', 'x': 50, 'y': 250, 'type': 'db'},
    {'id': 'ExtAuth', 'label': 'Auth Server (OIDC)', 'x': 300, 'y': 250, 'type': 'component'}
]

arch_edges = [
    {'source': 'Client', 'target': 'Middleware', 'label': 'CDS Hook (JSON)'},
    {'source': 'Middleware', 'target': 'Client', 'label': 'Card (Suggestion)'},
    {'source': 'Middleware', 'target': 'DB', 'label': 'FHIR Read/Write'},
    {'source': 'Middleware', 'target': 'ExtAuth', 'label': 'Verify Token'},
    {'source': 'Client', 'target': 'EHR', 'label': 'Native API'}
]

arch_xml = generate_drawio_xml("System Architecture", arch_nodes, arch_edges)
write_file("03-architecture/system-architecture-diagram.drawio", arch_xml)
write_file("03-architecture/system-architecture-diagram.html", generate_drawio_html("System Architecture", arch_xml))


# --- 3. Exec Summary & Docs ---
# 00-executive-summary.md
write_file("00-executive-summary.md", """# Executive Summary: Undiagnosed CKD Identifier & Stager

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
""")

# 01-clinical-requirements/clinical-use-case-specification.md
write_file("01-clinical-requirements/clinical-use-case-specification.md", """# Clinical Use Case: Undiagnosed CKD Identification

## Narrative
Dr. Smith is seeing Mr. Jones (58M) for a diabetes follow-up. Mr. Jones has had an eGFR of 52 and 55 on his last two metabolic panels (6 months apart), but "Chromic Kidney Disease" is missing from his Problem List.
As Dr. Smith opens the chart, the CKD Identifier app runs in the background. It recognizes the persistent eGFR < 60 and absence of diagnosis.
A non-intrusive alert appears: *"Clinical evidence suggests CKD Stage 3a. Click to add 'Chronic kidney disease, stage 3a (ICD-10 N18.31)' to Problem List."*
Dr. Smith reviews the trend line presented in the alert, agrees, and clicks "Add". The Problem List is updated, and an automatic order set for "CKD Stage 3 Management" (ACEi/ARB, Urine Microalbumin) is suggested.

## Triggers
- **Event**: Chart Open (Patient View) OR Result Verification (New Lab Result).
- **Condition**: 
  1. No existing active problem on Problem List matching ValueSet "Chronic Kidney Disease".
  2. Last eGFR < 60 mL/min/1.73m².
  3. Historical eGFR < 60 mL/min/1.73m² recorded > 90 days prior.
  4. OR: Persistent Albuminuria (UACR > 30 mg/g) > 90 days.

## Exclusion Criteria
- Patients with regular dialysis or kidney transplant (ESRD status).
- Acute Kidney Injury (AKI) diagnosis in active encounter (relative exclusion, context dependent).
- Patients < 18 years old (Pediatric logic differs).
""")

# 02-clinical-logic/interpretation-logic-specification.md
write_file("02-clinical-logic/interpretation-logic-specification.md", """# Interpretation Logic Specification: CKD Staging

## Data Inputs
- **Current_eGFR**: Latest valid eGFR result.
- **Previous_eGFR**: Most recent eGFR result recorded > 90 days prior to Current_eGFR.
- **Current_UACR**: Latest Urine Albumin-Creatinine Ratio.
- **Previous_UACR**: Most recent UACR recorded > 90 days prior.
- **Existing_Problems**: List of active conditions on Problem List.

## Algorithm

### Step 1: Exclusion Check
IF (`Existing_Problems` contains ANY code from ValueSet "CKD_All_Stages"):
    THEN EXIT (Patient already diagnosed).

### Step 2: eGFR Evaluation (G-Stage)
IF (`Current_eGFR` is Valid AND `Previous_eGFR` is Valid):
    IF (`Current_eGFR` < 60 AND `Previous_eGFR` < 60):
        # Confirmed low GFR > 3 months
        DETERMINE `Suggested_Stage` based on `Current_eGFR`:
            - score >= 90: Stage 1 (Requires Albuminuria)
            - 60-89: Stage 2 (Requires Albuminuria)
            - 45-59: **Stage 3a**
            - 30-44: **Stage 3b**
            - 15-29: **Stage 4**
            - < 15: **Stage 5**
        GO TO Step 4.
    ELSE:
        PROCEED to Step 3 (Check Albuminuria alone).

### Step 3: Albuminuria Evaluation (A-Stage)
IF (`Current_UACR` > 30 mg/g AND `Previous_UACR` > 30 mg/g):
    IF (`Current_eGFR` >= 90):
        SET `Suggested_Stage` = **Stage 1**
    ELSE IF (`Current_eGFR` between 60-89):
        SET `Suggested_Stage` = **Stage 2**
    GO TO Step 4.

### Step 4: Logic Output
IF `Suggested_Stage` IS SET:
    RETURN Object:
        - `Alert_Type`: "Undiagnosed CKD"
        - `Suggested_Concept`: SNOMED code for `Suggested_Stage`
        - `Rationale`: "Two eGFR values < 60 separated by > 90 days: [Date1: Val1], [Date2: Val2]"
ELSE:
    EXIT (No criteria met).
""")

# 03-architecture/system-architecture-overview.md
write_file("03-architecture/system-architecture-overview.md", """# System Architecture Overview

## Components
1. **EHR Interface (Client)**:
   - Epic Hyperspace (embedded web view or native alert).
   - Cerner PowerChart (MPages).
   - SMART on FHIR App (React.js frontend).
2. **CDS Service (Middleware)**:
   - Python (FastAPI) or Node.js (NestJS).
   - Implements CDS Hooks specification (`cds-services` endpoint).
   - Handles logic execution (KDIGO rules engine).
3. **FHIR Server / Facade**:
   - Connection to EHR database via FHIR R4.
   - Read: `Observation` (Labs), `Condition` (Problem List).
   - Write: `Condition` (via `Order` or direct POST if permitted).

## Technology Stack
- **Frontend**: React, SMART Client JS Library.
- **Backend API**: Python FastAPI.
- **Data Standard**: HL7 FHIR R4.

## Integration Pattern (CDS Hooks)
1. **Trigger**: Clinician opens patient chart (`patient-view` hook).
2. **Request**: EHR sends context.
3. **Analyze**: CDS Service executes logic.
4. **Response**: CDS Service returns a "Card".
""")

print("Documentation generated successfully (Draw.io Enabled, No Mermaid).")
