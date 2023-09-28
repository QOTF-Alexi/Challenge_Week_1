'''
    Put random stuff that doesn't fit elsewhere here.
    Written by:
'''

from os import system, name

# Will print an entered amount of - characters
def lines(length):
    print('-'*length)

def debug():
    lines(28)
    print("|" + " "*26 + "|")
    print("|  This is the TEST MODE!  |")
    print("|" + " "*26 + "|")
    lines(28)

def clear(): 
    # for Windows
    if name == 'nt': 
        _ = system('cls') 
  
    # for MacOS and Linux (Works on Android too :D)
    else: 
        _ = system('clear')