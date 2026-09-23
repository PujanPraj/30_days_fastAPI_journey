# datetime
from datetime import datetime, date, timedelta

today = date.today()
now = datetime.now()

print(f"Today {today}")
print(f"Current time {now}")

tomorrow = today + timedelta(days=1)
print(f"Tomorrow {tomorrow}")

# random
import random

numbers = [10, 20, 30, 40, 50]
print(f"Random number : {random.choice(numbers)}")
print(f"Random integer : {random.randint(1, 100)}")


# json
import json

user = {"name": "Alice", "age": 25, "email": "alice@gmail.com"}

# Dictionary -> json
json_data = json.dumps(user, indent=4)
print(json_data)

# json -> dictionary
data = json.loads(json_data)
print(data["name"])
