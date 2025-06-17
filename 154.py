a = int(input("Select a number: "))
b = int(input("select number: "))
c = int(a)
p = 8
h = 2
s = 1
j = 0

y = b + 2
for i in range(1,a+1):
    c -= 1
    m = c -1
    if i == 1:
        print(" " * c + "/")
    elif i == 2 :
        print(" "* m,"/" " " "/")
    elif i == a  :
        print(a * 2 * "/")
    elif  b + 1 == i:
        print(a * 2 * "/")
    elif i <= b:
        h += i - 2
        if  i > 0 :
           print(" " * c + "/" + " " * h , "/")
    elif b*2 + 2 == i:
        print(" " * s + "/"," "*(c*3+2) +"/")
    elif b*2 + 2 < i:
        print(" "* c + "/"," " *j +"/"," "* s+ "/")
        j +=2
    else:
        if i != a:
            if i != b + 1:
                if i >= b:
                    if i <=a:
                        p += 2
                        print(" " * s + "/" + " " * (c-s-2)  , "/" + " " * p + "/"," "* y + "/")
                        s +=1
                        y -=2

