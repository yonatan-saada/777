a = [-4,-3,4,-1,-2,1,5,-3]
b = []
c = []
for i in range(len(a)):
    for v in range(i+1,len(a)+1):
        b = a[i:v]
        if sum(b) > sum(c):
            c = b
print(c)
