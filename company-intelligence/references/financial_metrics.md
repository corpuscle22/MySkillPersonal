# Financial Metrics Reference

Guide to understanding financial metrics and KPIs used in company analysis.

---

## Profitability Metrics

### Revenue (Sales)
Total income from business operations before any expenses are deducted.
- **Good sign**: Consistent year-over-year growth
- **Red flag**: Declining revenue or heavy dependence on single customer

### Gross Profit
Revenue minus Cost of Goods Sold (COGS).
```
Gross Profit = Revenue - COGS
```

### Gross Margin
Percentage of revenue retained after direct costs.
```
Gross Margin = (Gross Profit / Revenue) x 100
```
- **Software/SaaS**: 70-90% typical
- **Retail**: 20-40% typical
- **Manufacturing**: 25-45% typical

### Operating Income (EBIT)
Profit from core operations, excluding interest and taxes.
```
Operating Income = Revenue - COGS - Operating Expenses
```

### Operating Margin
```
Operating Margin = (Operating Income / Revenue) x 100
```
Shows efficiency of core operations.

### Net Income
Bottom line profit after all expenses, interest, and taxes.

### Net Margin
```
Net Margin = (Net Income / Revenue) x 100
```

### EBITDA
Earnings Before Interest, Taxes, Depreciation, and Amortization.
- Often used for comparing companies with different capital structures
- Popular in private equity valuations

---

## Valuation Metrics

### Market Capitalization
Total market value of company's outstanding shares.
```
Market Cap = Share Price x Shares Outstanding
```

**Size categories:**
- Mega cap: >$200B
- Large cap: $10B-$200B
- Mid cap: $2B-$10B
- Small cap: $300M-$2B
- Micro cap: <$300M

### Enterprise Value (EV)
Total company value including debt.
```
EV = Market Cap + Total Debt - Cash
```
More accurate for acquisitions and company comparisons.

### Price-to-Earnings (P/E) Ratio
```
P/E = Stock Price / Earnings Per Share
```
- **High P/E (>30)**: Growth expectations priced in
- **Low P/E (<15)**: May be undervalued or declining
- **Negative P/E**: Company is unprofitable

### Price-to-Sales (P/S) Ratio
```
P/S = Market Cap / Revenue
```
Useful for unprofitable growth companies.
- **SaaS companies**: 5-15x typical
- **Mature companies**: 1-3x typical

### Price-to-Book (P/B) Ratio
```
P/B = Stock Price / Book Value Per Share
```
- **P/B < 1**: Trading below asset value
- **P/B > 3**: Premium valuation

### EV/EBITDA
```
EV/EBITDA = Enterprise Value / EBITDA
```
Common multiple for M&A valuations.
- Average: 8-12x
- High growth: 15-25x
- Mature/declining: 4-8x

### EV/Revenue
```
EV/Revenue = Enterprise Value / Revenue
```
Used for unprofitable companies.

---

## Growth Metrics

### Revenue Growth Rate
```
Growth Rate = ((Current Revenue - Prior Revenue) / Prior Revenue) x 100
```
Year-over-year (YoY) most common.

### CAGR (Compound Annual Growth Rate)
```
CAGR = (End Value / Start Value)^(1/Years) - 1
```
Smoothed growth rate over multiple years.

### Customer/User Growth
- Monthly Active Users (MAU)
- Daily Active Users (DAU)
- Total customers/subscribers

### Employee Growth
Proxy for company growth, especially for private companies.

---

## Efficiency Metrics

### Return on Equity (ROE)
```
ROE = Net Income / Shareholders' Equity
```
How well company uses shareholder investment.
- **Good**: >15%
- **Excellent**: >20%

### Return on Assets (ROA)
```
ROA = Net Income / Total Assets
```
How efficiently company uses assets.
- **Good**: >5%

### Return on Invested Capital (ROIC)
```
ROIC = NOPAT / Invested Capital
```
True return on all capital invested.
- Compare to Weighted Average Cost of Capital (WACC)
- **ROIC > WACC**: Creating value

