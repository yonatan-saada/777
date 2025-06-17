# 1
# b = 1
# while b < 1000:
#     if b % 3 == 0 and b % 5 == 0:
#         print("FuzzBuzz")
#     elif b % 3 == 0:
#         print("Fuzz")
#     elif b % 5 == 0:
#         print("Buzz")
#     else:
#         print(b)
#     b = b + 1
# 2
# a = int(input("enter a number:"))
# b =0
# c = "*"
# while b < a:
#      print(c)
#      b = b + 1
#      c += "*"
# v = "*"
# while a > 0:
#      a = a - 1
#      print(a*v)
# 3
# a = int(input("Add a number: "))
# c = 2
# while a > c:
#     if a % c == 0:
#         print("This is not a prime number")
#         break
#     c += 1
# else:
#     print("It's a prime number")
# 4
# h = 0
# a = int(input("Add a number: "))
# for i in range(1,a+1):
#     h += 1
#     t = int(i)
#     i = str(i)
#     if t < 10:
#         i = i + " "
#     else:
#         i = i
#     print(" "*(a-t),i*h)
# 5
# a = str(input(" add a number: "))
# b = str(a[:: -1])
# if a == b:
#     print("It's a palindrome")
# else:
#     print("It's not a palindrome")
# 6
# o = []
# t = []
# v = []
# while 1:
#     a = input("add a number: ")
#     if a == "exit":
#         if len(o) > 0:
#             break
#         print("Please add a number")
#     else:
#         o.append(int(a))
# s = input("""Choose an option:
# a:amount of numbers
# b:sum of numbers
# c:Amount of even numbers to amount of odd numbers
# d: The largest and smallest number
# e: Average numbers,(a,b,c,d,e)""")
# if s == "a":
#    print(len(o))
# elif s == "b":
#    print(sum(o))
# elif s == "c":
#     for i in o:
#         g = int(i)
#         if g % 2 == 0:
#             v.append(i)
#         else:
#             t. append(i)
#             print("These are the even numbers.:",v)
#             print("These are the odd numbers.: ",t)
# elif s == "d":
#     print(o)
#     print(max(o))
#     print(min(o))
# elif s == "e":
#     print(sum(o)/len(o))
#


































