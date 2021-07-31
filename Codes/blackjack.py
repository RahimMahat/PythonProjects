#!/usr/bin/env python3
import random
from os import system
'''
use the following list as a deck of cards
The King/Queen/Jack all count as 10
The ace can count 11 or 1
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
cards are not removed from the deck as they are drawn
Rules:
1. if any of player's score exceed 21 they lose
2. in final score who has the max score with all conditions match wins
3. you will only be shown first card of the computer
'''

def deal_card():
    ''' Returns a random card from the deck'''
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card 

def calculate_score(cards_lst):
    ''' Take a list of cards and return the score from given cards_list'''

    # checking for blackjack (i.e a hand with only 2 cards: ace + 10) and return 0
    if sum(cards_lst) == 21 and len(cards_lst) == 2:
        return 0
    # check if score is above 21 and if ace is in the card then replace it with 1
    elif 11 in cards_lst and sum(cards_lst) > 21:
        cards_lst.remove(11)
        cards_lst.insert(1)
        
    return sum(cards_lst)

def compare(user_score, computer_score):
    ''' Comparing the user and computer's score to get the winner '''
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lost, opponent has a blackjack"
    elif user_score ==0:
        return "Won, with a blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    print(r'''
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/                 
''')

    user_cards = []
    computer_cards = []

    # running for loop twice to get the card for user and computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # This while loop is for the user 
    game_over = False
    while not game_over:

        user_score = calculate_score(user_cards)
        computer_socre = calculate_score(computer_cards)
        print(f"user cards {user_cards} cureent score {user_score}")
        print(f"Computer's first card {computer_cards[0]}")

        # check for blackjack or score to be exceeded score then game over
        if user_score == 0 or computer_socre == 0 or user_score > 21:
            game_over = True
        else:
            user_choice = input("Choose wheather you want to continue or not? 'y','n' : ")
            if user_choice == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    # This while loop is for the computer
    while computer_socre != 0 and computer_socre < 17:
        computer_cards.append(deal_card())
        computer_socre = calculate_score(computer_cards)


    print(f"Your final hand: {user_cards} and final score: {user_score}")
    print(f"Computer's final hand: {computer_cards} and final score: {computer_socre}")
    # calling compare function as user and compter are now done drawing cards
    print(f"\n\t\t{compare(user_score,computer_socre)}\t\t\n")


while input("Do you want to play blackjack? 'y','n': ") == "y":
    system('cls')
    play_game()