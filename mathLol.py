'''
    The biggest waste of time ever.
    This code has no consequences for game progression.
    Written by:
'''

from random import randint

def calcPi():
    pi = 3.14159265

    print("You have to calculate the circumference of a circle!")
    print("The formula is 2*pi*r, but what was pi again?")
    inpi = float(input("Enter the number pi with 8 decimals precision"))
    if inpi == pi:
        print("Woah, you go big brain!")
    else:
        print("You can call yourself lucky that Pi can be rounded up to 4 without much issue")

def addRandom():
    num1 = randint(0, 50)
    num2 = randint(0, 50)
    print(f"Please calculate {num1}+{num2}")
    num3 = int(input("Please? "))
    if num3 == num1+num2:
        print("That seems accurate enough")
    else:
        print("So close yet so far")