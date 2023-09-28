#quiz game from The Heavenly Star Dragon [Veldora]
#location: Dragons Den
# if completed u get an item drop: Golden wings - Gives u the ability to fly like the heavenly star dragon across the planet eris. 

import miscStuffLib

print("Thou who is courageous enough to enter Veldora's Den shall be given the chance to recieve thy blessing.")
print("Welcome young travel!")

def quizdragon():
    questions = ("What is the name of the heavenly presence that is bestowing you one of its heavenly gifts?",
                 "Which ocean is the biggest ocean in the world?",
                 "What is the name of the planet you are saving?",
                 "Which continent is fully surrounded by a body of ocean?",
                 "What is the capital city of Canada?",
                 "What is the name of the pearcoach of class K?" )
    
    choices = (("A. Baldora","B. Veldora ","C. Valdrora", "D. Beldrora"),
               ("A. Pacific Ocean","B. Atlantic Ocean","C. Indian Ocean", "D. Artic Ocean"),
               ("A. Airis","B. Esis","C.Arsis", "D. Eris"),
               ("A. Antartica","B. South America","C. Africa", "D. Australia/Oceania"),
               ("A. Vancouver","B. Ottowa","C. Toronto", "D. Québec"),
               ("A. Cornelly","B. Cornelius","C. Cornelis", "D. Cornelion")
               )
    
    right_answers = ("B","A","D","D","B","C")

    answer = []
    
    numbering = 0

    points = 0

    for q in questions: 
        miscStuffLib.lines(76)
        print(q)
        for c in choices[numbering]:
            print(c)
        
        input_answer = input("Choose (A, B, C or D)").upper()
        if input_answer == right_answers[numbering]:
            points += 1
            print("That is correct. Good Job!")
        else:
            print("Too bad, you got it wrong.")
            print(f"The correct answer is {right_answers[numbering]}.")
        
        numbering += 1
    
    miscStuffLib.lines(76)

    result = int(points)
    print(f"|Your total score is {result}/6.                                                 |")
    print("|I shall now determine if you are worthy of the gift based on your points.|")

    miscStuffLib.lines(76)

    if result > 4: #gives the player an item 
        print(f"Congratulations  ! You are more than worthy to recieve my gift. I shall bestow a replica of my Golden Wings.")
        print("Although you can not use it to its full potential, you will still be able to travel the planet more easier.")
        print("You are able to use this gift to skip a obstacle once in your journey ahead.")
        print("Best of luck and have a safe journey.")



    else: #player continues without item
        print(f"You almost had it, but its unfortunate . I cannot trust you with the reponsibility of my golden wings.")
        print("I hope you travel safely and good luck with your journey.")

print(quizdragon())
    
