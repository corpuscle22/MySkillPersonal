# API Setup Guide

This guide walks you through obtaining free API keys for the Company Intelligence skill.

## Quick Setup

Run the interactive setup script:
```bash
python scripts/setup_apis.py
```

This will guide you through each API registration.

---

## API Details

### 1. Financial Modeling Prep (FMP)

**What it provides:**
- Company profiles and descriptions
- Financial statements (income, balance sheet, cash flow)
- Key financial metrics and ratios
- Stock quotes and historical prices
- Company search functionality

**Free tier limits:**
- 250 API calls per day
- Access to most endpoints
- No credit card required

**Registration steps:**
1. Go to: https://site.financialmodelingprep.com/developer/docs
2. Click "Get my API KEY"
3. Create a free account (email required)
4. Your API key appears in your dashboard

**Example API call:**
```
https://financialmodelingprep.com/api/v3/profile/AAPL?apikey=YOUR_KEY
```

---

### 2. Alpha Vantage

**What it provides:**
- Stock quotes and historical data
- Technical indicators
- Company fundamentals (overview, income statement, balance sheet)
- Sector performance
- Forex and crypto data

**Free tier limits:**
- 25 API calls per day
- 500 calls per month (some endpoints)
- Access to all endpoints

**Registration steps:**
1. Go to: https://www.alphavantage.co/support/#api-key
2. Fill out the form with your email
3. Your API key is displayed immediately and emailed

**Example API call:**
```
https://www.alphavantage.co/query?function=OVERVIEW&symbol=AAPL&apikey=YOUR_KEY
```

---

### 3. OpenCorporates (Optional)

**What it provides:**
- Company registry data from 140+ jurisdictions
- Company incorporation details
- Officers and directors
- Filing history
- Parent/subsidiary relationships

**Free tier limits:**
- 500 API calls per month (with key)
- Basic access without key (rate limited)
- Access to public company data only

**Registration steps:**
1. Go to: https://opencorporates.com/api_accounts/new
2. Create a free account
3. Your API token appears in your account settings

**Note:** OpenCorporates works without an API key for basic queries, but registering increases your rate limits.

---

### 4. SEC EDGAR (No Key Required)

**What it provides:**
- All public company SEC filings
- 10-K annual reports
- 10-Q quarterly reports
- 8-K current reports
- Proxy statements
- S-1 registration statements

**Access:**
- Completely free, no registration required
- Only requires a User-Agent header identifying your application

**Example API call:**
```
https://data.sec.gov/submissions/CIK0000320193.json
```

---

## Configuration Storage

API keys are stored in:
```
~/.company-intelligence/config.json
```

Configuration format:
```json
{
  "fmp_api_key": "YOUR_FMP_KEY",
  "alpha_vantage_api_key": "YOUR_ALPHAVANTAGE_KEY",
  "opencorporates_api_key": "YOUR_OPENCORPORATES_KEY"
}
```

---

## Troubleshooting

### "API rate limit exceeded"
- Free tiers have daily limits
- Wait until the next day or upgrade to paid tier
- Combine multiple data sources to spread calls

### "Invalid API key"
- Double-check the key for typos
- Ensure the key is active (check provider dashboard)
- Re-run setup_apis.py to update

### "Connection refused" or timeout
- Check internet connection
- API service may be temporarily down
- Try again in a few minutes

---

## Recommended Usage Pattern

To maximize free tier usage:

1. **Use FMP as primary source** (250 calls/day) - most comprehensive
2. **Use SEC EDGAR freely** (unlimited) - authoritative for public companies
3. **Use Alpha Vantage for stock data** (25 calls/day) - real-time quotes
4. **Use OpenCorporates for registry data** (500 calls/month) - incorporation details

### Sample workflow for one company:
- 1 FMP call: Company profile
- 1 FMP call: Financial statements
- 1 SEC EDGAR call: Recent filings
- 1 Alpha Vantage call: Current quote
- **Total: 3 paid API calls + 1 free call**
