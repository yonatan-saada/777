num1 = int(input("add a number? "))
num2 = int(input("add a number? "))
num3 = int(input("add a number? "))
num4 = int(input("add a number? "))
num5 = int(input("add a number? "))
list = [num1,num2,num3,num4,num5]
list[2], list[1],list[3],list[4] = list[1],list[2],list[4],list[3]
print(list)