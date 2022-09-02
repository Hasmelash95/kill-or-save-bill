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


def slow_print(text):
    """
    Function to define how the output is printed to the user. 
    Code credit to Stack Overflow.
    """
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)


def main():
    """
    Function to define the intro text, it will be the starting 
    point whenever a user selects exit
    """
    for team, value in score.items():
        score[team] = 0
    print("\nWelcome to this choose your own adventure"
          " game set in the city of Arx - based on\nthe"
          " text-based RPG Arx - After the Reckoning."
          " You can choose to play as members\nof the"
          " Ion Guard (the city watch) or the elusive"
          " group of assassins, the Smiling\nShadows."
          " As the game proceeds, you will be provided"
          " options that you can\nchoose from by enterring"
          " 'a' or 'b' into the terminal. A total of two"
          " points\nfor the team of the your choice is"
          " needed to win the game. Good luck!\n")
    while True:          
        proceed = input("\nEnter 'go' to proceed.\n"
                        "You can type 'exit' at"
                        " any time to exit.\n").lower().strip()
        if proceed == "go":
            get_username()
            break
        else:
            print(f"{proceed} is invalid."
                  "Please type 'go' to proceed.\n")
            

def get_username():
    """
    Function to define what a valid username would be. 
    An error is raised if the conditions listed are 
    not met.
    User must either enter a username between 1-8 chars.
    Typing 'exit' will take the user to intro section.
    """
    print(score)
    global username
    while True:
        username = input("\nWhat's your name?\n"
                         "Choose a name with 1-8 characters:\n"
                         "(Only a-z characters)\n")
        if username == "exit" or username == "Exit":
            main()
        elif len(username) >= 1 and len(username) <= 8:
            if username.isalpha():
                choose_org()
                break
            else:
                print("\nUsername must only consist of"
                      " a-z characters. Please try again.\n")
        else:
            print("\nUsername must be 1-8 characters."
                  f"{username} is {len(username)} characters."
                  " Please try again.\n")                    

def choose_org():
    """
    Function to define the two game choices (whether user wishes to be a
    good guy - the Iron Guard -  or a bad guy - the Smiling Shadows.)
    """
    while True:
        org = input("\nAre you an Iron Guard or a Smiling Shadow?\n"
                    "Choose A or B:\n"
                    " A: Iron Guard\n"
                    " B: Smiling Shadow\n").lower().strip()
        if org == "a":
            slow_print(f"Hello {username}, the citizens of Arx once" 
                       " again need you to keep them safe.\nThere are"
                       " rumors that a hit has been placed on poor"
                       " Bill, the Blacksmith.\nThe vile assassins of"
                       " the Smiling Shadows must be stopped before"
                       " another life\nis unjustly lost.\n")
            good_guy()
            break
        elif org == "b":
            slow_print(f"Hello {username}, the boss has a job for you"
                       " and it pays verrryyy well.\nBrace yourself."
                       " Apparently someone really has it in for Bill,"
                       " the Blacksmith.\nSomeone wealthy. We don't"
                       " ask questions beyond that as you well know."
                       " Today\nis your lucky day. Take this job and the"
                       " money is all yours. Minus a cut taken\nby your"
                       " betters.\n")    
            bad_guy()
            break
        elif org == "exit":
            main()
            break
        else:
            print("\nPlease choose A or B\n")   


def good_guy():
    """
    Part one of the good guy game (Iron Guard), player can choose 
    one option which will give them an automatic score increase,
    or the other option which will take them to a dice roll.
    While loop only breaks when user makes a valid input.
    """
    while True:
        investigation_style = input("\nDo you gently question the commoners"
                                    " in the Lower Boroughs?\n"
                                    "Choose A or B:\n"
                                    " A: Of course!\n"
                                    " B: No, I rough them up a bit.\n").lower().strip()
        if investigation_style == "a":
            score["iron_guard"] += 1 
            print(score)
            slow_print("\nYou catch more flies with honey than with vinegar.\n")       
            good_guy_two()
            break
        elif investigation_style == "b":
            dice_roll()
            increment_score("iron_guard", "smiling_shadows")
            good_guy_two()
            break
        elif investigation_style == "exit":   
            main()
            break
        else:
            print("\nPlease choose A or B\n") 


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


