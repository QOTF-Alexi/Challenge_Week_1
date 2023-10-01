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
            print(riddle)
            input_ans = input("Your answer: ".format(attempts + 1)).lower()

            if input_ans != right_ans:
                attempts += 1
                print("Wrong answer. Please try again.")
            else:
                print("Correct!")
                return True

        print("You've used up all your attempts. The correct answer is: {}".format(right_ans))
        return False

    riddles = {
        "What is a five-letter word that becomes shorter when you add two letters to it?": "short",
        "What goes up but never goes down?": "age",
        "Vonneke’s parents have three children: Jonneke and Lonneke. What’s the name of the third sister?": "vonneke",
        "You see me once in June, twice in November and not at all in May. What am I?": "e"
    }

    for riddle, right_ans in riddles.items():
        if_right = ask_riddle(riddle, right_ans)
        if not if_right:
            break

       

    print("|Congratulations on completing the riddles!                                              |")
    print("|Remember these answers well because you're going to need it to help you unlock the exit.|")
    print("|Here is the scroll to help you decipher the code for the exit.")
    return "scroll"

riddle_game()

#pt 2 of the game 
# with all the answers from the riddle they would need to form a word 
#it'll work as a passcode to unlock the door to go outside the rocket 