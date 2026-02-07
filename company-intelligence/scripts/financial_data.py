#!/usr/bin/env python3
"""
Financial Data Fetcher

Fetches financial data using Financial Modeling Prep and Alpha Vantage APIs.
Requires API keys - run setup_apis.py first.

Usage:
    python financial_data.py --ticker AAPL
    python financial_data.py --ticker TSLA --metrics
    python financial_data.py --ticker MSFT --income-statement
"""

import argparse
import json
import sys
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError


# Configuration
CONFIG_FILE = Path.home() / ".company-intelligence" / "config.json"

FMP_BASE_URL = "https://financialmodelingprep.com/api/v3"
ALPHA_VANTAGE_URL = "https://www.alphavantage.co/query"


def load_config():
    """Load API configuration."""
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {}


def fetch_json(url: str) -> dict:
    """Fetch JSON data from URL."""
    try:
        req = Request(url, headers={"User-Agent": "CompanyIntelligence/1.0"})
        with urlopen(req, timeout=30) as response:
            return json.loads(response.read())
    except HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
        return None
    except URLError as e:
        print(f"URL Error: {e}")
        return None
    except json.JSONDecodeError:
        print("Error: Invalid JSON response")
        return None


class FinancialModelingPrep:
    """Financial Modeling Prep API wrapper."""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = FMP_BASE_URL
    
    def get_profile(self, ticker: str) -> dict:
        """Get company profile."""
        url = f"{self.base_url}/profile/{ticker}?apikey={self.api_key}"
        data = fetch_json(url)
        return data[0] if data and isinstance(data, list) else data
    
    def get_quote(self, ticker: str) -> dict:
        """Get current stock quote."""
        url = f"{self.base_url}/quote/{ticker}?apikey={self.api_key}"
        data = fetch_json(url)
        return data[0] if data and isinstance(data, list) else data
    
    def get_key_metrics(self, ticker: str, period: str = "annual") -> list:
        """Get key financial metrics."""
        url = f"{self.base_url}/key-metrics/{ticker}?period={period}&limit=5&apikey={self.api_key}"
        return fetch_json(url)
    
    def get_income_statement(self, ticker: str, period: str = "annual") -> list:
        """Get income statement."""
        url = f"{self.base_url}/income-statement/{ticker}?period={period}&limit=5&apikey={self.api_key}"
        return fetch_json(url)
    
    def get_balance_sheet(self, ticker: str, period: str = "annual") -> list:
        """Get balance sheet."""
        url = f"{self.base_url}/balance-sheet-statement/{ticker}?period={period}&limit=5&apikey={self.api_key}"
        return fetch_json(url)
    
    def get_cash_flow(self, ticker: str, period: str = "annual") -> list:
        """Get cash flow statement."""
        url = f"{self.base_url}/cash-flow-statement/{ticker}?period={period}&limit=5&apikey={self.api_key}"
        return fetch_json(url)
    
    def get_ratios(self, ticker: str) -> list:
        """Get financial ratios."""
        url = f"{self.base_url}/ratios/{ticker}?limit=5&apikey={self.api_key}"
        return fetch_json(url)
    
    def get_enterprise_value(self, ticker: str) -> list:
        """Get enterprise value metrics."""
        url = f"{self.base_url}/enterprise-values/{ticker}?limit=5&apikey={self.api_key}"
        return fetch_json(url)


class AlphaVantage:
    """Alpha Vantage API wrapper."""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = ALPHA_VANTAGE_URL
    
    def get_overview(self, ticker: str) -> dict:
        """Get company overview."""
        url = f"{self.base_url}?function=OVERVIEW&symbol={ticker}&apikey={self.api_key}"
        return fetch_json(url)
    
    def get_income_statement(self, ticker: str) -> dict:
        """Get income statement."""
        url = f"{self.base_url}?function=INCOME_STATEMENT&symbol={ticker}&apikey={self.api_key}"
        return fetch_json(url)
    
    def get_balance_sheet(self, ticker: str) -> dict:
        """Get balance sheet."""
        url = f"{self.base_url}?function=BALANCE_SHEET&symbol={ticker}&apikey={self.api_key}"
        return fetch_json(url)
    
    def get_cash_flow(self, ticker: str) -> dict:
        """Get cash flow statement."""
        url = f"{self.base_url}?function=CASH_FLOW&symbol={ticker}&apikey={self.api_key}"
        return fetch_json(url)
    
    def get_quote(self, ticker: str) -> dict:
        """Get current quote."""
        url = f"{self.base_url}?function=GLOBAL_QUOTE&symbol={ticker}&apikey={self.api_key}"
        return fetch_json(url)


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


