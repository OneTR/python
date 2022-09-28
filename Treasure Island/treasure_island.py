import os

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
cross = input("""You're at a cross road. Where do you want to go? Type "left" or "right". """).lower()

if cross == "left":
    island = input("""You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. """).lower()
    if island == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose? ").lower()
        if door == "blue":
            print("You entered a room of beasts. Game over.")
        elif door == "red":
            print("It's a room full of fire. Game over.")
        elif door == "yellow":
            print("You found the treasure! You win!")
    elif island == "swim":
        print("You have been eaten by crocodiles. Game over.")
elif cross == "right":
    forest = input("""You found a forest, but it's too dark in here and you can get lost easily. Then you saw a light ahead. But you also heard a crackling from your left. Which way are you going to choose, "left" or "ahead"? """).lower()
    if forest == "left":
        print("That crackling was a wolf. It jumped on you and dismembered you. Game over.")
    elif forest == "ahead":
        shack = input("""You saw that the light comes from a little shack. You looked inside through the window stealthily, but no one is inside. No one's nearby, either. Do you want to enter the shack, or do want you wait for to light go off? Type "enter" or "wait". """).lower()
        if shack == "enter":
            inside = input("You sneaked in from the window. You saw an old man in the next room. Looks like the shack is not empty. You dropped a cup when you were entering the shack. The old man heard it and now see you. What are you going to do? ").lower()
            if inside == "fight" or inside == "kill":
                print("The old man had a rifle. He grabbed it and shot you. Game over.")
            elif inside == "hide":
                hiding = input("You immediately jumped off from the window and bended down. The old man fired his rifle, but he missed. Then you sneakily moved to back of the shack. The old man got outside, looking for you. Then you saw a silhouette of something behind the trees. It was not the old man, it was something that walks on its four legs. Do you want to wait for old man to go inside, or sneak in again? ").lower()
                if hiding == "wait":
                    print("The silhouette came closer and you realized it was a wolf pack. They encircled you and one of them attacked you from your throat. Game Over.")
                elif hiding == "sneak in":
                    whistle = input("The silhouette came closer and you realized it was a wolf. They must have come to the gunfire. But you had a plan. Just before you sneak in, you blew a whistle and jumped in to the shack again. The old man came to the back of the shack. The wolves encircled the old man. He shot few of the wolves but there were too many. Then he lost the fight and the wolves dismembered and ate him. Finally the old man was gone, but another danger was still there. You can go and look outside or you can search the shack for some items. ").lower()
                    if whistle == "go out":
                        print("The wolf pack was still there. They surrounded you and dismembered you. Game over.")
                    elif whistle == "search":
                        print("You've found a ton of precious jewellery in the closet! You win!")
        elif shack == "wait":
            print("You waited too long that a wolf pack surrounded you. They dismembered and ate you. Game over.")
os.system("pause")