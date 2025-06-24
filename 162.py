a = [[1,2,3,4,5],
     [6,7,8,9,10],
     [11,12,13,14,15],
     [16,17,18,19,20],
     [21,22,23,24,25]]
b = [[2,3,4,5],
     [7,8,9,10],
     [12,13,14,15],
     [17,18,19,20]]
u = []
for n,m in enumerate(a):
    for i ,v in enumerate(m):
        if b[0][0] == v:
            for c ,d in enumerate(b):
                for g,h in enumerate(d):
                    if b[c][g] == a[n + c][i + g]:
                         u.append(h)
                         if len(u) == len(b) * len(d):
                              print("in")
                    else:
                            print("not in")