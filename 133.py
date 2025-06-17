# 1
# def jump ():
#       return "jump ...3...2...1"
# print(jump())
# 2
# def wake_up():
#      return  "wake up"
# def eat_breakfast():
#     return  "eat breakfast"
# def go_to_school():
#     return  "go to school"
# print(wake_up(),eat_breakfast(),go_to_school())
# 3
complete_mission = False
def drive():
    return "The paramedic is riding in an ambulance to save someone."
def save_people():
    global complete_mission
    complete_mission = False
    return "Paramedic saves people"
def return_to_base():
    return "Paramedic returns to base"
print(drive(),save_people(),return_to_base())
if complete_mission == True:
    print("The task was successfully completed.")
else:
    print("Mission failed")
# 4
coffee_ready = False
def boil_water():
    return "Boils water"
def brew_coffee():
    return "making coffee"
def add_sugar():
    return "Adds sugar"
def serve_coffee():
    global coffee_ready
    coffee_ready = True
    return "Serves coffee"
print(boil_water()," ",brew_coffee()," ",add_sugar()," ",serve_coffee())
if coffee_ready == True:
    print("The coffee is ready")
elif coffee_ready == False:
    print("Something went wrong with the coffee.")
