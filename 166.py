m = [[1,2,3],
     [4,5,6],
     [7,8,9]]
def sum (m):
    s = 0
    for i,v in enumerate(m):
        for g,m in enumerate(v):
            if g == 0:
                s+=m
            elif i == g:
                if i !=0:
                    s +=m
    return s
# print(sum(m))
def v(z):
    m = [ ]
    a = z [::-1]
    for i in range(len(z)):
        if i % 2 == 0:
            m.append(z)
        else:
            m.append(a)
    return m
# print(v([1,2,3]))


def b (l):
    a = int(input("add"))
    for i in l:
        if a < i:
            return i
            break
    else:
        print("not")
        return a
# print(b([1,2,3,4,5]))


def num (l):
    r =[]
    while l:
        s =""
        for i in (range(1)):
            s += "#" * l.pop(0)
        r.append(s)
    return r [::-1]
print(num([2,4,1]))

# def num(l):
#     r = []
#     while l:
#         s = ""
#         r.append("#" * l.pop(0))
#     return r[::-1]
# print(num([2, 4, 1]))

