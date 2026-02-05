# Agent Instructions

> This file configures AI agent behavior for this workspace.

You operate in a **skills-based architecture** where reusable capabilities are packaged into modular skills.

## Skills Architecture

**What are Skills?**
Skills are self-contained packages in `.agent/skills/` that extend your capabilities with:
- Specialized workflows and procedures
- Domain-specific knowledge
- Bundled scripts, references, and assets

**How Skills Work:**
1. Each skill has a `SKILL.md` with instructions
2. Skills trigger based on user requests matching their description
3. When triggered, follow the skill's workflow exactly
4. Output files stay within the skill's folder

## Available Skills

| Skill | Trigger Phrases | Purpose |
|-------|-----------------|---------|
| **business-travel** | "business class flights", "flight search" | Find cheapest business/first class fares from DFW |
| **deal-finder** | "find deals", "compare prices" | Best online deals and promo codes |
| **jobs** | "job search", "find positions" | Physician Informatician job search |
| **newsmaker** | "write article", "Hindu perspective" | Indic/Dharmic article writing |
| **notebook-skill** | "research topic", "audio overview" | NotebookLM research & audio |
| **public** | "public salary", "employee compensation" | Search public employee salaries nationwide |
| **pubmed** | "medical research", "clinical question" | Evidence-based PubMed research |
| **ssd** | "SSD [TICKER]", "analyze stock" | Stock analysis & recommendations |

## Operating Principles

**1. Check for skills first**
Before doing work, check if a skill exists in `.agent/skills/`. Use the skill's workflow.

**2. Self-correct when things break**
- Read error messages carefully
- Fix issues and test again
- Update skill references if you learn something new

**3. Keep outputs organized**
Each skill has its own output folder:
- `jobs/job-results/` - Job search outputs
- `newsmaker/articles/` - Generated articles

**4. Use skill-creator for new skills**
To create new skills, use `skill-creator/scripts/init_skill.py`

## File Organization

```
.agent/
├── AGENTS.md           # This file (agent configuration)
├── skills/             # Active skills
│   ├── business-travel/
│   ├── deal-finder/
│   ├── jobs/
│   ├── newsmaker/
│   ├── notebook-skill/
│   ├── public/
│   ├── pubmed/
│   └── ssd/
└── workflows/          # Custom workflows (if any)
```

## Summary

Read skill instructions, follow workflows, keep outputs organized within skills.
Be reliable. Self-correct. Use the right skill for the job.
