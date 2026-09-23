from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# Lambda
square = lambda x: x**2
print(square(5))


# map - square every number
squares = list(map(lambda x: x**2, numbers))
print("Squares : ", squares)


# filter - keep even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers : ", even_numbers)


# reduce - calculate the sum
total = reduce(lambda x, y: x + y, numbers)
print("Total: ", total)
