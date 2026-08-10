import requests

def get_data(url):
    try:
        response = requests.get(url)
        status = response.status_code

        print(f"Status: {status}")

        if status == 200:
            print("Request successful")
            return response.json()   # Mission 5 : retourner les données
        else:
            print("Request failed")
            return None

    except Exception as e:
        print("An error occurred while making the request.")
        print(f"Details: {e}")
        return None


def main():
    url = "https://api.github.com"
    data = get_data(url)

    if data is not None:
        print(f"API Info: {data['current_user_url']}")
    else:
        print("No data returned.")


if __name__ == "__main__":
    main()
