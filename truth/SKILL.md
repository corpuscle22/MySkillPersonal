---
name: truth
description: Perform deep, evidence-based investigations of any news item, claim, or event to surface the most defensible account of what happened. Accepts news URLs, written statements, images, or other source material. Follows investigative journalism standards with primary-source-first evidence hierarchy (court filings, government databases, verified public records, authenticated media, official statements, original publications). Use when asked to "investigate a claim", "fact-check", "verify a story", "find the truth about", "deep-dive into", "investigate what really happened", or any request requiring rigorous, evidence-based analysis of events or claims.
---

# Truth — Evidence-Based Investigation

## Purpose

Conduct forensic, evidence-grounded investigations of news items, claims, or events. The goal is to produce the most defensible account of what happened, grounded in primary evidence and corroborated facts — not in rhetoric, repetition, or the volume of circulating claims.

## Evidence Hierarchy (Strict)

Prioritize sources in this order. Higher-tier evidence overrides lower-tier when they conflict:

1. **Primary Documents**: Court filings, legislation text, patent filings, SEC filings, official contracts, authenticated government records
2. **Official Institutional Statements**: Press releases from involved parties, government agency statements, corporate filings (10-K, 10-Q, 8-K), verified transcripts
3. **Verified Raw Media**: Authenticated and timestamped video/audio/photographs with provenance chain, EXIF/metadata analysis results
4. **Authoritative Datasets**: Government databases (PACER, EDGAR, Federal Register, census data), international body records (UN, WHO, ICC), academic/scientific repositories
5. **Original Reporting (with sourcing)**: Investigative journalism from outlets with named sources, documented methodology, and editorial accountability
6. **Expert Analysis**: Domain experts with verifiable credentials commenting within their area of expertise
7. **Secondary Reporting**: Wire services, news aggregation, newspaper coverage — useful for leads but must be verified against higher-tier sources
8. **Social Media / Commentary**: Treat as lead material only. Never cite as evidence unless authenticated

When a lower-tier source contradicts a higher-tier source, flag the discrepancy explicitly and resolve in favor of the primary evidence.

## Workflow

### Phase 1: Intake & Scoping

1. **Receive input**: News URL, article text, written claim, image, video, or other source material.
2. **Extract core claims**: Break the input into discrete, testable factual claims. List each claim explicitly.
3. **Identify key entities**: People, organizations, dates, locations, amounts, document references.
4. **Set investigation scope**: Define what claims will be investigated and what is out of scope.
5. **State any constraints**: Note if the user has specified a focus, a time frame, or particular concerns.

### Phase 2: Primary Source Retrieval

For each key claim and entity, systematically search primary sources. See `references/primary-source-databases.md` for detailed search guidance.

**Court & Legal Records**:
- Federal: PACER (via web search for docket numbers/case names), CourtListener
- State: Search `"{entity}" site:courts.{state}.gov` or state-specific portals
- International: Equivalent national court databases

**Government Databases**:
- SEC EDGAR (corporate filings, insider trading)
- Federal Register (regulations, executive orders)
- Congress.gov (bills, hearing transcripts, voting records)
- State legislature databases
- FOIA reading rooms (CIA, FBI, State Dept, DOD)
- Government Accountability Office (GAO) reports

**Public Records**:
- Property records (county assessor databases)
- Business registrations (Secretary of State databases)
- Campaign finance (FEC, state equivalents, OpenSecrets)
- Lobbying disclosures (Senate/House lobbying databases)
- Nonprofit filings (IRS Form 990 via ProPublica Nonprofit Explorer)

**Official Organizational Sources**:
- Visit the **actual websites** of every organization mentioned in the claim
- Locate official press releases, annual reports, financial statements
- Check organizational leadership pages, mission statements
- Search organization's own news/media pages for their account of events

**International Public Sources**:
- UN databases, WHO disease surveillance, ICC case filings
- National statistical agencies, central bank publications
- Foreign government official portals (translate as needed)

### Phase 3: Open Source Intelligence (OSINT)

Run `scripts/generate_investigation_queries.py` to produce systematic search queries, then execute:

1. **Web Archive**: Search Wayback Machine (`web.archive.org`) for deleted pages, changed statements, or historical versions of key documents.
2. **Document Discovery**: `filetype:pdf "{entity}" {claim_keyword}` — search for leaked, embedded, or published PDFs, presentations, and spreadsheets.
3. **Communication Trails**: Search for press releases, investor calls, congressional testimony transcripts.
4. **Media Forensics** (if images/video are provided):
   - Reverse image search (Google Images, TinEye)
   - Check EXIF/metadata if image file is available
   - Search for earliest known appearance of the image to establish provenance
   - Cross-reference location/time claims in media against known events
