
import datetime
import json
import pytz

def check_market_status():
    # US Central Time (CST/CDT)
    cst = pytz.timezone('US/Central')
    now = datetime.datetime.now(cst)
    
    # Market Hours (CST): 8:30 AM - 3:00 PM
    market_open = now.replace(hour=8, minute=30, second=0, microsecond=0)
    market_close = now.replace(hour=15, minute=0, second=0, microsecond=0)
    
    is_weekday = now.weekday() < 5 # 0-4 is Mon-Fri
    is_open = is_weekday and (market_open <= now <= market_close)
    
    status = {
        "current_time_cst": now.strftime("%Y-%m-%d %H:%M:%S %Z"),
        "is_market_open": is_open,
        "is_weekday": is_weekday,
        "message": "Market is OPEN" if is_open else "Market is CLOSED"
    }
    
    print(json.dumps(status, indent=2))

if __name__ == "__main__":
    try:
        check_market_status()
    except Exception as e:
        # Fallback if pytz not installed
        print(json.dumps({"error": str(e), "note": "Ensure pytz is installed or use standard lib"}))
