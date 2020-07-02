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

    def deal(self):
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


# function to set up the player's chips in hand
def chips_in_hand():

    while True:

        try:
            chips = int(input('Enter the amount (in $) you want to enter the game with: '))

        except ValueError:
            print('\nYou must enter only positive whole numbers\n')

        else:
            return chips


# function to ask player to place their bet
def place_bet(amount):

    bet = 'NO'
    bet_placed = amount + 1

    while bet not in ['y', 'n']:
        bet = input('\nWould you like to place a bet?[Y/N]: ').lower()

    if bet == 'n':
        print('\nIt was nice to have you. See you again!\n')
        exit()

    while bet_placed > amount:

        print(f'\nEnter a bet less than in hand amount: {amount} \n')

        try:
            bet_placed = int(input('Enter the amount (in $) to bet: '))

        except ValueError:
            print('\n(You must enter only positive whole numbers)')

    return bet_placed


# function to request a hit during the game
def hit(deck, hand):
    pass


# function to prompt user if they want a hit or stand
def hit_or_stand(deck, hand):
    pass


# functions to show cards and their Value for both players and dealer
def show_some(player, dealer):
    pass


def show_all(player, dealer):
    pass


# functions to handle possible outcomes of the game
def player_busts():
    pass


def player_wins():
    pass


def dealer_busts():
    pass


def dealer_wins():
    pass


# function to control game logic
def play_game():

    # Create a deck object
    new_deck = Deck()

    # Shuffle the 52 cards in the deck
    new_deck.shuffle()

    # Set up Player's Chips
    amount = chips_in_hand()
    player_chips = Chips(amount)

    # Player's bet amount
    bet_placed = place_bet(amount)

    # Deal two cards each to everyone(including dealer) playing one-by-one
    player_hand = Hand()
    dealer_hand = Hand()

    player_hand.add_card(new_deck.deal())
    dealer_hand.add_card(new_deck.deal())
    player_hand.add_card(new_deck.deal())
    dealer_hand.add_card(new_deck.deal())


if __name__ == "__main__":

    print('\n\nWelcome to the game of BlackJack!!!\n\n')

    # Start playing the game
    play_game()
