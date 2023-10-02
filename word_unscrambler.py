'''

Game that lets player unscramble words
written by: No'railly

'''
import miscStuffLib
import random

def word_unscrambler():
    print("|Hello young traveller. Welcome to The letter Crater.|")
    print("|You fell in here and got TRAPPED! To get out you need to play a game.|")
    print("|In this game you need to unscramble all the words that are given to you.|")
    print("|Only when you scramble 6 words correctcly, you will be teleported out of here.|")
    print("|If not you will be stuck here forever! Good luck|")

    miscStuffLib.lines(70)
    
    valid_words = ["windows", "basecamp", "laptop", "challenge", "backpack", "python"]

    guess_count = 0

    correct_guesses = 0

    for i in range(6):
        chosen_word = random.choice(valid_words)
        valid_words.remove(chosen_word)

        word_as_list = list(chosen_word) 
        random.shuffle(word_as_list)
        scrambled_word = ''.join(word_as_list)

        miscStuffLib.lines(70)

        print("Round " + str(guess_count + 1) + ": Unscramble the word: " + scrambled_word)
        
        while True:
            user_guess = input("Enter a valid English word: ").lower()

            if user_guess == chosen_word:
                miscStuffLib.lines(70)
                print("Correct! You unscrambled the word.")
                correct_guesses += 1
                break
            else:
                miscStuffLib.lines(70)
                print("Try again. It's not the same as the scrambled word.")

        guess_count += 1

    if correct_guesses == 6:
        miscStuffLib.lines(70)
        print("You have unscrambled all the words correctly. Good job!")
    else:
        miscStuffLib.lines(70)
        print("You have made too many mistakes. You only unscrambled", correct_guesses, "words correctly. Because of that you will stay here forever!")
        return "lost"