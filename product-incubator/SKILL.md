---
name: product-incubator
description: Comprehensive guide to conceptualize, plan, and prototype a product idea. Covers design, IP assessment, manufacturing, business structure, and licensing.
---

# Product Incubator Skill

This skill transforms a raw product idea into a detailed execution plan. It covers design, intellectual property checks, technical planning, business setup, and manufacturing strategies.

## Quick Start

To generate a complete product plan automatically, run:

```bash
python .agent/skills/product-incubator/scripts/generate_plan.py "Product Name" "Description of product"
```

This will generate:
- **Workflow Diagrams** (`.drawio` files) in `outputs/diagrams/`
- **Schematic Images** (`.png` files) in `outputs/images/`
- **Final Word Document** (`.docx` file) in `outputs/documents/`

---

## Output Folder Structure

Each product gets its own subfolder under `outputs/`:

```
product-incubator/
├── SKILL.md
├── scripts/
│   ├── generate_plan.py      # Main generator (runs all)
│   ├── generate_diagram.py   # Standalone diagram generator
│   ├── generate_schematics.py # PIL-based image generator
│   └── generate_docx.py      # Word document generator
└── outputs/
    ├── vertebra_focus_pad/   # Each product gets its own folder
    │   ├── vertebra_focus_pad_workflow.drawio
    │   ├── vertebra_focus_pad_system.drawio
    │   ├── vertebra_focus_pad_concept.png
    │   ├── vertebra_focus_pad_system.png
    │   └── vertebra_focus_pad_plan.docx
    ├── smart_water_bottle/
    │   ├── smart_water_bottle_workflow.drawio
    │   └── ...
    └── [other_products]/
```

---

## Tool Dependencies

### 1. Drawpyo (diagrams.net Style Diagrams)
Use `drawpyo` to create clean, professional workflow diagrams in `.drawio` format.

**Install:**
```bash
pip install drawpyo
```

**The `.drawio` files can be opened/edited in [diagrams.net](https://app.diagrams.net).**

### 2. NanoBanana (AI Image Generation)
NanoBanana is Google's AI-powered image generation platform. Use it for photorealistic product concept art.

**Usage via built-in tool:**
```python
generate_image(Prompt="Photorealistic product concept...", ImageName="product_concept")
```

**Fallback:** If AI image generation is unavailable, use the PIL-based `generate_schematics.py` script.

### 3. python-docx (Word Document Generation)
Used to create the final `.docx` output.

**Install:**
```bash
pip install python-docx pillow
```

### 4. Canva Connect API (Optional)
For polished marketing-ready visuals if the user needs professional branding.
- Register at [Canva Developer Portal](https://www.canva.com/developers/).

---

## Workflow

When the user provides a product idea, Claude should:

### Step 1: Gather Information
Ask clarifying questions if needed:
- What problem does this product solve?
- Who is the target audience?
- Any specific features or constraints?

### Step 2: Execute the Generator Script
Run the `generate_plan.py` script automatically:

```python
run_command(
    CommandLine='python .agent/skills/product-incubator/scripts/generate_plan.py "Product Name" "Description"',
    Cwd='c:\\Users\\drpra\\OneDrive\\Documents\\antigravity\\RANDOM',
    SafeToAutoRun=True
)
```

### Step 3: Enhance with Research
Use `search_web` for:
- **Patent Search**: `site:patents.google.com [key features]`
- **Regulatory Info**: `FDA regulation [product type]`
- **Manufacturing Costs**: `cost to manufacture [product type]`

### Step 4: Present the Plan
After generation, present a summary and point the user to the output files:
- `.drawio` files for editable diagrams
- `.docx` file for the complete plan

---

## Phase-by-Phase Workflow

### Phase 1: Conceptualization & Design
1.  **Refine the Idea**: Clarify the core problem and target audience.
2.  **Define Features**: MVP features vs. future roadmap.
3.  **Visual Concept Art**: Generate via NanoBanana or PIL fallback.

### Phase 2: Intellectual Property (IP) Check
1.  **Patent Search**: Query Google Patents and USPTO.
2.  **Assessment**: Identify prior art and novelty.
3.  *Disclaimer*: This is preliminary, not legal advice.

### Phase 3: Technical Planning & Workflow Diagrams
1.  **Diagrams**: Auto-generated via `drawpyo` → `.drawio` files.
2.  **BOM / Tech Stack**: List components and estimated costs.

### Phase 4: Prototyping Strategy
1.  **Fabrication Methods**: 3D Printing, PCB design, etc.
2.  **Estimated Prototype Costs**: Realistic range for one unit.

### Phase 5: Manufacturing & Supply Chain
1.  **Sourcing**: Digi-Key, Mouser (prototypes), Alibaba (bulk).
2.  **Manufacturing Partners**: PCBWay, JLCPCB, Shapeways, etc.
3.  **COGS Estimate**: Unit cost at scale (e.g., 1,000 units).

### Phase 6: Business & Legal Considerations
1.  **Business Entity**: LLC vs. C-Corp.
2.  **Registration**: Secretary of State, EIN.
3.  **Certifications**: FCC, CE, UL, FDA (if applicable).

---

## Output Format

The final output includes:
1.  **Word Document** (`.docx`) with all phases, images, and diagrams embedded.
2.  **Editable Diagrams** (`.drawio`) for user customization.
3.  **Image Assets** (`.png`) for use in presentations.

All files are saved to `outputs/` subfolders for easy access.
