#Rock Paper Scissors
import random
#importing all the ascii art from the asciiart.py file
from asciiArt import *

print(welcomeMsg)
game_Images = [rock,paper,scissors]
user_choice = int(input("Welcome to Rock Paper Scissors Game.\nYou will be playing against Computer. \nYou are going first and what do you choose? \nEnter 0 for Rock, 1 for Paper and 2 for Scissors\n"))

print("User Choice:\n")
print(game_Images[user_choice])

#generating a random integer from 0 to 2 for computer to play
computer_choice = random.randint(0,2)
print("\n\nComputer Choice:")
print(game_Images[computer_choice])

#game logic
if user_choice == 0 and computer_choice == 2:
    print(win)
elif computer_choice ==2 and user_choice ==1:
    print(lose)
if user_choice > computer_choice:
    print(win)
elif user_choice < computer_choice:
    print(lose)
elif user_choice == computer_choice:
    print(draw)
elif user_choice >2 or user_choice < 0:
    print("Invalid Option")
    print(lose)
