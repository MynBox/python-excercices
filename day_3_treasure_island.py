print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input(f'You are now at a crossroad, where do you want to go ? Type "Left" or "Right" \n ').lower()
if direction == "left":
    lake_choice = input("You've come to a lake, there is an island in the middle of the lake. What do you want to do ? type \"Wait\" to wait for a boat or \"Swim\" to swim across. \n ").lower()
    if lake_choice == "wait":
        print("A boat came and took you to the island")

        door_colour = input("You are in front of a house with 3 different doors. A red, blue and yellow one. Which color do you choose ? Type \"Red\", \"Blue\" or \"Yellow\" \n ").lower()
        if door_colour == "red":
            print("It's a room full of fire. You died by the flames")
        elif door_colour == "blue":
            print("It's a room full of water. You got drowned")
        elif door_colour == "yellow":
            print("You found the treasure! You win!")
        else:
            print("Game Over.")
    
    

    
    else:
        print("You got attacked by an angry trout. Game over.")
        
    
else:
    print(f"You fell into a hole. Game over")

input("Press [Enter] to exit")



