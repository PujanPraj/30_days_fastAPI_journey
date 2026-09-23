import utils

tasks = []

utils.add_task(tasks, "Learn Python")
utils.add_task(tasks, "Practice functions")
utils.add_task(tasks, "Build a project")

print("Tasks:")
utils.show_tasks(tasks)

print(f"Total tasks : {utils.count_task(tasks)}")

utils.remove_task(tasks, "Practice functions")

print("\nAfter removing a task:")
utils.show_tasks(tasks)
