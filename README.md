# tic-tac-toe

This is a game played in your command line written in Python 3.7.3. 

The game board is diplayed in a 3 X 3 pattern of nested lists which I built utilizing Pythons List comprehension.

The board spots are labeled left to right, top to bottom. Like so:

1 2 3

4 5 6

7 8 9

This is a two player game. Each player chooses where they would like to place their mark. Once three matching marks are found, either vertically, horizontally, or diagonally, the person who placed those marks wins.

I've imported sys and traceback to allow for a clean Quit from the game upon completion or Keyboard interupt.

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


### handle_turn()

* This function takes in one argument; the player who's turn it is currently.
* Takes one global variable: current_player
* It calls the display board function to show the current player which spots are available to play
* In a try block we prompt the current player to choose a number coorelating with the spot they want to mark
* Calls the check_position() function to check availability and validity of the players numerical choice.
* Except block catches Value error in case of a numerical choice that is too high or too low.

### check_position()

* Takes in one argument; the integer position on the game board that has been choosen by the current player. 
* Checks position integer passed into the function to see if it is within the range of 0 and 8, which are the indices available for use in the game board
* Checks position integer passed into the function against cooresponding numerical position on the game board to see if the spot is available for play
* If the position is not in range or the position chosen is already in use by another mark, a ValueError is raised


### flip_player()

* Takes in both of the players as arguments
* uses global variables current_player and turns
* if player one is current pllayer, then player two becomes current player and visa versa. 

### check_rows(), check_columns(), check_diagonals()

* Uses global variables board, winner, game_is_still_going
* 