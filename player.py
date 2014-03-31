__author__ = 'Gl'


import card
import gamelogic
import random

class Player():

    def __init__(self):
        self.hand = []

    @staticmethod
    def createplayer(playertype):
        if playertype == 'cpu':
            p = DumbCPUPlayer()
        elif playertype == 'bank':
            p = SmartCPUPlayer()
        else:
            p = HumanPlayer()
        return p

    def wantscard(self):
        return False

    def showhand(self):
        return self.hand

    def recievecard(self, card):
        self.hand.append(card)
        return True


class DumbCPUPlayer(Player):

    def wantscard(self):
        return random.choice([False,True])

class SmartCPUPlayer(Player):

    def wantscard(self, decktype):
        maxvalue = 21 - gamelogic.GameLogic.gethandvalue(self.showhand())
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


class HumanPlayer(Player):

    def wantscard(self):
        return gamelogic.GameLogic.getyesorno()
