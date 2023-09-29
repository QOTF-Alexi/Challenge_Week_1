'''
voice recorder is at a different location
minefield puzzle 
written by: no'railly

'''
import miscStuffLib 

print("|You have arrived at your next location.|")
print("|In front of you is a minefield.        |") 
voice  = input("Click PLAY on the voice recorder:    ")

if voice == "PLAY":
    print("|           ### VOICE MESSAGE ###            |")
    print("| For anyone that is receiving this message. |")
    print("|        please listen carefully.            |")
    print("|   This message will only be played once!   |")
    print("|  To get thru the minefield you need to go: |")
    print("|left, right, forward, left, backward, left. |")
    print("|  I hope you make it to the end. Good luck! |")

else:
    print("You did not click PLAY. Please try again.")
    
    
directions = ["left", "right", "forward", "left", "backward", "left"]
max_guesses = 10
current_step = 0
guess_count = 0

while current_step < len(directions) and guess_count < max_guesses:
    player_input = input(f"Enter your next move: ")

    if player_input == directions[current_step]:
        current_step += 1
    else:
        print("Oops! That's not the correct direction. Try again.")
        guess_count += 1

if current_step == len(directions):
    print("|Congratulations! You've successfully navigated the minefield.|")
else:
    print("You've exceeded the maximum number of guesses. Game over.")