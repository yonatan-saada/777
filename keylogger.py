# from pynput.keyboard import Listener
# s = ""
#
# def keylogger(key):
#     key = str(key).replace("'", "")
#     if key == 'Key.space':
#         key = ' '
#     if key == 'Key.enter':
#         key = '\n'
#     if key == 'Key.up':
#         key = ''
#     if key == 'Key.right':
#         key = ' '
#     if key == 'Key.left':
#         key = ''
#     if key == 'Key.down':
#         key = '\n'
#     if key == 'Key.ctrl_l':
#         key = 'ctrl '
#     if key == '\\x03':
#         key = 'copy '
#     if key == 'Key.backspace':
#         key = ''0
#     if key == '\\x18':
#         key = 'cut '
#     if key == '\\x16':
#         key = 'paste '
#     if not key.isalpha() or key.isnumeric():0

####11111
# a = [1,2,3,2,5,6]
# def f (a):
#     for i  in range(len(a)):
#         for v in range(len(a)):
#             if a[i] > a[v]:
#                 a[i],a[v] = a[v],a[i]
#     return a[::-1]
# print(f([1,2,3,4,9,5,11,5,8]))
# ######222222

def m (a):
    for i  in range(len(a)):
        for v in range(len(a)-1-i):
            if a[v] > a[v+1]:
                a[v],a[v+1] = a[v+1],a[v]
    return a
print(m([1,22,3,4,9,5,11,5,8]))
# #######333333
# def quick(l):
#     if len(l) <= 1:
#         return l
#     p = l[len(l) // 2]
#     s = []
#     for i in l:
#         if i < p:
#             s.append(i)
#     b = []
#     for i in l:
#         if i == p :
#             b.append(i)
#     c = []
#     for i in l:
#         if i > p:
#             c.append(i)
#     return quick(s) + b + quick(c)
# print(quick([1,2,-3,4,9,5,11,-555,1118]))
#
#
#
# # ###3333333########
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
print(merge_sort([12,2,5]))
#
#
#
# # def d (a,b):
# #     r= a * b
# #     return r
#
#
#
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
l = [12,5,4,8,11,2,1]
print(sort(l))
def facturial(n):
    if n == 1:
        return n
    return facturial(n-1) * n
print(facturial(6))
def f(n):
    if n <= 1:
        return n
    return f(n-1) + f(n -2)
print(f(10))








