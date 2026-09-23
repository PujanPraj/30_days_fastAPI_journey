class Task:
    def __init__(self, title, description, status="pending"):
        self.title = title
        self.description = description
        self.status = status

    def show_task(self):
        print(f"Title : {self.title}")
        print(f"Description : {self.description}")
        print(f"Status : {self.status}")


task1 = Task("Learn Python", "Study OOP concepts")

task1.show_task()
