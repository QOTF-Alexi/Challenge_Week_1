# player answers riddles to get words difficulty = easy
# players then needs to decipher a word from the riddle answers
# the deciphered word is needed to unlock a room with an item [Voice message device] 

import miscStuffLib
from time import sleep

def riddle_game():

    def ask_riddle(riddle, right_ans):
        attempts = 0

        while attempts < 3:
            sleep(1)
            miscStuffLib.lines(80)
            print(riddle)
            input_ans = input("Your answer: ".format(attempts + 1)).lower()
            print()

            if input_ans != right_ans:
                attempts += 1
                print("Wrong answer. Please try again.")
            else:
                print("Correct!")
                return True

        print("You've used up all your attempts. The correct answer is: {}".format(right_ans))
        return False

    print()
    print("After realizing what kind of situation you are in, you decided to just deal with it and take look around the rocket ship.")
    sleep(0.75)
    print("While looking around you just see a bunch of normal things you would see in a rocket ship.")
    sleep(0.75)
    print("Finally you found the exit but it's locked. Suddenly a pop-up window appears in from of your face. ")
    sleep(0.75)
    print("In the window it says: ")
    sleep(0.75)
    print()
    miscStuffLib.lines(100)
    print("|Congratulations on finding the exit! To open the door you would need to enter a password.         |")
    sleep(0.75)
    print("|But first you would need to play a game to get hints on what the password is.                     |")
    sleep(0.75)
    print("|The game is simple. You just need to answer a bunch of riddles. You have 3 attemps on each riddle.|")
    sleep(0.75)
    print("|Remember each correct answer. You're gonna need it for the password.                              |")
    sleep(0.75)
    print("|Good luck!                                                                                        |")
    sleep(0.75)
    miscStuffLib.lines(100)

    riddles = {
        "What is a five-letter word that becomes shorter when you add two letters to it?": "short",
        "What goes up but never goes down?": "age",
        "Vonneke’s parents have three children: Jonneke and Lonneke. What’s the name of the third sister?": "vonneke",
        "You see me once in June, twice in November and not at all in May. What am I?": "e"
    }

    ready_input = ""
    while ready_input.upper() != "READY":
        ready_input = input("To start the game type \"READY\".")
        if ready_input.upper() == "READY":
            for riddle, right_ans in riddles.items():
                ask_riddle(riddle, right_ans)
        else:
            print("That was not correct!")

    

    print()
    print()
    miscStuffLib.lines(97)
    print("|                                                                                               |")
    sleep(1)
    print("|Congratulations on completing the riddles!                                                     |")
    sleep(1) 
    print("|The correct answers were: Short, Age, Vonneke and E.                                           |")
    sleep(1)
    print("|Remember these answers well because you're going to need it to help you unlock the exit.       |")
    sleep(1)
    print("|Here is a projector device to help you decipher the code for the exit.                         |")
    sleep(1)
    print("|                                                                                               |")
    sleep(1)
    miscStuffLib.lines(97)
    sleep(3)
    return "projector device"
    
riddle_game()
#pt 2 of the game 
# with all the answers from the riddle they would need to form a word 
#it'll work as a passcode to unlock the door to go outside the rocket 

def doorcode():
    miscStuffLib.clear()
    print()
    print()
    miscStuffLib.lines(73)
    print("|Congratulations on solving the riddles.                                |")
    sleep(0.75)
    print("|To finally unlock the door you would need to open the projector device.|")
    sleep(0.75)
    print("|Type \"OPEN\" to see the message in the device.                          |")
    miscStuffLib.lines(73)
    open_device = input()
    print()

    if open_device.upper() == "OPEN":
        print("The device suddenly opened and a screen popped out of it. ")
        sleep(1)
        print("In the screen it says: ")
        sleep(1)
        miscStuffLib.lines(102)
        print("|This is a message for the people who are trying to open the door.                                   |")
        sleep(1)
        print("|If i am correct the password for the door consists out of two words.                                |")
        sleep(1)
        print("|The first word you will need decipher from the words you got from the riddle game.                  |")
        sleep(1)
        print("|You will need to put the answers under each other in the same order on how the questions were asked.|")
        sleep(1)
        print("|By then you would need to see if theres a pattern in those stack of words.                          |")
        sleep(1)
        print("|If you figured out the word you should put the name of the planet you're in after it.               |")
        sleep(1)
        print("|That's pretty much everything i can say, i hope it helps.                                           |")
        sleep(1)
        miscStuffLib.lines(102)
    
    print()
    print()
    
    print("The device suddenly closed. You go to the door and clicked on the tablet to enter the password.")
    sleep(0.5)
    print("On the screen you see \"_ _ _ _   _ _ _ _ \"")
    sleep(0.5)

    password = "SAVE ERIS"

    unlock_door = input("Enter the password to open the door: ")

    if unlock_door.upper() == password:
        print()
        print("Door unlocked. Congratulations! Welcome to planet Eris! May your adventures begin.")
        return "plusLife"
    else:
        print()
        print("Incorrect passcode. The door remains locked. Please try again.")

doorcode()
