from player import Player
import sys, traceback

# Global constants:

columns = 3
rows = 3
game_is_still_going = True
winner = None
player_one_name = ''
player_two_name = ''
player_one_team = ''
player_two_team = ''
current_player = ''
turns = 1

# setting up a game board
board = [['-' for n in range(columns)] for n in range (rows)]

def intro():
    global player_one_name, player_one_team, player_two_team, current_player, player_two_name

    player_one_name = """
        *****************************************
        Hello, engineers and employees of Rubica. 
        Please enter a name here for player one and 
        we'll get this party started:
        *****************************************       
        """

    player_two_name = """
        *****************************************
        Great! Now may I please have a name for
        our second player?
        *****************************************       
        """

    player_one_name = str(input(player_one_name))
    player_two_name = str(input(player_two_name))

    team_prompt = """
        **********************************************
              Player One, You will go first! 
            Would you like to be an X or an O? 
        ***********************************************       
        """
    player_one_team = str(input(team_prompt)).upper()

    if player_one_team != 'X' and player_one_team != 'O':
        print(f'I like your rebellion. Have it your way, {player_one_name}. You are team {player_one_team}. But your friend is still an O.')
    
    if len(player_one_team) > 1:
        print('That is too many characters for tic tac toe.')
        lets_roll()

    current_player = player_one_team

    if player_one_team != 'X':
        player_two_team = 'X'
    else:
        player_two_team = 'O'


def display_board():
    for row in board:
        print(row)

def handle_turn(player):
    global current_player
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
        check_position(int(position) - 1)

    except ValueError:
        print(f"Ahem. Close, but not quite. Pick yourself up, dust yourself off and try that again") 
        handle_turn(current_player) 

# Seeing if the player made a valid placement choice for their marker
def check_position(position):
    if position >= 0 and position <= 2:
        if board[0][position] == '-':
            board[0][position] = current_player

        elif board[0][position] == player_one_team or board[0][position] == player_two_team:
            print('That spot is taken! Try again')
            handle_turn(current_player)

    elif position >= 3 and position <= 5:
        position -= 3
        if board[1][position] == '-':
            board[1][position] = current_player

        elif board[1][position] == player_one_team or board[1][position] == player_two_team:
            print('That spot is taken! Try again')
            handle_turn(current_player)

    elif position >= 6 and position <= 8:
        position -= 6
        if board[2][position] == '-':
            board[2][position] = current_player

        elif board[2][position] == player_one_team or board[2][position] == player_two_team:
            print('That spot is taken! Try again')
            handle_turn(current_player)

    else:
        raise ValueError('please enter a whole number between 1-9')

def flip_player(player_one, player_two):

    global current_player, turns

    turns += 1

    if current_player == player_one.team:
        current_player = player_two.team
        if turns < 8:
            print(f'{player_two.name}, it is your turn!')

    elif current_player == player_two.team:
        current_player = player_one.team  
        print(f'Your turn to play, {player_one.name}')

def check_rows(player_one, player_two):

    global board, winner, game_is_still_going

    row_one = board[0][0] == board[0][1] == board[0][2] != '-'
    row_two = board[1][0] == board[1][1] == board[1][2] != '-'
    row_three = board[2][0] == board[2][1] == board[2][2] != '-'
            
    # if winner, change the game is still going on flag
    if row_one or row_two or row_three:
        display_board()
        game_is_still_going = False

    if row_one:
        check_who_won(player_one, player_two, 0, 0)

    if row_two:
        check_who_won(player_one, player_two, 1, 0)

    if row_three:
        check_who_won(player_one, player_two, 2, 0)

    return winner

def check_columns(player_one, player_two):

    global board, winner, game_is_still_going

    column_one = board[0][0] == board[1][0] == board[2][0] != '-'
    column_two = board[0][1] == board[1][1] == board[2][1] != '-'
    column_three = board[0][2] == board[1][2] == board[2][2] != '-'

    # if winner, change the game is still going on flag
    if column_one or column_two or column_three:
        display_board()
        game_is_still_going = False

    if column_one:
        check_who_won(player_one, player_two, 0, 0)

    if column_two:
        check_who_won(player_one, player_two, 0, 1)

    if column_three:
        check_who_won(player_one, player_two, 0, 2)

    return winner

def check_diagonals(player_one, player_two):

    global board, winner, game_is_still_going

    diagonals_one = board[0][0] == board[1][1] == board[2][2] != '-'
    diagonals_two = board[0][2] == board[1][1] == board[2][0] != '-'

    # if winner, change the game is still going on flag. Checks if player is winner
    if diagonals_one or diagonals_two:

        display_board()
        game_is_still_going = False
        check_who_won(player_one, player_two, 1, 1)

    return winner

#If there is a winner, was it X's or O's?
def check_who_won(player_one, player_two, pos1, pos2):
    global winner

    if board[pos1][pos2] == player_one.team:
        winner = player_one.name

    elif board[pos1][pos2] == player_two.team:
        winner = player_two.name

    else:
        winner = None

#checks to see if there's a winner yet        
def check_for_win(player_one, player_two):
    global winner, game_is_still_going, turns 

    #Check if gameboard if full for tie
    if turns == 9:
        game_is_still_going = False
        print('The game board is full!')
        winner = None

    #check rows
    row_winner = check_rows(player_one, player_two)
    
    #check columns
    column_winner = check_columns(player_one, player_two)

    #check diagonals
    diagonal_winner = check_diagonals(player_one, player_two)

    if row_winner:
        winner = diagonal_winner

    elif column_winner:
        winner = column_winner

    elif diagonal_winner:
        winner = diagonal_winner
    
    else:
        winner = None

  
# ask if player wants to play again
def play_again():
    global game_is_still_going, board, turns

    again_prompt = 'Would you like to play again?'
    again = input(again_prompt)
      
    if again.lower() == 'y' or again.lower() == 'yes':
        # Reset game board
        board = [['-' for n in range(columns)] for n in range (rows)]
        # Reset game is going flag
        game_is_still_going = True
        turns = 1
        lets_roll()
      
    if again.lower() == 'n' or again.lower() == 'no':
        print(f'Thanks for the game, {player_one_name}.')
        sys.exit(0)   

# Get it started
def play_game(player_one, player_two):
    global board, game_is_still_going

    try: 
        while game_is_still_going:

            # handle a single game for a player
            handle_turn(current_player)

            # check if the game is over
            check_for_win(player_one, player_two)

            # flip to the other player
            flip_player(player_one, player_two)

        #Handle a winner
        if winner == player_one.name or winner == player_two.name:
            print(f'They’ve done studies, you know. 60 percent of the time, it works every time. Well done, {winner}. You sure nailed your x\'s and o\'s.' )
            play_again()

        # Handle a tie
        if winner != player_one.name and winner != player_two.name:
            print(f' I\'m pretty sure there\'s a lot more to life than being really, really, ridiculously good at tic-tac-toe, but that was sure a fine match. {player_one.name}, {player_two.name}, it was a draw. ')
            play_again()

    except KeyboardInterrupt:
        print('Thanks for playing!')
        sys.exit(0)  

def lets_roll():

    intro()

    #Create new instances of Player class
    player_one = Player(player_one_name, player_one_team)
    player_two = Player(player_two_name, player_two_team)

    play_game(player_one, player_two)

lets_roll()