### Asset Turnover
```
Asset Turnover = Revenue / Total Assets
```
How efficiently assets generate revenue.

---

## Liquidity & Solvency

### Current Ratio
```
Current Ratio = Current Assets / Current Liabilities
```
Ability to pay short-term obligations.
- **Healthy**: 1.5-3.0
- **Concern**: <1.0

### Quick Ratio (Acid Test)
```
Quick Ratio = (Current Assets - Inventory) / Current Liabilities
```
More conservative liquidity measure.
- **Healthy**: >1.0

### Debt-to-Equity Ratio
```
D/E = Total Debt / Shareholders' Equity
```
Financial leverage indicator.
- **Low leverage**: <0.5
- **Moderate**: 0.5-1.5
- **High leverage**: >2.0

### Interest Coverage Ratio
```
Interest Coverage = EBIT / Interest Expense
```
Ability to service debt.
- **Safe**: >5
- **Concern**: <2

### Debt-to-EBITDA
```
Debt/EBITDA = Total Debt / EBITDA
```
Years to pay off debt.
- **Low risk**: <2x
- **Moderate**: 2-4x
- **High**: >5x

---

## Cash Flow Metrics

### Operating Cash Flow
Cash generated from core business operations.
- Should be positive for healthy companies
- More reliable than net income (harder to manipulate)

### Free Cash Flow (FCF)
```
FCF = Operating Cash Flow - Capital Expenditures
```
Cash available after maintaining/growing assets.
- Used for dividends, debt repayment, acquisitions

### FCF Margin
```
FCF Margin = Free Cash Flow / Revenue
```
Cash efficiency measure.

### Cash Conversion Cycle
Days to convert inventory to cash.
```
CCC = DIO + DSO - DPO
```
- DIO: Days Inventory Outstanding
- DSO: Days Sales Outstanding
- DPO: Days Payable Outstanding

---

## SaaS/Subscription Metrics

### Annual Recurring Revenue (ARR)
Normalized annual value of subscription contracts.

### Monthly Recurring Revenue (MRR)
Monthly subscription revenue.

### Customer Acquisition Cost (CAC)
```
CAC = Sales & Marketing Spend / New Customers Acquired
```

### Customer Lifetime Value (LTV)
```
LTV = Average Revenue Per User x Average Customer Lifespan
```

### LTV/CAC Ratio
```
LTV/CAC = Customer Lifetime Value / Customer Acquisition Cost
```
- **Healthy**: >3x
- **Great**: >5x

### Churn Rate
```
Churn = Customers Lost / Total Customers at Start
```
- **Good SaaS**: <5% annual
- **Excellent**: <2% annual

### Net Revenue Retention (NRR)
```
NRR = (Starting MRR + Expansion - Contraction - Churn) / Starting MRR
```
- **Good**: >100%
- **Excellent**: >120%

### Rule of 40
```
Revenue Growth Rate + Profit Margin >= 40%
```
Benchmark for healthy SaaS companies.

---

## Per-Share Metrics

### Earnings Per Share (EPS)
```
EPS = Net Income / Shares Outstanding
```

### Book Value Per Share
```
BVPS = Shareholders' Equity / Shares Outstanding
```

### Dividend Per Share
```
DPS = Total Dividends / Shares Outstanding
```

### Dividend Yield
```
Dividend Yield = Annual Dividend Per Share / Stock Price
```

### Payout Ratio
```
Payout Ratio = Dividends / Net Income
```
Percentage of earnings paid as dividends.

---

## Red Flags to Watch

### Financial Statement Red Flags
- Declining revenue with increasing receivables
- Growing gap between net income and operating cash flow
- Frequent "one-time" charges
- Aggressive revenue recognition
- Related party transactions
- Auditor changes

### Valuation Red Flags
- P/E much higher than industry peers
- Negative operating cash flow despite profitability
- Rapidly declining margins
- Heavy insider selling

### Growth Red Flags
- Growth primarily from acquisitions
- Declining customer retention
- Increasing customer acquisition costs
- Market saturation signs
