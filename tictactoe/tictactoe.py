import os

'''
This is a terminal based tic tac toe game
players dictionary keeps track of the points
'''
players = {'Player1': 0, 'Player2': 0, 'draw': 0}


def display_Board(current_board):
    '''
    displays the current game state to user
    '''
    print(current_board['q']+' | '+current_board['w']+' | '+current_board['e'])
    print('--+---+--')
    print(current_board['a']+' | '+current_board['s']+' | '+current_board['d'])
    print('--+---+--')
    print(current_board['z']+' | '+current_board['x']+' | '+current_board['c'])


def user_choice(check_choice):
    '''
    checks and confirms the user choice of where to put the marker
    '''
    wrong_choice = True

    while wrong_choice:

        choice = input('\nEnter a valid box to enter your mark: ').lower()

        if choice not in ['q', 'w', 'e', 'a', 's', 'd', 'z', 'x', 'c']:
            print('Sorry but you can only choose corresponding box letters provided in instructions!')

        elif choice in check_choice:
            print('Sorry but this box is already occupied! Select an empty space!!')

        else:
            wrong_choice = False

    return choice


def check_winner(board):
    '''
    checks if the current state of game has a winner
    '''
    if board['q'] == board['w'] == board['e'] == 'X' or \
       board['a'] == board['s'] == board['d'] == 'X' or \
       board['z'] == board['x'] == board['c'] == 'X' or \
       board['q'] == board['a'] == board['z'] == 'X' or \
       board['w'] == board['s'] == board['x'] == 'X' or \
       board['e'] == board['d'] == board['c'] == 'X' or \
       board['q'] == board['s'] == board['c'] == 'X' or \
       board['e'] == board['s'] == board['z'] == 'X':

        print('\n\n\t\tPLAYER1 WINS\n\n')
        players['Player1'] += 1
        return True

    elif board['q'] == board['w'] == board['e'] == 'O' or \
        board['a'] == board['s'] == board['d'] == 'O' or \
        board['z'] == board['x'] == board['c'] == 'O' or \
        board['q'] == board['a'] == board['z'] == 'O' or \
        board['w'] == board['s'] == board['x'] == 'O' or \
        board['e'] == board['d'] == board['c'] == 'O' or \
        board['q'] == board['s'] == board['c'] == 'O' or \
            board['e'] == board['s'] == board['z'] == 'O':

        print('\n\n\t\tPLAYER2 WINS\n\n')
        players['Player2'] += 1
        return True

    return False


def update_board(board, choice, symbol):
    '''
    updates the board data with the marker of user choice
    '''
    board[choice] = symbol
    return board


def clear():
    '''
    clears the terminal to show a refreshed game state
    '''
    os.system('cls')


def start_game():
    '''
    the game logic resides here
    '''

    # display the instruction for the players to know how to play
    instruction_board = [['q', 'w', 'e'], ['a', 's', 'd'], ['z', 'x', 'c']]

    # initially game_on is True as the players play the first game
    game_on = True

    print('\nThe following keyboard keys represent the box to put your mark "X" or "O" \n')

    for i, rows in enumerate(instruction_board):
        for j, cols in enumerate(rows):
            if j < 2:
                print(cols + ' |', end=' ')
            else:
                print(cols, end=' ')
        print()
        if i < 2:
            print('--+---+--')

    while game_on:

        # board is a dictionary where each key corresponds to a button on keyboard that needs to be pressed to fill in that space
        # initially the board is empty
        board = {'q': ' ', 'w': ' ', 'e': ' ', 'a': ' ', 's': ' ', 'd': ' ', 'z': ' ', 'x': ' ', 'c': ' '}
        check_choice = []

        print('\nPlayer1(X) your turn:\n')
        display_Board(board)

        # determines which player will play next
        turn = 1

        # loop till no winner is decided
        while not check_winner(board):

            # get the user choice of space to put their marker and update check_choice to disallow choosing that space further
            choice = user_choice(check_choice)
            check_choice.append(choice)

            # alternate turn switches between markers: 'X' and 'O'
            if turn % 2 == 0:
                symbol = 'O'
            else:
                symbol = 'X'

            # update the board after user selects their space of choice and display the current board state
            board = update_board(board, choice, symbol)
            clear()
            display_Board(board)
            turn += 1

            # break the loop if winner has been found
            if check_winner(board):
                break

            # if no winner, check if all spaces are already occupied and then declare a draw
            elif len(check_choice) == 9:

                print('\n\n\t\tGAME ENDED IN A DRAW!\n\n')

                # increase draw count by 1
                players['draw'] += 1
                break


start_game()
