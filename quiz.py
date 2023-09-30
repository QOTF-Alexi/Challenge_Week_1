'''
    Quiz game from The Star Dragon [Veldora]
    Location: Dragons Den
    If completed u get an item drop: Golden wings - Gives u the ability to fly like the  star dragon across the planet eris. 
    Written by: Ricci
'''

import miscStuffLib
from time import sleep


def quizdragon(name):

    miscStuffLib.lines(115)
    print("|Thou who is courageous enough to enter Veldora's Den shall be given the chance to recieve thy blessing.           |")
    sleep(1)
    print("|Welcome young traveller! I am the Star Dragon Veldora of planet Eris.                                             |")
    sleep(1)
    print("|You've woken me from my deep slumber and choose to enter my den.                                                  |")
    sleep(1)
    print("|You will be asked a series of questions and your correct answers will determine if you are worthy of my blessing. |")
    sleep(1)
    print("|Good luck!                                                                                                        |")
    sleep(1)
    
    miscStuffLib.lines(115)

    start = input("Type \"START\" to start the quiz ")
    if start == "start":

        questions = ("What is the name of the dragon that is bestowing you one of its heavenly gifts?",
                    "Which ocean is the biggest ocean in the world?",
                    "What is the name of the planet you are saving?",
                    "Which continent is fully surrounded by a body of ocean?",
                    "What is the capital city of Canada?",
                    "What is the name of the pearcoach of class K?" )
        
        choices = (("A. Baldora","B. Veldora ","C. Valdrora", "D. Beldrora"),
                ("A. Pacific Ocean","B. Atlantic Ocean","C. Indian Ocean", "D. Artic Ocean"),
                ("A. Airis","B. Esis","C.Arsis", "D. Eris"),
                ("A. Antartica","B. South America","C. Africa", "D. Australia/Oceania"),
                ("A. Vancouver","B. Ottawa","C. Toronto", "D. Québec"),
                ("A. Cornelly","B. Cornelius","C. Cornelis", "D. Cornelion")
                )
        
        right_answers = ("B","A","D","D","B","C")
        
        numbering = 0
        points = 0

        for q in questions: 
            sleep(1)
            miscStuffLib.lines(76)
            print(q)
            for c in choices[numbering]:
                print(c)
            
            input_answer = input("Choose (A, B, C or D) ").upper()
            if input_answer == right_answers[numbering]:
                points += 1
                print("That is correct. Good Job!")
            else:
                print("Too bad, you got it wrong.")
                print(f"The correct answer is {right_answers[numbering]}.")
            
            numbering += 1
        
        miscStuffLib.lines(76)

        result = int(points)
        print(f"| Your total score is {result}/6.                                         |")
        sleep(1)
        print("| I shall now determine if you are worthy of the gift based on your points.|")

        miscStuffLib.lines(76)

        print()
        print()

        if result > 4: #gives the player an item 

            miscStuffLib.lines(76)

            print(f"| Congratulations {name}! You are more than worthy to recieve my gift. I shall bestow a replica of my Golden Wings. |")
            sleep(1)
            print("| Although you can not use it to its full potential, you will still be able to travel the planet more easier.        |")
            sleep(1)
            print("| You are able to use this gift to skip a obstacle once in your journey ahead.                                       |")
            sleep(1)
            print("| Best of luck and have a safe journey.                                                                              |")
        
            miscStuffLib.lines(76)

            return "golden wings"


        else: #player continues without item
            miscStuffLib.lines(76)
            
            print(f"| You almost had it, but it's unfortunate, {name}. I cannot trust you with the reponsibility of my golden wings.|")
            sleep(1)
            print("| I hope you travel safely and good luck with your journey.                                                      |")
            miscStuffLib.lines(76)
            return "lost"
            

quizdragon("start")