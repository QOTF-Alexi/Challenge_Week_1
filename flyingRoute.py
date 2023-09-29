'''
    Route choosing activity for the game.
    Written by: Benno
'''

from random import randint
import mathLol

def route():
    feeling_brave = True
    instantDeath = randint(1, 3)
    hardLevel = randint(1, 3)
    if instantDeath == hardLevel:
        if hardLevel == 2:
            instantDeath = 1
        else:
            instantDeath = 2

    print(f"Three paths are ahead. One is safe.")
    print("One path will definitely result in a lost life, another might.")
    while feeling_brave == True:
        try:
            guess = int(input("Which will you take? (left, forward or right) "))
            if guess == "left":
                guess = 1
            elif guess == "forward":
                guess = 2
            elif guess == "right":
                guess = 3
            else:
                print("That is not a valid entry!")
                
            if guess == instantDeath:
                feeling_brave = False
                print("You took the wrong path!")
                mathLol.medium()
            elif guess == hardLevel:
                feeling_brave = False
                print("That was not the right path. You're going to have a hard time now!")
                mathLol.difficult()
            else:
                print("That wasn't too hard, was it? Let's continue.")
                mathLol.easy()
        except ValueError:
            print("Please enter a whole number!")