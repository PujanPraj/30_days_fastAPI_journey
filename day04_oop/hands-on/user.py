class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def show_tasks(self):
        print(f"\nTask for {self.name} : ")
        if not self.tasks:
            print("No tasks")
            return

        for task in self.tasks:
            print(task)

    def __str__(self):
        return f"User: {self.name} ({self.email})"
