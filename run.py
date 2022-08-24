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

"""
Dictionary to track the scores
"""
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


def intro():
    """
    Function to define the intro text, it will be the starting 
    point whenever a user selects exit
    """
    for team, value in score.items():
        score[team] = 0
    print(score)
    print("Welcome to this choose your own adventure"
          " game set in the city of Arx - based on the"
          " text-based rpg, Arx - After the Reckoning."
          " Players can choose to play as members of the"
          " Ion Guard (the city watch) or the elusive"
          " group of assassins, the Smiling Shadows."
          " As the game proceeds, players will be provided"
          " options that they can choose from by enterring"
          " 'a' or 'b' into the terminal. A total of two"
          " points for the team of the players' choice is"
          " needed to win the game. Good luck!")
    while True:           
        proceed = input("Enter 'go' to proceed.\n").lower()
        try:
            if proceed == "go":
                main()
                break
            else:
                raise ValueError("Please type 'go' to proceed.")
        except ValueError as e:
            print(f"Invalid input: {proceed}. {e}.")
            

def main():
    """
    Function defining main starting point and the option
    to start the game or not.
    """
    while True:
        user_input = input("Would you like to start the game?" 
                           " Choose A or B:\n"
                           " A: Yes\n"
                           " B: No\n"
                           " You can exit anytime by typing 'exit'\n").lower()
        if user_input == "a":
            get_username()
            break
        elif user_input == "b":
            print("Hope to see you again soon!")
            intro()
            break
        elif user_input == "exit":
            intro()
            break
        else:
            print("Please choose A or B")               


def get_username():
    """
    Function to define what a valid username would be. 
    An error is raised if the conditions listed are 
    not met.
    User must either enter a username between 1-8 chars.
    Typing 'exit' will take the user to intro section.
    """
    global username
    while True:
        username = input("What's your name?"
                         " Choose a name with 1-8 chars:\n"
                         " Only a-z characters\n").lower()
        try: 
            if username.isalpha():
                intro()
            else:
                raise ValueError("Username must only contain"
                                 " letters a-z")
            if username == "exit":
                intro()               
            elif len(username) >= 1 and len(username) <= 8:
                choose_org()  
                break
            else:
                raise ValueError("Username must be 1-8 chars long"
                                 f" {username} is {len(username)} chars")
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again. \n")       


def choose_org():
    """
    Function to define the two game choices (whether user wishes to be a
    good guy - the Iron Guard -  or a bad guy - the Smiling Shadows.)
    """
    while True:
        org = input("Are you an Iron Guard or a Smiling Shadow?\n"
                    " Choose A or B:\n"
                    " A: Iron Guard\n"
                    " B: Smiling Shadow\n").lower()
        if org == "a":
            slow_print(f"Hello {username}, the citizens of Arx once" 
                       " again need you to keep them safe. There are"
                       " rumors that a hit has been placed on poor"
                       " Bill, the Blacksmith. The vile assassins of"
                       " the Smiling Shadows must be stopped before"
                       " another life is unjustly lost.")
            good_guy()
            break
        elif org == "b":
            slow_print(f"Hello {username}, the boss has a job for you"
                       " and it pays verrryyy well. Brace yourself."
                       " Apparently someone really has it in for Bill,"
                       " the Blacksmith. Someone wealthy. We don't"
                       " ask questions beyond that as you well know."
                       " Today is your lucky day. Take this job and the"
                       " money is all yours. Minus a cut taken by yours"
                       " truly.")    
            bad_guy()
            break
        elif org == "exit":
            intro()
            break
        else:
            print("Please choose A or B")   


def good_guy():
    """
    Part one of the good guy game (Iron Guard), player can choose 
    one option which will give them an automatic score increase,
    or the other option which will take them to a dice roll.
    While loop only breaks when user makes a valid input.
    """
    while True:
        investigation_style = input("Do you gently question the commoners"
                                    " in the Lower Boroughs?"
                                    " Choose A or B:\n"
                                    " A: Of course!\n"
                                    " B: No, I rough them up a bit.\n").lower()
        if investigation_style == "a":
            score["iron_guard"] += 1 
            print(score)
            slow_print("You catch more flies with honey than with vinegar.")       
            good_guy_two()
            break
        elif investigation_style == "b":
            dice_roll()
            good_guy_increment_score()
            good_guy_two()
            break
        elif investigation_style == "exit":   
            intro()
            break
        else:
            print("Please choose A or B") 


