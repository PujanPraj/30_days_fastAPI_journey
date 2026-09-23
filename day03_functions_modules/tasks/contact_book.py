contact_book = {
    "Ram": {"phone": "9800000000", "email": "ram@gmail.com"},
    "Sita": {"phone": "9800000001", "email": "sita@gmail.com"},
    "Hari": {"phone": "9800000002", "email": "hari@gmail.com"},
}


def show_contact():
    for name, info in contact_book.items():
        print(f"Name : {name}")
        print(f"Phone : {info["phone"]}")
        print(f"Email : {info["email"]}")
        print()


def add_contact(name, phone, email):
    contact_book[name] = {"phone": phone, "email": email}


def remove_contact(name):
    if name in contact_book:
        del contact_book[name]
        print(f"{name} deleted")
    else:
        print("contact info not found")


def search_contact(name):
    if name in contact_book:
        info = contact_book.get(name)
        print(f"Name: {name}")
        print(f"Phone: {info["phone"]}")
        print(f"Email : {info["email"]}")
    else:
        print("Contact not found")
