'''
    This is the debugger code.
    It will walk through every function to verify functionality.
    Written by: Benno
'''

import miscStuffLib
import battler_debug
import flyingRoute
import mathLol
import minefieldd
import quiz

def debug():
    levelList = []
    miscStuffLib.lines(28)
    print("|" + " "*26 + "|")
    print("|  This is the TEST MODE!  |")
    print("|" + " "*26 + "|")
    miscStuffLib.lines(28)

    print("Starting Battler")
    battler_debug.battler("garlicbread")

    miscStuffLib.lines(28)
    print("Starting flyingRoute")
    while "lost" not in levelList and "hardTime" not in levelList and "itemDrop" not in levelList:
        level = flyingRoute.route(5)
        levelList.append(level)
    print("flyingRoute test completed.")

    miscStuffLib.lines(28)
    print("Starting mathLol")
    mathLol.debugTest()
    print("mathLol test completed.")

    miscStuffLib.lines(28)
    print("Starting quizdragon. Get more than 4 correct")
    quiz.quizdragon("debugger")
    print("Starting again. Get all incorrect")
    quiz.quizdragon("debugger")
    print("Quiz test completed.")

    miscStuffLib.lines(28)
    print("Starting minefield. Get all correct.")
    minefieldd.minefield()
    print("Starting again. Get all incorrect.")
    minefieldd.minefield()
    print("Minefield test completed.")
