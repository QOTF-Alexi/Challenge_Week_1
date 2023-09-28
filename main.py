''' 
    Main code for the challenge week game.
    Written by:
    Class: BC11K @ Hogeschool Rotterdam
'''

from random import randint

# Import our own activities and library
import miscStuffLib # Imports the miscStuffLib.py file as a library.
import flyingRoute
import mathLol
import battler

difficulty = 3 # Gradually gets higher throughout the game
lost = 0
hardTime = 0

activities = ["route", "math", "battler"]
inventory = []

# Startup sequence
miscStuffLib.lines(76)
print("| Loud noises and computer beeps awaken you.                               |")
print("| A computerized voice: Welcome. You have been chosen as a space traveler! |")
print("| You have to save a planet from invaders!                                 |")
miscStuffLib.lines(76)
name = input("May I ask, what is your name again? My memory is a bit fuzzy. ")
if name == "debug":
    miscStuffLib.debug() # Breakdown: "debug()" calls the function inside the file "miscStuffLib".
    print()
    # Needs to trigger playthrough of every activity.
else:
    print(f"I like your name, {name}. Prepare for some challenges. It won't be easy!\n")
    #This will probably never be used again


# This runs continuously 
while lost == 0:
    playGame = activities[randint(0, len(activities)-1)]
    if playGame == "route":
        level = flyingRoute.route(difficulty)
    elif playGame == "math":
        level = mathLol.thisDoesNothing()
    elif playGame == "battler":
        level = battler.battler(inventory)

    if level == "hardTime":
        hardTime = 1
        lost = 0
    elif level == "lost":
        hardtime = 0
        lost = 1
    elif level == None:
        print("No drops, no loss")
    else:
        inventory.append(level)

# Only appears when you lose
print(f"Oh no, that shouldn't have happened... You finished {difficulty-2} activities.")
print(f"You ended with the following items in your inventory: {inventory}")