def increment_score(pteam, cteam):
    """
    Function to increment the score for the good guy game as a 
    result of dice rolls.
    If the player gets a higher roll, player's team gets a point.
    If the computer gets a higher roll, the opposing team do.
    If player and computer rolls are tied, then there will be 
    reroll. 
    """
    if player_roll > comp_roll: 
        score[pteam] += 1 
        print(score)
    elif player_roll == comp_roll:
        dice_roll()   
    else: 
        score[cteam] += 1  
        print(score)            


def good_guy_two():
    """
    Function for second selection of options, for the 
    Iron Guard game one will lead to a dice roll while 
    the other will be an instant fail that gives the
    Smiling Shadows an additional two points and ends
    the game.
    """
    slow_print("\nYou find out that the an ambush is being plotted"
               " for poor Bill in Nightingale\nPark. The assassins"
               " were hired by his romantic rival, Bob.\n")
    while True:
        chase_shadows = input("\nWhat do you do?\n"
                              "Choose A or B:\n"
                              " A: Find Bob and bring him to justice\n"
                              " B: Get to Nightingale Park!\n").lower().strip()
        if chase_shadows == "a":
            slow_print("\nYou find Bob in his house and bring"
                       " him in to the House of Questions.\n"
                       "Unfortunately, you hear that Bill has"
                       " been found stabbed in the Park, declared\n"
                       "dead on site. With insufficient evidence,"
                       " the wealthy merchant, Bob, is\nreleased.")  
            # Instant fail code      
            game_over_fail()
            break              
        elif chase_shadows == "b":
            dice_roll()
            increment_score("iron_guard", "smiling_shadows")
            good_guy_final()
            break
        elif chase_shadows == "exit":   
            main()
            break
        else:
            print("\nPlease choose A or B\n") 


def good_guy_final():
    """
    Function that defines the final pair of selections 
    for the Iron Guard game.
    One will lead to a dice roll while the other will be
    an instant fail that will deduct one point from the
    Iron Guard and add a point to the Smiling Shadows.
    """
    while True:
        confront = input("\nYou get to the Nightingale Park, what do you do?\n"
                         "Choose A or B:\n"
                         " A: Charge at the assassins"
                         " as soon as you enter\n"
                         " B: Create a noise distraction"
                         " before aiming for the targets"
                         " while their heads are turned\n").lower().strip()
        if confront == "a":
            slow_print("\nYou immediately charge at the assassins but"
                       " they are professionals and simply\nslide"
                       " away. You find yourself with multiple stab"
                       " wounds in the back. It\nseems you will be"
                       " joining Bill.\n")
            # Instant fail code
            game_over_fail()
            break
        elif confront == "b":
            dice_roll()
            increment_score("iron_guard", "smiling_shadows")
            good_guy_final_score()
            break
        elif confront == "exit":
            main()
            break
        else: 
            print("\nPlease choose A or B\n")


def bad_guy():
    """
    Part one of the good guy game (Smiling Shadows), player can choose 
    one option which will give them an automatic score increase,
    or the other option which will take them to a dice roll.
    While loop only breaks when user makes a valid input.
    """
    while True:
        assassin_style = input("\nHow do you find your target?\n"
                               "Choose A or B:\n"
                               " A: Charm his friends\n"
                               " B: Stalk his movements\n").lower().strip()
        if assassin_style == "a":
            score["smiling_shadows"] += 1 
            print(score)
            slow_print("\nWell done. It's better if your prey isn't"
                       " on guard.\n")       
            bad_guy_two()
            break
        elif assassin_style == "b":
            dice_roll()
            increment_score("smiling_shadows", "iron_guard")
            bad_guy_two()
            break
        elif assassin_style == "exit":
            main()
            break
        else:
            print("\nPlease choose A or B\n") 


