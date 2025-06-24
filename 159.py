# def half_list(l):
#     for i in range(len(l)//2):
#         print( l[i],end=" ")
#     print()
#     for i in range(len(l)//2,len(l)):
#         print(l[i],end=" ")
#     return " "
# print(half_list([1,2,5,6]))
# הסיבוכיות נשארת זהה מכיוון שזה עדיין תלוי בקלט המשתמש o(n)
# def num (l):
#     for i in l:
#         print(i,i)
#     return " "
# print(num([1,2,3,4]))
#o(2n) הסיבוכית עדיין תלויה בגודל הקלט
# def min (l):
#     g = l[0]
#     for i in l:
#         if i < g:
#             g = i
#     return  g
# print(min([4,5,6,8,2,12,-5]))
#o(n) כרגע הסיבוכיות  o(1)במידה ומדובר ברשימה מאורגת ניתן לצמצם ל
# def even(l):
#     o = 0
#     for i  in l:
#         if i % 2 == 0:
#             o +=i
#     return o
# print(even([2,8,6,4]))
# סיבוכית o(n)
# def positive(l):
#     a = []
#     b = []
#     for i in l:
#         if i > 0:
#             a.append(i)
#         else:
#             if len(a) > len(b):
#                 b = a
#             a = []
#     if len(a) > len(b):
#         b = a
#     a = []
#     return (b)
# print(positive([2,1,-3,-5,5,4,1,-9,-9,-5,2,3,4,8]))
# סיבוכיות o(n)
# def even (l):
#     for i in l:
#         for v in l:
#             print(i,v)
#     return " "
# print(even([1,2,5,8,6]))
# סיבוכיות o(n**2)
c = 0
# def duplicate_number(l):
#     s = set()
#     for i,v in enumerate(l):
#         for g,m in enumerate(l):
#             if m == v and i !=g:
#                 s.add(m)
#     return s
# print(duplicate_number([1,2,2,3,5,7,8,7,8]))
# o(n**2)
################################################
# 9

def fun(n):
     for i in range(n):
         print(i * n)
print(fun(10))
#o(n)
def fun_time(n):
   k = 0
   for i in range(n):
        for j in range(n // 2):
            k += 1
            print(i + j)
print(fun_time(9))








