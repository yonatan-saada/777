text = "this is the text"
registered_users = {}
while True:
    user_selection = input("your choices: a:Login to the system b:Create a user c:Exit the system:    (a,b,c)  :")
    if user_selection == "a":
         user_name = input("user name: ")
         if user_name not in registered_users.keys():
             print("User does not exist")
         elif user_name in registered_users.keys():
             p = 0
             while p < 3:
                 password = input("password: ")
                 if password not in registered_users.values():
                     print("Incorrect password")
                     p +=1
                 elif password in registered_users.values():
                     print("Welcome to the system")
                     u = input("""Choose an option:
                           a:Print text
                           b:Change password
                           c:Delete a user
                           d:Exit the browser and return to the main menu.
                           e:Exit the system (a,b,c,d,e)  :  """)
                     if u == "a":
                         print(text)
                     elif u == "b":
                         new_password = input("Choose a new password: ")
                         registered_users[user_name] = new_password
                     elif u == "c":
                         registered_users.pop(user_name)
                     elif u == "d":
                         break
                     else:
                         exit()
    elif user_selection == "b":
        new_username = input("Add a username: ")
        new_user_password = input("add a password: ")
        registered_users[new_username] = new_user_password
    elif user_selection == "c":
        exit()
    elif user_selection == "*":
        break





