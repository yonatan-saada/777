class Room:
    def __init__(self,area = 4,doors = 1,windows = 1):
        self.area = area
        self.doors = doors
        self.windows = windows
class Bedroom(Room):
    def __init__ (self,area = 4,doors = 1,windows = 1):
        super().__init__(area,doors,windows)
        self.bed_size = 0
    def add_bed(self,bed_size):
        if bed_size > self.area:
            return "no"
        else:
            self.bed_size = bed_size
            return " "
class Bathroom(Room):
    def __init__(self,area = 4,doors = 1,windows = 1):
        super().__init__(area,doors,windows)
        self.shower = False
        self.bathtub = False
    def add_bathroom(self,choice):
        if choice == "shower":
            self.shower = True
        if choice == "bathtub":
            self.bathtub = True
        else:
            print("Unauthorized selection")
class Flat:
    def __init__(selfׁׁׁ):
        selfׁׁׁ.room = []
    def add_room(self,room:Room):
        self.room.append(room)
a = Flat()
b = Room(8,9,5)
c = Bedroom(8,8,8)
d = Bathroom(1,1,1,)
d.add_bathroom("shower")
c.add_bed(7)
a.add_room(b)
a.add_room(c)
a.add_room(d)
print(a.room[0].doors)
print(a.room[1].area)
print(a.room[1].bed_size)
print(a.room[2].shower)
print(a.room[2].bathtub)


