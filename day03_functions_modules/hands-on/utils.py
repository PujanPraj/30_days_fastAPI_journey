def add_task(tasks, task):
    tasks.append(task)
    return tasks


def remove_task(tasks, task):
    if task in tasks:
        tasks.remove(task)
    return tasks


def show_tasks(tasks):
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task}")


def count_task(tasks):
    return len(tasks)