def dice_roll():
    """
    Rolls a 10 sided dice against the computer and
    prints the result to user.  
    """
    global player_roll
    global comp_roll
    player_roll = randint(1, 10)
    comp_roll = randint(1, 10)
    print(f"You rolled {player_roll} against {comp_roll}!")


def good_guy_increment_score():
    """
    Function to increment the score for the good guy game as a 
    result of dice rolls.
    If the player gets a higher roll, player's team gets a point.
    If the computer gets a higher roll, the opposing team do.
    If player and computer rolls are tied, then there will be 
    reroll. 
    """
    if player_roll > comp_roll: 
        score["iron_guard"] += 1 
        print(score)
    elif player_roll == comp_roll:
        dice_roll()   
    else: 
        score["smiling_shadows"] += 1  
        print(score)            


def bad_guy_increment_score():
    """
    Function to increment the score for the bad guy game as a 
    result of dice rolls.
    If the player gets a higher roll, player's team gets a point.
    If the computer gets a higher roll, the opposing team do.
    If player and computer rolls are tied, then there will be 
    reroll. 
    """
    if player_roll > comp_roll: 
        score["smiling_shadows"] += 1 
        print(score)
    elif player_roll == comp_roll:
        dice_roll()   
    else: 
        score["iron_guard"] += 1  
        print(score)


def good_guy_two():
    """
    Function for second selection of options, for the 
    Iron Guard game one will lead to a dice roll while 
    the other will be an instant fail that gives the
    Smiling Shadows an additional two points and ends
    the game.
    """
    slow_print("You find out that the an ambush is being plotted"
               " for poor Bill in Nightingale Park. The assassins"
               " were hired by his romantic rival, Bob.")
    while True:
        chase_shadows = input("What do you do?\n"
                              " Choose A or B:\n"
                              " A: Find Bob and bring him to justice\n"
                              " B: Get to Nightingale Park!\n").lower()
        if chase_shadows == "a":
            slow_print("You find Bob in his house and bring"
                       " him in to the House of Questions."
                       " Unfortunately, you hear that Bill has"
                       " been found stabbed in the Park, declared"
                       " dead on site. With insufficient evidence,"
                       " the wealthy merchant, Bob, is released.")  
            # Instant fail code
            score["smiling_shadows"] += 2                  
            game_over_fail()
            break              
        elif chase_shadows == "b":
            dice_roll()
            good_guy_increment_score()
            good_guy_final()
            break
        elif chase_shadows == "exit":   
            intro()
            break
        else:
            print("Please choose A or B") 


def good_guy_final():
    """
    Function that defines the final pair of selections 
    for the Iron Guard game.
    One will lead to a dice roll while the other will be
    an instant fail that will deduct one point from the
    Iron Guard and add a point to the Smiling Shadows.
    """
    while True:
        confront = input("You get to the Nightingale Park, what do you do?\n"
                         " Choose A or B:\n"
                         " A: Charge at the assassins"
                         " as soon as you enter\n"
                         " B: Create a noise distraction"
                         " before aiming for the targets"
                         " while their heads are turned\n").lower()
        if confront == "a":
            slow_print("You immediately charge at the assassins but"
                       " they are professionals and simply slide"
                       " away. You find yourself with multiple stab"
                       " wounds in the back. It seems you will be"
                       " joining Bill.")
            # Instant fail code
            score["smiling_shadows"] += 1  
            score["iron_guard"] -= 1
            print(score)
            game_over_fail()
            break
        elif confront == "b":
            dice_roll()
            good_guy_increment_score()
            good_guy_final_score()
            break
        elif confront == "exit":
            intro()
            break
        else: 
            print("Please choose A or B")


def bad_guy():
    """
    Part one of the good guy game (Smiling Shadows), player can choose 
    one option which will give them an automatic score increase,
    or the other option which will take them to a dice roll.
    While loop only breaks when user makes a valid input.
    """
    while True:
        assassin_style = input("How do you find your target?\n"
                               " Choose A or B:\n"
                               " A: Charm his friends\n"
                               " B: Stalk his movements\n").lower()
        if assassin_style == "a":
            score["smiling_shadows"] += 1 
            slow_print("Well done. It's better if your prey isn't"
                       " on guard.")       
            bad_guy_two()
            break
        elif assassin_style == "b":
            dice_roll()
            bad_guy_two()
            break
        elif assassin_style == "exit":
            intro()
            break
        else:
            print("Please choose A or B") 


