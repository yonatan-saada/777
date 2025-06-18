a = int(input("add a number: "))
b = int(input("add a number: "))
n = a -1
c = 0
t =b + 2
d = a // 2
h = b * 2 -2
l = 0
g = 0
for i in range (1,a + b+1):
    if i == 1 or i == a+b:
        print(" "*(a-1) + "/")
    elif i == a or i == b+1:
        print("/"*(a*2))
    elif b < i < a :
        if i <= (a+b)//2:
             print(" " * c,"/"," " *(h)  + "/"," "* (d+1),"/"+" "*(h),"/")
             d += 2
             c += 1
             h -= 2
             t -= 2
        elif i == (a+b+1)//2:
             print(" "*b,"/"," "*(a+1),"/")
        else:

            print(" " * c + "/"," "*l+"/"," "* d +"/"," "*l + "/")
            d-=2
            c -= 1
            l+=2
    elif 1 < i < b+1:
        print(" "*(n-1)+"/"," "*(g+1)+"/")
        n-=1
        g+=2
    elif a < i < a+b+1:
        g-=2
        print(" "*n+"/"," "*(g+1)+"/")
        n+=1
