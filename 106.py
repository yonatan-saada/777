list = []
list.append(int(input("add a number:")))
list.append(int(input("add a number:")))
list.append(int(input("add a number:")))
list.append(int(input("add a number:")))
list.append(int(input("add a number:")))
list.append(int(input("add a number:")))
a = int(input("select a number: "))
if a in list:
    print("in")
    b= list.index(a)
    print(b)

    if b ==0:
        print(list[b+1])
    elif b== len(list) -1:
        print(list[b-1])
    else:
        print(list[b-1])
        print(list[b+1])