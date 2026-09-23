# A set is unordered, unique elemets only. Perfect for interseciton/union operations.

work_tasks = {"email", "meeting", "report", "review"}
personal_tasks = {"groceries", "gym", "review", "cooking"}

# common elements (intersection)
common = work_tasks & personal_tasks
print(common)

print("----------------------------------------------")

# all unique elements (union)
all_tasks = work_tasks | personal_tasks
print(all_tasks)

print("----------------------------------------------")

# in work but not personal
only_work = work_tasks - personal_tasks
print(f"only work : {only_work}")

print("----------------------------------------------")

# symmetric difference (in either, not both)
diff = work_tasks ^ personal_tasks
print(f"diff: {diff}")

print("----------------------------------------------")

# add/remove
work_tasks.add("planning")
print(work_tasks)
work_tasks.discard("email") # won't error if mission, unlike remove()
print(work_tasks)

