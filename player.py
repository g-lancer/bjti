__author__ = 'Gl'


import card
import gamelogic
import random

class Player():

    def __init__(self):
        self.hand = []

    @staticmethod
    def createplayer(playertype):
        if playertype == 'dcpu':
            p = DumbCPUPlayer()
        elif playertype == 'scpu':
            p = SmartCPUPlayer()
        elif playertype == 'bank':
            p = Bank17()
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

class Bank17(Player):

    def wantscard(self):
        if gamelogic.GameLogic.cantakecards(self.showhand()) < 17:
            return True
        else:
            return False


class HumanPlayer(Player):

    def wantscard(self):
        for c1 in self.showhand():
            print(c1)
        print('this means your current score is ', gamelogic.GameLogic.cantakecards(self.showhand()), 'do you want a card?')
        return gamelogic.GameLogic.getyesorno()