def format_percent(value):
    """Format value as percentage."""
    if value is None:
        return "N/A"
    try:
        return f"{float(value) * 100:.2f}%"
    except (ValueError, TypeError):
        return str(value)


def display_company_profile(profile: dict):
    """Display company profile."""
    print("\n" + "=" * 70)
    print("COMPANY PROFILE")
    print("=" * 70)
    
    fields = [
        ('Company Name', 'companyName'),
        ('Symbol', 'symbol'),
        ('Exchange', 'exchangeShortName'),
        ('Industry', 'industry'),
        ('Sector', 'sector'),
        ('CEO', 'ceo'),
        ('Employees', 'fullTimeEmployees'),
        ('Headquarters', 'city'),
        ('Country', 'country'),
        ('Website', 'website'),
        ('IPO Date', 'ipoDate'),
    ]
    
    for label, key in fields:
        value = profile.get(key, 'N/A')
        if key == 'fullTimeEmployees' and value != 'N/A':
            value = f"{int(value):,}"
        print(f"{label}: {value}")
    
    print(f"\nDescription: {profile.get('description', 'N/A')[:500]}...")


def display_quote(quote: dict):
    """Display current stock quote."""
    print("\n" + "=" * 70)
    print("CURRENT QUOTE")
    print("=" * 70)
    
    print(f"Price: ${quote.get('price', 'N/A')}")
    print(f"Change: {quote.get('change', 'N/A')} ({quote.get('changesPercentage', 'N/A')}%)")
    print(f"Day Range: ${quote.get('dayLow', 'N/A')} - ${quote.get('dayHigh', 'N/A')}")
    print(f"52 Week Range: ${quote.get('yearLow', 'N/A')} - ${quote.get('yearHigh', 'N/A')}")
    print(f"Market Cap: {format_currency(quote.get('marketCap'))}")
    print(f"Volume: {quote.get('volume', 'N/A'):,}" if quote.get('volume') else "Volume: N/A")
    print(f"Avg Volume: {quote.get('avgVolume', 'N/A'):,}" if quote.get('avgVolume') else "Avg Volume: N/A")
    print(f"P/E Ratio: {quote.get('pe', 'N/A')}")
    print(f"EPS: ${quote.get('eps', 'N/A')}")


def display_key_metrics(metrics: list):
    """Display key financial metrics."""
    if not metrics:
        print("\nNo metrics data available.")
        return
    
    print("\n" + "=" * 70)
    print("KEY FINANCIAL METRICS (Last 5 Years)")
    print("=" * 70)
    
    # Show header
    years = [m.get('date', 'N/A')[:4] for m in metrics[:5]]
    print(f"{'Metric':<30} | " + " | ".join(f"{y:>12}" for y in years))
    print("-" * 100)
    
    # Key metrics to display
    metric_labels = [
        ('revenuePerShare', 'Revenue Per Share'),
        ('netIncomePerShare', 'Net Income Per Share'),
        ('operatingCashFlowPerShare', 'Op. Cash Flow/Share'),
        ('freeCashFlowPerShare', 'Free Cash Flow/Share'),
        ('bookValuePerShare', 'Book Value/Share'),
        ('peRatio', 'P/E Ratio'),
        ('priceToBookRatio', 'P/B Ratio'),
        ('debtToEquity', 'Debt to Equity'),
        ('currentRatio', 'Current Ratio'),
        ('roe', 'Return on Equity'),
        ('roic', 'Return on Invested Capital'),
    ]
    
    for key, label in metric_labels:
        values = []
        for m in metrics[:5]:
            val = m.get(key)
            if val is not None:
                if 'Ratio' in label or key in ['debtToEquity', 'currentRatio']:
                    values.append(f"{float(val):.2f}")
                elif key in ['roe', 'roic']:
                    values.append(f"{float(val)*100:.1f}%")
                else:
                    values.append(f"${float(val):.2f}")
            else:
                values.append("N/A")
        print(f"{label:<30} | " + " | ".join(f"{v:>12}" for v in values))


