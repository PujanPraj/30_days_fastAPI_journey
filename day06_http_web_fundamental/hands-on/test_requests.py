import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url)
response.raise_for_status()

data = response.json()

print(data)
