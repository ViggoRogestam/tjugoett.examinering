import os

# Variables
ui_width = 60
player_in = True
dealer_in = True


class Card:
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    deck = []

    def __init__(self):
        """
        Creates deck of cards
        """
        # list of ranks
        ranks = ['Ace', '2', '3', '4', '5',
                 '6', '7', '8', '9', '10',
                 'Jack', 'Queen', 'King']
        # list of suits
        suits = ["\u2663", "\u2665",
                 "\u2666", "\u2660"]
        # iterate through ranks and suit and crate each card of a deck
        for suit in suits:
            for index, rank in enumerate(ranks):
                # increase index by 1 to get card value (i.e. ace = 1, 2 = 2, king = 13)
                value = index + 1
                card = Card(rank, suit, value)
                # add card to deck
                self.deck.append(card)

    # return deck
    def get_deck(self):
        """
        Get Deck
        :return: returns deck of cards
        """
        return self.deck

    # Deal x amount of random cars from deck, add to hand and remove from deck
    def deal_card(self, hand, times=1):
        """
        Deal cards to hand
        :param hand: player or dealer hand
        :param times: how many cards to draw
        """
        import random
        for i in range(times):
            drawn_card = random.choice(list(self.deck))
            self.deck.remove(drawn_card)
            hand.add_card(drawn_card)
        return

    def print_deck(self):
        deck_to_print = self.deck.copy()
        print(deck_to_print)


class Hand:
    def __init__(self):
        self.hand = []

    # Add card to hand
    def add_card(self, card):
        self.hand.append(card)

    # calculate values of cards in hand
    def calculate_cards_value(self):
        total_value = 0
        ace_count = 0
        for card in self.hand:
            total_value += card.value
            # Count ace as 14
            if card.rank == 'Ace':
                ace_count += 1
                total_value += 13
        # if total value over 21 and ace in hand count ace as 1
        while ace_count > 0 and total_value > 21:
            total_value -= 13
            ace_count -= 1

        return total_value

    # get hand
    def get_hand(self):
        cards = []
        for i in self.hand:
            cards.append(i)
        return cards


def print_rules():
    print("\033[1m" + ".: TJUGOETT :.".center(ui_width) + "\033[0m")
    print('*' * ui_width)
    print("\033[1m" + "RULES".center(ui_width) + "\033[0m")
    print('-' * ui_width)
    print('\033[1mGoal Of The Game:\033[0m')
    print('''- The goal is to have a hand that
      totals closer to 21 than the dealers hand
      without exceeding 21. If the player and
      the dealer has the same score, the dealer
      wins.''')

    print('\n\033[1mCard Values:\033[0m')
    print('- Number cards (2-10) are worth their face values')
    print('''- Face cards have the following values:
       * King: 13 points
       * Queen: 12 points
       * Jack: 11 points
       * Ace: 1 or 14 points''')

    print('\n\033[1mDealing:\033[0m')
    print('- The player is dealt two cards.')

    print('\n\033[1mPlayers Turn:\033[0m')
    print('- Hit: The player can choose to take an additional card.')
    print('''- Stand: The player can choose to not take any more cards
      and stick with their current hand.''')

    print('''\nThe player continues to take cards until they choose to 
      stad or until their total points exceed 21 
      (at which point they immediatley lose).''')

    print('\n\033[1mDealers Turn:\033[0m')
    print('''- The dealer reveals draws cards until they choose to stand
      or their total points exceeds 21.''')
    print('-' * ui_width)


def clear_terminal():
    # clear the terminal
    if os.name == 'posix':  # for Unix/Linux/macOS
        os.system('clear')
    else:  # for other OS:es
        os.system('cls')


def print_player_hand():
    for card in player_hand.get_hand():
        print('\n', '-', card, end='')
    print('\n')
    print('-' * ui_width)
    print(f'for a total of {player_hand.calculate_cards_value()}')
    print('-' * ui_width)


def print_dealer_hand():
    for card in dealer_hand.get_hand():
        print('\n', card, end='')
    print('\n')
    print('-' * ui_width)
    print(f'for a total of {dealer_hand.calculate_cards_value()}')
    print('-' * ui_width)


def calculate_result():
    if score_dealer_hand and score_player_hand > 21:
        print('\033[1m\nBoth player and dealer busts! Dealer Wins\033[0m')
    elif score_dealer_hand == score_player_hand:
        print('\033[1m\nDealer and player have the same score. Dealer Wins!\033[0m')
    elif score_dealer_hand == 21:
        print('\033[1m\n21! Dealer Wins.\033[0m')
    elif score_player_hand == 21:
        print('\033[1m\n21! Player Wins.\033[0m')
    elif score_player_hand > 21:
        print('\033[1m\nYou Bust! Dealer Wins.\033[0m')
    elif score_dealer_hand > 21:
        print('\033[1m\nDealer Bust! You Win.\033[0m')
    elif score_dealer_hand > score_player_hand:
        print('\033[1m\nDealer Wins!\033[0m')
    else:
        print('\033[1m\nPlayer Wins!\033[0m')


# Game LOOP:
# Create Deck
deck = Deck()
deck.get_deck()

# Deal 2 cards to player
player_hand = Hand()
deck.deal_card(player_hand, 1)

# Print rules
print_rules()

# Ask for user input to start gameloop
input('Press Enter to start...')

# Clear termnal
clear_terminal()

# stay or hit
while player_in:
    clear_terminal()
    # Print cards from player hand
    print('\n' + '-' * ui_width)
    print('You drew the following ', end='')
    print('Hand: ', end='')
    print('\n' + '-' * ui_width)
    print_player_hand()

    # if player busts break loop
    if player_hand.calculate_cards_value() > 21:
        break
    # if player still in
    if player_in:
        hit_or_stay = input('\n\n1: Hit\n2: Stay\n> ')

        # if player choose to hit add draw card
        if hit_or_stay == '1':
            deck.deal_card(player_hand)

        # if player choose to stay, print hand then break
        elif hit_or_stay == '2':
            clear_terminal()
            print('-' * ui_width)
            print('You choose to stay with this Hand: ')
            print('-' * ui_width)
            print_player_hand()
            break
        # if input not 1 or 2 replay the loop
        else:
            input('Error. Choose either "1" or "2"')
            continue

# Create dealer hand
dealer_hand = Hand()

# Print header for dealer turn
print('\n')
print('-' * ui_width)
print("\033[1m" + " .: DEALER PLAYS :. ".center(ui_width) + "\033[0m")

#  dealer plays
while dealer_in:

    # if dealerhand = empty, draw 2 cards
    if not dealer_hand.get_hand():
        deck.deal_card(dealer_hand, 2)
        continue

    # if dealerhand is greater 16 > dealer stays and prit out dealer hand
    elif dealer_hand.calculate_cards_value() > 16:
        dealer_in = False
        print('*' * ui_width)
        print('Dealer drew the following ', end='')
        print('Hand: ', end='')
        print('\n' + '-' * ui_width)
        print_dealer_hand()

    # if dealer still in, draw card
    elif dealer_in:
        deck.deal_card(dealer_hand)

    # if dealer busts, then break
    elif dealer_hand.calculate_cards_value() > 21:
        break

# create variables from player and dealer hand
score_player_hand = player_hand.calculate_cards_value()
score_dealer_hand = dealer_hand.calculate_cards_value()

# Detirmine winner and loser
calculate_result()
