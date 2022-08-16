# Importing modules
# To use os.clear to clear the terminal
import os 
# For slow print
import sys
import time

# Dictionary to track the scores
score = {"iron_guard": 0, "smiling_shadows": 0}

def slow_print(text):
    """
    Function to define how the output is printed to the user. 
    Code credit to Stack Overflow.
    """
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.07)


def main():
    """
    Function defining main starting point
    """
    while True:
        user_input = input("Would you like to start the game?" 
               " Choose A or B:\nA) Yes\nB) No\n").strip().lower()
        if user_input == "a":
            get_username()
            break
        elif user_input == "b":
            slow_print("awww")
            break
        else:
            slow_print("Please choose A or B")     
            

def get_username():
    """
    Function to define what a valid username would be
    """
    while True:
        username = input("What's your name?"
                        " Choose a name with 1-8 chars:\n").strip()
        if len(username) >= 1 and len(username) <= 8:
            break
        else:
            slow_print("Invalid input, username must be 1-8 chars long.\n")
        
    return username

main()   