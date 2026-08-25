import os
import requests

def fetch_eurusd():
    API_KEY = os.getenv("TWELVE_DATA_API_KEY")

    if not API_KEY:
        print("TWELVE_DATA_API_KEY is missing.")
        return

    url = "https://api.twelvedata.com/time_series"

    headers = {
        "Authorization": f"apikey {API_KEY}"
    }

    params = {
        "symbol": "EUR/USD",
        "interval": "1h",
        "outputsize": 10
    }

    try:
        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=10
        )

        status = response.status_code
        print(f"Status: {status}")

        if status != 200:
            print("Request failed")
            return None

        data = response.json()

        print("\n=== Structure JSON ===")
        print("Type :", type(data))
        print("Clés :", data.keys())

        print("\n=== Premier élément des bougies ===")
        if "values" in data:
            print(data["values"][0])

        return data

    except Exception as e:
        print("Erreur lors de la requête.")
        print(f"Détails : {e}")
        return None


def main():
    fetch_eurusd()


if __name__ == "__main__":
    main()
