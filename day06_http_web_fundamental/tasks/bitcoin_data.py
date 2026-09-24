import requests
import json


def get_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {"ids": "bitcoin", "vs_currencies": "usd,eur"}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()

        with open("bitcoin.json", "w") as file:
            json.dump(data, file, indent=4)

        usd_price = data["bitcoin"]["usd"]
        eur_price = data["bitcoin"]["eur"]

        print("\nBitcoin Price")
        print("----------------")
        print(f"USD: ${usd_price}")
        print(f"EUR: €{eur_price}")

    except requests.exceptions.RequestException as e:
        print("API request failed:", e)


get_bitcoin_price()
