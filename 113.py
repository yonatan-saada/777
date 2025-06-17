a = int(input("add number: "))
for number in range(2,a):
    c = 2
    while c < number:
        if number % c == 0:
            break
        c+=1
    else:
        print(number)
