'''
voice recorder is at a different location
minefield puzzle 
written by: no'railly

'''

import miscStuffLib
import time

def minefield(inventory):
    print("While walking to your next location you come across a big fench on this fench there is a sign (see below).")
    print(r"""
    ╔╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╗
    ╠╬╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╬╣
    ╠╣          _    _    _                _    _                 _       ╠╣
    ╠╣         / \  | |_ | |_  ___  _ __  | |_ (_)  ___   _ __   | |      ╠╣
    ╠╣        / _ \ | __|| __|/ _ \| '_ \ | __|| | / _ \ | '_ \  | |      ╠╣
    ╠╣       / ___ \| |_ | |_|  __/| | | || |_ | || (_) || | | | |_|      ╠╣
    ╠╣      /_/   \_\\__| \__|\___||_| |_| \__||_| \___/ |_| |_| (_)      ╠╣
    ╠╣               ____         _      _             _                  ╠╣
    ╠╣              | __ )   ___ | |__  (_) _ __    __| |                 ╠╣
    ╠╣              |  _ \  / _ \| '_ \ | || '_ \  / _` |                 ╠╣
    ╠╣              | |_) ||  __/| | | || || | | || (_| |                 ╠╣
    ╠╣              |____/  \___||_| |_||_||_| |_| \__,_|                 ╠╣
    ╠╣ _    _      _            __                              _         ╠╣
    ╠╣| |_ | |__  (_) ___      / _|  ___  _ __    ___  ___     (_) ___    ╠╣
    ╠╣| __|| '_ \ | |/ __|    | |_  / _ \| '_ \  / __|/ _ \    | |/ __|   ╠╣
    ╠╣| |_ | | | || |\__ \    |  _||  __/| | | || (__|  __/    | |\__ \   ╠╣
    ╠╣ \__||_| |_||_||___/    |_|   \___||_| |_| \___|\___|    |_||___/   ╠╣
    ╠╣                              __ _                                  ╠╣
    ╠╣                             / _` |                                 ╠╣
    ╠╣                            | (_| |                                 ╠╣
    ╠╣                             \__,_|                                 ╠╣
    ╠╣ __  __   ___   _   _   _____   _____   ___   _____   _       ____  ╠╣
    ╠╣|  \/  | |_ _| | \ | | | ____| |  ___| |_ _| | ____| | |     |  _ \ ╠╣
    ╠╣| |\/| |  | |  |  \| | |  _|   | |_     | |  |  _|   | |     | | | |╠╣
    ╠╣| |  | |  | |  | |\  | | |___  |  _|    | |  | |___  | |___  | |_| |╠╣
    ╠╣|_|  |_| |___| |_| \_| |_____| |_|     |___| |_____| |_____| |____/ ╠╣
    ╠╬╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╬╣
    ╚╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╝
   
          """)
    print("|The sign tells you that there is a minefield in front of you.  |")
    print("|To get past this minefield you have to choose exact directions.|")  
    

    if "voice recorder" in inventory:

        while True:
            voice = input("Click play on the voice recorder: ")
            if voice == "play":
                break
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
