#voice recorder is at a different location
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
    

directions = ["left", "right", "forward", "left", "backward", "left"]
current_step = 0

while current_step < len (directions):
    player_input = input (f"Enter your next move ({directions[current_step]}: ")

if player_input == directions[current_step]:
    current_step+= 1

else: 
    print("oops! that's not the correct direction. Try again.")


print("|Congratulations! you've succesfully navigated the minefield.|")
