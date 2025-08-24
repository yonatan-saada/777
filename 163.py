l = [13,13,3,5,6]
# def h(l):
#     b = []
#     while l:
#         a = l[0]
#         for i,v in enumerate(l[:]):
#             if v < a:
#                 a = v
#         l.remove(a)
#         b.append(a)
#     return b
# print(h([11,15,14,2,1,1,6]))
# def find_min_index(l,start):
#     new_list = l[start:]
#     min_num = new_list[0]
#     min_index = 0
#     for i,v in enumerate(new_list):
#         if v < min_num :
#             min_num = v
#             min_index = i
#     return min_index+start
# for x in range(len(l)):
#     print(find_min_index([-2,2,3,4,-55,1],x))
# def
# l = [ 0,1,2,3,9,5]
# for i,v in enumerate(l):
#     if v % 2 == 0:
#         print(v)
#         l.insert(5,1)
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# my_dict.pop("b")
# del my_dict["a"]
# print(my_dict)
# l = [1,2,3,4,5,6]
# # b = l [:]
# # l.pop(2)
# # print(b)
# a = [l[0:2],l[2:4],l[4:6]]
# print(a)
# print(a[2][0])
# b = {"a":1,"b":2,"c":3,"(1,2,3)":4}
# for v in b.keys():
#     print(v)
# b = "5"
# try:
#     a = int(b)
#     print("int")
# except ValueError:
#     print("str")
# def c(n):
#     m = []
#     a = []
#     b = 0
#     for i in range(n):
#         a.append(0)
#         m.append(a)
#         if i == b:
#             a[b]=1
#             b +=1
#     return (m)
# print(c(3)d(a)

# def b (n):
#     m = []
#     for i in range(n):
#         a = [0] * n
#         a[i] = 1
#         m.append(a)
# #     return m
# # print(b(5))
#
# def m(m):
#     a =[]
#     for i in range (len(m[0])):
#             s = []
#             for g in range (len(m)):
#                 s.append(m[g] [i])
#             a.append(s)
#     return a
# # print(m([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]))
# m =  [[5,10,15],[20,25,30]]
# t = []
# for i in m:
#     print(sum(i))
#
# for col in range(len(m)):
#     c = 0
#     for row in range(len(m[0])):
#         c += m[col][row]
#     t.append(c)
# print(t)
#
# p = [[1,0,1,0],
#      [0,1,0,1],
#      [1,0,1,0],
#      [0,1,0,1]]
# c = 0
# def s():
#     global c
#     c +=5
#     print(f"inside:{c}")
# def v():
#     c = 10
#     print(f"local:{c}")
# print(s())
# print(v())
# print(f"global{c}")
# n = [10,20,30,40]
# r = []
# while n:
#     d = n.pop()
#     r.append(d*2)
#     if len(n) == 2:
#         break
# print(r)
# print(n)
# n = "m"
# def a ():
#     global n
#     n = "p"
#     return 'h' + n *3
# def b ():
#     return "hi" + n
# print(b())
# print(a())
# print(b())
# a = [20,20,10]
# def g (l,b):
#     r = []
#     for i in range(len(l)):
#         if i % 2 ==0:
# #             r.append(l[i]*b)
#         else:
#             r.append(l[i]+ b)
#     return r
# b = g(a,3)
# print(b)
# print(a)
# def a (l):
#     d = {}
#     for i in l:
#         d[i[0]] = i
#     return d
# print(a(["kl","jk","df"]))
# def r (n):
#     e = []
#     if n % 2 == 0:
#         s = n
#     else:
#         s = n -1
#     for i in range(s,0,-2):
#         e.append(i)
#     return e
# print(r(10))
# def r (l):
#     a = ()
#     b  = 0
#     c = 0
#     for i in l:
#         if i % 2 ==0:
#            b = b + i
#         else:
#            c = c + i
#     a = a + (c,b)
#     return a
# print(r([1,1,1,1,1,6,6,6,6,6]))
# def m (n):
#     for i in n:
#         print( sum(i))
# print(m([[1,2,3],[4,5,6]]))
# def s (*n):
#     d = {}
#     for f in n:
#         for i in f:
#             if i not in d:
#                 d[i] = 1
#             else:
#                 d[i] +=1
#     return d
# print(s("hello","vgh"))
# def c (n):
#     if n <= 1:
#         return 1
#     else:
#         return  n * c(n-1)
# print(c(3))
#
# a = [1,2,3]
# b = "hello"
# c = (1,2,3)
# d = {1,2,2,1}
# h ={"a":1, "b":2 }
# print(a,b,c,d,h)
# a.append(5)
# a.remove(a[0])
# print(a)
# b = b + " world"
# print(b)
# b = "world"
# print(b)
# c = c +(2,)
# print(c)
# c = (2,2)
# print(c)
# print(c[0])
# d.add(3 )
# print(d)
# d.remove(3)
# print(d)
# h ["v"] = 5
# print(h)
# del h["v"]
# print(h)

#
# a = int (input("add a number: "))
# m = []
# for i in range(a):
#     m.append([0]*a)
# for i in range(a**2):
#     for c in range(len(m)):
#         for j in range(len(m[0])):
#             m[c][j]=i
# print(m)
# list_1 = []
# list_2 = []
# list_3 = []
# for i in range(4):
#  list_1.append(i)
# print(list_1)
# data = {"max": list_1[-1]}
# for i, x in enumerate(list_1):
#  list_2.append(list_1[i % 3] + x)
# list_2 = list_2[: : -1]
# print(list_2)
# while len(list_2) > 0:
#  x = list_2.pop() + list_2.pop()
#  list_3.append(x)
# print(list_3)
# print(data['max'] in list_3)
# x = 5
# for i in range(x):
#  s = ""
#  for j in range(x - i):
#      s += str(x - i - j)
#  print(s)
# list_a,list_b,list_c = [], [], []
# for num in range(4):
#     list_a.append(num * 2)
# print(list_a)
# mid = len(list_a) // 2
# max_val = max(list_a)
# info = {"mid": mid, "max_val": max_val}
# for i in range(info["max_val"]):
#     if i < len(list_a):
#         item = list_a[i]
#         list_b.append(item + 1)
#     else:
#         list_b.append(i % 3)
# print(list_b)
# while len(list_b) > 1:
#     x = list_b.pop(0) * list_b.pop(0)
#     list_c.append(x)
# print(list_c)
# is_max_in_list = info['max_val'] in list_c
# print(is_max_in_list)
# print(is_max_in_list or bool(len(list_a)))
# m = []
# for i in range(3):
#     a = [0]* 3
#     a[i] = 1
#     m.append(a)
# print(m)
m = [[1,2,3],
     [4,2,6],
     ]
n = []
for i in range (len(m[0])):
    l = []
    for f in range(len(m)):
        l.append(m[f][i])
    n.append(l)
print(n)
l = [1,2,3]

s = []
def y(l):
    g = ""
    for i in range(len(l)):
        g += "#"*l.pop(i)
    s.append(g)
    return s[::-1]
print(y(l))







