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
    player_one_team = str(input(team_prompt))
    
    if len(player_one_team) > 1:
        print('That is too many characters for tic tac toe.')
        lets_roll()

    current_player = player_one_team

    if player_one_team != 'x' and player_one_team != 'X':
        player_two_team = 'X'
    else:
        player_two_team = 'O'

def display_board():
    for row in board:
        print(row)

def handle_turn(player):
    global player_one_name, current_player

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
    except ValueError:
        print(f"Ahem. Close, {player_one_name}, but not quite. Pick yourself up, dust yourself off and try that again") 
        handle_turn(player_one_name) 

def flip_player():

    global current_player, player_one_team, player_two_team, player_one_name, player_two_name

    if current_player == player_one_team:
        current_player = player_two_team
        print(f'{player_two_name}, it is your turn!')
    elif current_player == player_two_team:
        current_player = player_one_team  
        print(f'Your turn to play, {player_one_name}')

def check_rows():

    global board, winner, player_one_name, game_is_still_going, player_one_team, player_two_name, player_two_team

    row_one = board[0][0] == board[0][1] == board[0][2] != '-'
    row_two = board[1][0] == board[1][1] == board[1][2] != '-'
    row_three = board[2][0] == board[2][1] == board[2][2] != '-'

    for j in range(0, 3):
        full_board = None
        for i in range(0, 3):
            if board[j][i] == '-':
                full_board = False
                break
            else:
                full_board = True

    if full_board == True:
        display_board
        print('There are no more spots!')
        winner = None
        game_is_still_going = False
            
    # if winner, change the game is still going on flag
    if row_one or row_two or row_three:
        display_board()
        game_is_still_going = False

    if row_one:
        if board[0][0] == player_one_team:
            winner = player_one_name
        elif board[0][0] == player_two_team:
            winner = player_two_name
        else:
            winner = None

    if row_two:
        if board[1][0] == player_one_team:
            winner = player_one_name
        elif board[1][0] == player_two_team:
            winner = player_two_name

        else:
            winner = None

    if row_three:
        if board[2][0] == player_one_team:
            winner = player_one_name
        elif board[2][0] == player_two_team:
            winner = player_two_name
        else:
            winner = None

    return winner


def check_columns():

    global board, winner, player_one_name, game_is_still_going, player_one_team, player_two_name, player_two_team

    column_one = board[0][0] == board[1][0] == board[2][0] != '-'
    column_two = board[0][1] == board[1][1] == board[2][1] != '-'
    column_three = board[0][2] == board[1][2] == board[2][2] != '-'

    # if winner, change the game is still going on flag
    if column_one or column_two or column_three:
        display_board()
        game_is_still_going = False

    if column_one:
        if board[0][0] == player_one_team:
            winner = player_one_name
        elif board[0][0] == player_two_team:
            winner = player_two_name
        else:
            winner = None

    if column_two:
        if board[0][1] == player_one_team:
            winner = player_one_name
        elif board[0][1] == player_two_team:
            winner = player_two_name
        else:
            winner = None

    if column_three:
        if board[0][2] == player_one_team:
            winner = player_one_name
        elif board[0][2] == player_two_team:
            winner = player_two_name
        else:
            winner = None

    return winner

def check_diagonals():

    global board, winner, player_one_name, game_is_still_going, player_one_team, player_two_name, player_two_team

    diagonals_one = board[0][0] == board[1][1] == board[2][2] != '-'
    diagonals_two = board[0][2] == board[1][1] == board[2][0] != '-'

    # if winner, change the game is still going on flag. Checks if player is winner
    if diagonals_one or diagonals_two:
        display_board()
        game_is_still_going = False
        if board[1][1] == player_one_team:
            winner = player_one_name
        elif board[1][1] == player_two_team:
            winner = player_two_name
        else:
            winner = None
    return winner

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
  
# ask if player wants to play again
def play_again():
    global game_is_still_going
    again_prompt = 'Would you like to play again?'
    again = input(again_prompt)
      
    if again.lower() == 'y' or again.lower() == 'yes':
        board = [['-' for n in range(columns)] for n in range (rows)]
        game_is_still_going = True
        lets_roll()
      
    if again.lower() == 'n' or again.lower() == 'no':
        print(f'Thanks for the game, {player_one_name}.')
        sys.exit(0)   

# Get it started
def play_game():
    global board, player_one_name, player_two_name

    try: 
        while game_is_still_going:

            # handle a single game for a player
            handle_turn(current_player)

            # check if the game is over
            check_for_win()

            # flip to the other player
            flip_player()

        #Handle a winner
        if winner == player_one_name or winner == player_two_name:
            print(f'They’ve done studies, you know. 60 percent of the time, it works every time. Well done, {winner}. You sure nailed your x\'s and o\'s.' )
            play_again()
        # Handle a tie
        if winner != player_one_name and winner != player_two_name:
            print(f' I\'m pretty sure there\'s a lot more to life than being really, really, ridiculously good at tic-tac-toe, but that was sure a fine match. {player_one_name}, {player_two_name}, it was a draw. ')
            play_again()

    except KeyboardInterrupt:
        print('Thanks for playing!')
        sys.exit(0)  

def lets_roll():
    intro()
    play_game()

lets_roll()
