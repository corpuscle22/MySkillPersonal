---
name: business-travel
description: Finds cheapest business/first class flight fares from Dallas (DFW) to any user-specified destination within the next 6 months. Searches travel portals and agencies.
---

# Business Travel Skill

## Overview
This skill is designed to find the best (cheapest) business class or domestic first class flight fares from Dallas (DFW) to any destination provided by the user. It searches across multiple travel portals and agencies for flights departing within the next 6 months.

## When to Use
Use this skill when:
- The user asks for business class or first class flight deals from Dallas/DFW.
- The user wants to find the "cheapest" premium cabin fares to a specific destination.
- The user mentions "business-travel" or asks to "search all portals" for flights.

## Configuration (API Setup)

To use real-time API data (Recommended), you must obtain API keys for one or both of the following services. This is **more reliable** than the browser-based method.

### Option 1: SerpApi (Google Flights) - *Recommended*
1.  Go to [SerpApi](https://serpapi.com/) and sign up.
2.  Get your `API Key`.
3.  Set the environment variable: `SERPAPI_KEY`

### Option 2: Amadeus (Self-Service)
1.  Go to [Amadeus for Developers](https://developers.amadeus.com/) and sign up.
2.  Create a new app to get your `API Key` and `API Secret`.
3.  Set the environment variables: `AMADEUS_API_KEY` and `AMADEUS_API_SECRET`

## Workflow

### 1. Gather Requirements
- **Origin**: Dallas (DFW) [Implicit]
- **Destination**: [User Provided] - If missing, ASK immediately.
- **Date Range**: Next 6 months.
- **Class**: Business (International) / First (Domestic).

### 2. Execution Method
**Check for API Keys first.**
- If `SERPAPI_KEY` or `AMADEUS_API_KEY` are present, use the `scripts/flight_search_api.py` script.
- If NO keys are present, fall back to the `browser_subagent` method (described below).

### 3. API Method (Primary)
Run the python script `scripts/flight_search_api.py`.
**Arguments:**
- `--destination`: IATA code or City name (e.g., 'COK' or 'Cochin')
- `--date`: Date in YYYY-MM-DD format (pick a date ~1 month out if flexible).
- `--cabin`: 'business' or 'first'

The script will automatically use whichever API is configured and return the top results.

### 4. Browser Method (Fallback)
*Only use if API keys are missing.*
Use the `browser_subagent` to search Google Flights, Skyscanner, Kayak, etc.
- **Search**: Round trip from DFW to [Destination].
- **Cabin**: Business/First.
- **Extract**: Top 3 Cheapest options with Price, Airline, and Link.

## presenting Results
Present findings in a clear table:

| Price | Airline | Date | Stops | Source |
|-------|---------|------|-------|--------|
| ...   | ...     | ...  | ...   | ...    |
