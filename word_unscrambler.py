'''
Game that lets player unscramble words
written by: No'railly

'''

import random

def word_unscrambler():
    valid_words = ["windows", "basecamp", "laptop", "challenge", "backpack", "mouse", "python"]

    guess_count = 0

    correct_guesses = 0

    for _ in range(6):
        chosen_word = random.choice(valid_words)
        valid_words.remove(chosen_word)

        word_as_list = list(chosen_word)
        random.shuffle(word_as_list)
        scrambled_word = ''.join(word_as_list)

        print("Round " + str(guess_count + 1) + ": Unscramble the word: " + scrambled_word)
        
        while True:
            user_guess = input("Enter a valid English word: ").lower()

            if user_guess == chosen_word:
                print("Correct! You unscrambled the word.")
                correct_guesses += 1
                break
            else:
                print("Try again. It's not the same as the scrambled word.")

        guess_count += 1

    if correct_guesses == 6:
        print("You have unscrambled all the words correctly. Good job!")
        return "voice recorder"
    else:
        print("You have completed the game. You unscrambled", correct_guesses, "words correctly.")
        return "lost"



