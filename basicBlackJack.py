import random


suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = [(rank, suit) for suit in suits for rank in ranks]


random.shuffle(deck)


player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop(), deck.pop()]


def calculate_hand_value(hand):
    value = 0
    num_aces = 0
    for card in hand:
        rank = card[0]
        if rank == 'Ace':
            value += 11
            num_aces += 1
        elif rank in ['King', 'Queen', 'Jack']:
            value += 10
        else:
            value += int(rank)
    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1
    return value


while True:
    print("Player's hand:", player_hand)
    print("Dealer's hand:", dealer_hand[0])
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    if player_value == 21:
        print("Blackjack! You win!")
        break
    elif player_value > 21:
        print("Bust! You lose.")
        break
    else:
        action = input("Do you want to hit or stand? ")
        if action.lower() == 'hit':
            player_hand.append(deck.pop())
        elif action.lower() == 'stand':
            while dealer_value < 17:
                dealer_hand.append(deck.pop())
                dealer_value = calculate_hand_value(dealer_hand)
            if dealer_value > 21:
                print("Dealer busts! You win!")
            elif dealer_value > player_value:
                print("Dealer wins!")
            elif dealer_value < player_value:
                print("You win!")
            else:
                print("Push! It's a tie.")
            break
        else:
            print("Invalid action. Please enter 'hit' or 'stand'.")