class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")


class User(Person):
    def __init__(self, name, age, username, password):
        super().__init__(name, age)
        self.username = username
        self.__password = password

    def show_user(self):
        self.show_info()
        print(f"Username: {self.username}")

    # getter
    def get_password(self):
        return self.__password

    # setter
    def set_password(self, new_password):
        if len(new_password) >= 3:
            self.__password = new_password
            print("Password changed successfully")
        else:
            print("Password must be at least 8 characters.")


# create user
user1 = User("Ram", 22, "ram123", "ram123")
user1.show_user()

print("Password", user1.get_password())
user1.set_password("ram12345")
print("New Password : ", user1.get_password())
