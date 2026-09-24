import requests

api_key = "your api key"

url = "https://api.openweathermap.org/data/2.5/weather"
params = {"q": "Kathmandu", "appid": api_key, "units": "metric"}

try:
    response = requests.get(url, params)

    print(response.status_code)

    data = response.json()

    print(data)

except requests.exceptions.RequestException as e:
    print("Request failed: ", e)
