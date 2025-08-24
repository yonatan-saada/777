# def r(n):
#     while n > 0:
#         print( n -1)
#         n -= 1
#     return n
# def v (n):
#     return r(r(n))
# print(v(9))
# def r(n):
#     while n > 0:
#         print( n -2)
#         n -= 2
#     return " "
# def v (n):
#     return r(n)
# print(v(9))
# def one_back(n):
#     return n - 1
# def two_back(n):
#     return one_back(one_back(n))
# def print_back(n):
#     while n >= 0:
#        print(n)
#        n = two_back(n)
# print(print_back(10))
# def rev(n):
#     if n < 10 :
#         print( n)
#     else:
#         d = n % 10
#         print(d,end="")
#         r = n //10
#         rev(r)
#     return " "
# print(rev(12345))
# 1
# def a():
#     print("a")
#     return a()
# print(a())
# 2
# def b(number):
#     print(number)
#     number = number + 1
#     return b(number)
# print(b(6))
# 3
# def c (s):
#     print(s)
#     s = s[:-1]
#     return c(s)
# print(c("saada"))
# 4
# def call_me(number):
#     if number == 0:
#         return " "
#     else:
#         print("call")
#         number = number -1
#         return call_me(number)
# print(call_me(8))
# 5
# def d (number):
#     if number < 0:
#         return " "
#     else:
#         print(number)
#         number -= 1
#         return d(number)
# print(d(9))
# 6
def where(Chair_number,number = 0):
    if Chair_number == 0:
        return number
    else:
        Chair_number = Chair_number-1
        number = number + 1
        return where(Chair_number,number)
print(where(8,0))
# 7
# def rev(n):
#     if n < 10 :
#         print( n)
#     else:
#         d = n % 10
#         print(d,end="")
#         r = n //10
#         rev(r)
#     return  " "
# print(rev(12345))
# def rev(n):
#     if n < 10 :
#         print( n,end="")
#     else:
#         d = n % 10
#         r = n //10
#         rev(r)
#         print(d, end="")
#     return " "
# print(rev(12345))
# 8
def rev(n):
    if len(n) == 1:
        print( n)
    else:
        d = n[-1]
        print(d,end="")
        r = n [:-1]
        rev(r)
    return " "
print(rev("saada"))
# # # 8 2
def rev(n):
    if len(n) == 1:
        print( n, end="")
    else:
        d = n[-1]
        r = n [:-1]
        rev(r)
        print(d, end="")
    return " "
print(rev("saada"))
# 9
def factoreil(number):
    if number == 1:
        return number
    return number * factoreil(number-1)
print(factoreil(5))
# 10
def fibonacci (num):
    if num <= 1:
        return num
    return fibonacci(num-2) + fibonacci(num-1)
print(fibonacci(3))
def sum(m):
    s = 0
    for i ,v in enumerate(m):
        for g,m in enumerate(v):
            if g == 0 :
                s += m
            elif i == g:
                if i != 0:
                    s +=m
    return s
print(sum([[1,2,3],[4,5,6],[7,8,9],[2,2,2,]]))
#######
# def num (a):
#     r = []
#     while a :
#         s =""
#         for i in range(len(a)):
#             s += "#" * a.pop(i)
#             r.append(s)
#     return r[::-1]
# print(num([2,4,1]))
# def num(a):
#     r = []
#     while a:
#         s = ""
#         for i in (range(1)):
#             s += "#" * a.pop(i)
#         r.append(s)
#     return r[::-1]
# print(num([2, 4, 1,8]))
