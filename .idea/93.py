

if year % 4 != 0:
    print("Not a leap year.")
elif year % 100 != 0:
    print("Leap year.")
elif year % 400 == 0:
    print("Leap year.")
else:
    print("Not a leap year.")
y=int(input("enter a year:"))
if y % 4 != 0:
    print("f")
elif y % 100 != 0:
    print("t")
elif y % 400 ==0:
    print("t")
else:
    print('f')