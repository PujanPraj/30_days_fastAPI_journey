import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_post():
    post_id = input("Enter the post id : ")

    try:
        response = requests.get(f"{BASE_URL}/posts/{post_id}")
        data = response.json()
        print(data)
    except requests.exceptions.RequestException as e:
        print("Request failed : ", e)


def main():
    while True:
        print("\n---POST CLIENT")
        print("1. Get Post")
        print("2. Exit")

        choice = input("Choose: ")

        if choice == "1":
            get_post()
        elif choice == "2":
            break
        else:
            print("Invalid choice")


main()
