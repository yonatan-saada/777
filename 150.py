# 1
# def Palindrome(a):
#     b = a[::-1]
#     if b == a:
#         c = True
#     else:
#         c = False
#     return c
# print(Palindrome("252"))
# 2
# def risking_numbers_until_the_variable(a):
#     b = 0
#     for i in range(0,a):
#         b += i
#     return b
# print(risking_numbers_until_the_variable(10))
# 3
# gh = [1,2,5,5,6,8]
# def my_sum(number):
#     list = []
#     for i in number:
#         list.append(i)
#     return sum(list)
# print(my_sum(gh))
# 4
# def asterisk(number):
#     list = []
#     for i in reversed(number):
#         list.append("*"*i)
#     return list
# print(asterisk([1,2,3]))
# 5
# def add (a,b):
#     a = a + b
#     return a
# def multiplication(a,b):
#     a = a * b
#     return a
# def r (a):
#     b = multiplication(a+1,a)
#     c = add(a+1,a)
#     d = multiplication(a-1,a)
#     e = add(a-1,a)
#     list1 =[b,c,d,e]
#     return list1
# print(r(5))
# 6
# def number (*numbers):
#     o = 0
#     for i in numbers:
#         o += i
#     return o
# print(number(5,5,5,5,5,5,8,8,8,))
# 7
# def double(*number):
#     list1 = []
#     for i,v in enumerate(number):
#         if i % 2 == 0:
#             list1.append(v)
#     return list1
# print(double(1,3,5,8,5,8,5))
# 8
# def quadratic_equation(a,b,c):
#     if (b**2 -4 * a * c) < 0:
#         return "There is no solution"
#     else:
#         g = (-b + (b**2 -4 * a * c)**0.5 ) / (2 * a)
#         u = (-b - (b**2 -4 * a * c)**0.5 ) / (2 * a)
#     return g,u
# print(quadratic_equation(3,2,-8))
# 9
# def dictionary(**name):
#     for i ,v in name.items():
#         name[i] = v
#     return name
# print(dictionary( name="yonatan",age=21 ,phon = " 0523216476"))


