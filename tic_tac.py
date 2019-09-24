# Board to display
# Play a game
# Handle a turn
# function to check win
    # check rows
    # check columns
    # check diagonals
# function to check for tie
# function to change players

# Global constants:

columns = 3
rows = 3
game_is_still_going = True
# setting up a game board
board = [['-' for n in range(columns)] for n in range (rows)]

def display_board():
    for row in board:
        print(row)

def handle_turn():
    try:
        position =  """
        **************************************
        **    Try your luck at tic tac toe! **
        **   The game board reads left to   **
        **        right, top to bottom      **
        **   and are in numerical order.    **
        **************************************
        #####################################################

        Choose a whole number between 1 and 9, please: 
    
        #####################################################
        """ 
        position = input(position)
        position = int(position) - 1
        if position >= 0 and position <= 2:
            board[0][position] = 'X'
        elif position >= 3 and position <= 5:
            position -= 3
            board[1][position] = 'X'
        elif position > 5 and position <= 8:
            position -= 6
            board[2][position] = 'X'
        elif position < 0 or position > 8:
            raise ValueError('please enter a whole number between 1-9')
        display_board()
    except ValueError:
        print('Ahem. Close, but not quite. Pick yourself up, dust yourself off and try that one again.') 
        handle_turn() 

def flip_player():
    return

def check_for_win():
    #check rows
    #check columns
    #check diagonals
    return

def check_for_tie():
    return


def check_if_game_over():
    check_for_win()
    check_for_tie()      

def play_game():
    try:

        while game_is_still_going:

            handle_turn(current_player)

            check_if_game_over()

            flip_player()
    
    except KeyboardInterrupt:
        print('Don\'t quit on me now!')

    # Display initial board
    # display_board()


if __name__ == '__main__':

    play_game()