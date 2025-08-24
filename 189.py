def bubble(l):
    n = len(l)
    for i in range(n):
        g = False
        for j in range(n-i-1):
            if l[j] > l[j+1] :
                l[j],l[j+1] = l[j+1],l[j]
                g = True
        if not g:
            break
    return l
print(bubble([1,8,9,45,2,4,5]))


















# import random
# x = [random.randint(1,100)for i in range(100)]
# print(x)

