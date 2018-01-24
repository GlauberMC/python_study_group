# -*- coding: utf-8 -*-

'''
Docktest do baralho


>>> deck  = create_deck()
>>> ten_firsts = deck[0:10]
>>> len(deck)
52
>>> shuffle(deck)
>>> deck[0:10] != ten_firsts
True
>>> card = hit(desk) # Test hit
>>> len(deck) == 51
True
>>> fake_deck = create_deck() # Test hit 2
>>> hand = [card1, card2, card3]
>>> is str = [isinstance(card, str) for card in hand]
>>> all(is_str)
True
>>> not_in_deck = [True for card in hand if card not in deck]
>>> all(not_in_deck)
True

'''



import random
from random import shuffle
# from random import shuffle as shuffle_deck

def create_deck():
    """This function create an deck with 52 cards """
    numbers = ['A', '2', '3', '4', '5', '6',
              '7', '8', '9', '10', 'Q', 'J',
              'K']

    suites = ['♠','♣', '♥', '♦']

    deck = []

    for suit in suites:
        for number in numbers:
           deck.append('{}{} -'.format(number, suit))
    return deck


def hit(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card




if __name__=="__main__":
    deck = create_deck()
    shuffle(deck)
    hit(deck)
    print(deck)


