# tic-tac-toe

Author: Raven W. Robertson 09/2019

This is a game played in your command line written in Python 3.7.3. 

The game board is displayed in a 3 X 3 pattern of nested lists which I built utilizing Pythons List comprehension.

The board spots are labeled left to right, top to bottom. Like so:

1 2 3

4 5 6

7 8 9

This is a two player game. Each player chooses where they would like to place their mark. Once three matching marks are found, either vertically, horizontally, or diagonally, the person who placed those marks wins.

I've imported sys and traceback to allow for a clean Quit from the game upon completion or Keyboard interrupt.

## Player Class

When you run the tic_tac.py file you will be prompted for both players names. 

An instance of the Player class will be instantiated for each of the two players.

The Player has a name (The names you enter into the initia prompts) and a team (Either X's or O's) attribute. 


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
* In a try block we prompt the current player to choose a number that coorelates with the spot they want to mark
* Calls the check_position() function to check availability and validity of the players numerical choice.
* Except block catches Value error in case of a numerical choice that is too high or too low.

### check_position()

* Takes in one argument; the integer position on the game board that has been chosen by the current player. 
* Checks position integer passed into the function to see if it is within the range of 0 and 8, which are the indices available for use in the game board
* Checks position integer passed into the function against cooresponding numerical position on the game board to see if the spot is available for play
* If the position is not in range or the position chosen is already in use by another mark, a ValueError is raised


### flip_player()

* Takes in both of the players as arguments
* uses global variables current_player and turns
* if player one is current player, then player two becomes current player and visa versa. 


### check_rows(), check_columns(), check_diagonals()

* Uses global variables: board, winner, game_is_still_going
* checks for a matching value in list indices:
    * check_rows(): horizontally 
    * check_columns(): vertically
    * check_diagonals(): diagonally
* calls check_who_won() function on whichever row, column or diagonal had a match
* returns winner
* changes the game_is_still_going flag to False to break the game play loop


### check_who_won()

* uses global variable: winner
* takes in four arguments:
    * player one
    * player two
    * position one (which nested list the winning combination was in)
    * position number two (which of the indices of the above nested list the held the value of the winning team)
* checks value at given coordinates (position one and position two) to see which player won


### check_for_win()

* Uses global variables: winner, game_is_still_going, turns 
* Takes in two arguments
    * player one
    * player two
* Checks to see if the game board is full
* Checks to see if there is any winner returned from our check rows, columns or diagonals by calling each of those function


### play_again()

* uses global variables: game_is_still_going and board
* prompts the player asking if they want to play again
* if they do, resets game board, reset turn count and reset game_is_still_going flag. 
* calls the lets_roll() to get the game started again
* if player does not want to play again, it says goodbye and calls a sys.exit(0) for a clean exit into the command line. 


### play_game()

* takes in two arguments:
    * player one
    * player two
* in a try block:
    * creates a while loop that goes as long as our game is still going flag is set to True
    * calls handle_turn() on current player
    * calls check_for_win()
    * calls flip_player()
    * conditional:
        * if winner prints out winner script
        * if tie prints out tie script
    * calls play_again()
* in an except block:
    * handles KeyboardInterrupt
    * calls sys.exit(0) for clean exit


## lets_roll()
* calls intro
* creates two instances of Player class based on input gathered in intro()
* calls play_game()

