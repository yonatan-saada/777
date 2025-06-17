num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Choose an operator (+, -, *, /, %, **): ")
if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero.")
elif operator == "%":
    if num2 != 0:
        print("Result:", num1 % num2)
    else:
        print("Error: Cannot divide by zero.")
elif operator == "**":
    print("Result:", num1 ** num2)
else:
    print("Invalid operator. Please choose one of: +, -, *, /, %, **")
