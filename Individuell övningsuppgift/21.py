import random
import os
import sys

# Deck of cards
deck_of_cards = {
    "Hearts": ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"],
    "Diamonds": ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"],
    "Clubs": ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"],
    "Spades": ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"],
}

# Variables
player_in = True
dealer_in = True
player_hand = []
dealer_hand = []
total_cards = 0
pot = 5000
ui_width = 60


#  give cards
def dealCards(turn):
    # Pick a random suit (key) from the dict deck_of_cards
    random_suit = random.choice(list(deck_of_cards.keys()))

    # pick a random card from the list inside the random suit
    card = random.choice(deck_of_cards[random_suit])

    # Create a variabel that contains suit and card (ex. 'King of Hearts')
    #full_card_name = card + ' of ' + random_suit
    # Add the card to the player
    turn.append(card)
    # Remove the card from the deck of cards
    deck_of_cards[random_suit].remove(card)


# calculate score
def calculate_card_values(turn):
    total = 0
    king = ['King']
    jack = ['Jack']
    queen = ['Queen']
    ace = 0
    for card in turn:
        if card in king:
            total += 13
        elif card in queen:
            total += 12
        elif card in jack:
            total += 11
        elif card == "Ace":
            total += 14
            ace += 1
        else:
            total += int(card)
    while total > 21 and ace > 0:
        total -= 13
        ace -= 1

    return total


# Deal card to player
for _ in range(1):
    dealCards(player_hand)
    # TODO: ask user to bet
# Print rules
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
print('- Number cars (2-10) are worth their face values')
print('''- Face cars hav the following values:
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


# Deal one more card & print hand
dealCards(player_hand)

# Ask for user input to start gameloop
input('Press Enter to start...')

# clear the terminal
if os.name == 'posix':  # for Unix/Linux/macOS
    os.system('clear')
else:  # for other OS:es
    os.system('cls')

# stay or hit
while player_in:
    # clear the terminal
    if os.name == 'posix':  # for Unix/Linux/macOS
        os.system('clear')
    else:  # for other OS:es
        os.system('cls')
    # Print cards from player hand
    print('\n' + '-' * ui_width)
    print('You drew the following ', end='')
    print('Hand: ', end='')
    for card in player_hand:
        print(card + ', ', end='')
    print(f'for a total of {calculate_card_values(player_hand)}')

    # if player busts break loop
    if calculate_card_values(player_hand) > 21:
        break
    # if player still in
    if player_in:
        print('-' * ui_width)
        hit_or_stay = input('\n\n1: Hit\n2: Stay\n> ')

        # if player choose to hit add draw card
        if hit_or_stay == '1':
            dealCards(player_hand)

        # if player choose to stay, print hand then break
        elif hit_or_stay == '2':
            print('You choose to stay with this \n Hand: ', end='')
            for card in player_hand:
                print(card + ', ', end='')
            break
        # if input not 1 or 2 replay the loop
        else:
            input('Error. Choose either "1" or "2"')
            continue

#  dealer play
while dealer_in:
    # if dealerhand = empty, draw card
    if not dealer_hand:
        dealCards(dealer_hand)
        continue
    # if dealerhand is greater 16 => dealer stays and prit out dealer hand
    elif calculate_card_values(dealer_hand) > 16:
        dealer_in = False
        print('\n\nDealer Drew: ', end='')
        for card in dealer_hand:
            print(card + ', ', end='')
        print(f'for a total of {calculate_card_values(dealer_hand)}')

    # if dealer still in, draw card
    elif dealer_in:
        dealCards(dealer_hand)

    # if dealer busts, then break
    elif calculate_card_values(dealer_hand) > 21:
        break

# create variables from player and dealer hand
score_player_hand = calculate_card_values(player_hand)
score_dealer_hand = calculate_card_values(dealer_hand)

# IF-statmentes for printing results
if score_dealer_hand and score_player_hand > 21:
    print('\nBoth player and dealr busts! Dealer Wins')
elif score_dealer_hand == score_player_hand:
    print('\nDealer and player has the same score. Dealer Wins!')
elif score_dealer_hand == 21:
    print('\n21! Dealer Wins.')
elif score_player_hand == 21:
    print('\n21! Player Wins.')
elif score_player_hand > 21:
    print('\nYou Bust! Dealer Wins.')
elif score_dealer_hand > 21:
    print('\nDealer Bust! You Win.')
elif score_dealer_hand > score_player_hand:
    print('\nDealer Wins!')
else:
    print('\nPlayer Wins!')
