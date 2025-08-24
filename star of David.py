a = int(input("add a number: "))
b = int(input("add a number: "))
n = a
c = 1
l = 1
g = 1
k = False
for i in range (1,a + b+1):
    if i == 1 or i == a+b:
        print(" "*(a-1) + "/")
    elif 1 < i < b+1:
        print(" "*(n-2)+"/"+" "*g+"/")
        n-=1
        g+=2
    elif i == a or i == b+1:
        print("/"*(a*2-1))
    elif b < i < a :
        if i <= (a+b)//2:
             g +=2
             print(" " * (i-b-1)+"/"+" " *((a-i)-(i-b))  + "/"+" "* (g)+"/"+" "* ((a-i)-(i-b))+"/")
             c += 1
        elif i == (a+b)//2+1 :
            if (a+b) % 2 == 0:
                print(" "*(((a-b)//2)-1)+"//"+" "*((a+b-2)-1)+"//")
                c -=1
            else:
                print(" " * ((a - b) // 2) + "/" +" " * (a + b - 2) + "/")
        else:
            if (a+b) % 2 == 0:
                c -= 1
                print(" " * (c) + "/"+" "*(l+1)+"/"+" "* (g-2) + "/"+" "*(l+1) + "/")
                g-=2
                l+=2
            else:
                c -= 1
                print(" " * (c) + "/" + " " * (l) + "/" + " " * (g) + "/" + " " * (l) + "/")
                g -= 2
                l += 2
    elif a < i < a+b+1:
        if (a+b) % 2 == 0:
            if not k:
                u = g -2
                k = True
            u -=2
            print(" "*(n-1)+"/"+" "*(u)+"/")
        else:
            g-=2
            print(" " * (n - 1) + "/" + " " * (g) + "/")
        n+=1
