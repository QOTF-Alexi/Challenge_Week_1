'''
    You weren't expecting this one, were you?
    Written by: Benno
'''

from random import randint

def easy():
    pi = 3.14159

    print("You have to calculate the circumference of a circle!")
    print("The formula is 2*pi*r, but what was pi again?")
    inpi = float(input("Enter the number pi with 5 decimals precision "))
    if inpi == pi:
        print("Woah, you go big brain!")
    else:
        print("Oh. Shouldn't everyone know that?")
        return "lost"

def medium():
    print("One math question coming right up!")

def hard():
    print("One hard question")

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