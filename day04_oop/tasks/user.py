class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")


class User(Person):
    def __init__(self, name, age, username):
        super().__init__(name, age)
        self.username = username

    def show_user(self):
        self.show_info()
        print(f"Username : {self.username}")


user1 = User("Ram", 22, "ram123")
user1.show_user()
