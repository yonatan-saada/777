# def make_a_list():
#     a = []
#     while True:
#         b = input("add a number: ")
#         if b == 'exit':
#             break
#         a.append(int(b))
#     return a
# def number_in(a,c):
#     for i in a:
#         if i == c:
#             return "in"
#     return "not in"
# a = make_a_list()
# c = int(input("select a number"))
# print(number_in(a,c))
# def make_a_list_str():
#####2
#     a = []
#     while True:
#         b = input("add a word (to stop write 'exit' ): ")
#         if b == 'exit':
#             break
#         a.append(b)
#     return a
# def word_in(a,c):
#     for i in a:
#         if i == c:
#             return "in"
#     return "not in"
# a = make_a_list_str()
# c = input("select a word: ")
# print(word_in(a,c))
######3
# def make_a_list1():
#     a = []
#     while True:
#         b = input("add a number: ")
#         if b == 'exit':
#             break
#         a.append(int(b))
#     return a
# def to_number_in(a,b,c):
#      for i,v in enumerate(a):
#         if v == b:
#             if a[i+1] == c :
#                 return "in"
#      return "not in"
# a = make_a_list1()
# b = int(input("select a number"))
# c = int(input("select a number"))
# print(to_number_in(a,b,c))
####
# m = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]
# x = int(input("select a number: "))
# for i ,v in enumerate(m):
#     for b,c in enumerate(v):
#         if c == x:
#             print("  in \n External index " ,i,"\n internal index",b)
m = [[1,4,7],
     [2,5,8],
     [3,6,9]]
l = [1,2,3,4,5,6,7,8,9,10]
a = 10



