#!/usr/bin/env python3
"""
Full Company Intelligence Report Generator

Generates a comprehensive company intelligence report by combining data
from multiple sources.

Usage:
    python full_report.py --company "Tesla" --ticker TSLA
    python full_report.py --company "OpenAI"
    python full_report.py --ticker AAPL --output report.md
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path


# Configuration
CONFIG_FILE = Path.home() / ".company-intelligence" / "config.json"


def load_config():
    """Load API configuration."""
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {}


def format_currency(value):
    """Format large numbers as currency."""
    if value is None:
        return "N/A"
    try:
        value = float(value)
        if abs(value) >= 1e12:
            return f"${value/1e12:.2f}T"
        elif abs(value) >= 1e9:
            return f"${value/1e9:.2f}B"
        elif abs(value) >= 1e6:
            return f"${value/1e6:.2f}M"
        else:
            return f"${value:,.2f}"
    except (ValueError, TypeError):
        return str(value)


def generate_report_template(company_name: str, ticker: str = None, profile: dict = None, 
                           financials: dict = None, is_public: bool = True) -> str:
    """Generate a comprehensive report template."""
    
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Start with header
    report = f"""# Company Intelligence Report: {company_name}
Generated: {today}

---

## Executive Summary
[2-3 sentence overview of the company, its core business, and key findings]

---

## Company Profile

"""
    
    if profile:
        report += f"""- **Company Name**: {profile.get('companyName', company_name)}
- **Founded**: {profile.get('ipoDate', '[Research needed]')[:4] if profile.get('ipoDate') else '[Research needed]'}
- **Headquarters**: {profile.get('city', 'N/A')}, {profile.get('state', '')}, {profile.get('country', 'N/A')}
- **Industry**: {profile.get('industry', 'N/A')}
- **Sector**: {profile.get('sector', 'N/A')}
- **Employees**: {int(profile.get('fullTimeEmployees', 0)):,} (as of latest filing)
- **Website**: {profile.get('website', 'N/A')}
- **Status**: {'Public' if is_public else 'Private'}
"""
        if ticker:
            report += f"- **Ticker**: {ticker}\n"
            report += f"- **Exchange**: {profile.get('exchangeShortName', 'N/A')}\n"
    else:
        report += f"""- **Company Name**: {company_name}
- **Founded**: [Research needed]
- **Headquarters**: [Research needed]
- **Industry**: [Research needed]
- **Sector**: [Research needed]
- **Employees**: [Research needed]
- **Website**: [Research needed]
- **Status**: {'Public' if is_public else 'Private'}
"""
        if ticker:
            report += f"- **Ticker**: {ticker}\n"
    
    # What They Do section
    report += """
### What They Do
"""
    if profile and profile.get('description'):
        desc = profile['description'][:800]
        report += f"{desc}...\n"
    else:
        report += "[Research company website, press releases, and industry sources for detailed description]\n"
    
    # Leadership section
    report += """
### Leadership Team

| Role | Name | Background |
|------|------|------------|
"""
    if profile and profile.get('ceo'):
        report += f"| CEO | {profile['ceo']} | [Research LinkedIn] |\n"
    else:
        report += "| CEO | [Research needed] | |\n"
    
    report += """| CFO | [Research needed] | |
| CTO | [Research needed] | |
| COO | [Research needed] | |

---

## Financial Overview

"""
    
    if is_public and financials:
        # Add financial data if available
        if financials.get('quote'):
            quote = financials['quote']
            report += f"""### Current Market Data
- **Stock Price**: ${quote.get('price', 'N/A')}
- **Market Cap**: {format_currency(quote.get('marketCap'))}
- **P/E Ratio**: {quote.get('pe', 'N/A')}
- **EPS**: ${quote.get('eps', 'N/A')}
- **52 Week Range**: ${quote.get('yearLow', 'N/A')} - ${quote.get('yearHigh', 'N/A')}

"""
        
        report += """### Key Metrics (Most Recent Fiscal Year)

| Metric | Value | YoY Change |
|--------|-------|------------|
| Revenue | [From 10-K] | |
| Net Income | [From 10-K] | |
| Gross Margin | [From 10-K] | |
| Operating Margin | [From 10-K] | |

### Revenue History (Last 5 Years)

| Year | Revenue | Growth Rate |
|------|---------|-------------|
| [Year] | | |
| [Year-1] | | |
| [Year-2] | | |
| [Year-3] | | |
| [Year-4] | | |

### Financial Health Indicators
- **Debt-to-Equity**: [From balance sheet]
- **Current Ratio**: [From balance sheet]
- **Cash Position**: [From balance sheet]
- **Free Cash Flow**: [From cash flow statement]

"""
    else:
        report += """### Financial Information

**Note**: As a private company, detailed financials are not publicly disclosed.

Known Financial Data:
- **Last Known Revenue**: [Search press releases, news]
- **Estimated Valuation**: [From funding announcements]
- **Profitability Status**: [Research needed]

Sources to check:
1. Press releases mentioning revenue milestones
2. Funding announcements with valuation data
3. Industry reports and estimates
4. Employee count as growth proxy

"""
    
    # Funding section
    report += """---

## Funding & Investment History

"""
    
    if is_public:
        report += """### IPO Information
- **IPO Date**: [Research SEC S-1 filing]
- **IPO Price**: [Research]
- **Initial Valuation**: [Research]

### Pre-IPO Funding
[Research Crunchbase, news archives for pre-IPO funding rounds]

