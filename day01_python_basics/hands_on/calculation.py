num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the seconnd number : "))

print(f"sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")

if num2 != 0:
    print(f"Quotient: {num1 / num2}")
else:
    print("Cannot divide by zero")

