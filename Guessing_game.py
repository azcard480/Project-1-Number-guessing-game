
    
"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random
high_score = 10


print("Welcome! Let's play a guessing game!  The number is between one and ten... GUESS!!")

def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player X.
    2. Store a random number as the answer/solution X.
    3. Continuously prompt the player for a guess X.
      a. If the guess greater than the solution, display to the player "It's lower" X.
      b. If the guess is less than the solution, display to the player "It's higher" X.
    
    4. Once the guess is correct, stop looping, inform the user they "Got it" X
         and show how many attempts it took them to get the correct number. X
    5. Let the player know the game is ending, or something that indicates the game is over. X
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    score = 0
    name = input("please enter your name: ")
    print("Okay {}, Guess a number between one and ten 1-10".format(name))
    
    the_number = random.randint(1,10)
    while True:
      try:
        number = int(input("Your guess is the number:  "))
        if number == the_number:
          print("WOW! You did it {}! You guessed the number in only {} guesses!".format(name, score))
          print("Thank you for playing {}, you did a super job!".format(name))
            
                

        if number < the_number:
          score += 1
          print("You're getting close {}, it is higher than {}. Try again.".format(name, number))
          print("Current Score: {}".format(score))
          continue
        elif number > the_number:
          score += 1
          print("You're getting close {}, it is lower than {}. Try again.".format(name, number))
          print("Current Score: {}".format(score))
          continue
        elif number >= 11:
          raise ValueError("It seemse like you guessed a number above 10.  Please guess between 1 and 10.")
          print("Current Score: {}".format(score))
        #else:
          #print("I don't think that is a number...")
    
    
      except ValueError:
        print("It seems like we have run into a slight problem please enter a different number.")  



                
# Kick off the program by calling the start_game function.
start_game()