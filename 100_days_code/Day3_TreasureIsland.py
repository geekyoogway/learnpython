print('''
'_                                     
| |                                    
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ 
| __| '__/ _ \/ _` / __| | | | '__/ _ \
| |_| | |  __/ (_| \__ \ |_| | | |  __/
 \__|_|  \___|\__,_|___/\__,_|_|  \___|''')


print('Welcome to Treasure Island. Your mission is to find the treasure')
print("Your mission is to find the Treasure\n")
name = input("Enter Your Name\n")
print(f"Lets start treasure hunting {name}\n")


crossroadsidelst=["left","l"]
swimoptionlst = ["wait","w"]
red=["red","r"]
blue= ["blue","b"]
yellow = ["yellow","y"]
crossroadside = input("You are at a cross road. Which side do you want to go. Right or Left?\n")

if crossroadside.lower() in crossroadsidelst:
    print("Good. Please walk towards the river")
    swimoption = input("There is river. Do you want to swim or wait for a ferry. Enter wait or swim?\n")

    if swimoption.lower() in swimoptionlst:
        print("Good. Walk towards the palace")
        door = input("You arrive at a palace. There are number of doors. Blue, Red, yellow. Choose one?\n")

        if door.lower() in red:
            print("Burned by fire.Game Over.")
        if door.lower() in blue:
            print("Eaten by beasts.Game Over.")
        if door.lower() in yellow:
            print("You Win!")
            print("Treasure is all yours")
    else:
        print("Attacked by trout.Game Over.")
else:
    print("Fall into a hole. Game Over.")



