
import requests
import time
from datetime import datetime

def get_crypto_prices():
    symbols = {
        'bitcoin': '₿',
        'ethereum': 'Ξ',
        'dogecoin': 'Ð'
    }
    
    try:
        response = requests.get(
            'https://api.coingecko.com/api/v3/simple/price',
            params={
                'ids': ','.join(symbols.keys()),
                'vs_currencies': 'usd',
                'include_market_cap': 'true',
                'include_24hr_change': 'true'
            }
        )
        data = response.json()
        
        print(f"\n{'🚀 Crypto Tracker':^50}")
        print(f"{'='*50}")
        
        for crypto, values in data.items():
            emoji = symbols[crypto]
            price = values['usd']
            change = values['usd_24h_change']
            change_color = '\033[92m' if change >=0 else '\033[91m'
            
            print(f"{emoji} {crypto.capitalize():<12}"
                  f"|\033[94m ${price:>9,.2f}\033[0m "
                  f"| 24h: {change_color}{change:>+6.2f}%\033[0m")
            
        print(f"\nLast update: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
    except Exception as e:
        print(f"🔴 Error fetching data: {e}")

if __name__ == "__main__":
    while True:
        get_crypto_prices()
        try:
            time.sleep(30)  # Update every 30 seconds
        except KeyboardInterrupt:
            print("\n👋 Exiting crypto tracker...")
            break
