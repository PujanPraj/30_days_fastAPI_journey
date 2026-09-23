def create_user(name, age=18, city="KTM"):
    return f"Name: {name}, Age: {age}, City: {city}"


# positional arguments
print(create_user("Alice", 22, "BKT"))

# Keyword arguments
print(create_user(name="Bob", age=20, city="POK"))

# Default arguments
print(create_user("Charlie"))
