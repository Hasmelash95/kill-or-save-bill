"""
Importing modules
"""
# To use os.clear to clear the terminal
import os
# For slow print
import sys
import time
# For dice rolls
from random import randint

# Constants
USERNAME_INPUT = None

# Messages to be printed depending on dice rolls
GUARD_FAILURE = "You can sense that time is running out!\n"
GUARD_SUCCESS = "You are one step closer to saving him!\n"
SHADOWS_FAILURE = "Your mark is getting increasingly wary!\n"
SHADOWS_SUCCESS = "Your mark is lowering his guard!\n"

# Dictionary to track the scores
score = {"iron_guard": 0, "smiling_shadows": 0}


def slow_print(text):
    """
    Function to define how the output is printed to the user.
    Code credit to Stack Overflow.
    Args:
    Text - parameter corresponds to the strings that will be
    slow printed. A letter at a time.
    """
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)


def clear_terminal():
    """
    Function to clear the terminal when it's called.
    Code credit to Stack Overflow.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    """
    Function to define the intro text, it will be the starting
    point whenever a user enters 'exit'.
    Sets the score for the dictionary values to 0 when function
    is called.
    Prints the introduction text and prompts the user to type 'go'
    to proceed with the game. Any input other than 'go' will get
    an invalid data alert.
    The pretty print function is called to print the score as
    defined by that function.
    """
    clear_terminal()
    slow_print("\nWelcome to this choose your own adventure"
               " game set in the city of Arx - based on\nthe"
               " text-based RPG Arx - After the Reckoning."
               " You can choose to play as members\nof the"
               " Ion Guard (the city watch) or the elusive"
               " group of assassins, the Smiling\nShadows."
               " As the game proceeds, you will be provided"
               " options that you can\nchoose from by entering"
               " 'a' or 'b' into the terminal. A total of two"
               " points\nfor the team of your choice is"
               " needed to win the game. Good luck!\n")
    pretty_print()
    while True:
        proceed = input("\nEnter 'go' to proceed.\n").lower().strip()
        if proceed != "go":
            print(f"{proceed} is invalid."
                  " Please type 'go' to proceed.\n")
        else:
            get_username()
            break


def get_username():
    """
    Function to define what a valid username would be.
    User must either enter a username between 1-8 chars
    and only use a-z characters.
    If the username is not valid, it will prompt an alert
    and ask the user to try again.
    Typing 'exit' will exit the application.
    """
    clear_terminal()
    global USERNAME_INPUT
    while True:
        USERNAME_INPUT = input("\nWhat's your name?\n"
                               "Choose a name with 1-8 characters:\n"
                               "(Only a-z characters)\n"
                               "You can type 'exit' at"
                               " any time to exit app.\n").strip()
        if USERNAME_INPUT == "exit" or USERNAME_INPUT == "Exit":
            print("Exiting application...")
            sys.exit()
        elif len(USERNAME_INPUT) > 8 or len(USERNAME_INPUT) < 1:
            print("\nUsername must be 1-8 characters."
                  f" {USERNAME_INPUT} is {len(USERNAME_INPUT)} characters."
                  " Please try again.\n")
        elif USERNAME_INPUT.isalpha() is not True:
            print("\nUsername must only consist of"
                  " a-z characters. Please try again.\n")
        else:
            choose_org()
            break


def choose_org():
    """
    Function to define the two game choices (whether user wishes to be a
    good guy - the Iron Guard -  or a bad guy - the Smiling Shadows.)
    Any input other than those two options will call the input_validation
    function.
    The While loop persists until the user types a valid input.
    """
    clear_terminal()
    while True:
        org = input("\nAre you an Iron Guard or a Smiling Shadow?\n"
                    "Choose A or B:\n"
                    " A: Iron Guard\n"
                    " B: Smiling Shadow\n").lower().strip()
        if org == "a":
            slow_print(f"\nHello {USERNAME_INPUT}, the citizens of Arx once"
                       " again need you to keep them safe.\nThere are"
                       " rumors that a hit has been placed on poor"
                       " Bill, the Blacksmith.\nThe vile assassins of"
                       " the Smiling Shadows must be stopped before"
                       " another life\nis unjustly lost.\n")
            good_guy()
            break
        if org == "b":
            slow_print(f"\nHello {USERNAME_INPUT}, the boss has a job for you"
                       " and it pays verrryyy well.\nBrace yourself."
                       " Apparently someone really has it in for Bill,"
                       " the Blacksmith.\nSomeone wealthy. We don't"
                       " ask questions beyond that as you well know."
                       " Today\nis your lucky day. Take this job and the"
                       " money is all yours. Minus a cut taken\nby your"
                       " betters.\n")
            bad_guy()
            break
        input_validation(org)


def good_guy():
    """
    Part one of the good guy game (Iron Guard), player can choose
    one option which will give them an automatic score increase,
    or the other option which will take them to a dice roll.
    The While loop persists until the user types a valid input.
    """
    while True:
        investigation_style = input("\nDo you gently question the commoners"
                                    " in the Lower Boroughs?\n"
                                    "Choose A or B:\n"
                                    " A: Of course!\n"
                                    " B: No, I rough them up a"
                                    " bit.\n").lower().strip()
        if investigation_style == "a":
            score["iron_guard"] += 1
            pretty_print()
            slow_print("\nYou catch more flies with honey"
                       " than with vinegar.\n")
            good_guy_two()
            break
        if investigation_style == "b":
            increment_score("iron_guard", "smiling_shadows", GUARD_FAILURE,
                            GUARD_SUCCESS)
            good_guy_two()
            break
        input_validation(investigation_style)


def increment_score(pteam, cteam, fail_message, success_message):
    """
    Function to roll a 10 sided dice for the player and the
    computer and compare their rolls.
    If the player gets a higher roll, player's team gets a point.
    If the computer gets a higher roll, the opposing team do.
    If player and computer rolls are tied, then there will be
    reroll and the While loop continues until the rolls are not
    tied.
    Args:
    Pteam - refers to the player's team in the dictionary.
    Cteam - refers to the computer's team in the dictionary.
    fail_message - for the message that will be printed when player
    loses dice roll.
    success_message - for the message that will be printed when
    player wins dice roll.
    """
    while True:
        player_roll = randint(1, 10)
        comp_roll = randint(1, 10)
        slow_print(f"\nYou rolled {player_roll} against {comp_roll}!")

        if player_roll > comp_roll:
            score[pteam] += 1
            pretty_print()
            slow_print(success_message)
            break
        if player_roll < comp_roll:
            score[cteam] += 1
            pretty_print()
            slow_print(fail_message)
            break


def good_guy_two():
    """
    Function for second selection of options, for the
    Iron Guard game one will lead to a dice roll while
    the other will be an instant fail that ends the game.
    """
    slow_print("\nYou find out that an ambush is being plotted"
               " for poor Bill in Nightingale\nPark. The assassins"
               " were hired by his romantic rival, Bob.\n")
    while True:
        chase_shadows = input("\nWhat do you do?\n"
                              "Choose A or B:\n"
                              " A: Find Bob and bring him to justice!\n"
                              " B: Get to Nightingale Park!\n").lower().strip()
        if chase_shadows == "a":
            slow_print("\nYou find Bob in his house and bring"
                       " him in to the House of Questions.\n"
                       "Unfortunately, you hear that Bill has"
                       " been found stabbed in the Park, declared\n"
                       "dead on site. With insufficient evidence,"
                       " the wealthy merchant, Bob, is\nreleased.\n")
            # Instant fail code
            game_over_fail()
            break
        if chase_shadows == "b":
            increment_score("iron_guard", "smiling_shadows", GUARD_FAILURE,
                            GUARD_SUCCESS)
            good_guy_final()
            break
        input_validation(chase_shadows)


def good_guy_final():
    """
    Function that defines the final pair of selections
    for the Iron Guard game.
    One will lead to a dice roll while the other will be
    an instant fail that ends the game.
    """
    while True:
        confront = input("\nYou get to the Nightingale Park, what do you do?\n"
                         "Choose A or B:\n"
                         " A: Charge at the assassins"
                         " as soon as I enter.\n"
                         " B: Create a noise distraction"
                         " before aiming for the targets.\n").lower().strip()
        if confront == "a":
            slow_print("\nYou immediately charge at the assassins but"
                       " they are professionals and simply\nslide"
                       " away. You find yourself with multiple stab"
                       " wounds in the back. It\nseems you will be"
                       " joining Bill.\n")
            # Instant fail code
            game_over_fail()
            break
        if confront == "b":
            increment_score("iron_guard", "smiling_shadows", GUARD_FAILURE,
                            GUARD_SUCCESS)
            good_guy_final_score()
            break
        input_validation(confront)


def bad_guy():
    """
    Part one of the bad guy game (Smiling Shadows), player can choose
    one option which will give them an automatic score increase,
    or the other option which will take them to a dice roll.
    The While loop persists until the user types a valid input.
    """
    while True:
        assassin_style = input("\nHow do you find your target?\n"
                               "Choose A or B:\n"
                               " A: Charm his friends.\n"
                               " B: Stalk his movements.\n").lower().strip()
        if assassin_style == "a":
            score["smiling_shadows"] += 1
            pretty_print()
            slow_print("\nWell done. It's better if your prey isn't"
                       " on guard.\n")
            bad_guy_two()
            break
        if assassin_style == "b":
            increment_score("smiling_shadows", "iron_guard", SHADOWS_FAILURE,
                            SHADOWS_SUCCESS)
            bad_guy_two()
            break
        input_validation(assassin_style)


def bad_guy_two():
    """
    Function for second selection of options, for the
    Smiling Shadows game one will lead to a dice roll while
    the other will be an instant fail that ends the game.
    The While loop persists until the user types a valid input.
    """
    slow_print("\nYou find out that Bill likes to wander around"
               " Nightingale Park in the evenings.\n")
    while True:
        timing = input("\nDo you ambush him the first chance you get"
                       " or map out the area for onlookers?\n"
                       " A: Map out the area.\n"
                       " B: Ambush ASAP!\n").lower().strip()
        if timing == "a":
            increment_score("smiling_shadows", "iron_guard", SHADOWS_FAILURE,
                            SHADOWS_SUCCESS)
            bad_guy_final()
            break
        if timing == "b":
            slow_print("\nYou may have wanted to do some reconnaissance."
                       " An Iron Guard man catches you\nin your"
                       " attempt and you are brought to the House"
                       " of Questions. Not to be\nlet free until you"
                       " talk about your employer. The boss may not"
                       " let you live\nthrough this failure.\n")
            # Instant fail code
            game_over_fail()
            break
        input_validation(timing)


def bad_guy_final():
    """
    Function that defines the final pair of selections
    for the Smiling Shadows game.
    One will lead to a dice roll while the other will be
    an instant fail that ends the game.
    The While loop persists until the user types a valid input.
    """
    while True:
        ambush = input("\nHow do you attack?\n"
                       " A: Leap out of the bushes and"
                       " attempt to strike with my"
                       " dagger!\n"
                       " B: Blend in to the surroundings,"
                       " behaving like any other\n passerby"
                       " before attacking once close"
                       "enough.\n").lower().strip()
        if ambush == "a":
            slow_print("\nYou leap out of the bushes and Bill,"
                       " startled by your presence\nscreams"
                       " like a maniac and flees, calling out"
                       " for help in the meanwhile.\nYou don't"
                       " dare follow after him. This did not"
                       " go as you had\nhoped. The boss may"
                       " laugh but not in your favor.\n")
            # Instant fail code
            game_over_fail()
            break
        if ambush == "b":
            increment_score("smiling_shadows", "iron_guard", SHADOWS_FAILURE,
                            SHADOWS_SUCCESS)
            bad_guy_final_score()
            break
        input_validation(ambush)


def good_guy_final_score():
    """
    Function to define what would count as a success
    and the message to display if the player succeeds
    or fails the Iron Guard game.
    If the player gets a score of 2 or more, then the
    success outcome will be printed. If not, the failure
    outcome will be.
    """
    if score["iron_guard"] >= 2:
        slow_print("\nYou succeed in striking and"
                   " killing the assassin who is"
                   " about to deal the\nkilling blow"
                   " to Bill. The other, you swiftly"
                   " hold at blade point, to bring her\n"
                   "in to the House of Questions."
                   " Maybe Bob will be brought to justice"
                   " after all.\nBill thanks you profusely"
                   " and lets you know that you will never"
                   " need to pay for\nhis smithing services"
                   " again. Maybe there's a promotion in"
                   " your near future\ntoo.\n")
        game_over_succeed()
    else:
        slow_print("\nYou try to attack the assassin who is"
                   " about to deal the killing blow to"
                   " Bill.\nHowever, you miss and stab the"
                   " other instead. She falls to the ground"
                   " lifelessly\nbut so does Bill. You"
                   " were not fast enough. The killer runs"
                   " off while you\nstare at Bill's still"
                   " body in shock.\n")
        game_over_fail()


def bad_guy_final_score():
    """
    Function to define what would count as a success
    and the message to display if the player succeeds
    or fails the Shadows game.
    If the player gets a score of 2 or more, then the
    success outcome will be printed. If not, the failure
    outcome will be.
    """
    if score["smiling_shadows"] >= 2:
        slow_print("\nYou walk past Bill nochalantly and"
                   " stab him until he falls to ground,"
                   " lifeless.\nNo one is around, so you"
                   " make your swift exit. A glorious"
                   " payday. There may even\nbe a promotion"
                   " in your near future.\n")
        game_over_succeed()
    else:
        slow_print("\nYou walk past Bill nochalantly and"
                   " attempt a mortal blow. Alas, you"
                   " are\nonly able to nick him a little"
                   " which gives him the time to struggle"
                   " from your\ngrip and call for help."
                   " It seems you've missed your chance."
                   " This will not\ngo over well at the"
                   " guildhall.\n")
        game_over_fail()


def game_over_succeed():
    """
    Function to display the general game success message when called.
    """
    slow_print(f"\nCongratulations, {USERNAME_INPUT}! You have succeeded"
               " in your mission!\n")
    start_again()


def game_over_fail():
    """
    Function to display the general game failure message when called.
    """
    slow_print(f"\nOh no, {USERNAME_INPUT}, you have failed your mission.\n")
    start_again()


def start_again():
    """
    Function that defines the start again options.
    The score for each team will revert to 0 and will
    display to user.
    User can start again without needing to go
    through the introduction or input their username
    by typing 'a' or exit to the main page by typing
    'b'.
    The While loop persists until the user types a valid input.
    """
    # Resetting the scores to 0
    score["iron_guard"] = 0
    score["smiling_shadows"] = 0

    while True:
        restart_game = input("\nWould you like to start again?\n"
                             " A: Yes.\n"
                             " B: No, take me to the"
                             " intro.\n").lower().strip()
        if restart_game == "a":
            choose_org()
            break
        if restart_game == "b":
            slow_print("\nHope you have another go soon!\n")
            main()
            break
        input_validation(restart_game)


def pretty_print():
    """
    Function to define how the scores (the dictionary) will be formatted.
    """
    for team, value in score.items():
        print("\n----------------------------\n"
              f"     {team}: {value} \n"
              "----------------------------\n")


def input_validation(variable):
    """
    A function to place the validation message global to a majority
    of the game. If a user selects anything other than 'a' or 'b'
    during the game, they will be taken here.
    If they type anything other than 'exit', the original question
    will be repeated until they enter a valid input.
    """
    if variable == "exit":
        print("Exiting application...")
        sys.exit()
    else:
        print("\nPlease choose A or B\n")


# The function will only be called if the file is run from the command line
# The code will not be executed if the file is imported from another file
if __name__ == "__main__":
    main()
