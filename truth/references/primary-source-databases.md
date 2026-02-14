# Primary Source Databases & Search Patterns

## Table of Contents
1. [U.S. Federal Court & Legal](#us-federal-court--legal)
2. [U.S. State Court & Legal](#us-state-court--legal)
3. [Corporate & Financial](#corporate--financial)
4. [U.S. Government & Legislative](#us-government--legislative)
5. [FOIA & Declassified Records](#foia--declassified-records)
6. [Campaign Finance & Lobbying](#campaign-finance--lobbying)
7. [Nonprofit & Tax Records](#nonprofit--tax-records)
8. [Property & Business Records](#property--business-records)
9. [International & Treaty Bodies](#international--treaty-bodies)
10. [Academic & Scientific](#academic--scientific)
11. [Media & Archive](#media--archive)
12. [Law Enforcement & Criminal](#law-enforcement--criminal)

---

## U.S. Federal Court & Legal

| Database | URL | What It Contains | Search Pattern |
|----------|-----|-----------------|----------------|
| PACER | pacer.uscourts.gov | Federal court filings, dockets | Search via web: `site:courtlistener.com "{party name}"` or `PACER "{case name}"` |
| CourtListener | courtlistener.com | Federal court opinions, oral arguments | `site:courtlistener.com "{party}" OR "{case number}"` |
| Supreme Court | supremecourt.gov | Opinions, orders, docket | `site:supremecourt.gov "{case name}"` |
| U.S. Sentencing Commission | ussc.gov | Sentencing data, guidelines | `site:ussc.gov "{topic}"` |
| DOJ Press Releases | justice.gov/news | Indictments, settlements, enforcement actions | `site:justice.gov "{entity}" indictment OR settlement OR plea` |

**Tips**:
- For active cases: search `"{party name}" docket number filetype:pdf`
- For case documents referenced in news: `"{exact case name}" OR "{docket number}" filetype:pdf`
- CourtListener is free and often has what PACER has behind a paywall

## U.S. State Court & Legal

**General pattern**: `"{entity}" site:courts.{state abbreviation}.gov`

| State | Court System URL | Notes |
|-------|-----------------|-------|
| California | courts.ca.gov | Extensive online records |
| New York | nycourts.gov | eCourts portal |
| Texas | txcourts.gov | re:SearchTX for case search |
| Florida | flcourts.org | Broad public records access |
| Illinois | illinoiscourts.gov | Searchable dockets |

**Tips**:
- Many states have separate portals for civil vs. criminal
- Search county-level courts independently: `"{entity}" "{county}" court records`
- Appellate decisions often more accessible than trial court records

## Corporate & Financial

| Database | URL | What It Contains | Search Pattern |
|----------|-----|-----------------|----------------|
| SEC EDGAR | sec.gov/cgi-bin/browse-edgar | Public company filings (10-K, 10-Q, 8-K, proxy, insider trades) | `site:sec.gov/cgi-bin "{company}" OR "{CIK number}"` |
| EDGAR Full-Text Search | efts.sec.gov/LATEST/search-index | Full-text search of all EDGAR filings | `efts.sec.gov "{search term}"` |
| SEC Enforcement Actions | sec.gov/litigation | SEC enforcement, litigation releases | `site:sec.gov/litigation "{entity}"` |
| FINRA BrokerCheck | brokercheck.finra.org | Broker/advisor disciplinary history | Search by name directly |
| FDIC BankFind | fdic.gov/bank/individual | Bank financial data, failures | Search by institution name |
| Federal Reserve | federalreserve.gov | Enforcement actions, monetary policy | `site:federalreserve.gov "{entity}" enforcement` |

**Tips**:
- For insider trading: search EDGAR for Form 4 filings
- 8-K filings reveal material events (layoffs, mergers, lawsuits) in real-time
- Proxy statements (DEF 14A) reveal executive compensation

## U.S. Government & Legislative

| Database | URL | What It Contains | Search Pattern |
|----------|-----|-----------------|----------------|
| Congress.gov | congress.gov | Bills, resolutions, hearing transcripts, voting records | `site:congress.gov "{topic}" OR "{bill number}"` |
| Federal Register | federalregister.gov | Rules, proposed rules, executive orders | `site:federalregister.gov "{topic}" OR "{agency}"` |
| GAO Reports | gao.gov | Government accountability investigations | `site:gao.gov "{topic}"` |
| CBO | cbo.gov | Congressional Budget Office cost estimates | `site:cbo.gov "{bill}" OR "{topic}"` |
| Congressional Record | congress.gov/congressional-record | Floor speeches, debates verbatim | `site:congress.gov/congressional-record "{topic}"` |
| White House | whitehouse.gov | Executive orders, statements, briefings | `site:whitehouse.gov "{topic}"` |
| GovInfo | govinfo.gov | Official publications of all three branches | `site:govinfo.gov "{topic}" filetype:pdf` |

## FOIA & Declassified Records

| Database | URL | What It Contains |
|----------|-----|-----------------|
| CIA FOIA Reading Room | cia.gov/readingroom | Declassified intelligence documents |
| FBI Vault | vault.fbi.gov | Released FBI files on persons, orgs, events |
| State Dept FOIA | foia.state.gov | Diplomatic cables, records |
| DOD FOIA | open.defense.gov | Military and defense records |
| National Archives | archives.gov | Historical federal records |
| NSA Declassified | nsa.gov/helpful-links/nsa-foia | Declassified NSA documents |
| MuckRock | muckrock.com | Crowdsourced FOIA requests and results |

**Search pattern**: `site:{agency domain} FOIA "{topic}"` or `"{topic}" declassified`

## Campaign Finance & Lobbying

| Database | URL | What It Contains | Search Pattern |
|----------|-----|-----------------|----------------|
| FEC | fec.gov | Federal campaign contributions, expenditures | `site:fec.gov "{candidate}" OR "{committee}"` |
| OpenSecrets | opensecrets.org | Campaign finance analysis, lobbying data | `site:opensecrets.org "{entity}"` |
| Senate Lobbying | lda.senate.gov | Lobbying registrations and disclosures | Search directly by registrant/client |
| House Lobbying | lobbyingdisclosure.house.gov | Lobbying reports | Search directly |
| FollowTheMoney | followthemoney.org | State-level campaign finance | `site:followthemoney.org "{candidate}"` |
| FARA | fara.gov | Foreign agent registrations | `site:fara.gov "{entity}"` |

## Nonprofit & Tax Records

| Database | URL | What It Contains |
|----------|-----|-----------------|
| ProPublica Nonprofit Explorer | projects.propublica.org/nonprofits | IRS Form 990 filings for all nonprofits |
| GuideStar (Candid) | guidestar.org | Nonprofit financial data, leadership |
| IRS Tax Exempt Search | apps.irs.gov/app/eos | Tax-exempt organization status |
| Charity Navigator | charitynavigator.org | Charity ratings, financial health |

**Search pattern**: `site:projects.propublica.org/nonprofits "{organization name}"`

## Property & Business Records

**Business Registrations**: Search `"{company name}" site:sos.{state}.gov` or `"{company name}" secretary of state {state}`

**Property Records**: Search `"{owner name}" property records {county} {state}` — most counties have online assessor databases

**UCC Filings**: Uniform Commercial Code filings reveal secured transactions — search state SOS websites

## International & Treaty Bodies

| Database | URL | What It Contains |
|----------|-----|-----------------|
| UN Documents | documents.un.org | Resolutions, reports, meeting records |
| ICC Case Law | icc-cpi.int/cases | International criminal cases |
| ICJ | icj-cij.org | International Court of Justice cases |
| WHO | who.int | Health data, outbreak reports, guidelines |
| World Bank Open Data | data.worldbank.org | Economic indicators by country |
| OECD | oecd.org | Economic policy, statistical data |
| UK Companies House | find-and-update.company-information.service.gov.uk | UK company registrations, directors |
| UK Gazette | thegazette.co.uk | Official UK public notices, insolvency |
| Indian eCourts | ecourts.gov.in | Indian court case search |
| Indian Kanoon | indiankanoon.org | Indian legal database |
| EU Law (EUR-Lex) | eur-lex.europa.eu | EU legislation, case law |
| Canadian Court Decisions | canlii.org | Canadian legal information |
| Australian Legal | austlii.edu.au | Australian legal information |

## Academic & Scientific

| Database | URL | What It Contains |
|----------|-----|-----------------|
| PubMed | pubmed.ncbi.nlm.nih.gov | Biomedical literature |
| Google Scholar | scholar.google.com | Academic papers across disciplines |
| arXiv | arxiv.org | Preprints (physics, CS, math, etc.) |
| SSRN | ssrn.com | Social science research papers |
| Retraction Watch | retractionwatch.com | Retracted academic papers |
| ClinicalTrials.gov | clinicaltrials.gov | Clinical trial registrations and results |

## Media & Archive

| Database | URL | What It Contains |
|----------|-----|-----------------|
| Wayback Machine | web.archive.org | Archived web pages (historical snapshots) |
| Google Cache | `cache:{URL}` | Recent cached versions of pages |
| Internet Archive | archive.org | Books, audio, video, web archives |
| C-SPAN Video Library | c-span.org/video | Congressional proceedings, political events |
| AP Fact Check | apnews.com/APFactCheck | Associated Press fact-checking |
| Reuters Fact Check | reuters.com/fact-check | Reuters fact-checking unit |
| Snopes | snopes.com | Longstanding fact-checking database |

**Tips**:
- Wayback Machine: `web.archive.org/web/*/{URL}` to see all snapshots
- For deleted social media: `web.archive.org/web/*/twitter.com/{handle}/status/*`
- Google cache search: `cache:example.com/specific-page`

## Law Enforcement & Criminal

| Database | URL | What It Contains |
|----------|-----|-----------------|
| FBI Most Wanted | fbi.gov/wanted | Current wanted persons |
| Interpol Red Notices | interpol.int/en/How-we-work/Notices/Red-Notices | International wanted persons |
| DEA Drug Scheduling | dea.gov/drug-information | Drug classification, enforcement |
| BOP Inmate Locator | bop.gov/inmateloc | Federal prison inmate search |
| National Sex Offender Registry | nsopw.gov | Sex offender registry search |
| State Corrections | Varies by state | State prison inmate databases |

**Search pattern**: `"{entity}" site:fbi.gov` or `"{entity}" arrest {jurisdiction}`
