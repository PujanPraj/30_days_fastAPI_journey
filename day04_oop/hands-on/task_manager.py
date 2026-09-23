class Task:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def mark_incomplete(self):
        self.completed = False

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.title} - {status}"

    def __repr__(self):
        return f"Task(title='{self.title}', description='{self.description}')"

    def __eq__(self, other):
        if not isinstance(other, Task):
            return False
        return self.title == other.title


class RecurringTask(Task):
    def __init__(self, title, description="", frequency="daily"):
        super().__init__(title, description)
        self.frequency = frequency

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.title} - {status} - Repeats: {self.frequency}"


class PriorityTask(Task):
    def __init__(self, title, description="", priority="Medium"):
        super().__init__(title, description)
        self.priority = priority

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.title} - {status} - Priority: {self.priority}"
