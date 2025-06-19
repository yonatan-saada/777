a = int(input("add a number: "))
b = int(input("add a number: "))
n = a
c = 1
t =b + 2
d = a // 2 + a//7
h = a//2
l = 1
g = 1
for i in range (1,a + b+1):
    if i == 1 or i == a+b:
        print(" "*(a-1) + "/")
    elif i == a or i == b+1:
        print("/"*(a*2-1))
    elif b < i < a :
        if i <= (a+b)//2:
             print(" " * (i-b-1)+"/"+" " *((a-i)-(i-b))  + "/"+" "* ((a-b)+2*(i-6)-2)+"/"+" "* ((a - b) - 2 * (i - 4))+"/")
             d += 2
             c += 1
             h -= 2
             t -= 2
        elif i == (a+b)//2+1:
             print(" "*((a-b)//2)+"/"+" "*(a+b-2)+"/")
        else:
            d -= 2
            c -= 1
            print(" " * (c) + "/"+" "*l+"/"+" "* (d) + "/"+" "*l + "/")
            #d-=2
            #c -= 1
            l+=2
    elif 1 < i < b+1:
        print(" "*(n-2)+"/"+" "*g+"/")
        n-=1
        g+=2
    elif a < i < a+b+1:
        g-=2
        print(" "*(n-1)+"/"+" "*(g)+"/")
        n+=1