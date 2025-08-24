###### 1
b = 0
def mini(l,s):
    min = s
    for i in range(s,len(l)):
        if l[i] < l[min]:
            min = i
    return min
def big(l,s):
    bigi = s
    for i in range(s,len(l)):
        if l[i] < l[min]:
            bigi = i
    return bigi
def swap(l,i,j):
    l[i],l[j] = l[j] ,l[i]
    global b
    b +=1
    return b
def sort(l):
    c = 0
    for i in range(len(l)):
        m=mini(l,i)
        swap(l,i,m)
        c +=1
    return l
def sort1(l):
    c = 0
    for i in range(len(l)):
        m=big(l,i)
        swap(l,i,m)
        c +=1
    return l
def sort2(l):
    c = 0
    for i in range(len(l)):
        m=mini(l,i)
        b = 0
        if i != m :
            b = swap(l,i,m)
            return b
    return b
l = [12,5,4,8,11,2,1]
#print(sort(l))
###     2
def m (a):
    c = 0
    for i  in range(len(a)):
        for v in range(len(a)-1 - i):
            if a[v] > a[v+1]:
                a[v],a[v+1] = a[v+1],a[v]
                c +=1
    return a
def m1 (a):
    c = 0
    for i  in range(len(a)):
        for v in range(len(a)-1 - i):
            if a[v] < a[v+1]:
                a[v],a[v+1] = a[v+1],a[v]
                c +=1
    return a
#print(m([1,5,8,11,-2]))
##### 3
import random
def rando():
    ran = [random.randint(0,10) for i in range(10)]
    print(ran)
    a = m(ran)
    b = sort(ran)
    return a,b
#print(rando())
##### 4
# l = ["gjk","kl","aljk","s"]
# for i in range(len(l)):
#     for v in range(len(l)-1-i):
#         if len(l[v]) > len(l[v+1]):
#              l[v],l[v+1] = l[v+1],l[v]
# print(l)
##### 5
def sorti(l,n):
    a = m(l[:n]) +l[n:]
    b = sort(l[:n])+l[n:]
    return a,b
print(sorti([11,2,55,4,1],3))
#### 6
def y(l):
    a = m(l)
    b = sort(l)
    return a,b
print(y(["sd","as","bh"]))
### 7
def func7(l):
    a = input("a:Sort by selection sort and print number of iterations,"
              "b:Sort by bubble sort and print number of iterations,"
              "c:Partial sorting of the list,"
              "d:Checking whether the list is up to date(a,b,c,d)")
    if a == "a":
        b = input("y:Sort from smallest to largest?n:Sorting from largest to smallest(y,n)")
        if b == "y":
            r = m(l)
            print( r)
        if b == "n":
            r = m1(l)
            print(r)
    if a == "b":
        b = input("y:Sort from smallest to largest?n:Sorting from largest to smallest(y,n)")
        if b == "y":
            r = sort(l)
            print(r)
        if b == "n":
            r = sort1(l)
            print(r)
    if a == "c":
        a = int(input("Select a range"))
        r = m(l[:a])
        print(r)
    if a == "d":
        s = sort2(l)
        if s == 0:
            print("in order")
        else:
            print("no order")
# print(func7([2,51,8,12]))
##### 8
def nn(a,n):
    c = 0
    for i  in range(len(a)):
        for v in range(len(a)-1 - i):
            if a[v][n] > a[v+1][n]:
                a[v],a[v+1] = a[v+1],a[v]
                c +=1
    return a
def func8(l):
    mat = []
    for i in l:
        a = i.split(",")
        mat.append(a)
    a = input("0:Sort list by first name,"
              "1:Sort list by last name,"
              "2:Sort list by age(0,1,2)")
    if a == "0":
        b = input("y:Sort from smallest to largest?,n:Sorting from largest to smallest(y,n)")
        if b == "y":
           mat = nn(mat,0)
           a = [','.join(i) for i in mat]
           print(a)
        if b == "n":
           mat = nn(mat,0)[::-1]
           a = [','.join(i) for i in mat]
           print(a)
    if a == "1":
        b = input("y:Sort from smallest to largest?,n:Sorting from largest to smallest(y,n)")
        if b == "y":
            mat = nn(mat, 1)
            a = [','.join(i) for i in mat]
            print(a)
        if b == "n":
            mat = nn(mat,1)[::-1]
            a = [','.join(i) for i in mat]
            print(a)
    if a == "2":
        b = input("y:Sort from smallest to largest?,n:Sorting from largest to smallest(y,n)")
        if b == "y":
            mat = nn(mat, 2)
            a = [','.join(i) for i in mat]
            print(a)
        if b == "n":
            mat = nn(mat, 2)[::-1]
            a = [','.join(i) for i in mat]
            print(a)
print(func8(["co,yon,21","bh,jhr,17","xn,bn,20"]))














































































































# m = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]
# r = 0
# for i in m:
#     r += i[2]
# s = m[-1]
# for t in  s:
#     r += t
# r -=m[-1][-1]
# print(r)
# j = ["h","e","l"]
# d ={}
# for i,v in enumerate(j):
#     d[v] = i
# print(d)
