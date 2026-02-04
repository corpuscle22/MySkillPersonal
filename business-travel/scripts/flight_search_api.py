
import os
import sys
import json
import argparse
from datetime import datetime, timedelta
import concurrent.futures

print("DEBUG: Script started.")

# Load Config
try:
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    if os.path.exists(config_path):
        print(f"DEBUG: Found config at {config_path}")
        with open(config_path, 'r') as f:
            config = json.load(f)
            os.environ["AMADEUS_API_KEY"] = config.get("AMADEUS_API_KEY", "")
            os.environ["AMADEUS_API_SECRET"] = config.get("AMADEUS_API_SECRET", "")
    else:
        print("DEBUG: Config not found.")
except Exception as e:
    print(f"DEBUG: Config error: {e}")

try:
    from amadeus import Client, ResponseError
    print("DEBUG: Amadeus imported.")
except ImportError:
    print("ERROR: Amadeus not installed.")
    sys.exit(1)

def search_single_date(client, origin, destination, date, cabin, airline, via=None):
    # print(f"Scanning {date} via {via or 'Direct'}...")
    try:
        kwargs = {
            'originLocationCode': origin,
            'destinationLocationCode': destination,
            'departureDate': date,
            'returnDate': (datetime.strptime(date, "%Y-%m-%d") + timedelta(days=14)).strftime("%Y-%m-%d"),
            'adults': 1,
            'travelClass': cabin.upper(),
            'currencyCode': 'USD',
            'max': 50
        }
        
        if via:
            kwargs['includedConnectionPoints'] = via

        response = client.shopping.flight_offers_search.get(**kwargs)
        if not response.data:
            return []
            
        results = []
        for f in response.data:
            # Post-filter: Check entire itinerary for the airline
            itineraries = f['itineraries'][0]['segments']
            carriers = [s['carrierCode'] for s in itineraries]
            
            # If airline target is set, ensure it exists in the chain
            if airline and airline not in carriers:
                continue
                
            filtered_airline_str = f"{carriers[0]} (via {','.join(carriers[1:])})" if len(carriers)>1 else carriers[0]
            
            results.append({
                'price': float(f['price']['total']),
                'airline': filtered_airline_str,
                'date': date,
                'stops': len(itineraries) - 1,
                'via': via
            })
        return results
    except Exception as e:
        # print(f"Err {date}: {e}")
        return []

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--origin", default="DFW")
    parser.add_argument("--destination", required=True)
    parser.add_argument("--month", required=True)
    parser.add_argument("--airline")
    parser.add_argument("--cabin", default="BUSINESS")
    args = parser.parse_args()

    print(f"DEBUG: Main Args: {args}")

    api_key = os.environ.get("AMADEUS_API_KEY")
    api_secret = os.environ.get("AMADEUS_API_SECRET")

    if not api_key or not api_secret:
        print("ERROR: Missing Keys.")
        return

    amadeus = Client(client_id=api_key, client_secret=api_secret)
    print("DEBUG: Client init success.")

    start_date = datetime.strptime(args.month, "%Y-%m")
    # End of month logic
    if start_date.month == 12:
        end_date = datetime(start_date.year + 1, 1, 1) - timedelta(days=1)
    else:
        end_date = datetime(start_date.year, start_date.month + 1, 1) - timedelta(days=1)

    dates = []
    curr = start_date
    while curr <= end_date:
        dates.append(curr.strftime("%Y-%m-%d"))
        curr += timedelta(days=1)

    print(f"Scanning {len(dates)} days in {args.month} for {args.airline or 'ANY'}...")
    
    # Define Gateways to check (Smart Routing)
    gateways = [None] # Always check default/direct first
    if args.airline == 'EY':
        gateways.extend(['JFK', 'ORD', 'BOS', 'IAD', 'CLT']) # Add user requested gateways
    elif args.airline == 'QR':
        gateways.extend(['JFK', 'ORD', 'IAH', 'BOS', 'PHL'])
    elif args.airline == 'EK':
        gateways.extend(['JFK', 'ORD', 'BOS', 'IAH', 'IAD'])
        
    print(f"DEBUG: Checking gateways: {gateways}")

    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for d in dates:
            for g in gateways:
                futures.append(executor.submit(search_single_date, amadeus, args.origin, args.destination, d, args.cabin, args.airline, g))
                
        for future in concurrent.futures.as_completed(futures):
            res = future.result()
            if res:
                results.extend(res)
            # print(".", end="", flush=True)

    if not results:
        print("No flights found.")
        return

    results.sort(key=lambda x: x['price'])
    
    print(f"\nTop 10 Deals for {args.airline or 'ANY'} in {args.month}:")
    
    seen = set()
    count = 0 
    for r in results:
        # Dedupe
        key = f"{r['price']}-{r['date']}"
        if key in seen: continue
        seen.add(key)
        
        via_str = f" via {r.get('via')}" if r.get('via') else " (Direct routing from DFW)"
        print(f"${r['price']:<10} | {r['date']:<12} | {r['airline']:<20} | {r['stops']} stops | Routing:{via_str}")
        count += 1
        if count >= 10: break

if __name__ == "__main__":
    main()
