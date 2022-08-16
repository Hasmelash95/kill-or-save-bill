# Importing modules
# To use os.clear to clear the terminal
import os 
# For slow print
import sys
import time

def slow_print(text):
    """
    Function to define how the output is printed to the user. Code credit to StackOverflow.
    """
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.08)