def bad_guy_two():
    """
    Function for second selection of options, for the 
    Smiling Shadows game one will lead to a dice roll while 
    the other will be an instant fail that gives the
    Iron Guard an additional two points and ends
    the game.
    """
    slow_print("You find out that Bill likes to wander around"
               " Nightingale Park in the evenings.")
    while True:
        timing = input("Do you ambush him the first chance you get"
                       " or map out the area for onlookers?\n"
                       " A: Map out the area\n"
                       " B: Ambush ASAP\n").lower()
        if timing == "a":
            dice_roll()
            bad_guy_increment_score()
            bad_guy_final()
            break
        elif timing == "b":
            slow_print("You may have wanted to do a reconnaissance."
                       " An Iron Guard man catches you in your"
                       " attempt and you are brought to the House"
                       " of Questions. Never to be let free till"
                       " you admit who hired you. The boss may not"
                       " let you live through this failure.")
            # Instant fail code
            score["iron_guard"] += 2                  
            game_over_fail()
            break 
        elif timing == "exit":
            intro()
            break          
        else:
            print("Please choose A or B") 


def bad_guy_final():
    """
    Function that defines the final pair of selections
    for the Smiling Shadows game.
    One will lead to a dice roll while the other will be
    an instant fail that will deduct one point from the
    Smiling Shadows and add a point to the Iron Guard.
    """
    while True:
        ambush = input("How do you attack?\n"
                       " A: Leap out of the bushes and"
                       " attempt to strike with my"
                       " dagger"
                       " B: Blend in to the surroundings,"
                       " behaving like any other passerby"
                       " before attacking once close enough").lower()
        if ambush == "a":
            slow_print("You leap out of the bushes and Bill,"
                       " startled by your presence screams"
                       " like a maniac and flees, calling out"
                       " for help in the meanwhile. You don't"
                       " dare follow after him. This did not"
                       " go as you had hoped.")
            # Instant fail code
            score["iron_guard"] += 1  
            score["smiling_shadows"] -= 1
            print(score)
            game_over_fail()
            break
        elif ambush == "b":
            dice_roll()
            bad_guy_increment_score()
            bad_guy_final_score()
            break
        elif ambush == "exit":
            intro()
            break
        else:
            print("Please choose A or B")


def good_guy_final_score():
    """
    Function to define what would count as a success
    and the message to display if the player succeeds 
    or fails.
    """
    if score["iron_guard"] >= 2:
        slow_print("\nYou succeed in striking and"
                   " killing the assassin who is"
                   " about to deal the killing blow"
                   " to Bill. The other, you swiftly"
                   " hold at blade point, to bring her"
                   " in to the House of Questions."
                   " Maybe Bob will be brought to justice"
                   " after all. Bill thanks you profusely"
                   " and lets you know that you will never"
                   " need to pay for his smithing services"
                   " again. Maybe there's a promotion in"
                   " your near future too.")
        game_over_succeed()
    else:
        slow_print("You try to attack the assassin who is"
                   " about to deal the killing blow to"
                   " Bill. However, you miss and stab"
                   " other instead. He falls to the ground"
                   " lifelessly but so too does Bill. You"
                   " were not fast enough. The killer runs"
                   " off while you stare at Bill's still"
                   " body in shock.") 
        game_over_fail()


def bad_guy_final_score():
    """
    Function to define what would count as a success
    and the message to display if the player succeeds 
    or fails.
    """
    if score["smiling_shadows"] >= 2:
        slow_print("You walk past Bill nochalantly and"
                   " stab him until he fals to ground,"
                   " lifeless. No one is around, so you"
                   " make your swift exit. A glorious"
                   " payday. There may even be a promotion"
                   " in your near future.")
        game_over_succeed()


def game_over_succeed():
    slow_print("Congratulations, you have succeeded in your" 
               " mission!")
    start_again()


def game_over_fail():
    slow_print("You have failed your mission.")
    start_again()


def start_again():    
    while True:
        start_again = input("Would you like to start again?\n"
                            " A: Yes\n"
                            " B: No\n").lower()
        if start_again == "a":
            for team, value in score.items():
                score[team] = 0
            choose_org()
            break
        elif start_again == "b":
            print("Hope to see you again soon!")
            intro()
            break
        elif start_again == "exit":
            intro()
            break
        else:
            print("Please choose A or B")
         
    print(score)


intro()
