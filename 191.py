# 1
# def binari(l,n):
#     low  = 0
#     high = len(l)-1
#     while low <= high:
#         mid = (low+high)//2
#         if l[mid] == n:
#             return mid
#         elif l[mid] < n :
#             low = mid +1
#         else:
#             high = mid -1
#     return "not found"
# l = [12,22,54]
# print(binari(l,54))
# 2
# def binari(l,n):
#     low  = 0
#     high = len(l)-1
#     while low <= high:
#         mid = (low+high)//2
#         if l[mid] == n:
#             return mid
#         elif l[mid] < n :
#             low = mid +1
#         else:
#             high = mid -1
#     return "not found"
# l = ["zx","lk","jk"]
# print(binari(l,"jk"))
# 3
# def binari(l,n1,n2):
#     low  = 0
#     high = len(l)-1
#     while low <= high:
#         mid = (low+high)//2
#         if l[mid] == n1:
#             if l[mid+1] == n2:
#                return "in"
#             else:
#                 return "not in"
#         elif l[mid] < n1 :
#             low = mid +1
#         else:
#             high = mid -1
#     return "not found"
# l = [11,12,21,54]
# print(binari(l,12,21))
# 4
# def ma(m,c):
#     for i,v in enumerate(m):
#         f = False
#         for a,b in enumerate(v):
#             if c == b:
#                print(i,a)
#                f =  True
#     if not f:
#         print("not in")
#     return " "
# print(ma([[1,2,3],[4,5,6],[7,8,9]],3))
# 4,2
def binari_mat(m, n):
    for i in m:
        low = 0
        high = len(i) - 1
        while low <= high:
            mid = (low + high) // 2
            if i[mid] == n:
                return mid
            elif i[mid] < n:
                low = mid + 1
            else:
                high = mid - 1
    return "not found"
#print(binari_mat([[1,2,3],[4,5,6],[7,8,9]],1))
# 5
def binarit(m, n):
        low = 0
        high = len(m) - 1
        while low <= high:
            mid = (low + high) // 2
            if m[mid] == n:
                return True
            elif m[mid] < n:
                low = mid + 1
            else:
                high = mid - 1
        return False
# 6
def f (l):
    return l[0],l[-1]
# 7
def binari(l,n):
    low  = 0
    high = len(l)-1
    while low <= high:
        mid = (low+high)//2
        if l[mid] == n:
            return mid
        elif l[mid] < n :
            low = mid +1
        else:
            high = mid -1
    return "not found"
# 8
def binarin(l):
    low  = 0
    high = len(l)-1
    while low <= high:
        mid = (low+high)//2
        if l[mid] == True:
            high = mid -1
        elif l[mid] == False:
            if l[mid+1] == True:
                return mid
            else:
                low = mid+1
    return " "
print(binarin([0,0,0,0,0,1,1,1,1,1]))


def binarit(l, n):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] == n:
            return True
        elif l[mid] < n:
            low = mid + 1
        else:
            high = mid - 1
    return False
l = [1,2,3,4,5,6,7,8,9,10]







