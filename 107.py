a = [1,4,0,2,8]
print(a[-2])
print(a[3:5])
print(a[::-1])
a.insert(0,5)
print(a)
print(a.pop(5))
a.remove(5)
if 0 in a:
    print("true")
else:
    print("false")
print(a.index(0))
print(a)
b = [a[0],a[1],a[2]]
print(b)
a.insert(0,3)
c = [a[2],a[3],a[0]]
print(c)
a.append(8)
d = [a[5],a[4],a[3]]
print(d)

print(b)
print(c)
print(d)
m = b,c,d
print(m[2][1])
r = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
    ]
print(len(r))
print(len(r[0]))
print(*r,sep= '\n')
print(*r[::-1],sep='\n')
