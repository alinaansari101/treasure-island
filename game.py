print("""
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'" =.__________________|_______
|                   |    __.--" , ; `"=._o." ,-""''-._ ".   |
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
""")


print("Welcome to to treasure island!")
print("You have come here in search of treasure.\n")


crossroad = input("You are at a crossroad, which way do you choose to go? Type 'left' or 'right' ")

if crossroad == "right" or crossroad == "Right":
  print("\nYou drown in quicksand, You died.")

elif crossroad == "left" or crossroad == "Left":
   swim = input("\nYou reach a lake. There is land across it. Type 'wait' to wait for a boat. Type 'swim' to swim across it ")
  
   if swim == "swim" or swim == "Swim":    
     print("\nThere were piranhas in the lake, You died.")
     
   elif swim == "wait" or swim == "Wait":
      cave = input("\nYou arrive at the island unharmed. There is a cave with three entrances. Type 'left' to go in the left entrance,'middle' to go in the middle one and 'right' to go in the right one. ")
     
      if cave in ["left", "Left", "right", "Right"] :
        print("You entered a room full of the undead, You died.")
        
      elif cave == "middle":
        print("\nYou found the treasure, You win! ")
     


 
