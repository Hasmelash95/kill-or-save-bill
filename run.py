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
    Function to define how the output is printed to the user. Code credit to Stack Overflow.
    """
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.07)

def user_prompt(prompt):
    """
    Function to format the user response
    """

    user_input = input(prompt + "\n").strip().lower()
    return user_input

def 