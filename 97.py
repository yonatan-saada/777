print("1. Floor\n2. Ceil\n3. Round")
c = int(input())
n = float(input())
if c == 1: print(math.floor(n))
elif c == 2: print(math.ceil(n))
elif c == 3: print(round(n))
else: print("Invalid")
