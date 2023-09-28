'''
    A text-based clone of a popular game.
    Written by:
'''

from random import randint
from time import sleep
import miscStuffLib

characters = ["The vampire", "The very dangerous sheep", "Desmond the moon bear"]

# These will deal damage to the opponent
goodAttacks = {
    "The vampire": ["flashlight", "silver", "extracted teeth", "take off shoes"],
    "The very dangerous sheep": ["stand tall", "bark", "pull wool", "throw a stinky sock"],
    "Desmond the moon bear": ["Answer their question", "make a flame", "grab ears"]
}

# These will deal damage to the player
damageDealers = {
    "The vampire": ["trick", "bite", "paralyse", "litte curse"],
    "The very dangerous sheep": ["bonk", "bite", "trample", "deafening blah"],
    "Desmond the moon bear": ["How did I get here", "bite", "scratch", "run into"]
}

chosenOne = characters[randint(0, 2)]
liGoodAttacks = goodAttacks[chosenOne]
liDamageDealers = damageDealers[chosenOne]

def proposeAttacks(inventory):
    proposedAttacks = goodAttacks[chosenOne]
    if "garlicbread" in inventory:
        proposedAttacks.insert((randint(0, len(proposedAttacks))), "garlicbread")
    print("You have the following attacks available to you:\n")
    print(proposedAttacks, '\n')

def battler(inventory):
    opponentLife = 100
    playerLife = 101
    print(f"You will have to battle {chosenOne} to continue!")
    while opponentLife > 0 and playerLife > 0:
        if chosenOne == "The vampire":
            print(f"You have {playerLife} life left. {chosenOne} has {opponentLife} left")
            print("Your turn!")

            proposeAttacks(inventory)
            attack = input("Which will you choose? (enter without quotation marks) ")
            if attack == "garlicbread":
                print("This vampire really likes garlic bread! You share the bread and no damage was dealt.")
            elif attack == "flashlight":
                print("You pulled out a high power flashlight! The vampire fell to its knees.")
                opponentLife -= randint(10, 28)
            elif attack == "silver":
                print("You pulled out a spoon! The vampire does not like spoons.")
                opponentLife -= randint(10, 28)
            elif attack == "extracted teeth":
                print("Why do you even have a handful of teeth on you?")
                opponentLife -= randint(10, 28)
            elif attack == "take off shoes":
                print("The vampire dislikes bare feet a lot!")
                opponentLife -= randint(30, 50)
            else:
                print("That was not a valid attack. You've just played your turn!")
            sleep(2)

            if opponentLife > 0:
                print("\nNow it's the vampire's turn")
                sleep(1)
                counterAttack = liDamageDealers[randint(0, len(liDamageDealers)-1)]
                if counterAttack == "trick":
                    print("The vampire does a little trickery!")
                    playerLife -= randint(10, 28)
                elif counterAttack == "bite":
                    print("The vampire bites you! Yeouch!")
                    playerLife -= randint(30, 50)
                elif counterAttack == "paralyse":
                    print("The vampire paralyses you. You fall over hit the ground really hard.")
                    playerLife -= randint(10, 28)
                elif counterAttack == "little curse":
                    print("The vampire lets out a little curse. That hurt!")
                    playerLife -= randint(10, 28)

                sleep(2)
            else:
                print(f"{chosenOne} has lost!")
                sleep(2)
            miscStuffLib.clear() # PUT THIS AFTER THE ATTACK IS DEALT

        elif chosenOne == "The very dangerous sheep":
            print(f"You have {playerLife} life left. {chosenOne} has {opponentLife} left")
            print("Your turn!")

            proposeAttacks(inventory)
            attack = input("Which will you choose? (enter without quotation marks) ")
            if attack == "stand tall":
                print("You decided to stand tall. That spooked the sheep!")
                opponentLife -= randint(10, 28)
            elif attack == "bark":
                print("What are you? A dog? Scared the sheep though.")
                opponentLife -= randint(10, 28)
            elif attack == "pull wool":
                print("You pulled out a hand of wool. That hurt the sheep.")
                opponentLife -= randint(10, 28)
            elif attack == "throw a stinky sock":
                print("That's a really bad smell...")
                opponentLife -= randint(30, 50)
            else:
                print("That was not a valid attack. You've just played your turn!")
            sleep(2)

            if opponentLife > 0:
                print("\nNow it's the sheep's turn")
                sleep(1)
                counterAttack = liDamageDealers[randint(0, len(liDamageDealers)-1)]
                if counterAttack == "bonk":
                    print("The sheep bonks its head into your leg")
                    playerLife -= randint(10, 28)
                elif counterAttack == "bite":
                    print("The sheep bites you! Yeouch!")
                    playerLife -= randint(10, 28)
                elif counterAttack == "deafening blah":
                    print("A deafening BLAAHHHHHH! the sheep let out.")
                    playerLife -= randint(10, 28)
                elif counterAttack == "trample":
                    print("You were pushed over and are now being trampled.")
                    playerLife -= randint(30, 50)

                sleep(2)
            else:
                print(f"{chosenOne} has lost!")
                sleep(2)
            miscStuffLib.clear() # PUT THIS AFTER THE ATTACK IS DEALT

        elif chosenOne == "Desmond the moon bear":
            print(f"You have {playerLife} life left. {chosenOne} has {opponentLife} left")
            print("Your turn!")

            proposeAttacks(inventory)
            attack = input("Which will you choose? (enter without quotation marks) ")
            if attack == "make a flame":
                print("Desmond is easily spooked by fire.")
                opponentLife -= randint(10, 28)
            elif attack == "grab ears":
                print("You got ahold of their ears and pulled. That hurt.")
                opponentLife -= randint(10, 28)
            elif attack == "Answer their question":
                print("You answered Desmond's question. That made them sad!")
                opponentLife -= randint(30, 50)
            else:
                print("That was not a valid attack. You've just played your turn!")
            sleep(2)

            if opponentLife > 0:
                print("\nNow it's Desmond's turn")
                sleep(1)
                counterAttack = liDamageDealers[randint(0, len(liDamageDealers)-1)]
                if counterAttack == "How did I get here":
                    print("Desmond wonders how they got here, which hits you, so saddening.")
                    playerLife -= randint(10, 28)
                elif counterAttack == "bite":
                    print("Desmond bites you! Yeouch!")
                    playerLife -= randint(10, 28)
                elif counterAttack == "scratch":
                    print("Desmond scratches you in the face! That'll leave a mark.")
                    playerLife -= randint(10, 28)
                elif counterAttack == "run into":
                    print("Desmond runs into you!")
                    playerLife -= randint(30, 50)

                sleep(2)
            else:
                print(f"{chosenOne} has lost!")
                sleep(2)
            miscStuffLib.clear() # PUT THIS AFTER THE ATTACK IS DEALT

    if opponentLife <= 0:
        print("You won!")
        # Item drop?
    elif playerLife <= 0:
        print("You lost!")
        return "lost"