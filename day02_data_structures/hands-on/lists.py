# list is a ordered, mutable and allows duplicates

tasks = []

# add tasks
tasks.append("Buy groceries")
tasks.append("Finish python list")
tasks.append("Write python script")
print(tasks)

# insert at specific position
tasks.insert(1, "Call plumber")
print(tasks)

print("---------------------------------")

# access by index
print(tasks[0])
print(tasks[-1])

print("---------------------------------")

# slicing
print(tasks[1:3])

print("---------------------------------")

# remove
tasks.remove("Call plumber")
print(tasks)
popped = tasks.pop()
print(popped)
print(tasks)

print("---------------------------------")

# udpate
tasks[0] = "Buy groceries (urgent)" 
print(tasks)

print("---------------------------------")

# iterate
for i, task in enumerate(tasks):
    print(f"{i+1}. {task}")

print("---------------------------------")

# useful methods
print(len(tasks))
tasks.sort()
print(tasks)

# * complexity note: append()/pop() (from the end) are O(1).
# * insert()/remove()/pop(0) are O(n) because everything shifts. Matters once task list grows large.