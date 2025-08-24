import random
class Animal:
    def __init__(self,name,number_of_legs):
        self.name = name
        self.number_of_legs = number_of_legs
    def add_tail(self,length,thickness):
        self.tail = Tail(length,thickness)
class Tail:
    def __init__(self,length,thickness):
        self.length = length
        self.thickness = thickness
class Cat(Animal):
    def __init__(self,color,mustache_length):
        super().__init__("cat", 4 )
        self.color = color
        self.mustache_length = mustache_length
        self.counter_mice=0
    def f(self):
        print("Mouse hunting")
        self.counter_mice +=1
    def get_hunted_mice(self):
        return self.counter_mice

a = Animal("dog", 9)
a.add_tail(5,4)
b = Cat("bk",8)
b.add_tail(1,2)
a1 = Cat("bk",8)
b.f()
b.f()
b.f()
b.get_hunted_mice()
print(b.get_hunted_mice())
print(a1.get_hunted_mice())
print(a.tail.length)





