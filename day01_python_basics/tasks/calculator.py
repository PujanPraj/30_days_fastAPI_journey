num1 = float(input("Enter a first number : "))
num2 = float(input("Enter a second number : "))

operator = input("Enter operator : (+, -, /, *) : ")

match operator:
    case "+":
        print(f"Sum : {num1 + num2}")
    case "-":
        print(f"Subtract : {num1 - num2}")
    case "/":
        if num2 != 0:
            print(f"Divide : {num1 / num2}")
        else:
            print("num2 cannot be 0")
    case "*":
        print(f"Multiply: {num1 * num2}")