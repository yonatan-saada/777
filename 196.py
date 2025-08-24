# # d = [{"a":1},{"b":2}]
# # for i in d:
# #     print(i.values())
# #     for v in i.values():
# #         print(v)
# # a ="hello"
# # for i in a:
# #     print(i)
# # b = ord("a")-32
# # def to_upper_manual(s):
# #     result = ''
# #     for c in s:
# #         if 'a' <= c <= 'z' :
# #             result += chr(ord(c) - 32)
# #         else:
# #             result += c
# #     return result
# # print(to_upper_manual("hello"))
# D = dict()
# for x in enumerate(range(2)):
#  D[x[0]] = x[1]
#  D[x[1]+7] = x[0]
# print(D)
# # class Acc:
# #  def __init__(self, id):
# #     self.id = id
# #     id = 555
# #
# # acc = Acc(111)
# # print (acc.id)
# from random import randrange
# L = list()
# for x in range(5):
#  L.append(randrange(0, 100, 2)-10)
# print(L)
# number_dct = {}
# number_dct[(1,2,4)] = 8
# number_dct[(4,2,1)] = 10
# number_dct[(1,2)] = 12
# sm = 0
# for k,v in number_dct.items():
#  if k[0] < 3:
#     sm += v
#
# print ( len(number_dct) + sm)
# st = "akbobaabdcbodaeab"
# res = ""
# for ch in st:
#     if ch not in "abc":
#         res += ch
# print(res)
# fb2= 15
#
# def func(n):
#      global fb2
#      if n <= 2:
#          fb2= 1
#          return 1
#
#      t = func(n - 1)
#      f = t + fb2
#      fb2 = t
#      return f
# print(func(0))
from symtable import Class


# def multiply(a, b):
#      if b == 0:
#
#         return 0
#
#      if b % 2 == 0:
#         return multiply(a+a, b//2)
#      return multiply(a+a, b//2) + a
# print(multiply(3,3))
# L = [13, 28, 21, 16, 35, 7, 4]
# s = 5
# s1 = 3
# for i in L:
#      if not i % 4:
#         s += i
#         continue
#      if not i % 7:
#          s1 += i
# print(s, end=" ")
# print(s1)
# 2= 15

# def func(n):
#      global fb2
#      if n <= 2:
#         fb2= 1
#         return 1
#
#      t = func(n - 1)
# #      f = t + fb2
# #      fb2 = t
# #      return f
# #
# # print(func(5))
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)
# print(factorial(5))
# class G:
#    def __init__(self, id):
#        self.id = id
# manager = G(100)
# manager.__dict__['life'] = 49
# manager.__dict__["f"] = 22
# print (manager.life + len(manager.__dict__))
# m = ["abcdefg", "hijklmn", "opqrstu", "vwxyz__"]
# idx = [(3, 2), (1, 1), (2, 3), (2, 5), (0, 0), (1, 5)]
# inner = []
# for r in m:
#     inner.append(len(r))
# p = {"rows": len(m), "columns": max(inner) }
# print(p["rows"], "X", p["columns"])
# while idx:
#     i = idx.pop()
#     print(m[i[0]][i[1]], end="")

# def a (l):
#     l = list(l.split(" "))
#     j = []
#     for i in l:
#         r = ""
#         for n in reversed(i):
#             r += n
#         j.append(r)
#     return j
# print(a("hello world"))
# def b (l,n):
#     l = list(l.split(" "))
#     j = []
#     for i in l:
#         if i[0] == n :
#             r = ""
#             for n in reversed(i):
#                 r += n
#             j.append(r)
#         else:
#             j.append(i)
#     r = " "
#     for i in j:
#         r+= i + " "
# #     return r
# # print(b("hello bhj hjk world","h"))
# def r (s):
#     d = {}
#     for i in s:
#         if i in d :
#             d[i] +=1
#         else:
#             d[i] = 1
#     r = ""
#     for i,v in d.items():
#         r += str(i)
#         r += str(v)
#     return r
# print(r("aaabbc"))
# class Book:
#     def __init__(self,title,auther,year,genres):
#         self.title = title
#         self.auther = auther
#         self.year = year
#         self.genres = genres
#     def is_genres(self,genres):
#         if genres in self.genres:
#             return True
#         else:
#             return False
# class L:
#     def __init__(self):
# #         self.books = []
# #     def add_book(self,book):
# #         self.books.append(book)
# #     def find_book_by_auther(self,auther):
# #         for i in self.books:
# #             if i.auther == auther:
# #                 print("in")
# # av = Book("a","b","c","d")
# # t = L()
# # t.add_book(av)
# # t.find_book_by_auther("b")
# def num(n):
#    if 4 > n:
#       return 1 < n
#    if not (n % 2 and n % 3):
#        return False
#    i = 5
#    while i <= n / i:
#       if not (n % i and n % (i + 2)):
#          return False
#       i += 6
#    return True
# print(num(5))
# print(41/5)
# def f(n, me={}):
#  if n in me:
#     return me[n]
#  if n == 0:
#      return 0
#  if n == 1:
#     return 1
#  me[n] = f(n - 1, me) + f(n - 2, me)
#  return me[n]
# print(f(6))
# def f1(n,m= {}):
#     if n <=1:
#         return n
#     return f1(n-1) + f1(n -2)
# print(f1(7))
# a = "  Hello world  "
# print(a)
# print(a.strip())
# print(a.lower())
# if "hello" in a:
#     print(True)
# x = 10
# print(f"{x:.2f}")
# a =[12,12]
# b = [12]
# b.extend(a)
# # b = a[:]
# # a.append(1)
# # # print(a)
# print(b)
#
# c = [0] * 3
# print(c)
# d ={"a":1,"b":2}
# d.pop(0)
# print(d)

