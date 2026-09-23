import json


class Task:
    def __init__(self, title, description, status="pending"):
        self.title = title
        self.description = description
        self.status = status

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["description"], data["status"])

    def __str__(self):
        return f"{self.title} - {self.status}"


def save_tasks(tasks):
    data = []

    for task in tasks:
        data.append(task.to_dict())

    with open("tasks.json", "w") as file:
        json.dump(data, file, indent=4)


def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            data = json.load(file)

        tasks = []

        for item in data:
            tasks.append(Task.from_dict(item))

        return tasks

    except FileNotFoundError:
        return []


def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter description: ")

    if not title:
        print("Title cannot be empty.")
        return

    task = Task(title, description)
    tasks.append(task)

    print("Task added successfully.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def delete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))

        task = tasks.pop(number - 1)

        print(f"Deleted: {task.title}")

    except ValueError:
        print("Please enter a valid number.")

    except IndexError:
        print("Task number does not exist.")


# Load existing tasks
tasks = load_tasks()


# Main menu
while True:
    print("\n--- TASK MANAGER ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Save and exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        view_tasks(tasks)

    elif choice == "3":
        delete_task(tasks)

    elif choice == "4":
        save_tasks(tasks)
        print("Tasks saved. Goodbye!")
        break

    else:
        print("Invalid choice.")
