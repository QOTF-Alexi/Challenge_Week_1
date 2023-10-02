'''
voice recorder is at a different location
minefield puzzle 
written by: no'railly

'''

import miscStuffLib
import time

def minefield(inventory):
    print("|You have arrived at your next location.|")
    print("|In front of you is a minefield.        |")

    if "voice recorder" in inventory:

        while True:
            voice = input("Click play on the voice recorder: ")
            if voice == "play":
                break  # Exit the loop if the user enters "play" correctly
            else:
                print("You did not click play. Please try again.")

        text = [
            "|############## VOICE MESSAGE ###############|",
            "| For anyone that is receiving this message. |",
            "|        please listen carefully!            |",
            "|   This message will only be played once!   |",
            "|To get through the minefield you need to go:|",
            "|left, right, forward, left, backward, left. |",
            "|  I hope you make it to the end. Good luck! |",
            "                                              "
        ]

        for line in text:
            words = line.split()
            for word in words:
                print(word, end=" ")
                time.sleep(0.3)  
        print()

    else:
        print("You unfortunately do not have the voice recorder. You are going in blind.")

    directions = ["left", "right", "forward", "left", "backward", "left"]


    time.sleep(10)

    miscStuffLib.clear()

    max_guesses = 10
    current_step = 0
    guess_count = 0

    while current_step < len(directions) and guess_count < max_guesses:
        player_input = input("Enter your next move : ")

        if player_input == directions[current_step]:
            current_step += 1
        else:
            print("Oops! That's not the correct direction. Try again.")
            guess_count += 1

    if current_step == len(directions):
        print("|Congratulations! You've successfully navigated the minefield.|")
    else:
        print("You've exceeded the maximum number of guesses. Game over.")
        return "lost"
