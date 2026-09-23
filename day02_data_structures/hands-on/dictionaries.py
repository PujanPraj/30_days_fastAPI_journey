# A dict maps keys to values - unordered before python 3.7, insertion-ordered since 

contacts = {
    "Ram": {
        "phone": "9800000001",
        "email": "ram@gmail.com"
    },
    "Sita": {
        "phone": "9800000002",
        "email": "sita@gmail.com"
    }
}

# add 
contacts["Hari"] = {
    "phone": "9800000003",
    "email": "hari@gmail.com"
}

# access
print(contacts)

print("--------------------------------------------------")

print(f"Contact of Ram is : { contacts["Ram"]["phone"] }")

print("--------------------------------------------------")

# safe access (avoids KeyError)
print(contacts.get("Gita", "Not found"))

print("--------------------------------------------------")

# check existence
if "Sita" in contacts:
    print("Sita exists")

print("--------------------------------------------------")

# delete
del contacts["Hari"]
print(contacts)

print("--------------------------------------------------")

# iterate
for name, info in contacts.items():
    print(f"{name}: {info["phone"]}")

print("--------------------------------------------------")

# keys/values only
print(list(contacts.keys()))
print(list(contacts.values()))
