#!/usr/bin/env python3

from os import system

bids = {}
bid_end = False

def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"\n\nThe winner is {winner} with the bid of ${highest_bid}\n")


while not bid_end:
    print(r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
    ''')



    name = input("Enter your name: ")
    bid = float(input("What is your bid? $"))
    bids[name] = bid
    cont = input("Do you want to continue bidding? 'yes' or 'no'\n")
    if cont == "no":
        bid_end = True
        highest_bidder(bids)
    elif cont == "yes":
        system('cls')