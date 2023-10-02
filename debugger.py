'''
    This is the debugger code.
    It will walk through every function to verify functionality.
    Written by: Benno
'''

import miscStuffLib
import battler_debug
import flyingRoute
import mathLol
import minefield
import quiz
import riddles
import word_unscrambler

def debug():
    miscStuffLib.lines(28)
    print("|" + " "*26 + "|")
    print("|  This is the TEST MODE!  |")
    print("|" + " "*26 + "|")
    miscStuffLib.lines(28)

    print("Starting Battler")
    battler_debug.battler("garlicbread")

    miscStuffLib.lines(28)
    print("Starting flyingRoute")
    level = flyingRoute.route()
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
    print("Starting riddlegame. Get all correct")
    riddles.riddle_game()
    print("Starting again. Get all incorrect")
    riddles.riddle_game()
    print("riddlegame test completed.")

    miscStuffLib.lines(28)
    print("Starting unscrambler. Get all correct")
    word_unscrambler.word_unscrambler()
    print("Starting again. Get all incorrect")
    word_unscrambler.word_unscrambler()
    print("unscrambler test completed.")

    miscStuffLib.lines(28)
    print("Starting minefield. Get all correct.")
    minefield.minefield()
    print("Starting again. Get all incorrect.")
    minefield.minefield()
    print("Minefield test completed.")
    quit()
