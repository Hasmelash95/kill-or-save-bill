# Hermon Asmelash

# Kill (or save) Bill 

Kill (or save) Bill is A Choose Your Own Adventure style game created using Python based on story elements of the text-based RPG Arx - After the Reckoning. It's a minigame that players of the game or simply anyone who enjoys that style of game can play in their downtime, choosing to either play as an assassin of the Smiling Shadows or a member of the Iron Guard, defenders of the city. The game uses a score based system with a goal to get a higher score before the other team (the computer).

[For the deployed app, click here.](https://kill-or-save-bill.herokuapp.com/)

![Screenshot 2022-09-15 at 10 26 21](https://user-images.githubusercontent.com/103432143/190368063-cc78d386-cf64-43c0-b69d-4e2115c734f6.png)

## Table of Contents

[User Experience (UX)](#user-experience)

[Features](#features)

[Technologies Used](#technologies-used)

[Testing](#testing)

[Known Bugs](#known-bugs)

[Deployment](#deployment)

[Acknowledgements](#acknowledgements)

## User Experience (UX) <a name="user-experience">

### User Stories

1. I'm an Arx player and would love to play out a sandboxed story based on elements from the game.
2. I enjoy cops and robbers style games or choose your own adventure games in general and would love an opportunity to try another. 
3. I want to play a game that doesn't occupy my time with character generation or load times.
4. I would like a game that allows me to restart at the end without needing to run through the introduction so I can try every option available easily.
5. I like games of chance, leaving the outcome partly to the dice.

### Game Flowchart

To plan out the structure of the game, I used [smartdraw](https://cloud.smartdraw.com/).

![](https://github.com/Hasmelash95/kill-or-save-bill/blob/main/README-assets/flowchart/flowchart.png)

## Features <a name="features">

Opening the app takes the user to a browser hosted by heroku. The headings for the game are at the top using Georgia font and an off-white color `#dbe4e7` against a teal `#1f2e39` background. 

![Screenshot 2022-09-13 at 11 40 46](https://user-images.githubusercontent.com/103432143/189881224-aaf1f30d-e772-44fa-8d3e-41fd8696343c.png)

### Intro Text

The intro text introduces the game and gives the player instructions in second person to go along with the adventure theme. Slow print is used to print the text one letter at a time for the ambience. It also provides the current scores for the two teams, which at the start will be 0. User is provided the option to proceed by typing "go". 

![Screenshot 2022-09-15 at 10 24 57](https://user-images.githubusercontent.com/103432143/190367803-6745a556-9bd8-42e4-9c28-d31eb6420691.png)

Typing anything other than "go" will prompt the invalid input message and the user will be asked to type "go" again.

![Screenshot 2022-09-13 at 11 45 07](https://user-images.githubusercontent.com/103432143/189881975-298f7503-3903-4f79-9fa1-16d4e2ff5d67.png)

"Go" and " go" are valid inputs as the strip() and lower() methods have been used.

### Enter Username 

Typing go will clear the terminal and ask user to input their username. Usernames must be 1-8 characters long and only have a-z letters. The strip() method ensures that empty spaces will not be marked as invalid - if the user also has letters in their input. E.g. " Hermon" will be a valid username. 

![Screenshot 2022-09-13 at 11 49 00](https://user-images.githubusercontent.com/103432143/189882717-f87617ae-bbfb-4b8b-8145-b5f1ce3339d9.png)

![Screenshot 2022-09-13 at 12 04 05](https://user-images.githubusercontent.com/103432143/189885808-1d84daa3-0697-43d1-af7b-14709c97d31c.png)

### Choose Game

Entering a valid username will clear the terminal and take the user to the option to choose the game they want to play. To play as an Iron Guard or a Shadow. Typing any option other than "a" or "b" will prompt an invalid input message. "A", "B", " a", " b" are all valid inputs due to the strip() and lower() methods. 

![Screenshot 2022-09-13 at 12 49 57](https://user-images.githubusercontent.com/103432143/189893563-cb7e6cf7-b89c-4807-a13f-003a3d0179bf.png)

### First Decision

The user is given a story setting and two options as to how to proceed. The gentle/subtle option will give the user a free point, whereas the other option will take them to a dice roll.

![Screenshot 2022-09-13 at 12 13 39](https://user-images.githubusercontent.com/103432143/189887119-cc1290b8-6c3e-4284-9122-c3bbd31471e8.png)

![Screenshot 2022-09-13 at 12 15 45](https://user-images.githubusercontent.com/103432143/189887728-80084a06-d3ba-4bce-8b59-a5e19c5c08b0.png)

### Dice Roll

A random number (1-10) is chosen for the player and the computer. The higher number wins the round and their team's score is incremented. If the rolls are tied then the game will roll again until the numbers are different. 

### Imports

Imported modules: 
os - to clear the terminal.
sys and time - to control the rate that text is printed. One letter at a time.
randint - a random number generator for the dice rolls. 

### Second Decision

The next set of options provides an instant fail option (generally the less cautious option) and an option that takes the user to another dice roll. Once again, typing anything other than or "a" or "b" would trigger the "Please choose A or B" message. 

![Screenshot 2022-09-13 at 12 36 45](https://user-images.githubusercontent.com/103432143/189891249-b4dfb290-19cf-45bb-9d65-28264049cc69.png)

![Screenshot 2022-09-13 at 12 32 45](https://user-images.githubusercontent.com/103432143/189890520-ea934df2-b794-4156-920a-0920af570431.png)

Instant fail:

![Screenshot 2022-09-13 at 12 30 46](https://user-images.githubusercontent.com/103432143/189890141-8701abd3-6935-4759-9f92-737d03bce6db.png)

Typing "a" will take the user to the choose game section, whereas "b" will take them to the introduction. In both cases, the terminal will be cleared and the scores for both teams will reset to 0.

### Final Decision

The final set of options is like the second, in that one option is an instant fail and the other takes the user to a dice roll.

![Screenshot 2022-09-13 at 12 34 15](https://user-images.githubusercontent.com/103432143/189891045-9cd44baa-9c61-481e-85f3-4218a168c354.png)

![Screenshot 2022-09-13 at 12 34 25](https://user-images.githubusercontent.com/103432143/189891058-195e49e7-ccfc-47e0-9453-8b4e12c7e59b.png)

This time, the scores are compared after the dice roll and if the player has a score of 2 or more, they win the game. If not, they lose and get the fail message. 

### Smiling Shadows Game

This game works in the same way as the Iron Guard game. The screenshots are below:

![Screenshot 2022-09-13 at 12 41 02](https://user-images.githubusercontent.com/103432143/189892222-5f15e423-1da0-4cfe-a85f-099534c27e9e.png)

![Screenshot 2022-09-13 at 12 41 19](https://user-images.githubusercontent.com/103432143/189892236-254b6917-f8e4-45d6-a855-f7ba1e76f8dc.png)

![Screenshot 2022-09-13 at 12 51 30](https://user-images.githubusercontent.com/103432143/189893844-a772d971-4742-4dad-b469-98c1e66c5d32.png)

### Exiting Game

Typing "exit" or "Exit" or " exit" will exit the app. 

![Screenshot 2022-09-13 at 12 54 56](https://user-images.githubusercontent.com/103432143/189894452-1f6edf62-2b7b-496b-a47d-3aa77b50ab2c.png)

### Future Features

1. Possibility of more game options to give repeat players variety in the game. 
2. A score board to compare results.
3. Adding a multiplayer option.

## Technologies Used <a name="technologies-used"> 

Python 

HTML5

CSS3

GitHub

Gitpod

Git

Heroku 

## Testing <a name="testing">

### Validation

The app was run through PEP8 with no errors or warnings: 

![Screenshot 2022-09-13 at 10 52 10](https://user-images.githubusercontent.com/103432143/189965623-7e9e0f90-1235-4f41-a80a-e1c8088cda1f.png)

Running the app through [W3C](https://validator.w3.org/) and [Jigsaw](https://jigsaw.w3.org/css-validator/) also resulted in no errors. 

### Performance

A Lighthouse test was taken:

![Screenshot 2022-09-13 at 18 22 58](https://user-images.githubusercontent.com/103432143/189967381-e2b0d64c-8a06-4adc-91f6-66eb576c691b.png)

### Functionality
![Screenshot 2022-09-13 at 18 24 44](https://user-images.githubusercontent.com/103432143/189968279-9f5c820a-aaf9-4f93-b874-87ae988ec216.png)

![Screenshot 2022-09-13 at 18 25 04](https://user-images.githubusercontent.com/103432143/189968306-db992995-3867-4040-b982-9f9c646c8b85.png)

![Screenshot 2022-09-13 at 18 25 18](https://user-images.githubusercontent.com/103432143/189968329-b4b451ed-6e47-410b-b441-fcca60e67d41.png)

![Screenshot 2022-09-13 at 18 25 30](https://user-images.githubusercontent.com/103432143/189968369-34f043bc-1d7e-4d75-8ccd-bd9ab8e82131.png)

![Screenshot 2022-09-13 at 18 25 49](https://user-images.githubusercontent.com/103432143/189968413-b5e62372-b591-4a1c-bef1-41ade68a6f85.png)

![Screenshot 2022-09-13 at 18 27 08](https://user-images.githubusercontent.com/103432143/189968810-f106fd1c-3cf2-4818-9c0a-6478e9b3c4dd.png)

Tests 8 and 9 were carried out for each question that asked the user to type "a" or "b". 

### Compatibility 

Functional tests were carried out on Google Chrome, Safari, Firefox and Microsoft Edge and passed. 

The app does not work on mobile devices at this time. The game loads but the user is unable to type anything without a proper keyboard.

### Testing User Stories

1. I'm an Arx player and would love to play out a sandboxed story based on elements from the game.

PASS - The game uses multiple elements from the Arx-world and players can play the game as much as they'd like with no broader implications.

2. I enjoy cops and robbers style games or choose your own adventure games in general and would love an opportunity to try another. 

PASS - The game offers a player the option to play as the good guy or the bad guy and the outcome is a result of both their decision (as is the case of this style of game) and the dice roll. 

3. I want to play a game that doesn't occupy my time with character generation or load times.

PASS - Besides needing to input a valid username, there is no character generation and it doesn't take long for the user to start the game properly. 

4. I would like a game that allows me to restart at the end without needing to run through the introduction so I can try every option available easily.

PASS - Typing yes when the prompt asks if they'd like to start again takes the player to the choose a game section, not needing to read the intro text again.

5. I like games of chance, leaving the outcome partly to the dice.

PASS - The dice roll check adds an element of chance. While decisions the player makes can give them an extra point for free or lead to an instant fail, the outcome is dependant on dice rolls. A random number is generated (1-10) for both the user and the opposing team (the computer). The score increments depending on which team's roll is higher. 

## Known Bugs <a name="known-bugs">

### Fixed Bugs

1. An empty space was interpreted as a valid username. The cause of the bug was unnecessary nesting inside the if statement. Removing this unnecessary indentation of the is.alpha() fixed the bug.
2. An empty space before the username was invalid because a space is not an a-z letter. Adding the strip() method solved this issue. 

### Unfixed Bugs

Aside from the incompatibility with mobile devices, there are no unfixed bugs in the application.

## Deployment <a name="deployment">

### Deploying the App

1. Create a Heroku account or log in if you have one.
2. Click on the "Create new app" button on the dashboard.
3. Give the app a unique name. (For this one kill-or-save-bill was used.) 
4. Select your region.
5. Click on the settings tab. 
6. Add a Config Var with the key PORT and the value 8000.
7. Add the builpacks python and node.js in that order, with python on top, and save changes.
8. Click on the deploy tab.
9. Connect to Github under deployment method, search the repository you wish to link to and click 'connect'.
10. Select either automatic or manual deploy. The former rebuilds the app everytime you git push. 
11. You will see an "App was successfully deployed" message.
12. The application can be run by clicking 'Open App'.

### Cloning the Repository

1. Log on to your Github account and head to the main page of the repository you wish to clone.
2. Click on the 'Code' button above the list of files and choose from HTTPS, SSH or Github CLI, to copy the URL provided.
3. Open terminal and ensure you are in the correct location.
4. Type in 'git clone' and paste the URL you'd copied in step 2 and press enter.

## Acknowledgements <a name="acknowledgements">

I would like to thank my mentor, Brian Macharia for his help during the process and offering much needed advice. 

My friend, Victoria for talking through some problems with me. 

My friend Daniel for spotting typos. 

Dan and Dave, creators of [Arx - After the Recknoning](https://play.arxmush.org/) for the lore that inspired this game.

[StackOverflow](https://stackoverflow.com/questions/2084508/clear-terminal-in-python) for the clear terminal code.

[SJECollins](https://github.com/SJECollins/ci-pp3-hide-and-seek/blob/main/run.py) for the slow print code.

[charlie-vf](https://github.com/charlie-vf/the-hobbit-game/blob/main/run.py) for inspiration on setting the username input.

Code Institute for the template and learning material. 

