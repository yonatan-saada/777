num1 =int(input("enter a number: "))
num2 = int(input("enter another number: "))
num3 = int(input("enter a number: "))
if num1 > num2 > num3:
    print("descending series")
elif num3 > num2 > num1:
    print("rising series")
else:
    print("out of order")