# x = [1,2,3]
# for i in map(range, x):
#    for j in i:
#        print(j, end=" ")
#    print()
# a = b = 5
# a+=1
# print(b)
# a =print
# a("h")
# b = 8
# A = self = 6
# class A:
#  def A(self):
#     global A
#     A = print
#     A(self)
#  A(7)
#  def A():
#     global self, A
#     A(self)
#     A = 5
#     print(A)
#     A = self - A
#  def __init__(self):
#     self.A = 2
#     print(self.A + int(str(self)))
#  def __str__(self):
#     global A
#     A = 1
#     return str(A)
#  A()
#  print(4)
# A = A().A
# print(A.__str__())
# a = "hello"
# a =list(a)
# print(a)
# b = "h,n,m,m,n,n"
# b = b.split(",")
# v = "".join(b)
# print(b)
# print(v)
# print([0 for _ in range(5)])
# import os
# print(os.getcwd())
# print(os.listdir())
# print(os.path)
# w = [1,2,3]
# def d (a):
#     return a * 2
# for i in w:
#     print(d(i))
# y = map(d,w)
# print(list(y))
# a = 5
# def multiply(a, b):
#  if (b == 0):
#      return 0
#  if (b % 2 == 0):
#     return multiply(a+a, b//2)
#  return multiply(a+a,b//2) + a
# print(multiply(2,5))
# class G:
#  def __init__(self, id):
#     self.id = id
#
# manager = G(100)
# manager.__dict__['life'] = 49
# print (manager.__dict__)
def d (x):
    def wrapper(*n,**m):
        print("Choose a number and what power you want it to be.")
        x()
        print("This is the result")
    return wrapper
def f():
    n = int(input(":"))
    n1 = int(input(":"))
    print(n**n1)
# class Acc:
#  def __init__(self, id):
#     self.id = id
#     id = 555
#
# acc = Acc(111)
# print (acc.id)
#
# d = {"a":1,"c":1}
# for v in d.values():
#     print(v)
class G:
 def __init__(self, id):
     self.id = id

# manager = G(100)
# manager.__dict__['life'] = 49
# print(manager.__dict__)
# def v (n):
#  if 4 > n:
#     return 1 < n
#  if not (n % 2 and n % 3):
#     return False
#  i = 5
#  while i <= n / i:
#      if not (n % i and n % (i + 2)):
#         return False
#  i += 6
#  return True
# print(v(3))
# print(ord("x"))
# a = self = 6
# class A:
#  def A(self):
#     global A
#     A = print
#     A(self)
#  A(7)
#  def A():
#     global self, A
#     A(self)
#     A = 5
#     print(A)
#     A = self - A
#  def __init__(self):
#     self.A = 2
#     print(self.A + int(str(self)))
#  def __str__(self):
#     global A
#     A = 1
#     return str(A)
#  A()
#  print(4)
# A = A().A
# print(A.__str__())

# A = self = 6
# class A:
#     def A(self):
#         global A
#         A = print
#         A(self)
#     A(7)
#     def A():
#         global self, A
#         A(self)
#         A = 5
#         print(A)
#         A = self - A
#
#     def __init__(self):
#         self.A = 2
#         print(self.A + int(str(self)))
#
#     def __str__(self):
#         global A
#         A = 1
#         return str(A)
#     A()
#     print(4)
#
# A = A().A
# print(A.__str__())

# class int:

#print((3).__str__())
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # starting time
        result = func(*args, **kwargs) # starting the function with its arguments
        end_time = time.time()    # ending time
        print(f" Time taken to run {func.__name__}: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def long_running_function(n):
    # function that takes a long time to run
    sum = 0
    for i in range(n):
        sum += i
    return sum

# start the function and measure its execution time
long_running_function(100000)
class Dog:
  # This is the constructor method
  def __init__(self):
    print("A new dog has been created!")
    self.energy = 10 # Initialize the 'energy' attribute

  def bark(self):
    print("Woof! Woof!")

# Create a new object (instance) from the Dog class
my_dog = Dog() # The __init__ method is called automatically here

print(f"My dog's energy level is: {my_dog.bark}")
a ={"a":1,"b":2}
def s (a):
    k,v = a
    return (k,v+1)
y = map(s,a.items())
print(list(y))
a = "s"
a = [ a for _ in range(10)]
print(a)
print(  [i*2 for i in range(10)])

c = {k:k//2 for k in range(10)}
print(c)
a = 10
b = a *2 if a < 20 else a
print(b)
try:
   print( 10 / 0)
except:
    print("nn")

