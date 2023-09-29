''' 
    Main code for the challenge week game.
    Written by:
    Class: BC11K @ Hogeschool Rotterdam
'''

from random import randint
from time import sleep

# Import our own activities and library
import miscStuffLib  # Imports the miscStuffLib.py file as a library.
import battler
import debugger
import flyingRoute
import minefieldd
import quiz
import riddles

lives = 5
inventory = []

# Startup sequence
miscStuffLib.lines(76)
sleep(0.3)
print("| Loud noises and computer beeps awaken you.                               |")
sleep(0.3)
print("| A computerized voice: Welcome. You have been chosen as a space traveler! |")
sleep(0.3)
print("| You have to save a planet from invaders!                                 |")
sleep(0.3)
miscStuffLib.lines(76)
sleep(1)
name = input("May I ask, what is your name again? My memory is a bit fuzzy. ")
if name == "debug":
    debugger.debug() # Breakdown: "debug()" calls the function inside the file "debugger".
    print()
else:
    print(f"\nI like your name, {name}. Prepare for some challenges. It won't be easy!")


# This runs continuously 
while lives > 0:
    print(f"You have {lives} lives.\n")
    sleep(5)
    miscStuffLib.clear()
    level = riddles.riddlegame()
    miscStuffLib.clear()
    level = flyingRoute.route()
    miscStuffLib.clear()
    level = quiz.quizdragon(name)
    miscStuffLib.clear()
    level = minefieldd.minefield()
    miscStuffLib.clear()
    level = battler.battler(inventory)

    if level == "lost":
        lives -= 1
    elif level == None:
        print("No drops, no loss")
    elif level == "breadUsed":
        inventory.remove("garlicbread")
    else:
        inventory.append(level)

# Only appears after game completion.
if lives <= 0:
    print(f"Oh no, that shouldn't have happened... You died and the game ended.")
    print(f"You ended with the following items in your inventory: {inventory}")
else:
    print("The planet has been saved. You won the game!")
    print(f"You had {lives} lives left.")
    print(f"You had the following items left: {inventory}")
