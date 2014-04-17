__author__ = 'Gl'


import card
import gamestate
import random

class Player():

    def __init__(self):
        self.hand = []

    def wants_card(self):
        return False

    def show_hand(self):
        return self.hand

    def get_hand_value(self):
        val = 0
        for card in self.hand:
            val = val + card.value()
        return val

    def recieve_card(self, card):
        self.hand.append(card)

    def has_space(self):
        val = self.get_hand_value()
        if val < 21:
            return True
        else:
            return False


class DumbCPUPlayer(Player):

    def wants_card(self):
        if self.has_space():
            return random.choice([False,True])
        else:
            return False

class SmartCPUPlayer(Player):

    def __init__(self, decktype):
        self.hand = []
        self.decktype = decktype

    def wants_card(self):
        if self.has_space():
            maxvalue = 21 - self.get_hand_value()
            tempdeck = card.BjCard.create_deck(self.decktype,1)
            numberofsuitablecards = 0
            for c1 in tempdeck:
                if c1.value() <= maxvalue:
                    numberofsuitablecards = numberofsuitablecards + 1
            chance = numberofsuitablecards/len(tempdeck)
            if chance > 0.5:
                return True
            else:
                return False
        else:
            return False

class Bank17(Player):

    def wants_card(self):
        if self.has_space():
            if self.get_hand_value() < 17:
                return True
            else:
                return False
        else:
            return False


class HumanPlayer(Player):
    didntrefuseyet = True

    def wants_card(self):

        if self.has_space() and self.didntrefuseyet:
            for c1 in self.hand:
                print(c1)
            print('this means your current score is ',\
                  self.get_hand_value(), 'do you want a card?')
            self.didntrefuseyet = gamestate.GameState.get_yes_or_no()
            return self.didntrefuseyet
        else:
            return False

    def recieve_card(self, card):
        self.hand.append(card)
        print('you got ', card)
        input('press enter to continue')
