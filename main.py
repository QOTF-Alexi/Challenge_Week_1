''' 
    Main code for the challenge week game.
    Written by:
    Class: BC11K @ Hogeschool Rotterdam
'''

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
game = 0
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
    print("Your objective will become more clear throughout the game.")
    print("Whomever put you into this rocket did leave a note saying you're going to a planet in need of help.")


# This runs continuously 
while lives > 0 and game < 6:
    print(f"You have {lives} lives.\n")
    game += 1
    sleep(5)
    miscStuffLib.clear()
    if game == 1:
        level = riddles.riddlegame()
    elif game == 2:
        level = flyingRoute.route()
    elif game == 3:
        level = quiz.quizdragon(name)
    elif game == 4:
        level = minefieldd.minefield()
    elif game == 5:
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
    sleep(1)
    print("You now have a very difficult choice to make")
    sleep(0.3)
    print("You can choose to return to your home planet and you will forget everything that happened.")
    print("Or, you can stay here, on Eris, and build up your kingdom")
    endIn = input("What will you choose? ")
    if "return" in endIn:
        print("You suddenly pass out.")
        sleep(0.5)
        print("And you wake up, late for school!")
    elif "stay" in endIn:
        print("So you chose to stay, huh? Solid choice!")
        sleep(0.5)
        print("And now it's time to build your kingdom!")
    else:
        print("You just got wiped off the face of the planet because you couldn't choose.")
