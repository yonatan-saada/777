# 1
from operator import index

# b = []
# while True:
#     a = input("add a number: ")
#     if a == "0":
#        break
#     b.append(a)
# c = [b.pop()]
# b = c + b
# print(b)
# 2
# for i ,x in enumerate([5, 4, 3, 2, 1]):
#     print((i + 1)*x)
#     print((i + 1),x)
# 3
# arr1 =[5,4,3]
# arr2 =[1,10,-5]
# arr3 = [10,30,15,2]
# arr4 = [200,20]
# all = [arr1 , arr2 ,arr3 , arr4 ]
# #print(len(all))
# c =[3, 44, 10, 5, 6 ]
# for i,f in enumerate(all):
#     for u,n in enumerate(f):
#         if n in c :
#             print(n,"in" ,"index:" ,i,u)
#     else:
#             print("not in all")
# 4
# n = 0
# m = 10
# a = [[],[],[],[],[],[],[],[],[],[]]
# for i in range(1,101):
#     if i < m:
#         a[n].append(i)
#     else:
#         a[n].append(i)
#         m += 10
#         n += 1
# print(a)
# 5
# a = int(input("add a number: "))
# d = a
# b = []
# for i in range(a):
#     b.append([])
# c = 0
# for i in range(1,a*a+1):
#     if i < a:
#          b[c].append(i)
#     else:
#         b[c].append(i)
#         a += d
#         c += 1
# print(b)
# 6
# m = [[1,2,4,4],[5,8,12,8],[9,8,11,12],[13,14,8,16]]
# r = []
# for i,n  in enumerate(m):
#     for f ,g in enumerate(n):
#         if f % 2 ==0:
#            r.append(g)
# print(r)
# print("the sum of m is: ",sum(r))
# d = {}
# c = 1
# for i in m:
#     for y in i :
#       if y not in d:
#          d[y] = c
#       else:
#          d[y] +=  1
# max_value = 0
# for key, value in d.items():
#     if value > max_value:
#         max_value = value
#         max_key = kay
# print(max_key)
# 7

# o = [
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15],
#     [16,17,18,19,20],
#     [21,22,23,24,25]]
# b = 0
# k = []
# for i ,v in enumerate(o):
#     for n,m in enumerate(v):
#         if n == b:
#             k.append(m)
#     b+=1
# print(sum(k))
# b = len(o)-1
# k = []
# for i,v in enumerate(o):
#     for n,m in enumerate(v):
#         if n == b:
#             k.append(m)
#     b-=1
# print(sum(k))
# k = []
# for i ,v in enumerate(o):
#     k.append(v[0])
# print(sum(k))
# k = []
# for i ,v in enumerate(o):
#     k.append(v[len(o)-1])
# print(sum(k))
# b = 0
# for i,v in enumerate(o):
#     if i == 0 or i == len(o)-1:
#         b += sum(v)
#     else:
#         b += v[0]
#         b += v[len(o)-1]
# print(b)
# # 8
o = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]]
# r = 0
# m = 0
# for i,v in enumerate(o):
#     if sum(v) > r:
#         r = sum(v)
#         m = i
# print(m)
# r = 0
# m = 0
# ###
# for i,v in enumerate(o):
#     r +=sum(v)
# for i,v in enumerate(o):
#     if sum(v) < r:
#         r = sum(v)
#         m = i
# print(m)
######
# b = []
# for i in range(len(o[0])):
#      a = []
#      for h in range(len(o)):
#          a.append(0)
#      b.append(a)
# for i in range(len(o)):
#     for j in range(len(o)):
#         b[j][len(o) - 1 - i] = o[i][j]
# for i in b:
#     print(i)
# ## #
# a = int (input("add a number: "))
# for i ,v in enumerate(o):
#     for n,m in enumerate(v):
#         if m == a:
#             if 0 < n < len(o)-1:
#                 if i != 0:
#                     print(o[i-1][n-1],o[i-1][n],o[i-1][n+1])
#                 print(o[i][n-1],"  ",o[i][n+1])
#                 if i != len(o)-1:
#                    print(o[i+1][n-1],o[i+1][n],o[i+1][n+1])
#             elif n == 0 :
#                 if i != 0 :
#                     print(o[i-1][n],o[i-1][n+1])
#                 print("   ",o[i][n+1])
#                 if i != len(o)-1:
#                     print(o[i+1][n],o[i+1][n+1])
#             #elif n == len(o)-1 and i != 0 or len(o)-1:
#             elif n == len(o[0]) - 1:
#                 if i != 0:
#                     print(o[i - 1][n-1], o[i - 1][n])
#                 print( o[i][n -1],"   ")
#                 if i != len(o)-1:
#                    print(o[i + 1][n-1], o[i + 1][n])
#             else:
#                 if n == len(o)-1 and i == 0 :
#                         print(o[i][n-1])
#                         print(o[i+1][n-1],o[i+1][n])













