5. **Social Media Archaeology**: Search for original posts, deleted statements (via archive services), and timestamped reactions from involved parties.
6. **Non-English Sources**: If the event involves non-English-speaking regions, **translate and search** local-language sources for ground-truth reporting that may differ from English-language coverage.

### Phase 4: Cross-Corroboration & Conflict Resolution

1. **Map evidence to claims**: For each extracted claim, list all evidence found (with tier classification).
2. **Corroboration check**: A fact is "corroborated" when confirmed by 2+ independent sources, at least one from tiers 1-4.
3. **Conflict analysis**: When sources disagree, document both accounts, state the evidence tier of each, and assess which is more credible based on:
   - Proximity to the event (firsthand > secondhand)
   - Independence (unrelated sources agreeing > affiliated sources)
   - Documentary evidence (documents > recollections)
   - Temporal proximity (contemporaneous accounts > retrospective ones)
   - Incentive analysis (who benefits from each version?)
4. **Identify gaps**: Explicitly list what could not be confirmed or denied. Do not fill gaps with speculation.

### Phase 5: Timeline Construction

Build a detailed, evidence-anchored timeline:
- Every entry must cite its source with tier classification
- Include timestamps at maximum available precision
- Flag entries where timing is uncertain or disputed
- Note temporal gaps where events are unknown

### Phase 6: Report Generation

Save the investigation report as a markdown file:
`truth/investigations/[topic_slug]_[YYYY-MM-DD].md`

#### Report Structure

```
# Investigation: [Title]
**Date**: [Investigation date]
**Subject**: [What was investigated]
**Input**: [What the user provided]

## Executive Summary
[2-3 paragraph summary of the most defensible account of what happened,
based on the totality of evidence. State confidence level.]

## Claims Analyzed
| # | Claim | Verdict | Confidence | Primary Evidence |
|---|-------|---------|------------|-----------------|
| 1 | [Claim text] | Confirmed/Refuted/Unverified/Partially True/Disputed | High/Medium/Low | [Source] |

## Evidence Map

### Claim 1: [Claim text]
**Verdict**: [Confirmed / Refuted / Unverified / Partially True / Disputed]
**Confidence**: [High / Medium / Low]

**Supporting Evidence (by tier)**:
- [Tier 1] [Source description and citation]
- [Tier 3] [Source description and citation]

**Contradicting Evidence**:
- [Tier 7] [Source description and citation] — [why this is less credible]

**Analysis**: [Reasoning for verdict]

### Claim 2: ...

## Timeline of Events
| Date/Time | Event | Source | Tier |
|-----------|-------|--------|------|
| [Timestamp] | [Event] | [Citation] | [1-8] |

## Source Registry
| # | Source | Type | Tier | URL | Access Date |
|---|--------|------|------|-----|-------------|
| 1 | [Name] | [Court filing / Press release / etc.] | [1-8] | [Clean URL] | [Date] |

## Unresolved Questions
- [What remains unknown or could not be verified]

## Methodology Notes
- [Any limitations, access constraints, or caveats]
```

## Critical Investigation Rules

1. **Never assume a widely repeated claim is true.** Repetition across outlets does not constitute corroboration if all trace back to a single original source.
2. **Trace to origin.** For every factual claim, ask: "Who first reported this, and what was their source?"
3. **Read the actual documents.** When a news article says "according to court filings" — find the filing. When it says "a report showed" — find the report.
4. **Check what organizations say about themselves.** Always visit the websites of involved organizations for their official account.
5. **Distinguish between claims and evidence.** A person saying something happened is a claim. A document showing it happened is evidence.
6. **Flag circular sourcing.** If Source A cites Source B, and Source B cites Source A, this is one source, not two.
7. **Translate and search non-English sources.** Critical ground-truth may only exist in local-language media.
8. **Preserve provenance.** Every piece of evidence must have a clear chain: where it came from, when it was accessed, what tier it belongs to.
9. **URL Hygiene**: Provide clean, canonical URLs to publisher sites. No redirect URLs, no search-engine cache URLs. If a clean URL cannot be found, provide the full bibliographic citation instead.
10. **No editorializing.** The report presents evidence and analysis. Conclusions must be stated in terms of evidence weight, not moral judgment.

## Scripts

- `scripts/generate_investigation_queries.py`: Generate systematic search queries for entities, claims, and evidence categories. Run early in Phase 2/3.

## References

- `references/primary-source-databases.md`: Comprehensive catalog of authoritative databases, search patterns, and access methods organized by domain (legal, financial, government, international, media).
- `references/evidence-hierarchy.md`: Detailed guidance on evidence classification, tier assignment, conflict resolution, and common verification pitfalls.
