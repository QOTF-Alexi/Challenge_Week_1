'''
    A text-based clone of a popular game.
    Written by:
'''

from random import randint
import miscStuffLib

opponentLife = 100
playerLife = 101

characters = ["The vampire", "The very dangerous sheep", "Desmond the moon bear"]

# These will deal damage to the opponent
goodAttacks = {
    "The vampire": ["flashlight", "silver", "extracted teeth", "take off shoes"],
    "The very dangerous sheep": [],
    "Desmond the moon bear": ["Answer their question"]
}

# These will deal damage to the player
damageDealers = {
    "The vampire": ["trick", "bite", "paralyse", "litte curse"],
    "The very dangerous sheep": [],
    "Desmond the moon bear": ["How did I get here"]
}

chosenOne = characters[randint(0, 2)]
liGoodAttacks = goodAttacks[chosenOne]
liDamageDealers = damageDealers[chosenOne]

def proposeAttacks(inventory):
    proposedAttacks = goodAttacks[chosenOne]
    if "garlicbread" in inventory:
        proposedAttacks.insert((randint(0, len(proposedAttacks))), "garlicbread")
    print("You have the following attacks available to you:\n")
    print(proposedAttacks)

def battler(inventory):
    print(f"You will have to battle {chosenOne} to continue!")
    while opponentLife > 0 and playerLife > 0:
        if chosenOne == "vampire":
            print(f"You have {playerLife} life left. {chosenOne} has {opponentLife} left")
            print("Your turn!")
            proposeAttacks(inventory, '\n')
            attack = input("Which will you choose? ")
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
            counterAttack = liDamageDealers[randint(0, len(liDamageDealers))]
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

            miscStuffLib.clear() # PUT THIS AFTER THE ATTACK IS DEALT

        elif chosenOne == "very dangerous sheep":
            print(f"You have {playerLife} life left. {chosenOne} has {opponentLife} left")
            print("Your turn!")
            proposeAttacks(inventory, '\n')
            attack = input("Which will you choose? ")
            counterAttack = liDamageDealers[randint(0, len(liDamageDealers))]

            miscStuffLib.clear() # PUT THIS AFTER THE ATTACK IS DEALT

        elif chosenOne == "Desmond the moon bear":
            print(f"You have {playerLife} life left. {chosenOne} has {opponentLife} left")
            print("Your turn!")
            proposeAttacks(inventory, '\n')
            attack = input("Which will you choose? ")
            counterAttack = liDamageDealers[randint(0, len(liDamageDealers))]

            miscStuffLib.clear() # PUT THIS AFTER THE ATTACK IS DEALT
            
    if opponentLife <= 0:
        print("You won!")
        # Item drop?
    elif playerLife <= 0:
        print("You lost!")
        return "lost"