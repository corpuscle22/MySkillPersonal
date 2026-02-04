---
name: investigator
description: Conducts thorough and deep background investigations on individuals across public worldwide sources. Use this skill when asked to "investigate", "background check", or "find details about" a person. Covers social media, news, legal/police records, and public data globally.
---

# Investigator

## Overview

The Investigator skill is a comprehensive protocol for conducting deep background checks on individuals using Open Source Intelligence (OSINT) techniques. It is designed to uncover details across social media, professional history, legal records, news media, and other public datasets worldwide. The primary goal is to provide a complete profile, highlighting any concerning information.

## Workflow

Follow this step-by-step workflow to conduct a thorough investigation.

### 1. Subject Profiling & Strategy
**Goal**: Establish a baseline profile and identify search parameters.
- **Action**: Analyze the user's request.
- **Check**: Do you have the *Full Name*? *Location*? *Approximate Age*? *Profession*? *Known Associates*?
- **Decision**: 
  - If key details are missing (especially Name and Location/Context), **ask the user clarifying questions** before proceeding.
  - If sufficient details exist, formulate a search strategy (e.g., "Focus on India/UK legal records due to subject's history").

### 2. Broad Initial Sweep
**Goal**: Get a "lay of the land" and identify potential aliases or handles.
- **Tools**: `search_web`
- **Queries**:
  - `"{Full Name}"`
  - `"{Full Name}" {Location}`
  - `"{Full Name}" {Profession}`
  - `"{Full Name}" email / contact`
- **Output**: Note down any usernames, email addresses, or specific locations found. These become pivots for deeper searching.

### 3. Social Media Deep Dive
**Goal**: Map the subject's digital footprint and personal life.
- **Tools**: `search_web`, `open_browser_url` (if needed for specific profile views, but use `search_web` primarily for discovery).
- **Execution**: Search specifically within major platforms using site operators.
  - **LinkedIn**: `site:linkedin.com "{Full Name}"` (Look for employment history, education, connections).
  - **Facebook**: `site:facebook.com "{Full Name}"` (Look for family, interests, public posts).
  - **Twitter/X**: `site:twitter.com "{Full Name}"` OR `site:x.com "{Full Name}"` (Look for opinions, controversies).
  - **Instagram**: `site:instagram.com "{Full Name}"` (Visual lifestyle checks).
  - **TikTok**: `site:tiktok.com "{Full Name}"`
  - **Reddit**: `site:reddit.com "{Full Name}"` (Look for forum activity).
- **Username Pivot**: If a username (e.g., "johnny456") is found, search that username across all platforms: `"{Username}"`.

### 4. Legal, Police, & Public Records (Global)
**Goal**: Identify criminal history, lawsuits, or concerning legal issues.
- **Context**: Adjust based on the subject's location (Global scope).
- **Queries**:
  - `"{Full Name}" arrest`
  - `"{Full Name}" court record`
  - `"{Full Name}" criminal`
  - `"{Full Name}" lawsuit`
  - `"{Full Name}" verdict`
  - `"{Full Name}" fraud`
  - `"{Full Name}" bankrupt`
- **Specific Databases**:
  - **USA**: Search state-specific court portals (e.g., "Texas court records search"), federal PACER (via generic web search for cases).
  - **UK**: Companies House (for directorships/disqualifications), The Gazette (insolvency).
  - **India**: eCourts services, Indian Kanoon (`site:indiankanoon.org "{Full Name}"`).
  - **Global**: Interpol Red Notices (public list), local police "most wanted" or press releases.

### 5. News & Media Analysis
**Goal**: Find mentions in news, blogs, or independent media.
- **Queries**:
  - `"{Full Name}" news`
  - `"{Full Name}" scandal`
  - `"{Full Name}" interview`
  - `"{Full Name}" controversy`
- **Tip**: Use Google News tab if available via browser, or append "news" to search queries.

### 6. Concerning Information Check
**Goal**: Specifically target negative or high-risk info.
- **Keywords**: Combine name with: *scam, fraud, allegations, accused, harassment, misconduct, banned, suspended, fired, investigation, warning*.

### 7. Synthesis & Reporting
**Goal**: Present findings clearly to the user.
- **Format**:
  - **Executive Summary**: High-level overview.
  - **Key Findings**: Bullet points of confirmed facts.
  - **Concerning Information**: Dedicated section for any red flags (legal, reputation, safety).
  - **Digital Footprint**: List of social media profiles and websites.
  - **Unresolved Questions**: details that could not be verified.

## Tools & Resources

### Scripts
- `scripts/generate_dorks.py`: Generates a list of advanced Google Dork queries for a specific target to aid your manual searching.

### External APIs
- If the user requests API setup, advise on available services (e.g., specialized background check APIs like Checkr, PeopleDataLabs - requiring keys) but proceed with maximum available OSINT first.
