def cal (a,b):
    list = []
    add = a+ b
    sub = a-b
    list.append(add)
    list.append(sub)
    return list
print(cal(5,8))
def sum(*number):
    sum1 = 0
    for i in number:
        sum1 += i
    return sum1
print(sum(5,2,5,5,2,5,2,5,))
def name(**names):
    for k,v in names.items():
         print (k,v)
def user():
    data={}
    nam = input("your name: ")
    age = input("your age: ")
    phon = input("your phon: ")
    data["name"] = nam
    data["age"] = age
    data["phon"] = phon
    return data
print(name(**user()))










