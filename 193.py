# l = [1,8,5,96,4,2,3,85,42,56,15,25]
# def m (l):
#     if len(l) <= 1:
#         return l
#     else:
#         pivot = len(l)//2
#         l1 = m(l[:pivot])
#         l2 = m(l[pivot:])
#         return sort_mo(l1 ,l2)
# def sort_mo(l1,l2):
#     l3 = []
#     i,j = 0,0
#     while i < len(l1) and j < len(l2):
#         if l1[i] < l2[j]:
#             l3.append(l1[i])
#             i +=1
#         else:
#             l3.append(l2[j])
#             j += 1
#     l3 += l1[i:]
#     l3 += l2[j:]
#     return l3
# print(m(l))
# ########
# for i in range (len(l)):
#     for j in range(len(l)-i-1):
#         if l[j] > l[j+1] :
#             l[j],l[j+1] = l[j +1],l[j]
# print(l)
# ######
# def min(l,c):
#     mini = c
#     for i in range(c,len(l)):
#         if l [i] < l[mini]:
#             mini = i
#     return mini
# def swap(l,i,v):
#     l[i],l[v] = l[v],l[i]
# def sort(l):
#     for i in range(len(l)):
#         a = min(l,i)
#         b = swap(l,i,a)
#     return l
# print(sort([22,8,5,46,2]))
# def all(s):
#     if "?" not in s:
#         return [s]
#     else:
#         i = s.index("?")
#         L = all(s[:i] + "L" + s[i+1:])
#         R = all(s[:i] + "R" + s[i+1:])
#         return L + R
#
# print(all("R?RL?"))
# c = 0
# def d(l):
#     global  c
#     if len(l)==0:
#         return c
#     if l[len(l)-1] % 2 == 0:
#         c +=1
#     l.pop()
#     return d(l)
# print(d([2,2,5,8,12,14]))
#### 1
c = 0
# def a(string,v):
#     if len(string) == 0:
#         global c
#         return c
#     elif string[-1] == v :
#         c += 1
#     return a(string[:-1],v)
# print(a("aba","a"))
# #### 2
# def b(string):
#     if len(string) == 0:
#         return " "
#     if len(string) > 0:
#         print(string[-1], end="")
#     return b(string[:-1])
# print(b("abc"))
### 3
def r (num):
    l = str(num)
    if len(l) <= 1:
        return True
    else:
        if l[-1] == l[0]:
            return r(l[1:-1])
        else:
            return False
print(r(98641234689))
# #### 4
# def cev(a,i = 0):
#     if len(a) == 0:
#         return i
#     if a [-1] % 2 ==0:
#         i +=1
#     a = a[:-1]
#     return cev(a,i)
# print(cev([2,1,2,4,5]))
#### 5
# def isi(a,i = 0):
#     if len(a) <= 1:
#         return "yes"
#     if a[0] < a[1]:
#         i += 1
#         return isi(a[i:])
#     else:
#         return "no"
# print(isi([1,2,6,4,5]))
#### 6
# def negativ(a,i = 0):
#     if a[i] <= 0:
#         return "yes"
#     else:
#         i +=1
#         if i != len(a):
#             return negativ(a,i)
#         else:
#             return "no"
# print(negativ([1,2,1,5,2]))
### 7
# def most(l,i = 0, max_num = None,max_count = 0):
#     if i >= len(l)-1:
#         return max_num
#     c = 0
#     for d in l:
#         if l[i] == d :
#             c +=1
#     if c > max_count:
#         max_count = c
#         max_num = l[i]
#     return most(l,i+1, max_num,max_count)
# print(most([1,2,2,15,1,1,2,2,15,15,15,15,],))
#### 8
# def m(l,i = 0):
#     if i == len(l)-1:
#         return False
#     if l[i] == l [i+1]-1:
#         return True
#     return m(l,i+1)
# print(m([1,1,5,2,2,4]))
### 9
# def average(l,i=0,sum=0,count = 0):
#     if i == len(l):
#         return sum // count
#     sum +=l[i]
#     return average(l,i+1,sum,count+1)
# print(average([80,100,90,92,60,20]))



# def f():
#     print("hi")
# d = {"field": [1, 2], "function": f()}
# print(d["field"])
# # print(d["function"])
# class MyClass:
#     def __init__(self, name,age,addresses):
#         self.name = name
#         self.age = age
# y = MyClass("yonatan",22,"hadera")
# i = MyClass("idan",13,"roshe hain")
# print(y.name)
class Tail:
    def __init__(self,length,thickness):
        self.length = length
        self.thickness = thickness
class Animal:
    def __init__(self,animal,color,number_of_legs):
        self.animal = animal
        self.color = color
        self.number_of_legs = number_of_legs
    def add_tail(self,length,thickness):
        self.tail=Tail(length,thickness)
o = Animal("a",2,2)
o.add_tail(8,7)
print(o.tail.thickness)
class Cat(Animal):
    def __init__(self,color):
        super().__init__("cat", color, 4)
        self.color = color

a = Cat('asd')
print(a.animal)
b = Animal(1,2,3)
b.add_tail(2,2)
print(b.tail.length)









