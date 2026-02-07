---
name: company-intelligence
description: Comprehensive company research and intelligence gathering. Provides deep-dive analysis including company overview, financials, investors, funding history, customer growth, and competitive landscape. Use when researching any company (public or private), analyzing investments, due diligence, market research, or gathering business intelligence. Covers SEC filings, funding rounds, investor details, financial metrics, and publicly available company data.
---

# Company Intelligence

Comprehensive research tool for gathering detailed company information from multiple public data sources.

## Overview

This skill enables deep-dive research on any company, providing:
- **Company Profile**: What the company does, products/services, target market
- **Financials**: Revenue, profit margins, growth rates, financial health
- **Investors & Funding**: Investment rounds, investors, valuations, funding history
- **Customer/Growth Metrics**: User growth, market share, employee count trends
- **Competitive Landscape**: Key competitors, market positioning

## Available Data Sources

### Free APIs (Configured)
| Source | Coverage | API Key Required | Rate Limit |
|--------|----------|------------------|------------|
| SEC EDGAR | Public US companies | No | Unlimited |
| Alpha Vantage | Stock data, financials | Yes (free) | 25/day |
| Financial Modeling Prep | Company profiles, financials | Yes (free) | 250/day |
| OpenCorporates | Company registry data | Optional | 500/month |

### Web Sources (No API)
- Company websites and press releases
- LinkedIn company pages
- News articles and announcements
- Crunchbase (public profiles)
- PitchBook (limited public data)

## Setup Requirements

Before first use, run the API setup script to configure free API keys:

```bash
python scripts/setup_apis.py
```

This will guide you through obtaining and storing free API keys. See `references/api_setup_guide.md` for detailed instructions.

## Workflow

### Step 1: Identify Company

Gather initial company information:
- Official company name and any aliases
- Stock ticker (if public)
- Company website URL
- Headquarters location

### Step 2: Determine Company Type

**Public Company** (traded on stock exchange):
- Use SEC EDGAR for official filings (10-K, 10-Q, 8-K)
- Use Alpha Vantage/FMP for real-time financial data
- Rich financial disclosure available

**Private Company** (not publicly traded):
- Use web search for funding announcements
- Check Crunchbase public profiles
- Search news for investor information
- Limited official financial data available

### Step 3: Gather Data by Category

#### Company Overview
1. Run `scripts/company_profile.py --company "Company Name"` for basic profile
2. Search company website for:
   - Mission statement and values
   - Products/services offered
   - Target customers and markets
   - Leadership team
3. Check LinkedIn for employee count and growth

#### Financial Information

**For Public Companies:**
```bash
python scripts/sec_edgar.py --ticker AAPL --filing-type 10-K
python scripts/financial_data.py --ticker AAPL
```

**For Private Companies:**
- Search for funding announcements
- Check news for revenue disclosures
- Look for employee count as proxy for growth

#### Investors & Funding

```bash
python scripts/funding_search.py --company "Company Name"
```

This searches multiple sources for:
- Funding rounds (Seed, Series A, B, C, etc.)
- Lead investors and participants
- Valuation at each round
- Total funding raised

#### Customer/Growth Metrics

- Employee count (LinkedIn, company filings)
- User/customer counts (press releases, filings)
- Revenue growth (public filings or announcements)
- Market share data (industry reports)

### Step 4: Compile Intelligence Report

Use the gathered data to create a comprehensive report following the output format below.

## Output Format

```markdown
# Company Intelligence Report: [Company Name]
Generated: [Date]

## Executive Summary
[2-3 sentence overview of the company and key findings]

## Company Profile
- **Founded**: [Year]
- **Headquarters**: [Location]
- **Industry**: [Primary industry]
- **Employees**: [Count] (as of [date])
- **Website**: [URL]
- **Status**: [Public/Private]
- **Ticker**: [If public]

### What They Do
[Description of products/services, target market, business model]

### Leadership
| Role | Name | Background |
|------|------|------------|
| CEO | | |
| CFO | | |
| CTO | | |

## Financial Overview

### Key Metrics (Most Recent Fiscal Year)
| Metric | Value | YoY Change |
|--------|-------|------------|
| Revenue | | |
| Net Income | | |
| Gross Margin | | |
| Operating Margin | | |

### Financial History
[Revenue/growth chart or table for past 3-5 years]

### Financial Health Indicators
- **Debt-to-Equity**: 
- **Current Ratio**: 
- **Cash Position**: 

## Funding & Investment History

### Total Funding Raised: $[Amount]
### Latest Valuation: $[Amount] (as of [date])

### Funding Rounds
| Date | Round | Amount | Lead Investor | Valuation |
|------|-------|--------|---------------|-----------|
| | | | | |

### Notable Investors
[List key investors with brief descriptions]

## Growth & Traction

### Customer/User Metrics
- **Total Users/Customers**: 
- **Growth Rate**: 
- **Key Markets**: 

### Employee Growth
[Employee count trend over time]

## Competitive Landscape

### Direct Competitors
| Competitor | Key Differentiator | Est. Revenue |
|------------|-------------------|--------------|
| | | |

### Market Position
[Analysis of company's position in the market]

## Recent News & Developments
- [Date]: [Headline/Summary]
- [Date]: [Headline/Summary]

## Risk Factors
[Key risks identified from filings or analysis]

## Data Sources
[List all sources used with dates accessed]
```

## Scripts Reference

| Script | Purpose | Example Usage |
|--------|---------|---------------|
| `setup_apis.py` | Configure API keys | `python scripts/setup_apis.py` |
| `company_profile.py` | Get company overview | `python scripts/company_profile.py --company "Tesla"` |
| `sec_edgar.py` | Fetch SEC filings | `python scripts/sec_edgar.py --ticker TSLA --filing-type 10-K` |
| `financial_data.py` | Get financial metrics | `python scripts/financial_data.py --ticker TSLA` |
| `funding_search.py` | Search funding history | `python scripts/funding_search.py --company "OpenAI"` |
| `full_report.py` | Generate complete report | `python scripts/full_report.py --company "Tesla" --ticker TSLA` |

## Configuration

API keys are stored in `~/.company-intelligence/config.json`:

```json
{
  "alpha_vantage_api_key": "YOUR_KEY",
  "fmp_api_key": "YOUR_KEY",
  "opencorporates_api_key": "YOUR_KEY"
}
```

## Additional Resources

- `references/api_setup_guide.md` - Detailed API registration instructions
- `references/data_sources.md` - Comprehensive list of data sources and what they provide
- `references/financial_metrics.md` - Explanation of financial terms and metrics
