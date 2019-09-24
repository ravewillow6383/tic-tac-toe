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
winner = None
current_player = 'X'
player_name = ''
player_team = ''

# setting up a game board
board = [['-' for n in range(columns)] for n in range (rows)]

def intro():
    global player_name
    global player_team
    name_prompt = """
        *****************************************
        Hello, engineers and employees of Rubica. 
        Please enter your name here and we'll get 
        this party started:
        *****************************************       
        """
    player_name = str(input(name_prompt))

    team_prompt = """
        *****************************************
        Would you like to be an X or an O? 
        *****************************************       
        """
    player_team = str(input(team_prompt))


def display_board():
    for row in board:
        print(row)

def handle_turn(player):
    global player_name
    global player_team

    try:

        display_board()

        position =  """
        **************************************
        **    Try your luck at tic tac toe! **
        **   The game board reads left to   **
        **        right, top to bottom      **
        **   and the games slots are in     **
        **         numerical order.         **
        **************************************
        ###############################################

        Choose a whole number between 1 and 9, please: 
    
        ################################################
        """ 
        position = input(position)
        position = int(position) - 1
        if position >= 0 and position <= 2:
            board[0][position] = player_team
        elif position >= 3 and position <= 5:
            position -= 3
            board[1][position] = player_team
        elif position > 5 and position <= 8:
            position -= 6
            board[2][position] = player_team
        else:
            raise ValueError('please enter a whole number between 1-9')
    except ValueError:
        print(f"Ahem. Close, {player_name}, but not quite. Pick yourself up, dust yourself off and try that again") 
        handle_turn(player_name) 

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

    while game_is_still_going:

        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    if winner is not None:
        print('')
    
    # Display initial board
    # display_board()


if __name__ == '__main__':
    intro()
    play_game()
