'''
    A text-based clone of a popular game.
    Written by:
'''

from random import randint

opponentLife = 100
playerLife = 101

characters = ["vampire", "very dangerous sheep", "Desmond the moon bear"]

# These will deal damage to the opponent
goodAttacks = {
    "vampire": ["Foobar", "foo", "bar", "baz"],
    "very dangerous sheep": [],
    "Desmond the moon bear": ["Answer their question"]
}

# These will deal damage to the player
damageDealers = {
    "vampire": ["Foobar", "foo", "bar", "baz"],
    "very dangerous sheep": [],
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
    print(f"You will have to battle a {chosenOne} to continue!")
    proposeAttacks(inventory, '\n')
    while opponentLife > 0 and playerLife > 0:
        if chosenOne == "vampire":
            #battle