import os
import requests

def fetch_range(start_date, end_date):
    """
    Récupère une plage de données Twelve Data.
    Retourne la liste 'values' brute.
    """
    API_KEY = os.getenv("TWELVE_DATA_API_KEY")
    if not API_KEY:
        print("TWELVE_DATA_API_KEY is missing.")
        return []

    url = "https://api.twelvedata.com/time_series"
    headers = {
        "Authorization": f"apikey {API_KEY}"
    }

    params = {
        "symbol": "EUR/USD",
        "interval": "1h",
        "start_date": start_date,
        "end_date": end_date,
        "outputsize": 5000,
        "timezone": "UTC"
    }

    try:
        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=10
        )

        if response.status_code != 200:
            print(f"HTTP error: {response.status_code}")
            return []

        data = response.json()

        # Vérification d’erreur métier Twelve Data
        if data.get("status") == "error":
            print("API error:", data.get("message"))
            return []

        return data.get("values", [])

    except requests.RequestException as e:
        print("Network error:", e)
        return []


def fetch_eurusd_2025():
    """
    Retourne toutes les bougies disponibles pour l'année 2025.
    """

    # Première moitié : 01/01/2025 → 30/06/2025
    values_1 = fetch_range(
        "2025-01-01 00:00:00",
        "2025-06-30 23:59:59"
    )

    # Deuxième moitié : 01/07/2025 → 31/12/2025
    values_2 = fetch_range(
        "2025-07-01 00:00:00",
        "2025-12-31 23:59:59"
    )

    # Logs détaillés pour le mémoire
    print(f"Jan-Jun candles: {len(values_1)}")
    print(f"Jul-Dec candles: {len(values_2)}")

    # Fusion
    all_values = values_1 + values_2

    print(f"Historical candles received: {len(all_values)}")

    return {"values": all_values}
