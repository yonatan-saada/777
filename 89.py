request=int(input("Choose a number between 1 and 1000000? "))
if request < 0:
    print("Invalid input")
if request > 1000000:
    print("invali input")
if request > 1 and request  <500000:
    print("It's a small number")
if request > 500000 and request <750000:
    print("This is an average number")
if request > 750000 and request <1000000:
    print("That's a big number")