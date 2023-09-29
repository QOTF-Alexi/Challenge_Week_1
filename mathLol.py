'''
    The biggest waste of time ever.
    This code has no consequences for game progression.
    Written by: Benno
'''

from random import randint

def calcPi():
    pi = 3.14159

    print("You have to calculate the circumference of a circle!")
    print("The formula is 2*pi*r, but what was pi again?")
    inpi = float(input("Enter the number pi with 5 decimals precision "))
    if inpi == pi:
        print("Woah, you go big brain!")
    else:
        print("Oh. Shouldn't everyone know that?")
        return "lost"

def addRandom():
    num1 = randint(0, 50)
    num2 = randint(0, 50)
    print(f"Please calculate {num1}+{num2}")
    num3 = int(input("Please? "))
    if num3 == num1+num2:
        print("That seems accurate enough")
    else:
        print("So close yet so far")

def subRandom():
    num1 = randint(0, 50)
    num2 = randint(0, 50)
    print(f"Please calculate {num1}-{num2}")
    num3 = int(input("Please? "))
    if num3 == num1-num2:
        print("That seems accurate enough")
    else:
        print("So close yet so far")

def thisDoesNothing():
    playWhich = randint(0, 2)
    if playWhich == 0:
        calcPi()
    elif playWhich == 1:
        addRandom()
    elif playWhich == 2:
        subRandom()

def debugTest():
    print("Enter the correct one here!")
    calcPi()
    print("Enter the incorrect one here!")
    calcPi()

    print("Enter the correct one here!")
    addRandom()
    print("Enter the incorrect one here!")
    addRandom()

    print("Enter the correct one here!")
    subRandom()
    print("Enter the incorrect one here!")
    subRandom()