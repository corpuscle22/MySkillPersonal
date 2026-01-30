---
name: pubmed
description: Perform extensive PubMed research on any medical topic or clinical question. Searches NCBI PubMed database, prioritizes high-quality evidence (meta-analyses, systematic reviews, RCTs, guidelines), and synthesizes findings into concise, evidence-based answers with inline citations. Use when the user asks medical research questions, wants literature review, needs evidence-based medical information, or asks about treatment efficacy, drug interactions, clinical guidelines, or medical conditions.
---

# PubMed Research Skill

Search PubMed for credible medical literature and synthesize findings into clear, evidence-based answers with inline citations.

## Prerequisites

**API Key (Optional but Recommended):**
- Without key: 3 requests/second (works fine for most queries)
- With key: 10 requests/second (faster for extensive research)

To set up: Create NCBI account at https://www.ncbi.nlm.nih.gov/, go to Account Settings → API Key Management → Create. Set environment variable `NCBI_API_KEY`.

## Workflow

### Step 1: Run PubMed Search

Execute the search script with the user's query:

```bash
python scripts/pubmed_search.py "USER'S MEDICAL QUESTION" --max 30 --years 10
```

Parameters:
- `--max N`: Limit results (default 30, use 50 for comprehensive research)
- `--years N`: Limit to last N years (default 10, use 0 for all time)
- `--json`: Output raw JSON only (for programmatic use)

### Step 2: Analyze Results

Review the output which includes:
- Articles sorted by evidence quality score (10 = meta-analysis, down to 3 = case report)
- Abstracts for context
- **Full Text Excerpts** (automatically fetched from PMC if available)
- DOI and detailed link information
- PMIDs and URLs for citations

See `references/evidence-hierarchy.md` for the scoring methodology.

### Step 3: Synthesize Answer

Compose a concise, evidence-based response following these rules:

#### Answer Format

```
**Summary**: [1-2 sentence direct answer to the question]

**Key Findings**:
- [Finding 1 with inline citation]
- [Finding 2 with inline citation]
- [Finding 3 with inline citation]

**Evidence Quality**: [Brief note on strength of evidence]

**Clinical Considerations**: [If applicable, practical implications]

**References**:
[1] Author et al. (Year). Title. Journal. [PMID: 12345678](https://pubmed.ncbi.nlm.nih.gov/12345678/)
```

#### Citation Rules

1. **Inline citations**: Use format `[Author Year]` or numbered `[1]` 
2. **Link PMIDs**: Always hyperlink to PubMed: `[PMID: X](https://pubmed.ncbi.nlm.nih.gov/X/)`
3. **Prioritize evidence**: Lead with meta-analyses/SRs, then RCTs, then observational
4. **Note limitations**: State when evidence is limited, conflicting, or low-quality
5. **Be concise**: 4-8 key findings, not a literature dump

#### Synthesis Guidelines

- **Be definitive when evidence allows**: "Meta-analyses consistently show X reduces Y by 30%"
- **Acknowledge uncertainty**: "Limited RCT data; observational studies suggest..."
- **Quantify when possible**: Include effect sizes, NNT, odds ratios from the abstracts
- **Note conflicts**: "While [Author 2023] found X, [Author 2022] reported opposite findings"
- **Clinical relevance**: Connect to practical patient care when applicable

## Example Output

User asks: "Is vitamin D effective for preventing COVID-19?"

**Summary**: Current evidence does not support vitamin D supplementation for COVID-19 prevention in the general population, though it may benefit those with deficiency.

**Key Findings**:
- A meta-analysis of 13 RCTs (n=14,968) found no significant reduction in COVID-19 infection risk with vitamin D supplementation (RR 0.97, 95% CI 0.88-1.08) [Jolliffe 2023]
- Subgroup analysis showed potential benefit in vitamin D-deficient individuals (RR 0.74) [Jolliffe 2023]
- An RCT of high-dose vitamin D (n=2,690) showed no effect on COVID-19 incidence [Brunvoll 2022]

**Evidence Quality**: Strong - Multiple large RCTs and meta-analyses available

**Clinical Considerations**: Screen for and treat vitamin D deficiency; routine supplementation for COVID-19 prevention not recommended.

**References**:
[1] Jolliffe DA et al. (2023). Vitamin D supplementation... Lancet Diabetes Endocrinol. [PMID: 36681598](https://pubmed.ncbi.nlm.nih.gov/36681598/)
[2] Brunvoll SH et al. (2022). Prevention of covid-19... BMJ. [PMID: 36130778](https://pubmed.ncbi.nlm.nih.gov/36130778/)

---

## Troubleshooting

### No Results Found
- Broaden the search terms
- Use MeSH terms (e.g., "hypertension" instead of "high blood pressure")
- Remove year filter: `--years 0`
- Check spelling

### Too Many Low-Quality Results
- Add specific terms: "randomized controlled trial", "meta-analysis"
- Use `--max 50` and filter by evidence score in synthesis
- Focus on recent years: `--years 5`

### Rate Limiting Errors
- The script handles rate limiting automatically
- If errors persist, get an API key (see Prerequisites)
