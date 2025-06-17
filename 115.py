# r = []
# e =[]
# for y in range(1900,2001):
#     if y % 4 == 0 and y % 100 !=0 or y % 400 == 0:
#         e.append(y)
#     else:
#         r.append(y)
# print(len(e))
# print(len(r))
# print(e)
#print(r)
#
# a = int(input("select a number: "))
# b = int(input("select a number: "))
# c = input(" do you want to add the numbers (y/n)")
# if c =="y":
#     print(a, "+", b, "=", a + b)
# if c == "n":
#     print(a, "-", b, "=", a - b)
# else:
#     print("invalid input")
# h = "15454"
# d = list(h[::-1])
# print(d)
# x = int(input("select a number"))
# r = 0
# while x > 0:
#     r = (r * 10) + (x % 10)
#     x //= 10
# print(r)
# x = 10
# if x > 8:
#     if x > 12:
#         print(x)
# l = ["a","b","c","d"]
# for r ,i in enumerate(l):
#     print(r ,i )
# y = "abcdef"
# g =list(y[::-1])
# print(g[1:5])
# f = "nmbvgh"
# print(f[0])
# for f ,y in enumerate(f):
   # print(f,y)

# d = {"a":1,"b":2,"c":3,"d":4}
# b = ["d","d","d","dd","d","d"]
# for k , f in enumerate(b):
#     print(k,f)



d = {"a":1,"b":2,"c":3,"d":4}
f = {"a":8,"j":7}
# for k,v in d.items():
#     if v not in f:
#         f[v] = [k]
#     else:
#         f[v].append(k)
#print(f)
r = {}
for k,v in d.items():
    if k not in r:
            r[k] = [v]
    else:
            r[k].append(v)
for g,h in f.items():
    if g not in r:
           r[g] = [h]
    else:
        r[g].append(h)
print(r)








