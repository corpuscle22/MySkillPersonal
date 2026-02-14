# Evidence Hierarchy & Verification Guide

## Table of Contents
1. [Evidence Tier Definitions](#evidence-tier-definitions)
2. [Assigning Tiers](#assigning-tiers)
3. [Corroboration Standards](#corroboration-standards)
4. [Conflict Resolution Protocol](#conflict-resolution-protocol)
5. [Common Verification Pitfalls](#common-verification-pitfalls)
6. [Source Authentication Checklist](#source-authentication-checklist)

---

## Evidence Tier Definitions

### Tier 1: Primary Documents
Legally filed, officially published, or authenticated documents with institutional provenance.

**Examples**: Court filings (complaints, motions, orders, judgments), enacted legislation, patent filings, SEC filings (10-K, 10-Q, 8-K, proxy statements), official contracts, government-issued records (birth/death certificates, property deeds), authenticated treaties.

**Why highest tier**: These documents have legal standing. Fabricating them carries criminal penalties. They are filed with institutions that verify identity and maintain custody chains.

**Caveats**: Court filings contain *allegations* by one party — the filing itself is a fact ("X alleged Y in court"), but the allegations within it are claims until adjudicated. Distinguish between: "The complaint alleges..." vs. "The court found..."

### Tier 2: Official Institutional Statements
Communications from organizations speaking in their official capacity about their own actions or positions.

**Examples**: Press releases from involved parties, official government agency statements, corporate earnings reports, verified official transcripts (congressional hearings, depositions), university statements from communications offices.

**Why tier 2**: Organizations have reputational and legal incentives for accuracy in official statements. However, they also have incentive to frame events favorably. Treat as the organization's stated position, which is itself a fact, while recognizing it may be self-serving.

### Tier 3: Verified Raw Media
Audio, video, or photographic material with established provenance — the chain of custody from creation to publication is known.

**Examples**: Authenticated body camera footage, surveillance video from identified sources, broadcast recordings (C-SPAN, official press conferences), EXIF-verified photographs from known photographers, court-admitted media exhibits.

**Assessment criteria**: Who captured it? When? Where was it stored? Has it been edited? Is the original available?

**Caveats**: Even authentic media can be misleadingly cropped, taken out of context, or selectively excerpted. Always seek the full, unedited version.

### Tier 4: Authoritative Datasets
Structured data from government agencies, international bodies, or academic institutions with documented methodology.

**Examples**: Census data, economic indicators (BLS, BEA, Federal Reserve), CDC/WHO epidemiological data, NASA/NOAA climate data, EDGAR filings database, election results from state boards, crime statistics from FBI UCR/NIBRS.

**Why tier 4**: Data collection methodology is documented and auditable. However, methodology choices affect outcomes (e.g., how unemployment is defined). Note methodology when citing.

### Tier 5: Original Reporting with Named Sources
Investigative journalism where reporters identify their sources by name or provide sufficient detail to assess credibility.

**Examples**: Long-form investigative pieces with named witnesses, quoted documents, or described methodology. Organizations like ProPublica, The Intercept, Reuters Investigates, NYT Investigations, Washington Post Investigations, local investigative units.

**Assessment criteria**: Are sources named? Is methodology described? Are documents referenced available? Does the outlet have editorial standards and correction policies?

**Caveats**: Even excellent journalism can contain errors. Use as strong leads for finding primary sources.

### Tier 6: Expert Analysis
Commentary from individuals with verifiable domain expertise, speaking within their area of qualification.

**Examples**: A securities lawyer analyzing an SEC filing, an epidemiologist interpreting disease data, a constitutional scholar analyzing a court ruling, a forensic accountant reviewing financial statements.

**Assessment criteria**: Does the expert have relevant credentials? Are they speaking within their expertise? Do they have conflicts of interest? Are other experts saying different things?

### Tier 7: Secondary Reporting
Reporting that synthesizes, summarizes, or repackages information from other sources.

**Examples**: Wire service summaries, news aggregation sites, newspaper articles that cite other newspaper articles, "reports say" attributions, roundups.

**Utility**: Good for identifying what claims are in circulation and finding leads. Not sufficient for establishing facts.

**Key test**: Does this article add original information, or is it restating what others reported?

### Tier 8: Social Media & Commentary
Unverified claims, opinions, reactions, and commentary from individuals or anonymous accounts.

**Examples**: Tweets, Facebook posts, Reddit comments, blog posts, YouTube commentary, TikTok videos, forum discussions.

**Utility**: Leads only. A social media post can point you to a primary document, but the post itself is not evidence of anything except that someone made that post.

**Exception**: When a key actor makes an official statement via social media (e.g., a company CEO announcing a decision on Twitter), the statement itself becomes Tier 2 if verified as authentic.

---

## Assigning Tiers

When classifying a source, ask:

1. **Is this an original document with institutional filing/custody?** → Tier 1
2. **Is this an organization speaking officially about itself?** → Tier 2
3. **Is this authenticated raw media with known provenance?** → Tier 3
4. **Is this structured data from an authoritative institution?** → Tier 4
5. **Is this original journalism with named sources?** → Tier 5
6. **Is this expert commentary within the expert's domain?** → Tier 6
7. **Is this reporting that relies on other reports?** → Tier 7
8. **Is this social media or unverified commentary?** → Tier 8

**When uncertain**: Assign the *lower* (less authoritative) tier. It is better to underrate than overrate a source.

---

## Corroboration Standards

### Confirmed Fact
Requires **2+ independent sources**, with at least one from **Tiers 1-4**.

"Independent" means the sources do not share an origin. Two news articles citing the same press release = one source. A court filing + an independent news investigation = two sources.

### Strong Indication
**2+ independent sources from Tiers 1-6**, but lacking a Tier 1-4 anchor.

### Reported but Unverified
**Single source from Tiers 5-6**, or **multiple sources from Tier 7** that appear to trace to a single original report.

### Unverified Claim
**Only Tier 7-8 sources**, or a single Tier 7 source.

### Disputed
**Multiple sources across tiers asserting contradictory versions.**

---

## Conflict Resolution Protocol

When sources conflict, follow this resolution sequence:

### Step 1: Tier Comparison
Higher-tier evidence is presumptively more reliable. A court order (Tier 1) overrides a newspaper account (Tier 7) of what the order says.

### Step 2: Independence Assessment
Are the conflicting sources truly independent, or do they share an upstream source?

### Step 3: Proximity Analysis
Who is closer to the event? Firsthand witnesses > secondhand accounts. Contemporaneous records > retrospective recollections.

### Step 4: Documentary vs. Testimonial
Written records created at the time of events > later recollections of events.

### Step 5: Incentive Analysis
Who benefits from each version? A party's self-serving account is less weight than a disinterested party's account. (But do not dismiss self-serving accounts entirely — they may still be accurate.)

### Step 6: Volume vs. Origin
If 50 articles all repeat the same claim but trace to one original report, this is **one piece of evidence repeated 50 times**, not 50 pieces of evidence. Trace every claim to its origin.

### If Unresolvable
Present both versions with full evidence analysis. State: "The available evidence does not definitively resolve this conflict. [Version A] is supported by [evidence]. [Version B] is supported by [evidence]."

---

## Common Verification Pitfalls

### 1. Circular Sourcing
**Pattern**: Source A quotes Source B, who got it from Source A.
**Detection**: Trace every claim backwards. Ask: "Who originally reported this?"
**Example**: A Wikipedia article cites a newspaper. The newspaper got the fact from Wikipedia. Both now appear to confirm the same thing, but neither has an independent source.

### 2. Repetition = Truth Illusion
**Pattern**: A claim appears in many outlets, creating the impression of broad corroboration.
**Detection**: Check if all outlets trace back to a single original report. Often, one outlet breaks a story and dozens rephrase it.

### 3. Allegation vs. Adjudication
**Pattern**: "X was charged with fraud" is reported as "X committed fraud."
**Detection**: Distinguish carefully between: charged/indicted (accusation), convicted/found liable (adjudicated), settled (agreed resolution, not admission).

### 4. Selective Quoting
**Pattern**: A quote is accurately reproduced but taken out of context, changing its meaning.
**Detection**: Find the full original text (transcript, document, video). Read surrounding context.

### 5. Date Confusion
**Pattern**: Old events resurfacing as current news, or undated claims.
**Detection**: Verify when events occurred. Check Wayback Machine for when content first appeared online.

### 6. Deepfakes & Manipulated Media
**Pattern**: AI-generated or edited images/video/audio presented as authentic.
**Detection**: Reverse image search, check for known originals, note any forensic indicators (artifacts, inconsistencies). Flag when media authenticity cannot be confirmed.

### 7. Unnamed Sources
**Pattern**: "Sources say" or "according to people familiar with the matter."
**Detection**: This is not zero evidence — reputable outlets stake their reputation on unnamed sources. But it is lower tier than named sources, and cannot alone corroborate a claim.

### 8. False Balance
**Pattern**: Presenting a well-supported position and a fringe position as equally weighted.
**Detection**: Assess the evidence distribution. If 10 primary documents support Version A and one blog post supports Version B, do not present them as "two sides."

---

## Source Authentication Checklist

For each key source in the investigation:

- [ ] **Provenance**: Where did this come from? What is the custody chain?
- [ ] **Authenticity**: Is this the genuine, unmodified document/media?
- [ ] **Timeliness**: When was this created? When was it published? Are these different?
- [ ] **Authority**: Who created this? Are they in a position to know?
- [ ] **Independence**: Is this source independent from other sources being cited?
- [ ] **Completeness**: Is this the full document/media, or an excerpt?
- [ ] **Incentive**: Does the source have an incentive to present information in a particular way?
- [ ] **Corroboration**: Is this claim confirmed by at least one other independent source?
