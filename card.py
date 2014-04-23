__author__ = 'Gl'

import random
import main

class BjCard():
    suits = ['clubs', 'diamonds', 'hearts', 'spades']
    names = ['2', '3', '4', '5', '6', '7', '8',
             '9', '10', 'J', 'Q', 'K', 'A']
    values = [2, 3, 4, 5, 6, 7, 8, 0, 10, 2, 3, 4, 11]

    def __init__(self, suit, name):
        self.suit = suit
        self.name = name

    def __str__(self):
        stringtoprint = self.names[self.name] + ' of ' +\
                        self.suits[self.suit] + ', value ' +\
                        str(self.values[self.name])
        return stringtoprint

    @staticmethod
    def create_deck(decktype, numberofdecks):
        deck = []
        if decktype == main.NORMALDECK:
            for i in range(len(BjCard.suits)):
                for j in range(4,len(BjCard.names)):
                    c1 = BjCard(i,j)
                    deck.append(c1)
        else:
            print('unknown deck type, sry')
        deck = deck * numberofdecks
        random.shuffle(deck)
        return deck



    def value(self):
        return self.values[self.name]