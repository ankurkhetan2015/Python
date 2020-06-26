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
    pass


def check_winner(board):
    '''
    checks if the current state of game has a winner
    '''
    pass


def update_board(board, choice, symbol):
    '''
    updates the board data with the marker of user choice
    '''
    pass


def clear():
    '''
    clears the terminal to show a refreshed game state
    '''
    os.system('cls')


def start_game():
    '''
    the game logic resides here
    '''

    '''
    display the instruction for the players to know how to play
    '''
    instruction_board = [['q', 'w', 'e'], ['a', 's', 'd'], ['z', 'x', 'c']]
    '''
    initially game_on is True as the players play the first game
    '''
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
        '''
        board is a dictionary where each key corresponds to a button on keyboard that needs to be pressed to fill in that space

        initially the board is empty
        '''
        board = {'q': ' ', 'w': ' ', 'e': ' ', 'a': ' ', 's': ' ', 'd': ' ', 'z': ' ', 'x': ' ', 'c': ' '}

        print('\nPlayer1(X) your turn:\n')
        display_Board(board)


start_game()
