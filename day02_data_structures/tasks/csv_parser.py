import csv
from io import StringIO

csv_data = """name,age,email
Alice,25,alice@example.com
Bob,30,bob@example.com
Charlie,28,charlie@example.com
"""

data = list(csv.DictReader(StringIO(csv_data)))
print(data)
