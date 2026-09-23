from user import User
from task_manager import Task, RecurringTask, PriorityTask

# create a user
user1 = User("Ram", "ram@gmail.com")

# create normal task
task1 = Task("Learn FastAPI", "Study OOP")

# create recurring task
task2 = RecurringTask("Exericse", "Exercise for 30 min", "daily")
#
# create priority task
task3 = PriorityTask("Complete Project", "Finish Python Project", "High")

# add tasks to user
user1.add_task(task1)
user1.add_task(task2)
user1.add_task(task3)

# Display user
print(user1)

# display tasks
user1.show_tasks()

# complete a task
task1.mark_complete()

print("\nAfter completing task:")
user1.show_tasks()

# test __repr__
print("\nRepr:")
print(repr(task1))

# test __eq__
task4 = Task("Learn FastAPI")

print("\nEquality:")
print(task1 == task4)
