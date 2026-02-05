# RANDOM - Agent Skills & Tools Workspace

This workspace contains AI agent skills, tools, and related resources.

## Directory Structure

```
RANDOM/
├── .agent/                     # 🤖 Agent Configuration
│   ├── AGENTS.md               # Agent behavior instructions
│   ├── skills/                 # 🔧 Installed/Active Skills
│   │   ├── jobs/               # Physician Informatician job search
│   │   │   ├── SKILL.md
│   │   │   ├── job-results/    # 💼 Search results & resume
│   │   │   └── references/
│   │   ├── newsmaker/          # Indic/Dharmic article writing
│   │   │   ├── SKILL.md
│   │   │   ├── articles/       # 📝 Generated articles
│   │   │   └── references/
│   │   ├── notebook-skill/     # NotebookLM research & audio
│   │   │   └── SKILL.md
│   │   └── ssd/                # Smart Stock Decider
│   │       ├── SKILL.md
│   │       └── scripts/
│   └── workflows/              # Custom workflows (optional)
│
├── skill-creator/              # 🛠️ Skill Development Tool
│   ├── scripts/                # init, package, validate scripts
│   ├── references/             # Skill creation documentation
│   ├── examples/               # Demo/example code
│   ├── SKILL_skillcreator.md
│   └── LICENSE.txt
│
├── skill-packages/             # 📦 Distributable .skill files
│   ├── jobs.skill
│   ├── newsmaker.skill
│   ├── notebook-skill.skill
│   └── SSD.skill
│
├── .env.example                # Environment variable template
├── .gitignore                  # Git ignore patterns
└── README.md                   # This file
```

## Skills Overview

| Skill | Trigger | Description |
|-------|---------|-------------|
| **jobs** | "job search", "find positions" | Search for Physician Informatician positions |
| **newsmaker** | "write article from Hindu perspective" | Write articles from Indic/Dharmic viewpoint |
| **notebook-skill** | "research topic", "audio overview" | NotebookLM research & audio generation |
| **ssd** | "SSD AAPL", "analyze stock" | Stock analysis with Buy/Hold/Sell recommendation |

## Usage

### Using Skills
Skills in `.agent/skills/` are automatically available. Trigger by keyword:
```
"Find physician informatician jobs"     → jobs skill
"Write an article on Bangladesh"        → newsmaker skill  
"Research AI in healthcare"             → notebook-skill
"SSD TSLA"                              → ssd skill
```

### Creating New Skills
```bash
python skill-creator/scripts/init_skill.py <skill-name> --path .agent/skills/
```

### Packaging Skills for Distribution
```bash
python skill-creator/scripts/package_skill.py .agent/skills/<skill-name> skill-packages/
```

## Quick Start

1. Skills are ready to use - just ask
2. Outputs go into each skill's folder (e.g., `newsmaker/articles/`)
3. Packaged `.skill` files in `skill-packages/` can be shared/installed elsewhere
