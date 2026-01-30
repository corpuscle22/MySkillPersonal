---
name: notebook-skill
description: Create a NotebookLM notebook with fast research and generate a long audio overview. Use when the user asks to "research a topic", "create a notebook", or wants an "audio overview" on any subject.
---

# NotebookLM Fast Research Skill

Create a notebook, populate it with sources via fast research, and generate a long audio overview.

## Workflow

Execute these steps in order. All tools are from the `notebooklm-mcp` MCP server.

### Step 1: Create Notebook

```
Tool: mcp_notebooklm-mcp_notebook_create
Args: title="<USER'S TOPIC>"
```

Save the returned `notebook_id` for all subsequent steps.

### Step 2: Start Fast Research

```
Tool: mcp_notebooklm-mcp_research_start
Args:
  notebook_id: <notebook_id from Step 1>
  query: "<USER'S TOPIC>"
  mode: "fast"
  source: "web"
```

Save the returned `task_id`. Fast research takes ~30 seconds and returns ~10 sources.

### Step 3: Wait for Research Completion

```
Tool: mcp_notebooklm-mcp_research_status
Args:
  notebook_id: <notebook_id>
  task_id: <task_id from Step 2>
  max_wait: 120
  poll_interval: 10
  compact: false
```

Wait until status is `"completed"`. Review the discovered sources list.

### Step 4: Import Sources (CRITICAL)

**This step is required.** Research only *discovers* sources—they must be explicitly imported.

```
Tool: mcp_notebooklm-mcp_research_import
Args:
  notebook_id: <notebook_id>
  task_id: <task_id>
```

Omitting `source_indices` imports all discovered sources. To filter, specify indices like `source_indices: [0, 1, 3, 5]`.

### Step 5: Verify Sources Were Added

```
Tool: mcp_notebooklm-mcp_notebook_get
Args:
  notebook_id: <notebook_id>
```

Confirm the `sources` array is populated. If empty, repeat Steps 2-4 with a refined query.

### Step 6: Generate Long Audio Overview

```
Tool: mcp_notebooklm-mcp_audio_overview_create
Args:
  notebook_id: <notebook_id>
  format: "deep_dive"
  length: "long"
  confirm: true
```

### Step 7: Report Completion

Provide the user with:
- Notebook URL (from Step 1)
- Number of sources imported
- Confirmation that audio generation has started

Audio generation runs in the background. User can check status anytime with `studio_status`.

## Pre-Flight: Ensure Authentication

**Before Step 1**, always attempt a headless token refresh to avoid browser login prompts:

```
Tool: mcp_notebooklm-mcp_refresh_auth
Args: (none)
```

This tool automatically:
1. Reloads cached auth tokens from disk
2. If tokens expired, attempts headless re-authentication using the saved Chrome profile
3. Returns success if authentication is valid

**Note**: NotebookLM has no public API. Authentication uses browser cookies from a dedicated Chrome profile. After the initial `notebooklm-mcp-auth` setup, the `refresh_auth` tool handles headless re-authentication automatically.

---

## Troubleshooting

### Authentication Expired
If any tool returns "Authentication expired":
1. First, call `mcp_notebooklm-mcp_refresh_auth` — this does **headless re-auth** using the saved Chrome profile (no browser popup)
2. If refresh_auth returns success, retry the failed step immediately
3. Only if refresh_auth fails, run `notebooklm-mcp-auth` in terminal for initial setup

### Empty Notebook After Research
The most common cause is **skipping Step 4 (research_import)**. Research only finds sources; import adds them to the notebook.

### Research Taking Too Long
Fast mode typically takes ~30 seconds and returns ~10 sources. If it takes longer, check your network connection or try again.