def bad_guy_two():
    """
    Function for second selection of options, for the 
    Smiling Shadows game one will lead to a dice roll while 
    the other will be an instant fail that gives the
    Iron Guard an additional two points and ends
    the game.
    """
    slow_print("\nYou find out that Bill likes to wander around"
               " Nightingale Park in the evenings.\n")
    while True:
        timing = input("\nDo you ambush him the first chance you get"
                       " or map out the area for onlookers?\n"
                       " A: Map out the area\n"
                       " B: Ambush ASAP\n").lower().strip()
        if timing == "a":
            dice_roll()
            increment_score("smiling_shadows", "iron_guard")
            bad_guy_final()
            break
        elif timing == "b":
            slow_print("\nYou may have wanted to do some reconnaissance."
                       " An Iron Guard man catches you\nin your"
                       " attempt and you are brought to the House"
                       " of Questions. Not to be\nlet free until you"
                       " talk about your employer. The boss may not"
                       " let you live\nthrough this failure.\n")
            # Instant fail code       
            game_over_fail()
            break 
        elif timing == "exit":
            main()
            break          
        else:
            print("\nPlease choose A or B\n") 


def bad_guy_final():
    """
    Function that defines the final pair of selections
    for the Smiling Shadows game.
    One will lead to a dice roll while the other will be
    an instant fail that will deduct one point from the
    Smiling Shadows and add a point to the Iron Guard.
    """
    while True:
        ambush = input("\nHow do you attack?\n"
                       " A: Leap out of the bushes and"
                       " attempt to strike with my"
                       " dagger"
                       " B: Blend in to the surroundings,"
                       " behaving like any other passerby"
                       " before attacking once close enough\n").lower().strip()
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
        elif ambush == "b":
            dice_roll()
            increment_score("smiling_shadows", "iron_guard")
            bad_guy_final_score()
            break
        elif ambush == "exit":
            main()
            break
        else:
            print("\nPlease choose A or B\n")


def good_guy_final_score():
    """
    Function to define what would count as a success
    and the message to display if the player succeeds 
    or fails.
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
                   " your near future\ntoo.")
        game_over_succeed()
    else:
        slow_print("\nYou try to attack the assassin who is"
                   " about to deal the killing blow to"
                   " Bill. However,/nyou miss and stab"
                   " other instead. He falls to the ground"
                   " lifelessly but so\ntoo does Bill. You"
                   " were not fast enough. The killer runs"
                   " off while you stare at\nBill's still"
                   " body in shock.\n") 
        game_over_fail()


def bad_guy_final_score():
    """
    Function to define what would count as a success
    and the message to display if the player succeeds 
    or fails.
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
                   " and attempt a mortal blow. Alas, you"
                   " are\nonly able to nick him a little"
                   " which gives him the time to struggle"
                   " from your\ngrip and call for help."
                   " It seems you've missed your chance."
                   " This will not\ngo over well at the"
                   " guildhall.\n")
        game_over_fail()           


def game_over_succeed():
    slow_print(f"\nCongratulations, {username}! You have succeeded" 
               " in your mission!\n")
    start_again()


def game_over_fail():
    slow_print(f"\nOh no, {username}, you have failed your mission.\n")
    start_again()


def start_again():    
    while True:
        start_again = input("\nWould you like to start again?\n"
                            " A: Yes\n"
                            " B: No\n").lower().strip()
        if start_again == "a":
            for team, value in score.items():
                score[team] = 0
            choose_org()
            break
        elif start_again == "b":
            print("\nHope to see you again soon!\n")
            main()
            break
        elif start_again == "exit":
            main()
            break
        else:
            print("\nPlease choose A or B\n")
         
    print(score)

# The function will only be called if the file is run from the command line
# The code will not be executed if the file is imported from another file
if __name__ == "__main__":
    main()
