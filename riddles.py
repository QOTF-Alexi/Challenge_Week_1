# player answers riddles to get words difficulty = easy
# players then needs to decipher a word from the riddle answers
# the deciphered word is needed to unlock a room with an item [Voice message device] 

import miscStuffLib
from time import sleep

def riddle_game():

    def riddlequestion(riddle, right_ans):
        attemps = 0

        while attemps < 3   :
            sleep(1)
            miscStuffLib.lines(76)
            print(riddle)
            input_ans = input("Your answer: ".format(attemps+1)).lower()

            if input_ans != right_ans:
                attemps += 1
                print("Wrong answer. Please try again.")
            
            else: 
                print("Correct!")
                
        print("You've used up all your attemps. The correct answer is: {}".format(right_ans)) 


    riddles = {"What is a five-letter word that becomes shorter when you add two letters to it?" : "short" ,
               "What goes up but never goes down?": "age",
               "Vonneke’s parents has three children: Jonneke and Lonneke. What’s the name of the third sister?": "vonneke" ,
               "You see me once in June, twice in November and not at all in May. What am I?": "e"
    }

    score = 0

    for riddle,right_ans in riddles.items():
        if_right = riddlequestion(riddle, right_ans)
        if if_right:
            score += 1

    print("Congratulations on answering ")

riddle_game()

#pt 2 of the game 
# with all the answers from the riddle they would need to form a word 
#it'll work as a passcode to unlock the door to go outside the rocket 

