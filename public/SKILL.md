---
name: public
description: Nationwide search for public employee salaries and total compensation. Identifies employer, position, and most recent compensation from public databases using deep web searches, API endpoints, or bulk data downloads.
---

# Public Salaries & Compensation Finder

Identify the employer, position, and total compensation for a given name or specific position using public records and reliable databases.

## Workflow

### Phase 1: Identity & Entity Resolution
**Goal:** Determine *where* the person works.
*   **Search:** `[Name] current position linkedin`, `[Name] official biography`, `[Name] state employee directory`.
*   **Verify:** Is it a Government Entity, Public University, or Non-Profit (501c3)?

### Phase 2: Surface Search & Error Recovery
**Goal:** Find an indexed exact match.
1.  **Direct Search:** `govsalaries.com [Name]`, `openpayrolls.com [Name]`, `[State] transparency portal`.
2.  **Browser Subagent:** Navigate to the official transparency portal (e.g., `transparent.utah.gov`).
    *   **CRITICAL ERROR HANDLING:** If the browser fails to launch (e.g., `$HOME` error or environment issues), **DO NOT GIVE UP**.
    *   **Pivot Strategy:** Immediately switch to **Phase 3 (Data Acquisition)**.

### Phase 3: Data Acquisition (APIs & Bulk Download)
**Goal:** If the browser fails, get the data via API or Bulk Download using `run_command` (Curl/Wget).

#### Strategy A: Check for APIs
1.  **Scan for Open Data:**
    *   Search: `[State/Org] open data api csv`, `[State] socrata api employee pay`.
    *   Common Platforms: Socrata (`opendata.[state].gov`), CKAN.
2.  **API Setup (User Interactive):**
    *   If a restricted API (like BigQuery) is found, **ASK THE USER**: *"I found an official API for [Organization]. Shall I set this up?"*
    *   If an *Open* API is found (e.g., Socrata), **USE IT** immediately.
    *   *Example Socrata Query:* `curl "https://data.state.gov/resource/id.json?name=[Name]"`

#### Strategy B: The "Download & Grep" (The Ultimate Fallback)
If individual search is blocked/broken, download the full dataset for the specific entity and search locally.
1.  **Find the Download URL:**
    *   Search: `[Organization] salary transparency download`, `[State] compensation export`.
    *   Target: `transparent.utah.gov` -> "Compensation Downloader".
2.  **Execute Download (via standard terminal):**
    *   Use `curl` or `Select-String` (Grep) to find the name in the remote file if possible, or download to `c:\Users\drpra\OneDrive\Documents\antigravity\RANDOM\temp\` and inspect.
    *   *Command:* `Invoke-WebRequest -Uri "[URL]" -OutFile "salaries.csv"`
3.  **Search Local File:**
    *   *Command:* `Select-String -Path "salaries.csv" -Pattern "[Name]"`

### Phase 4: Fallback (Soft Estimates)
**Only** if Phases 2 & 3 fail completely.
1.  **Pay Scales:** `[Organization] salary schedule [Year]`.
2.  **H1B Data:** `h1bdata.info [Employer] [Name]`.

## Output Format

```markdown
## Salary Report: [Name or Position]

### 🏛️ Employment Details
- **Individual:** [Name]
- **Position:** [Official Title]
- **Organization:** [Employer]
- **Location:** [City, State]

### 💰 Compensation
- **Total Compensation:** $[Amount]
- **Base Salary:** $[Amount]
- **Fiscal Year:** [Year]
- **Source:** [Exact Link or "Bulk Dataset Download"]

### ℹ️ Methodology
- **Search Method:** [e.g., "Manual Browser", "Socrata API", "Bulk CSV Download"]
- **Notes:** [Details on API usage or strictness of the match]
```

## Rules
1.  **Persistence:** If one tool breaks (Browser), use another (Terminal/Curl).
2.  **Precision:** Prioritize exact cents over round numbers.
3.  **Environment Awareness:** If `$HOME` or environment errors occur, explain them briefly to the user but *bypass* them using standard shell commands.
