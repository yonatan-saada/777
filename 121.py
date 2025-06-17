# 1
d = {"a":1,"b":2,"c":3,"":4}
# f = {"a":8,"j":7}
# for k,v in d.items():
#     if v not in f:
#         f[v] = [k]
#     else:
#         f[v].append(k)
# print(f)
#
# # 2
# r = {}
# for k,v in d.items():
#     if k not in r:
#             r[k] = [v]
#     else:
#             r[k].append(v)
# for g,h in f.items():
#     if g not in r:
#            r[g] = [h]
#     else:
#         r[g].append(h)
# print(r)
#
# # 3
d = {"a":1,"b":2,"c":3,"d":4}
g= []
for k,v in d.items():
    k = list(k)
    k.append(v)
    g.append(k)
print(g)

my_tuple=tuple(tuple(d.items()))
print(my_tuple)