"""
    else:
        report += """### Total Funding Raised: $[Amount]
### Latest Valuation: $[Amount] (as of [date])

### Funding Rounds

| Date | Round | Amount | Lead Investor(s) | Valuation |
|------|-------|--------|------------------|-----------|
| | Seed | | | |
| | Series A | | | |
| | Series B | | | |
| | Series C | | | |

"""
    
    report += """### Notable Investors
[List key investors with brief descriptions - check Crunchbase, PitchBook]

1. **[Investor Name]** - [Description, other notable investments]
2. **[Investor Name]** - [Description]

---

## Growth & Traction

### Customer/User Metrics
- **Total Users/Customers**: [Research press releases, earnings calls]
- **Growth Rate**: [Calculate from available data]
- **Key Markets**: [Research]
- **Notable Customers**: [Check website, case studies]

### Employee Growth Trend

| Year | Employee Count | Growth |
|------|----------------|--------|
| [Current] | | |
| [Previous] | | |
| [2 years ago] | | |

Source: LinkedIn company page, SEC filings, or press releases

### Key Milestones
- [Date]: [Milestone]
- [Date]: [Milestone]

---

## Competitive Landscape

### Direct Competitors

| Competitor | Key Differentiator | Est. Revenue | Notable |
|------------|-------------------|--------------|---------|
| [Competitor 1] | | | |
| [Competitor 2] | | | |
| [Competitor 3] | | | |

### Market Position
[Analysis of company's position - market share, competitive advantages, moats]

### SWOT Analysis

**Strengths:**
- 

**Weaknesses:**
- 

**Opportunities:**
- 

**Threats:**
- 

---

## Recent News & Developments

| Date | Headline | Source |
|------|----------|--------|
| | | |
| | | |
| | | |

---

## Risk Factors

"""
    
    if is_public:
        report += """[Extract from 10-K Risk Factors section - SEC EDGAR]

Key risks to monitor:
1. 
2. 
3. 

"""
    else:
        report += """Key risks to monitor:
1. Competitive pressure
2. Funding/runway considerations
3. Market/regulatory risks
4. 

"""
    
    report += """---

## Data Sources & Research Checklist

### Sources Used
- [ ] Company website
- [ ] SEC EDGAR filings (10-K, 10-Q, 8-K)
- [ ] Crunchbase profile
- [ ] LinkedIn company page
- [ ] News search (last 12 months)
- [ ] Industry reports

### API Data Retrieved
"""
    
    config = load_config()
    if config.get('fmp_api_key'):
        report += "- [x] Financial Modeling Prep (profile, financials)\n"
    else:
        report += "- [ ] Financial Modeling Prep (API not configured)\n"
    
    if config.get('alpha_vantage_api_key'):
        report += "- [x] Alpha Vantage (stock data)\n"
    else:
        report += "- [ ] Alpha Vantage (API not configured)\n"
    
    report += """- [x] SEC EDGAR (filings - no API key needed)

### Manual Research Needed
- [ ] Leadership backgrounds (LinkedIn)
- [ ] Customer case studies (company website)
- [ ] Competitive analysis (industry sources)
- [ ] Recent news (news search)

---

*Report generated by Company Intelligence Skill*
*Last updated: """ + today + "*\n"
    
    return report


def main():
    parser = argparse.ArgumentParser(
        description="Generate comprehensive company intelligence report",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python full_report.py --company "Tesla" --ticker TSLA
    python full_report.py --company "OpenAI"
    python full_report.py --ticker AAPL --output report.md
        """
    )
    
    parser.add_argument('--company', '-c', help='Company name')
    parser.add_argument('--ticker', '-t', help='Stock ticker (for public companies)')
    parser.add_argument('--output', '-o', help='Output file path (default: stdout)')
    parser.add_argument('--fetch', '-f', action='store_true', 
                       help='Fetch live data from APIs (requires API keys)')
    
    args = parser.parse_args()
    
    if not args.company and not args.ticker:
        parser.error("Either --company or --ticker is required")
    
    company_name = args.company or args.ticker
    is_public = bool(args.ticker)
    
    profile = None
    financials = None
    
    # Fetch live data if requested
    if args.fetch and args.ticker:
        config = load_config()
        
        if config.get('fmp_api_key'):
            print("Fetching live data from APIs...", file=sys.stderr)
            
            # Import and use financial_data module
            try:
                from financial_data import FinancialModelingPrep
                
                api = FinancialModelingPrep(config['fmp_api_key'])
                
                print("  - Fetching company profile...", file=sys.stderr)
                profile = api.get_profile(args.ticker)
                
                print("  - Fetching quote...", file=sys.stderr)
                quote = api.get_quote(args.ticker)
                
                financials = {'quote': quote}
                
                if profile:
                    company_name = profile.get('companyName', company_name)
                    print(f"  - Found: {company_name}", file=sys.stderr)
                
            except Exception as e:
                print(f"  - Error fetching data: {e}", file=sys.stderr)
        else:
            print("Note: FMP API key not configured. Using template mode.", file=sys.stderr)
            print("Run 'python setup_apis.py' to configure APIs.", file=sys.stderr)
    
    # Generate report
    report = generate_report_template(
        company_name=company_name,
        ticker=args.ticker,
        profile=profile,
        financials=financials,
        is_public=is_public
    )
    
    # Output
    if args.output:
        output_path = Path(args.output)
        output_path.write_text(report, encoding='utf-8')
        print(f"Report saved to: {output_path}")
    else:
        print(report)


if __name__ == "__main__":
    main()
