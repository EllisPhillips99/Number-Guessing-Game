"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random
"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    import time
    import random
    welcome ="Welcome to the number guessing game!"
    words = welcome.split()
    for word in words:
        print(word)
        time.sleep(.3)
    user_name = input("What is your name?   ")
    print(f"Hello {user_name}! I have chosen a random number between 1 and 10. Try guessing what it is.")

    random_number = random.randint(1,10)
    tries = 0
    while True:
    
    
        tries +=1
        try:
            user_guess = int(input("Number Guess: "))
         except ValueError: 
        print("Please enter a numeric value.")
    else:
        if user_guess > random_number:
            print('Too high')
    
        if user_guess < random_number:
            print('Too low.')
         
        if user_guess == random_number:
            print(f"Congrats {user_name}! You guessed correctly.")
            print(f"It took you {tries} tries.")
            play_again = input("Would you like to play again? (Yes/No)")
            if play_again.lower() == 'yes':
                random_number = random.randint(1,10)
                tries = 0
                continue
            elif play_again.lower() == 'no':
                break
start_game()

def start_game():
   
