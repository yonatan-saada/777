# 1
# f = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10}
# for v in f.values():
#     print(v)
# o = (2,3,5,4,22,8,9,99,63,6,36,52,85,26)
# for v in o:
#     print(v)
# 2
# h = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"m":11,"r":12}
# for k,v in h.items():
#     int(v)
#     if v % 2 == 0:
#         print(k,v)
# 3
# m = {}
# l = {"a":1,"b":2,"c":3,"d":4}
# for k,v in l.items():
#     m[v] = k
# print(m)
# 4
# n = input("Choose twenty characters: ")
# h = {}
# for i in n:
#    if i not in h:
#       h[i]=1
#    else:
#       h[i] += 1
# print(h)
# 5
# b = int(input("add a number: "))
# j = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
# while b > 0:
#     i = b % 10
#     j[i] += 1
#     b = b//10
# print(j)
# 6
# k= []
# a = [(1,5,3),(5,4,3,2,1),(10,20)]
# for i in range(len(a)):
#     a[i] = list(a[i])
# print(a, sep="\n")
# 7
# a = input("Add words, numbers, and values:" )
# a =a.split()
# o = {}
# n = {}
# m =  {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
#
# for i in a:
#     try:
#          num = int(i)
#          while num > 0:
#               k = num%10
#               if k in m:
#                 m[k] += 1
#               num = num //10
#     except ValueError:
#         if i.isalpha():
#               if i not in n:
#                  n[i] = 1
#               else:
#                 n[i] += 1
#         else:
#             for w in i:
#                if w not in o:
#                  o[w] = 1
#                else:
#                  o[w] += 1
# x = n.copy()
# x["m"] = m
# x["o"] = o
#print(x)
# 8
# n = {"a":{"a":11,"b":55,"c":3},"b":{"d":4,"e":5,"f":6},"c":{"g":7,"h":8,"n":9}}
# for i in n.values():
#     m = 0
#     for k,v in i.items():
#         v = int(v)
#         if v > m:
#             m = v
#             maxkey = k
#     print(maxkey,end=" " )
# print("Key with the maximum value")
# for i in n.values():
#     b = 9999
#     for k,v in i.items():
#         v = int(v)
#         if v < b:
#             b = v
#             minkey = k
#     print(minkey ,end=" ")
# print("Key with the minimum value")
# # # # #
# for i in n.values():
#     for k,v in i.items():
#         v = int(v)
#         if v > m:
#             m = v
#             maxkey = k
# print(maxkey )
# for i in n.values():
#     for k,v in i.items():
#         v = int(v)
#         if v < b:
#             b =v
#             maxkey = k
# print(maxkey )
# ###
# l = []
# for i in n.values():
#     for k,v in i.items():
#         l.append(v)
# print(sum(l))
#
#






















