__author__ = 'Gl'

import random
import main

class Card():
    suits = ['clubs', 'diamonds', 'hearts', 'spades']
    names = ['2', '3', '4', '5', '6', '7', '8',
             '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, suit, name):
        self.suit = suit
        self.name = name

    def __str__(self):
        return self.names[self.name] + ' of ' + self.suits[self.suit]

    @classmethod
    def create_deck(cls, decktype, number_of_decks):
        deck = []
        if decktype == main.NORMALDECK:
            for i in range(len(Card.suits)):
                for j in range(4,len(Card.names)):
                    c1 = cls(i,j)
                    deck.append(c1)
        else:
            print('unknown deck type, sry')
        deck = deck * number_of_decks
        random.shuffle(deck)
        return deck

class BJCard(Card):
    values = [2, 3, 4, 5, 6, 7, 8, 0, 10, 2, 3, 4, 11]

    def __str__(self):
        stringtoprint = self.names[self.name] + ' of ' +\
                        self.suits[self.suit] + ', value ' +\
                        str(self.values[self.name])
        return stringtoprint

    def value(self):
        return self.values[self.name]

class DurakCard(Card):

    @classmethod
    def trump_roster(trump):
        tr_roster = []
        for n1 in range(len(super.names)):
            tr_roster.append(DurakCard(super.suit[trump], n1))
        return tr_roster

    def is_trump(self, trump):
        if self.suit == trump:
            return True
        else:
            return False

    def beats(self,card_to_beat, trump):
        if self.suit == card_to_beat.suit:
            if self.name > card_to_beat.name:
                return True
            else:
                return False
        else:
            if self.suit == trump:
                return True
            else:
                return False

    def tell_suit(self):
        #print('we have a trump!, it\'s ', self.suit)
        return self.suit

    def tell_rank(self):
        return self.names.index(self.name)