def display_income_statement(statements: list):
    """Display income statement summary."""
    if not statements:
        print("\nNo income statement data available.")
        return
    
    print("\n" + "=" * 70)
    print("INCOME STATEMENT (Last 5 Years)")
    print("=" * 70)
    
    years = [s.get('date', 'N/A')[:4] for s in statements[:5]]
    print(f"{'Item':<25} | " + " | ".join(f"{y:>14}" for y in years))
    print("-" * 105)
    
    items = [
        ('revenue', 'Revenue'),
        ('costOfRevenue', 'Cost of Revenue'),
        ('grossProfit', 'Gross Profit'),
        ('operatingExpenses', 'Operating Expenses'),
        ('operatingIncome', 'Operating Income'),
        ('netIncome', 'Net Income'),
        ('eps', 'EPS'),
    ]
    
    for key, label in items:
        values = []
        for s in statements[:5]:
            val = s.get(key)
            if val is not None:
                if key == 'eps':
                    values.append(f"${float(val):.2f}")
                else:
                    values.append(format_currency(val))
            else:
                values.append("N/A")
        print(f"{label:<25} | " + " | ".join(f"{v:>14}" for v in values))


def main():
    parser = argparse.ArgumentParser(
        description="Fetch financial data for a public company",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python financial_data.py --ticker AAPL
    python financial_data.py --ticker TSLA --metrics
    python financial_data.py --ticker MSFT --income-statement
    python financial_data.py --ticker GOOGL --all --json
        """
    )
    
    parser.add_argument('--ticker', '-t', required=True, help='Stock ticker symbol')
    parser.add_argument('--profile', '-p', action='store_true', help='Show company profile')
    parser.add_argument('--quote', '-q', action='store_true', help='Show current quote')
    parser.add_argument('--metrics', '-m', action='store_true', help='Show key metrics')
    parser.add_argument('--income-statement', '-i', action='store_true', help='Show income statement')
    parser.add_argument('--all', '-a', action='store_true', help='Show all available data')
    parser.add_argument('--json', '-j', action='store_true', help='Output as JSON')
    parser.add_argument('--source', '-s', choices=['fmp', 'alphavantage'], default='fmp',
                       help='Data source (default: fmp)')
    
    args = parser.parse_args()
    
    # Default to showing all if nothing specified
    if not any([args.profile, args.quote, args.metrics, args.income_statement, args.all]):
        args.all = True
    
    if args.all:
        args.profile = args.quote = args.metrics = args.income_statement = True
    
    # Load configuration
    config = load_config()
    
    # Check for API key
    if args.source == 'fmp':
        api_key = config.get('fmp_api_key')
        if not api_key:
            print("Error: Financial Modeling Prep API key not configured.")
            print("Run 'python setup_apis.py' to configure API keys.")
            sys.exit(1)
        api = FinancialModelingPrep(api_key)
    else:
        api_key = config.get('alpha_vantage_api_key')
        if not api_key:
            print("Error: Alpha Vantage API key not configured.")
            print("Run 'python setup_apis.py' to configure API keys.")
            sys.exit(1)
        api = AlphaVantage(api_key)
    
    ticker = args.ticker.upper()
    print(f"Fetching financial data for: {ticker}")
    
    if args.source == 'fmp':
        results = {}
        
        if args.profile:
            print("Fetching company profile...")
            results['profile'] = api.get_profile(ticker)
        
        if args.quote:
            print("Fetching quote...")
            results['quote'] = api.get_quote(ticker)
        
        if args.metrics:
            print("Fetching key metrics...")
            results['metrics'] = api.get_key_metrics(ticker)
        
        if args.income_statement:
            print("Fetching income statement...")
            results['income_statement'] = api.get_income_statement(ticker)
        
        if args.json:
            print(json.dumps(results, indent=2))
        else:
            if results.get('profile'):
                display_company_profile(results['profile'])
            if results.get('quote'):
                display_quote(results['quote'])
            if results.get('metrics'):
                display_key_metrics(results['metrics'])
            if results.get('income_statement'):
                display_income_statement(results['income_statement'])
    else:
        # Alpha Vantage
        if args.profile:
            overview = api.get_overview(ticker)
            if args.json:
                print(json.dumps(overview, indent=2))
            else:
                print(f"\nCompany: {overview.get('Name')}")
                print(f"Industry: {overview.get('Industry')}")
                print(f"Sector: {overview.get('Sector')}")
                print(f"Market Cap: {format_currency(overview.get('MarketCapitalization'))}")
                print(f"P/E Ratio: {overview.get('PERatio')}")
                print(f"EPS: ${overview.get('EPS')}")
                print(f"Dividend Yield: {overview.get('DividendYield')}")


if __name__ == "__main__":
    main()
