__author__ = 'Gl'


import card
import gamestate
import random

class Player():

    def __init__(self):
        self.hand = []

    def wantscard(self):
        return False

    def showhand(self):
        return self.hand

    def gethandvalue(self):
        val = 0
        for card in self.hand:
            val = val + card.value()
        return val

    def recievecard(self, card):
        self.hand.append(card)
        return True

    def hasspace(self):
        val = self.gethandvalue()
        if val < 21:
            return True
        else:
            return False


class DumbCPUPlayer(Player):

    def wantscard(self):
        if self.hasspace():
            return random.choice([False,True])
        else:
            return False

class SmartCPUPlayer(Player):

    def __init__(self, decktype):
        self.hand = []
        self.decktype = decktype

    def wantscard(self, decktype):
        if self.hasspace():
            maxvalue = 21 - self.gethandvalue()
            tempdeck = card.BjCard.createdeck(decktype,1)
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

    def wantscard(self):
        if self.hasspace():
            if self.hasspace() < 17:
                return True
            else:
                return False
        else:
            return False


class HumanPlayer(Player):
    didntrefuseyet = True

    def wantscard(self):

        if self.hasspace() and self.didntrefuseyet:
            for c1 in self.hand:
                print(c1)
            print('this means your current score is ', self.gethandvalue(), 'do you want a card?')
            self.didntrefuseyet = gamestate.Gamestate.getyesorno()
            return self.didntrefuseyet
        else:
            return False
