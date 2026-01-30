---
name: ssd
description: Smart Stock Decider (SSD) - Detailed stock analysis and Buy/Hold/Sell recommendation based on real-time news, macro factors, and market trends. Use this skill when the user asks for a stock recommendation, analysis of a ticker, or specifically invokes "SSD".
---

# Smart Stock Decider (SSD)

## Overview

This skill performs an exhaustive analysis of a given stock ticker by aggregating real-time news, macro-economic factors, and company-specific events. It progressively searches for news (3h -> 24h), checks market status, and synthesizes data to provide an actionable Buy, Hold, or Sell recommendation.

**Goal:** Provide an immediate, actionable investment recommendation backed by thorough evidence.

## Prerequisites

- **Ticker Symbol**: The user must provide a stock ticker (e.g., AAPL, MSFT, TSLA). If not provided, ask for it.
- **Timezone**: Analysis uses US Central Time (CST).

## Workflow

Follow this specialized workflow to generate the report.

### Phase 1: Context & Market Status

1. **Establish Time & Status**:
   Run the helper script to get the official time and market status.
   ```bash
   python SSD/scripts/market_status.py
   ```
   *Note: This ensures all "last 3 hours" calculations are accurate to CST.*

2. **Identify Ticker**: Confirm the primary ticker symbol.

### Phase 2: News Aggregation (The "Crawl")

You must perform an elaborate and exhaustive search. Do not be lazy. Use multiple permutations of search queries.

**Step 2a: Recent News (Last 3 Hours)**
- Search Query: `"{TICKER} stock news"` (using tool filters for 'past 3 hours' if available, otherwise append "last 3 hours" to query text).
- Search Query: `"{TICKER} press release"`
- **Decision**: 
  - If < 5 relevant articles found, proceed to Step 2b immediately.
  - If relevant news found, read the content of top results.

**Step 2b: Expanded Search (6h - 24h)**
- Only if 2a yielded low results.
- Search Query: `"{TICKER} stock news last 12 hours"`
- Search Query: `"{TICKER} stock news today"`
- Search Query: `"{TICKER} latest financial news"`

**Step 2c: Source Coverage**
- Ensure you have scanned headlines from major networks (CNBC, Bloomberg, Reuters, WSJ, etc.). You don't need to visit every site, but your search results should reflect broad coverage.

### Phase 3: Macro & Sector Analysis

Search for external factors that could impact the stock regardless of company news.
- **Macro**: Search `"US jobs report today"`, `"Federal Reserve news today"`, `"global conflict news impact markets"`.
- **Sector**: Search `"{SECTOR} sector news today"` (e.g., "Tech sector news", "Oil prices today").

### Phase 4: Company Specifics

- **Earnings/Events**: Search `"{TICKER} earnings date"`, `"{TICKER} investor presentation"`.
- **Price & Trend**: Search `"{TICKER} stock price quote"`. Capture the **EXACT** current price to two decimal places (e.g., $145.32) and today's change (e.g., +$1.20). Do not use approximations (e.g., "around $145"). If the market is closed, get the "After Hours" price if available.

### Phase 5: Synthesis & Recommendation

Analyze all gathered text. Look for:
- **Catalysts**: Earnings beats, new products, regulatory approvals, insider buying.
- **Risks**: Lawsuits, downgrades, sector headwinds, macro fear.
- **Momentum**: Is the stock trending up or down today?

## Output Format

Present the final response in this format:

```markdown
# SSD Analysis: [TICKER]

**Recommendation: [BUY / HOLD / SELL]**
**Current Price:** $[EXACT PRICE] ([CHANGE])

## Rationale
[Brief, punchy explanation of the recommendation. Why this? Why now?]

## Key drivers
- **News (Last 3-24h)**: [Summary of critical news items]
- **Macro/Sector**: [Impact of wars, jobs, interest rates, etc.]
- **Company Events**: [Upcoming earnings, recent filings]
- **Trend**: [Current price action if valid]

## Evidence
[Bullet points of specific headlines or data points found]

*Analysis performed at [Current Time CST]*
```

## Rules of Engagement
1. **Be Decisive**: Do not strictly hedge. If the news is good, recommend BUY. If bad, SELL. If neutral/mixed, HOLD.
2. **Actionable**: The user wants to know what to do *now*.
3. **No Placeholders**: Do not say "Search results not found". Expand your search until you find relevant context.
4. **Safety**: Do not provide financial advice as a certified professional; provide it as a "Smart Stock Decider" persona based on data.
