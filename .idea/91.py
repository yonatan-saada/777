print("Welcome to our coffee bar!")
print("Please choose a drink:")
print("A. Black Coffee")
print("B. Instant Coffee")
print("C. Hot Chocolate")

choice = input("Enter your choice (A/B/C): ")

if choice == "A":
    print("Your order of Black Coffee is on the way!")
elif choice == "B":
    print("Your order of Instant Coffee is on the way!")
elif choice == "C":
    print("Your order of Hot Chocolate is on the way!")
else:
    print("Invalid choice. Please try again.")
