'''

Game that lets player unscramble words
written by: No'railly

'''
import miscStuffLib
import random
from time import sleep


def word_unscrambler():

    miscStuffLib.lines(94)

    print("|Hello young traveller. Welcome to The letter Crater.                                        |")
    sleep(0.75)
    print("|You unfortunately fell in here and got TRAPPED! To get out you need to play a game.         |")
    sleep(0.75)
    print("|In this game you need to unscramble all the words that are given to you.                    |")
    sleep(0.75)
    print("|Only when you scramble 6 words correctcly, you will be teleported out of here.              |")
    sleep(0.75)
    print("|If not you will be stuck here forever! Good luck.                                           |")
    sleep(0.75)

    miscStuffLib.lines(94)
    
    valid_words = ["windows", "basecamp", "laptop", "challenge", "backpack", "python"]

    guess_count = 0

    correct_guesses = 0

    for guess_count in range (6):
        chosen_word = random.choice(valid_words)
        valid_words.remove(chosen_word)

        word_as_list = list(chosen_word) 
        random.shuffle(word_as_list)
        scrambled_word = ''.join(word_as_list)

        miscStuffLib.lines(70)

        print("Round " + str(guess_count + 1) + ": Unscramble the word: " + scrambled_word)
        
    
        user_guess = input("Enter a valid English word: ").lower()

        if user_guess == chosen_word:
            miscStuffLib.lines(70)
            print("Correct! You unscrambled the word.")
            correct_guesses += 1
        
        else:
            miscStuffLib.lines(70)
            print("Try again. It's not the same as the scrambled word.")


    if correct_guesses == 6:
        miscStuffLib.lines(70)
        print("You have unscrambled all the words correctly. Good job!")
    else:
        miscStuffLib.lines(70)
        print("You have made too many mistakes. You only unscrambled", correct_guesses, "words correctly. Because of that you will stay here forever!")
        return "lost"
    
word_unscrambler()