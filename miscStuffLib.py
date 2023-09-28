'''
    Put random stuff that doesn't fit elsewhere here.
    Written by:
'''

from os import system, name

# Will print an entered amount of - characters
def lines(length):
    print('-'*length)

def clear(): 
    # for Windows
    if name == 'nt': 
        _ = system('cls') 
  
    # for MacOS and Linux (Works on Android too :D)
    else: 
        _ = system('clear')