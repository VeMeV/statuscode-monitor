import requests
import time
from datetime import datetime

def check_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True, "✅ File exists"
        elif response.status_code == 404:
            return False, "❌ File does not exist"
        else:
            return False, f"Unexpected status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return False, f"Error checking URL: {str(e)}"

def main():
    url = "https://www.google.com/robots.txt" # CHANGE THIS
    print(f"Starting monitoring: {url}")
    
    try:
        while True:
            exists, status = check_url(url)
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            status_symbol = "✓" if exists else "✗"
            print(f"[{current_time}] {status_symbol} {status}")
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nMonitoring stopped")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")

if __name__ == "__main__":
    main()
