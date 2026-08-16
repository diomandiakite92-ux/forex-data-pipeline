import requests

def fetch_instrument_list():
    url = "https://freeserv.dukascopy.com/2.0/"
    
    params = {
        "path": "api/instrumentList"
    }

    try:
        response = requests.get(url, params=params)
        status = response.status_code
        print(f"Status: {status}")

        # 🟠 Cas 429 — Too Many Requests
        if status == 429:
            print("Rate limit exceeded (429). Please wait and retry.")
            return None

        # 🟠 Cas général d'erreur
        if status != 200:
            print("Request failed")
            return None

        # 🟢 Cas 200 — OK → on peut analyser le JSON
        data = response.json()

        # 1. Type de data
        print("\nType de data :", type(data))

        # 2. Si dict → afficher les clés
        if isinstance(data, dict):
            print("\nClés du dictionnaire :", data.keys())

        # 3. Si liste → afficher longueur + premier élément
        if isinstance(data, list):
            print("\nLongueur de la liste :", len(data))
            if len(data) > 0:
                print("\nPremier élément :")
                print(data[0])

        return data

    except Exception as e:
        print("An error occurred while making the request.")
        print(f"Details: {e}")
        return None


def main():
    fetch_instrument_list()


if __name__ == "__main__":
    main()
