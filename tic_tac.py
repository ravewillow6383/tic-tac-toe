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

def check_rows():

    global board, winner, game_is_still_going

    row_one = board[0][0] == board[0][1] == board[0][2] != '-'
    row_two = board[1][0] == board[1][1] == board[1][2] != '-'
    row_three = board[2][0] == board[2][1] == board[2][2] != '-'

    # if winner, change the game is still going on flag
    if row_one or row_two or row_three:
        game_is_still_going = False

    if row_one:
        return board[0][0]

    if row_two:
        return board[1][0]

    if row_three:
        return board[2][0]


def check_columns():
    global board, game_is_still_going

    column_one = board[0][0] == board[1][0] == board[2][0] != '-'
    column_two = board[0][1] == board[1][1] == board[2][1] != '-'
    column_three = board[0][2] == board[1][2] == board[2][2] != '-'

    # if winner, change the game is still going on flag
    if column_one or column_two or column_three:
        game_is_still_going = False

    if column_one:
        return board[0][0]

    if column_two:
        return board[0][1]

    if column_three:
        return board[0][2]

    return

def check_diagonals():
    global board, game_is_still_going

    diagonals_one = board[0][0] == board[1][1] == board[2][2] != '-'
    diagonals_two = board[0][2] == board[1][1] == board[2][0] != '-'

    # if winner, change the game is still going on flag
    if diagonals_one or diagonals_two:
        game_is_still_going = False
        return board[1][1]

    return

def check_for_win():
    global winner 

    #check rows
    row_winner = check_rows()
    
    #check columns
    column_winner = check_columns()

    #check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = diagonal_winner

    elif column_winner:
        winner = column_winner

    elif diagonal_winner:
        winner = diagonal_winner
    
    else:
        winner = None

def check_for_tie():
    return


def check_if_game_over():
    check_for_win()
    check_for_tie()      

# Get it started
def play_game():
    global board, columns, rows, player_name
    
    while game_is_still_going:

        # handle a single game for a player
        handle_turn(current_player)

        # check if the game is over
        check_if_game_over()

        # flip to the other player
        flip_player()

    #Handle a winner
    if winner is not None:
        print(f'They’ve done studies, you know. 60 percent of the time, it works every time. Well done, {player_name}')
    
    # Handle a tie
    if winner == None:
        print(f' I\'m pretty sure there\'s a lot more to life than being really, really, ridiculously good at tic-tac-toe. And I plan on finding out what that is.')
        again_prompt = 'Would you like to play again?'
        again = input(again_prompt)
      
    if again.lower() == 'y' or again.lower() == 'yes':
        board = [['-' for n in range(columns)] for n in range (rows)]
        play_game()
      
    if again.lower() == 'n' or again.lower() == 'no':
        print(f'Thanks for the game, {player_name}.')
        sys.exit(0)   

if __name__ == '__main__':
    intro()
    play_game()
