age = float(input("how old are you? "))
height = float(input("how tall are you? "))
weight = float(input("what is your weight? "))
Height_to_weight_ratio = height / weight
if 0 > age or age >120:
    print("There is no proper menu")
elif  Height_to_weight_ratio < 0.5 or Height_to_weight_ratio >5:
    print("There is no proper menu")
if 0.5 < Height_to_weight_ratio < 2:
    print("Your menu is: menu a")
elif 2 < Height_to_weight_ratio < 3.5:
    if 11 < age <40:
        print("your menu is: menu b")
    elif 40 < age < 120:
        print("your menu is: menu c")
elif 3.5 < Height_to_weight_ratio <5.0:
    if 11 < age <20:
        print("your menu is: menu C")
    elif 20 <age < 40:
        print("your menu is: menu a")
    elif 40 < age < 120:
         print("your menu is: menu c ")




