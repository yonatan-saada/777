def mini(l,s):
    min = s
    for i in range(s,len(l)):
        if l[i] < l[min]:
            min = i
    return min
def swap(l,i,j):
    l[i],l[j] = l[j] ,l[i]
def sort(l):
    for i in range(len(l)):
        m=mini(l,i)
        swap(l,i,m)
    return l
l = [1,5,8]
print(sort(l))
########## 2
def mini(l,s):
    min = s
    for i in range(s,len(l)):
        if l[i] < l[min]:
            min = i
    return min
def swap(l,i,j):
    l[i],l[j] = l[j] ,l[i]
def sort(l):
    for i in range(len(l)):
        m=mini(l,i)
        swap(l,i,m)
    return "".join((l))
l = "saadalkfg"
l = list(l)
print(sort(l))
###########3
def positive(l):
    r = []
    for i in l:
        if i > 0:
            r.append(i)
    return r
def mini(l,s):
    min = s
    for i in range(s,len(l)):
        if l[i] < l[min]:
            min = i
    return min
def swap(l,i,j):
    l[i],l[j] = l[j] ,l[i]
def sort(l):
    l = positive(l)
    for i in range(len(l)):
        m=mini(l,i)
        swap(l,i,m)
    return l
print(sort([1,-5,-55,80,27,26,24,3,-20]))
######## 4
def mini(l,s):
    min = s
    for i in range(s,len(l)):
        if len(l[i]) < len(l[min]):
            min = i
    return min
def swap(l,i,j):
    l[i],l[j] = l[j] ,l[i]
def sort(l):
    for i,v in enumerate(l):
        m=mini(l,i)
        swap(l,i,m)
    return l
l = ["asa","jh","a"]
print(sort(l))
#######5
def mini(l,s):
    min = s
    for i in range(s,len(l)):
        if l[i] < l[min]:
            min = i
    return min
def swap(l,i,j):
    l[i],l[j] = l[j] ,l[i]
def sort(l,k):
    for i in range(k):
        m=mini(l,i)
        swap(l,i,m)
    return l
l = [15,5,8,6,22,2]
print(sort(l,2))
