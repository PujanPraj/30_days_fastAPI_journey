# Tuples are like lists but immutable - use them for fixed data (coordinates, RGB values, function returns that shouldn't change)

point = (10, 20)
# point[0] = 5 # TypeError - types can't be modified

# convert between structures
task_list = ["email", "meeting", "review", "review"]  # has duplicate

# remove duplicate
task_set = set(task_list)

# freezes the list
task_tuple = tuple(task_list)

# convert back
back_to_list = list(task_set)

print(task_set)
print(task_tuple)
print(back_to_list)
