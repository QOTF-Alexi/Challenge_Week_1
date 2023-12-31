'''
    The biggest waste of time ever.
    This code has no consequences for game progression.
    Written by: Benno
'''

from random import randint

def medium():
    pi = 3.14159

    print("You are trapped in this hypercube and to get out, you have to calculate the circumference of a circle!")
    print("The formula is 2*pi*r, but what was pi again?")
    inpi = float(input("Enter the number pi with 5 decimals precision "))
    if inpi == pi:
        print("Woah, you go big brain!")
        return "drop"
    else:
        print("Oh. Shouldn't everyone know that?")
        return "lost"


def easy():
    num1 = randint(0, 50)
    num2 = randint(0, 50)
    print("You are trapped in this hypercube and to get out, you need to calculate the size of a side.")
    print(f"Please calculate {num1}+{num2}")
    num3 = int(input("Please? "))
    if num3 == num1+num2:
        print("That seems accurate enough. This should help you cross the gap easily.")
        return "drop"
    else:
        print("So close yet so far. Guess you have some climbing to do.")
        return "lost"

def hard():
    print("You are trapped inside a hypercube. Some robot in a space suit will let you out but wants to ask you the following:")
    print("Please solve 2^3+2^0+8/4")
    answer = int(input("Please? "))
    if answer == int(2**+2**0+8/4):
        print("\"That is indeed correct\", the robot says.")
        return "plusLife"
    else:
        print("Nope. But you'll be spared.")



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