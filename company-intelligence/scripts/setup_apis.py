#!/usr/bin/env python3
"""
API Setup Script for Company Intelligence Skill

This script guides users through obtaining and configuring free API keys
for the company intelligence data sources.
"""

import json
import os
from pathlib import Path

# Configuration directory
CONFIG_DIR = Path.home() / ".company-intelligence"
CONFIG_FILE = CONFIG_DIR / "config.json"


def get_existing_config():
    """Load existing configuration if it exists."""
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {}


def save_config(config):
    """Save configuration to file."""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=2)
    print(f"\nConfiguration saved to: {CONFIG_FILE}")


def setup_alpha_vantage(config):
    """Guide user through Alpha Vantage API setup."""
    print("\n" + "=" * 60)
    print("ALPHA VANTAGE API SETUP")
    print("=" * 60)
    print("\nAlpha Vantage provides free stock data, financials, and more.")
    print("Free tier: 25 API calls per day")
    print("\nTo get your free API key:")
    print("1. Go to: https://www.alphavantage.co/support/#api-key")
    print("2. Fill out the form (email required)")
    print("3. Copy your API key")
    
    current_key = config.get('alpha_vantage_api_key', '')
    if current_key:
        print(f"\nCurrent key: {current_key[:8]}...")
        update = input("Update this key? (y/N): ").strip().lower()
        if update != 'y':
            return config
    
    api_key = input("\nEnter your Alpha Vantage API key (or press Enter to skip): ").strip()
    if api_key:
        config['alpha_vantage_api_key'] = api_key
        print("Alpha Vantage API key saved!")
    
    return config


def setup_fmp(config):
    """Guide user through Financial Modeling Prep API setup."""
    print("\n" + "=" * 60)
    print("FINANCIAL MODELING PREP API SETUP")
    print("=" * 60)
    print("\nFinancial Modeling Prep provides company profiles, financials,")
    print("stock data, and more.")
    print("Free tier: 250 API calls per day")
    print("\nTo get your free API key:")
    print("1. Go to: https://site.financialmodelingprep.com/developer/docs")
    print("2. Click 'Get my API KEY' and create a free account")
    print("3. Your API key will be shown in your dashboard")
    
    current_key = config.get('fmp_api_key', '')
    if current_key:
        print(f"\nCurrent key: {current_key[:8]}...")
        update = input("Update this key? (y/N): ").strip().lower()
        if update != 'y':
            return config
    
    api_key = input("\nEnter your FMP API key (or press Enter to skip): ").strip()
    if api_key:
        config['fmp_api_key'] = api_key
        print("Financial Modeling Prep API key saved!")
    
    return config


def setup_opencorporates(config):
    """Guide user through OpenCorporates API setup."""
    print("\n" + "=" * 60)
    print("OPENCORPORATES API SETUP (Optional)")
    print("=" * 60)
    print("\nOpenCorporates provides company registry data from around the world.")
    print("Free tier: 500 API calls per month (no key required for basic access)")
    print("\nFor higher limits, you can register for an API key:")
    print("1. Go to: https://opencorporates.com/api_accounts/new")
    print("2. Create a free account")
    print("3. Copy your API token")
    
    current_key = config.get('opencorporates_api_key', '')
    if current_key:
        print(f"\nCurrent key: {current_key[:8]}...")
        update = input("Update this key? (y/N): ").strip().lower()
        if update != 'y':
            return config
    
    api_key = input("\nEnter your OpenCorporates API key (or press Enter to skip): ").strip()
    if api_key:
        config['opencorporates_api_key'] = api_key
        print("OpenCorporates API key saved!")
    
    return config


def verify_config(config):
    """Display current configuration status."""
    print("\n" + "=" * 60)
    print("CONFIGURATION STATUS")
    print("=" * 60)
    
    apis = [
        ('alpha_vantage_api_key', 'Alpha Vantage', 'Stock data, financials'),
        ('fmp_api_key', 'Financial Modeling Prep', 'Company profiles, financials'),
        ('opencorporates_api_key', 'OpenCorporates', 'Company registry data'),
    ]
    
    for key, name, description in apis:
        status = "Configured" if config.get(key) else "Not configured"
        icon = "[OK]" if config.get(key) else "[--]"
        print(f"{icon} {name}: {status}")
        print(f"    {description}")
    
    print("\nNote: SEC EDGAR requires no API key (free public access)")


def main():
    print("=" * 60)
    print("COMPANY INTELLIGENCE - API SETUP")
    print("=" * 60)
    print("\nThis script will help you configure free API keys for")
    print("gathering company intelligence data.")
    print("\nAll APIs have free tiers - no credit card required!")
    
    config = get_existing_config()
    
    # Setup each API
    config = setup_alpha_vantage(config)
    config = setup_fmp(config)
    config = setup_opencorporates(config)
    
    # Save and verify
    save_config(config)
    verify_config(config)
    
    print("\n" + "=" * 60)
    print("Setup complete! You can now use the company intelligence scripts.")
    print("Run 'python scripts/full_report.py --company \"Company Name\"' to start.")
    print("=" * 60)


if __name__ == "__main__":
    main()
