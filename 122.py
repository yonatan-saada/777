p = 1
i = []
while p >0:
    u = int(input("add a number: "))
    i.append(u)
    if u < 0:
        i.pop(-1)
        print(sum(i))


