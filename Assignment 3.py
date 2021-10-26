# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 08:40:31 2021

@author: hanne
"""


import random


def shuffledDeck():
    'returns shuffled deck'
    
    # suits is a set of 4 Unicode symbols: back spade and club,
    # and white diamond and heart 
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}
    ranks = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}
    deck = []

    # create deck of 52 cards
    for suit in suits:
        for rank in ranks:             # card is the concatenation
            deck.append(rank+' '+suit) # of suit and rank

    # shuffle the deck and return
    random.shuffle(deck)
    return deck


def dealCard(index):
    deck = shuffledDeck()
    card = deck[index]
    
    return card



def total(hand):
    result = 0 
  
    for card in hand:
        if card[0] in ('J','Q','K'):
             result = result + 10
        elif card[0] in ('A'): 
             calculation_eleven = result + 11 
             calculation_one = result + 1
            
             if calculation_eleven > 21: 
                 result = calculation_one
             else:
                 result = calculation_eleven

        else: 
             result = result + int(card[0])
        
    return result       ### so we can use it in compare_hands             
             



def compareHands(total_house, total_player, player, house):
    for card in player:
        if card in ('10','J','Q','K'):
           valueten = True
        elif card == 'A':
           valueA = True
        else:
            valueten = False
            valueA = False
    if valueten and valueA:
        blackjack_player = True

    for card in house:
        if card in ('10','JQK'):
            valueten = True
        elif card == 'A':
            valueA = True
    if valueten and valueA:
        blackjack_house = True



    if total_player > 21:
       print('You lost..')
    elif total_house > 21:
       print('Congratulations, you won!')
    elif total_house < total_player:
       print('Congratulations, you won!')
    elif total_house > total_player:
       print('You lost..')
    elif total_house == total_player: 
       if total_player == 21 and blackjack_player and not blackjack_house:
           print('Congratulations, you won!')
       elif total_player == 21 and not blackjack_player and blackjack_house:
           print('You lost..')
       else:
           print('It is a draw.') 
           
           
    

def blackjack():

    shuffledDeck()

    player = set()
    house = set()

    # deal the cards
    player.add(dealCard(0))
    house.add(dealCard(1))
    player.add(dealCard(2))
    house.add(dealCard(3))


    # initialize a counter
    counter = 3
    # Ask if player wants a new card
    new_card = True
    while new_card:

        total_player = total(player)
        print("\nYour cards are: ",end='')
        for card in player:
            print(card, end=', ')
        if total_player > 21:
            print("\nSorry, you lost..", end=' ')
            for card in player:
                print(card, end=', ')
                new_card = False
        else:
            print("\nDo you want to hit or stand?")
            play = input("Please enter 'h' for hit and 's' for stand: ").lower()
            while play not in ('hs'):
                print("Wrong input! Try again.")
                play = input("Please enter 'h' for hit and 's' for stand: ").lower()
            if play == 'h':
                counter = counter + 1
                player.add(dealCard(counter))
            else:
                new_card = False

    if total_player <= 21:
        # Ask if house wants a new card
        total_house = total(house)
        while total_house < 17:
            counter = counter + 1
            house.add(dealCard(counter))
            total_house = total(house)
            
    else: 
        total_house = total(house)
    
    print("The house has the following cards: ", end='')
    for card in house:
        print(card, end=', ')
    
    print('*'*30)
    compareHands(total_house, total_player, player, house)

if __name__ == '__main__':
    blackjack()





