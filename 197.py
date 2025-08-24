class Bank:
    def __init__(self,balance,first_name,last_name):
        self.__balance = balance
        self.first_name = first_name
        self.last_name = last_name
    @property
    def balance(self):
        return self.__balance
    def duspit(self,sum):
        self.__balance += sum
    @property
    def full_name(self):
        return f"{self.first_name}{self.last_name}"
    @full_name.setter
    def full_name(self,full_name):
        a = full_name.split(" ")
        self.first_name = a[0]
        self.last_name = a[1]
    def __str__(self):
        return f"the name is {self.first_name} {self.last_name} the balance {self.balance}"
    def __repr__(self):
        return "this func is for create bank acuont"
a = Bank(1000,"yonatan","sad")
b = Bank(850,"avi","cheon")
b.duspit(1000)
print(b)









class Ax:
    def __init__(self,data):
        self.data = data
        self. next = None
fir = Ax(1)
sec = Ax(2)
tre = Ax(3)
fir.next = sec
sec.next = tre
tre.next = None
temp = fir
while temp:
    print(temp.data, end="")
    temp = temp.next
print(fir.next.next.data)










# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None
#
# class BinaryTree:
#     def __init__(self):
#         self.root = None
#
#     def is_empty(self):
#         return not self.root
#
#     def add_node(self,data):
#         def add_node_req(root,data):
#             if not root:
#                 return Node(data)
#             if data > root.data:
#                 root.right = add_node_req(root.right, data)
#             else:
#                 root.left = add_node_req(root.tleft, data)
#             return root
#         self.root = add_node_req(self.root, data)
#
#     def print_tree(self):
#         def print_tree_req(root):
#             if not root:
#                 return
#             print_tree_req(root.left)
#             print(root.data)
#             print_tree_req(root.right)
#         print_tree_req(self.root)
#
#     def search_node(self,data):
#         def search_node_req(root,data):
#             if not root:
#                 return None
#             if data > root.data:
#                 return search_node_req(root.right, data)
#             else:
#                 return search_node_req(root.left, data)
#         return  search_node_req(self.root,data)
#
#     # def delite(self,data):
# s = [1,2,3,4]
# print(s[0:3])
# print(s[4:1:-1])
# print(s.index(1))
# l = [1,2,3,4,5]
# def fll(l):
#    for i in l:
#       yield i + 1
# g = fll(l)
# next(g)




