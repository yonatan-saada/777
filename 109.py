#1
set_of_booleans = {True, False}
set_of_ints = {1,2,3}
set_of_floats = {5.0,4.2,8.5}
#2
#print(set_of_ints[0])
set_of_floats.add(1)
print(set_of_floats)
print(len(set_of_ints))
set_of_ints.add(3)
print(len(set_of_ints))
#3
numbers = {"a":100,"b":200,"c":300,"d":400,"e":500}
print(numbers["a"])
print(numbers["b"])
print(numbers["c"])
print(numbers["d"])
print(numbers["e"])
numbers.pop("d")
del numbers["e"]
numbers["a"] = 101
numbers["b"] = 201
numbers["c"] = 301
print(numbers)
#4
#a = {1: "hello",2:"world", 3:"are"}
#b = {True:[10,11,1,1], False:[0,0,5,]}
#c = {(777):{"dan" ,"ben","eli"},(999):{"df","jk","rt"}}
#d = {{"a","b","c"}:22,{"n","m","l"}:56}
#e = {["a","b","c",]:True,[1,2,3]:False}
#f = {{"g":2}:"hello",{"p":5}:"world"}
#5
names = ["or","dan","yehonatan","roman","bar"]
year_of_birth = (2004,2003,1999,1980,1948)
native_land = ("israel","france","greece","use","uk")
print(names[0],year_of_birth[0],native_land[0])
print(names[1],year_of_birth[1],native_land[1])
print(names[2],year_of_birth[2],native_land[2])
print(names[3],year_of_birth[3],native_land[3])
print(names[4],year_of_birth[4],native_land[4])
#6
f = [ 1,2,3]
h = [4,5,6]
v = [7,8,9]
m = (1,2,2)
r = (4,5,6)
q = (7,8,9)
ab = "df"
sd = "fg"
ty = "ert"
er = {4,5,5}
fg = {5,8,9}
we = {8,7,8}
tuple(f)
str(h)
set(v)
list(m)
str(r)
set(q)
list(ab)
tuple(sd)
set(ty)
str(er)
list(fg)
tuple(we)
#7
price_list = {"milk": 50 , "agg": 70, "water": 30}
price_list["milk"] = 60
price_list["agg"] = 20
price_list["water"] = 60
for t in range(10):
    print("print")
print(len(er))












