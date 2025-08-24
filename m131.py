# from pynput.keyboard import Listener
from numpy.f2py.symbolic import as_ge

# print("dddddd")
# print("kkkkk")
# print("sssss")
# print(pynput.mouse)
# x = 0
# g = 5
# b = 10
# name = input("your name: ")
# # age = input("your age: ")
# # print("hello",name,"your age is :" ,age)
# # def ten():
# #     for i in range(10):
# #         print(i)
# #     return 10
# # def one_hundred():
# #     for i in range(10,100):
# #         print( i)
# #     return 100
# # l = "//////////"
# # print(len(l))
# a = [1000000,200000,30000000]
# def v(l):
#     for i in l:
#         yield i+ 100
#         yield i + 200
# d = (v(a))
# print(next(d))
# print(next(d))
# print(next(d))
# print(a)
# a = [1,2,3]
# y = map(lambda c:c*2 , a)
# print(y)
# m = [[1,2,3],[4,5,6],[7,8,9]]
# y = [i for b in m for i in b]
# print(list(y))
# b = [[i for i in range(10) ]for g in range(6)]
# print(b)
# d = {i:i*2 for i in range(10)}
# print(d)
# dollar = {"backpack": 100, "case": 200, "bag": 20}
# s = {k:v*3 for(k,v) in dollar.items()}
# print(s)
# a = "l"
# # f = [a for _ in range(10)]
# # print(f)
# # class Person:
# #   def __init__(self, name, age):
# #     self.__name = name
# #     self.age = age
# #
# #   def myfunc(self):
# #     print("Hello my name is " + self.__name)
# #
# #   @property
# #   def __str__(self):
# #       return "hhhh"
# #   def __repr__(self):
# #       return "htnht;fodtlrkm;l"
# #
# # p1 = Person("John", 36)
#
# #
# # print(p1.myfunc())
# # print(p1.__str__)
# # print(p1.__repr__())
# # class Dog:
# #     def s (self):
# #         return "hhhh"
# # class Cat:
# #     def s(self):
# #         return "nnnnn"
#
#
# a =Dog()
# b=Cat()
# print(b.s())
# print(a.s())
# animal(a)
# animal(b)
# import platform
# x =platform.system()
# print(x)
# l = [1,1,2,3,3]
# def summ(l):
#     d ={}
#     a = 0
#     for i in l:
#         if i not in d:
#             d[i] = i
#         else:
#             d[i] = 0
#     return sum(d.values())
#
#
# print(summ(l))
# l = [1, 1, 2, 3, 3]
#
# def summ(l):
#     d = {i: (i if l.count(i) == 1 else 0) for i in set(l)}
#     return sum(d.values())
# print(summ(l))
# y = [i for i in range(10)if i % 2 == 0]
# print(list(y))
# s = list(filter(lambda k:k % 2 ==0 ,range(10)))
# print(s)
# a = [5,7,8,2]
# b = [str(i) for i in a if i % 2 == 0]
# print(b)
# def f():
#     x =lambda  a : lambda b: a + b
#     y = x(5)
#     return y(3) * 2
# print(f())
# d = {"a":lambda x:x**2 ,"b": lambda x:x +1 }
# k = ["a","b", "a"]
# m = 3
# print([d[i](m)for i in k])
# print(b.s())
# d = {"C":1,"b":2}
# d.update({"b": 5})
# print(d)
# a  = [1,2,3]
# b = [4,5,6]
# c =zip(a,b)
# d = [ y for x in c for y in x]
# print(d)
class Anima:
    def t(self):
        return "d"
class D(Anima):
    @property
    def t(self):
        return "v"
cv = D()
cv.t
print(cv.t)
class Animal:
    def __init__(self,name,age,number_of_luegs):
        self.name = name
        self.age = age
        self.number_of_luegs = number_of_luegs
    def __str__(self):
        return f" the age is {self.age}"
    @property
    def __repr__(self):
        return f"class to create animal"
class Dog(Animal):
    def __init__(self,age):
        super().__init__("dog",age,4)
a = Animal("dog",12,4)
b = Dog(14)
print(a.name)
print(b.number_of_luegs)
print(a)
print(a.__repr__)
class Bank:
    def __init__(self,balance,first_name,last_name):
        self.__balance = balance
        self.first_name = first_name
        self.last_name = last_name
    @property
    def balance(self):
        return self.__balance
    def duspit(self,sum):
        self.__balance += sum
    @property
    def full_name(self):
        return f"{self.first_name}{self.last_name}"
    @full_name.setter
    def full_name(self,full_name):
        a = full_name.split(" ")
        self.first_name = a[0]
        self.last_name = a[1]
    def __str__(self):
        return f"the name is {self.first_name} {self.last_name} the balance {self.balance}"
    def __repr__(self):
        return "this func is for create bank acuont"
a = Bank(1000,"yonatan","sad")
b = Bank(850,"avi","cheon")
b.duspit(1000)
print(b)


