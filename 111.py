y = {"a":0,"b":1,"c":2,"d": 1}
r ={}
for a ,b in y.items():
    if b in r:
        r[b].append(a)
    else:
       r[b] = [a]
print(r)