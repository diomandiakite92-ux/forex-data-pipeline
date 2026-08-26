import os
import requests

def fetch_eurusd():
    API_KEY = os.getenv("TWELVE_DATA_API_KEY")

    if not API_KEY:
        print("TWELVE_DATA_API_KEY is missing.")
        return None

    url = "https://api.twelvedata.com/time_series"
    headers = {
        "Authorization": f"apikey {API_KEY}"
    }

    params = {
        "symbol": "EUR/USD",
        "interval": "1h",
        "outputsize": 10,
        "timezone": "utc"
    }

    try:
        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=10
        )

        if response.status_code != 200:
            print(f"Request failed: {response.status_code}")
            return None

        data = response.json()
        return data

    except requests.RequestException as e:
        print("Network error:", e)
        return None
