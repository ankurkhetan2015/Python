import random

# Defined the SUIT, RANK and VALUE of all cards in blackjack game
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}


# Class to create a card of and assign it a value
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


# Class to create a deck of 52 cards. The member functions allows to shuffle the deck and allow deal the topmost card
class Deck:

    def __init__(self):

        # Create a list of all cards in a deck
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create a card object
                created_card = Card(suit, rank)

                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


# Class to handle cards in hand and deal with aces and card values
class Hand:

    def __init__(self):

        # Initially no cards in hand
        self.cards = []
        # Initially hand has no value
        self.value = 0
        # Initially no ace in hand
        self.ace = 0

    def add_card(self, card):
        pass

    def adjust_ace(self):
        pass


# Chips class to handle starting chips in players hand and the win/loss
class Chips:

    def __init__(self, money=0):

        # Starting money with a player
        self.amount = money
        # Initially no bet
        self.bet = 0

    def win_bet(self):
        pass

    def lose_bet(self):
        pass


def place_bet():

    play = 'NO'

    while play not in ['y', 'n']:
        play = input('Would you like to place a bet?[Y/N]: ').lower()

    if play == 'n':
        print('\nIt was nice to have you. See you again!\n')
        exit()

    print()

    while True:

        try:
            bet_placed = int(input('Enter the amount (in $) to bet: '))

        except ValueError:
            print('\nYou must enter only positive whole numbers\n')

        else:
            return bet_placed


def play_game():

    # Create a deck object
    new_deck = Deck()

    # Shuffle the 52 cards in the deck
    new_deck.shuffle()

    bet_placed = place_bet()

    print(bet_placed)


if __name__ == "__main__":

    print('\n\nWelcome to the game of BlackJack!!!\n\n')
    # Start playing the game
    play_game()
