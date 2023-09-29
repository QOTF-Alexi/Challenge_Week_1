'''
    The biggest waste of time ever.
    This code has no consequences for game progression.
    Written by: Benno
'''

from random import randint

def medium():
    pi = 3.14159

    print("You have to calculate the circumference of a circle!")
    print("The formula is 2*pi*r, but what was pi again?")
    inpi = float(input("Enter the number pi with 5 decimals precision "))
    if inpi == pi:
        print("Woah, you go big brain!")
    else:
        print("Oh. Shouldn't everyone know that?")
        return "lost"


def easy():
    num1 = randint(0, 50)
    num2 = randint(0, 50)
    print(f"Please calculate {num1}+{num2}")
    num3 = int(input("Please? "))
    if num3 == num1+num2:
        print("That seems accurate enough")
    else:
        print("So close yet so far")
        return "lost"

def hard():
    print("Please solve 2^3+2^0+8/4")
    answer = input("Please? ")
    if answer == (2^3+2^0+8/4):
        print("That is indeed correct")
    else:
        print("Nope.")
        return "lost"



def debugTest():
    print("Enter the correct one here!")
    easy()
    print("Enter the incorrect one here!")
    easy()

    print("Enter the correct one here!")
    medium()
    print("Enter the incorrect one here!")
    medium()

    print("Enter the correct one here!")
    hard()
    print("Enter the incorrect one here!")
    hard()