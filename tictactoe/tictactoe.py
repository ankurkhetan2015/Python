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
    pass


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
    pass


start_game()
