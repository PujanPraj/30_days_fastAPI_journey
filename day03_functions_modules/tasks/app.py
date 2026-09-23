import contact_book
import operation


def contact_menu():
    while True:
        print("\n========= CONTACT BOOK ==============")
        print("1. Show contact")
        print("2. Add contact")
        print("3. Remove contact")
        print("4. Search contact")
        print("5. Back")

        choice = input("Enter a choice : ")
        match choice:
            case "1":
                contact_book.show_contact()

            case "2":
                name = input("Enter name : ")
                phone = input("Enter phone : ")
                email = input("Enter email : ")
                contact_book.add_contact(name, phone, email)
                print("Contact added successfully")

            case "3":
                name = input("Enter name to remove : ")
                contact_book.remove_contact(name)

            case "4":
                name = input("Enter name to search : ")
                contact_book.search_contact(name)

            case "5":
                break

            case _:
                print("Invalid choice.")


def math_operation_menu():
    while True:
        print("\n=========== MATH OPERATION ================")
        print("1. Add")
        print("2. Subtract")
        print("3. Back")

        choice = input("Enter your choice : ")

        a = float(input("Enter first number : "))
        b = float(input("Enter second number : "))

        match choice:
            case "1":
                sum = operation.add(a, b)
                print(f"{a} + {b} = {sum}")

            case "2":
                sub = operation.sub(a, b)
                print(f"{a} - {b} = {sub}")

            case "3":
                break

            case _:
                print("Invalid choice")


def main():
    while True:
        print("\n============= MAIN MENU ===============")
        print("1. Contact Book")
        print("2. Math Operation")
        print("3. Exit")

        choice = input("Enter your choice : ")
        match choice:
            case "1":
                contact_menu()

            case "2":
                math_operation_menu()

            case "3":
                print("Goodbye!")
                break

            case _:
                print("Invalid ")


main()
