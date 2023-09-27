'''
    Flying route activity for the game.
    Written by: 
'''

from random import randint

def route(difficulty):
    feeling_brave = True
    if difficulty >= 5:
        instantDeath = randint(1, difficulty)
    else:
        instantDeath = 99
    hardLevel = randint(1, difficulty)
    if instantDeath == hardLevel:
        if hardLevel == 2:
            instantDeath = 99
        else:
            instantDeath = 2

    print(f"{difficulty} paths ahead. {difficulty-2} paths are safe.")
    print("One path will result in death, another might")
    while feeling_brave == True:
        try:
            guess = int(input("Which will you open? "))
            if guess > difficulty or guess < 1:
                print("That is not a valid entry!")
            elif guess == instantDeath:
                feeling_brave = False
                return "lost"
            elif guess == hardLevel:
                feeling_brave = False
                print("That was not the right path. You're going to have a hard time now!")
                return "hardTime"
            else:
                print("That wasn't too hard, was it? Let's continue.")
                feeling_brave = False
        except ValueError:
            print("Please enter a whole number!")