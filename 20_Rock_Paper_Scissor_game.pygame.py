import random

'''
The logic (who beats whom):

Rock🪨 crushes Scissors → Rock beats Scissors
Scissors✂️cuts Paper → Scissors beats Paper
Paper 📄covers Rock → Paper beats Rock'''

'''

R -> Rock -> 1
P -> Paper -> -1
S -> Scissors -> 0

'''

yourdict = {"R": 1, "P": -1, "S": 0}
computer = random.choice([1, -1, 0])
yourstr = input("Enter your choice (R/P/S)")
you = yourdict[yourstr]

if computer == you:
    print("It's a tie!") # TIE

# ROCK CASE 
elif computer == 1 and you == -1: # rock vs paper -> paper wins
    print("You win :)")
elif computer == 1 and you == 0: # rock vs scissor -> rock wins 
    print("You lost:(")

# PAPER CASE 
elif computer == -1 and you == 0: # paper vs scissor -> scissor wins 
    print("You win :)!")

elif computer == -1 and you == 1: # paper vs Rock -> paper wins
    print("You lost:(!")

# SCISSOR CASE 
elif computer == 0 and you == 1: # scissor vs rock -> rock wins 
    print("You win :)!")

elif computer == 0 and you == -1: # scissor vs paper -> scissor wins
    print("You lost:(!")

else:
    print("Something went wrong!!")


'''ONE MORE GAME TASK WITH SAME RULES WE CAN TRY OUT ->
_______"SNAKE WATER GUN GAME"_______

This->beat->because
🐍 Snake->Water->Snake drinks the water
💧 Water->Gun->Water floods/rusts the gun, making it useless
🔫 Gun->Snake->Gun shoots the snake'''
