# Importing modules
# To use os.clear to clear the terminal
import os 
# For slow print
import sys
import time
# For dice rolls
from random import randint

# Dictionary to track the scores
score = {"iron_guard": 0, "smiling_shadows": 0}
GUARD = "guard"
SHADOW = "shadow"
player = ""

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
                           " Choose A or B:\nA) Yes\nB) No\n"
                           "You can exit anytime by typing 'exit'\n").lower()
        if user_input == "a":
            get_username()
            break
        elif user_input == "b":
            slow_print("awww")
            break
        elif user_input == "exit":
            main()
        else:
            slow_print("Please choose A or B")                


def get_username():
    """
    Function to define what a valid username would be
    """
    global username
    while True:
        username = input("What's your name?"
                         " Choose a name with 1-8 chars:\n")
        if len(username) >= 1 and len(username) <= 8:
            choose_org()  
            break
        else:
            slow_print("Invalid input, username must be 1-8 chars long.\n")       


def choose_org():
    """
    Function to define the two game choices (whether user wishes to be a
    good guy or a bad guy.)
    """
    while True:
        org = input("Are you an Iron Guard or a Smiling Shadow?\n"
                    " Choose A or B:\n"
                    " A: Iron Guard\n"
                    " B: Smiling Shadow\n").lower()
        if org == "a":
            print(f"Hello {username}, the citizens of Arx once" 
                       " again need you to keep them safe. There are"
                       " rumors that a hit has been placed on poor"
                       " Bill, the Blacksmith. The vile assassins of"
                       " the Smiling Shadows must be stopped before"
                       " another life is unjustly lost.")
            good_guy()
            break
        elif org == "b":
            slow_print(f"Hello {username}, the boss has a job for you"
                       " and it pays verrryyy well. Brace yourselves."
                       " Apparently someone really has it in for Bill,"
                       " the Blacksmith. Someone wealthy. We don't"
                       " ask questions beyond that as you well know."
                       " Today is your lucky day. Take this job and the"
                       " money is all yours. Minus a cut taken by yours"
                       " truly.")    
            bad_guy()
            break
        elif org == "exit":
            main()
        else:
            slow_print("Please choose A or B")   

def good_guy():
    investigation_style = input("Do you gently question the commoners"
                                " in the Lower Boroughs?"
                                " Choose A or B:\n"
                                " A: Of course!\n"
                                " B: No, I rough them up a bit.\n").lower()
    if investigation_style == "a":
        good_guy_two()
    elif investigation_style == "b":
        dice_roll_1()
    elif investigation_style == "exit":   
        main()
    else:
        slow_print("Please choose A or B") 


def dice_roll_1():
    """
    Roll a 10 sided dice against the computer for Iron Guard game
    """
    player_roll = randint(1, 10)
    comp_roll = randint(1, 10)
    print(f"You rolled {player_roll} against {comp_roll}!")
    
    if player_roll >= comp_roll: 
        for team, value in score.items():
            if team == "iron_guard":
                score[team] += 1
    else: 
        for team, value in score.items():
            if team == "smiling_shadows":
                score[team] += 1


def good_guy_two():
    print("woo!")

def bad_guy():
    print("mwahaha")

main()
 
print(score)
