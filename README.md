# tic-tac-toe

This is a game played in your command line written in Python 3.7.3. 

The game board is diplayed in a 3 X 3 pattern of nested lists which I built utilizing Pythons List comprehension.

The board spots are labeled left to right, top to bottom. Like so:

1 2 3

4 5 6

7 8 9

This is a two player game. Each player chooses where they would like to place their mark. Once three matching marks are found, either vertically, horizontally, or diagonally, the person who placed those marks wins.

## Player Class
When you run the tic_tac.py file you will be promtped for both players names. 

An instance of the Player class will be instantiated for each of the two pllayers.

The Player has a name (The names you enter into the intial prompts) and a team (Either X's or O's) attribute. 

## Functions 

### intro()

* Greets Players
* Prompts for Names
* Prompts for team choice, either X's or O's

### display_board() 

* Loops through our primary board list, printing out each 1 X 3 nested list until we can see all three nested lists, giving us a 3X3 game board to start with.
* Game board is initialized with each tile, where you would place either your 'X' or 'O' mark, filled with '-' so the players can see which spots are available for play. 
