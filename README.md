# Hermon Asmelash

## Kill (or save) Bill 

Kill (or save) Bill is A Choose Your Own Adventure style game created using Python 3 based on story elements of the text-based RPG Arx - After the Reckoning. It's a minigame that players of the game or simply anyone who enjoys that style of game can play in their downtime, choosing to either play as an assassin of the Smiling Shadows or a member of the Iron Guard, defenders of the city. The game uses a score based system with a goal to get a higher score before the other team (the computer).

[For the deployed app, click here.](https://kill-or-save-bill.herokuapp.com/)

## User Experience (UX)

### User Stories

1. I'm an Arx player and would love to play out a sandboxed story based on elements from the game.
2. I enjoy cops and robbers style games or choose your own adventure games in general and would love an opportunity to try another. 
3. I want to play a game that doesn't occupy my time with character generation or load times.
4. I would like a game that allows me to restart at the end without needing to run through the introduction so I can try every option available easily.
5. I like games of chance, leaving the outcome partly to the dice.

### Game Flowchart

To plan out the structure of the game, I used [smartdraw](https://cloud.smartdraw.com/).

![](https://github.com/Hasmelash95/kill-or-save-bill/blob/main/README-assets/flowchart/flowchart.png)

## Features

Opening the app takes the user to a browser hosted by heroku. The headings for the game are at the top using Georgia font and an off-white color against a teal background. 

![Screenshot 2022-09-13 at 11 40 46](https://user-images.githubusercontent.com/103432143/189881224-aaf1f30d-e772-44fa-8d3e-41fd8696343c.png)

### Intro Text

The intro text introduces the game and gives the player instructions in second person to go along with the adventure theme. User is provided the option to proceed by typing "go". 

![Screenshot 2022-09-13 at 11 43 32](https://user-images.githubusercontent.com/103432143/189881843-7cbdafec-8dd8-401e-a14f-e3786d22c480.png)

Typing anything other than "go" will prompt the invalid input message and the user will be asked to type "go" again.

![Screenshot 2022-09-13 at 11 45 07](https://user-images.githubusercontent.com/103432143/189881975-298f7503-3903-4f79-9fa1-16d4e2ff5d67.png)

"Go" and " go" are valid inputs as the strip() and lower() methods have been used.

### Enter Username 

Typing go will clear the terminal and ask user to input their username. Usernames must be 1-8 characters long and only have a-z letters. 

![Screenshot 2022-09-13 at 11 49 00](https://user-images.githubusercontent.com/103432143/189882717-f87617ae-bbfb-4b8b-8145-b5f1ce3339d9.png)


When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!
