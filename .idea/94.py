num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 < num2 < num3:
    print("Ascending sequence")
elif num1 > num2 > num3:
    print("Descending sequence")
else:
    print("No particular order")
