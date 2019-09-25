# tic-tac-toe

Author: Raven W. Robertson 09/2019

This is a game played in your command line written in Python 3.7.3. 

The game board is displayed in a 3 X 3 pattern of nested lists which I built utilizing Pythons List comprehension. I'm using lists as my game board not only because it is aesthetically suited for a tic-tac-toe game board, but because we are able to look up the value of a listat a given index in constant time, which gives us a time complexity of O(1). This is an action that we're performing every time the player chooses a position to play. 

The board spots are labeled left to right, top to bottom. Like so:

1 2 3

4 5 6

7 8 9

This is a two player game. Each player chooses where they would like to place their mark. Once three matching marks are found, either vertically, horizontally, or diagonally, the person who placed those marks wins.

I've imported sys and traceback to allow for a clean Quit from the game upon completion or Keyboard interrupt.


## About this project

My MVP for this game was simply to build a playable, functional tic tac toe game in that played in the command line. I gave myself a day to finish it. The result is the code that I have here as of 9 / 24/2019.


### What I like about this program

It plays cleanly in my console. I have error handling and I'm checking for edge cases (i.e. integers given by the user that are outside of range, a blank input for a user name, a string instead of an integer for the game board placement). It does everything that I would expect a tic tac toe game to do.

### Where I would take this project further

I have a few thoughts. I would either expand the Player class, adding in attributes such as self.total_wins and self.total_losses or it might be fun to do a kind of madlib input request, asking for verbs, nouns ect.. and using the input to build up a self.catch_phrase for when that player wins. 


I would also build up a game_board class and move many of my functiodns into the class as methods. 


My other thought, depending on how wild we wanted to get with a tic tac toe game, was to build a django app out of it. Then, I could build up a player model and a game board model, store instances of the Player in a database and then use an ORM (object relational mapping), to interact with out database in our code. We could add a self.rank attribute to the player class and increase the rank when the player hits a certain number of wins. We could have a lot of fun with it.


On that note, with programming, I feel that it quickly becomes easy to go into a rabbit hole of continously building on my code, making it more exciting and intericate and I truly love doing it. However, I don't want to lose the opportunity to interview with a company that I would like to work with because I ended up lost down a rabbit hole of building up ranks for tick tac toe players and consequently, didn't finish in a timely enough way. So, for now, here is my MVP built in about a day, with breaks for a few meetings and meals. If anyone would like to have expand upon this game in any of they ways that I have mentioned or any other way, I'm open and available to code for fun and/or code for hire. 

Thank you for your time. I hope you enjoy the game!


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

