contact_book = {
    "Ram": {"phone": "9800000000", "email": "ram@gmail.com"},
    "Sita": {"phone": "9800000001", "email": "sita@gmail.com"},
    "Hari": {"phone": "9800000002", "email": "hari@gmail.com"},
}

for name, info in contact_book.items():
    print(f"Name : {name}")
    print(f"Phone : {info["phone"]}")
    print(f"Email : {info["email"]}")
    print()
