''' 
    Main code for the challenge week game.
    Written by:
    Class: BC11K @ Hogeschool Rotterdam
'''
import debugger # Imports the debugger.py file as a library.
import flyingRoute

difficulty = 3 # Gradually gets higher throughout the game
lost = 0
hardTime = 0

while lost == 0:
    debugger.debug() # Breakdown: "debug()" calls the function inside the file "debugger".
    level = flyingRoute.route(difficulty)
    if level == "hardTime":
        hardTime = 1
        lost = 0
    elif level == "lost":
        hardtime = 0
        lost = 1

print(f"Oh no, that shouldn't have happened... You finished {difficulty-2} activities.")