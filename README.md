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

To plan out the structure of the game, I used smartdraw.

### Features

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