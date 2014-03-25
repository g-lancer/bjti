__author__ = 'Gl'

import random

class BjCard():
    suits = ['clubs', 'diamonds', 'hearts', 'spades']
    names = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    values = [2, 3, 4, 5, 6, 7, 8, 0, 10, 2, 3, 4, 11]

    def __init__(self, suit, name):
        self.suit = suit
        self.name = name

    def print(self):
        print(self.names[self.name], 'of ', self.suits[self.suit],', value ', self.values[self.name])
        return

    def createdeck(self, decktype, numberofdecks):
        deck = []
        if decktype == 1:
            for i in range(len(self.suits)):
                for j in range(4,len(self.names)):
                    c1 = self.BjCard(i,j)
                    deck = deck.append(c1)
        deck = deck * numberofdecks
        random.shuffle(deck)
        return deck



    def value(self):
        return self.values[self.name]