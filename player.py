__author__ = 'Gl'


import card
import gamestate
import random

class Player():

    def __init__(self):
        self.hand = []
        self.cantakecard = True

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

    @staticmethod
    def createlistofplayers():
        banker = Player.createplayer('bank')
        humanplayer = Player.createplayer('human')
        playerlist = [banker, humanplayer]
        print('we have 1 banker and one human player here')
        print('tell me how many dumb CPUs you want added to this game')
        dumbcpunumber = gamestate.Gamestate.getnumber()
        for i in range(dumbcpunumber):
            playerlist.append(Player.createplayer('dcpu'))
        print('and now tell me how many smart CPUs you want here')
        smartcpunumber = gamestate.Gamestate.getnumber()
        for i in range(smartcpunumber):
            playerlist.append(Player.createplayer('scpu'))
        return playerlist

    def wantsscard(self):
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
        val = self.hand
        if val < 21:
            return True
        else:
            return False


class DumbCPUPlayer(Player):

    def wantsscard(self):
        if self.hasspace():
            return random.choice([False,True])
        else:
            return False

class SmartCPUPlayer(Player):

    def wantsscard(self, decktype):
        if self.hasspace():
            maxvalue = 21 - gamestate.Gamestate.gethandvalue(self.showhand())
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

    def wantsscard(self):
        if self.hasspace():
            if gamestate.Gamestate.cantakecards(self.showhand()) < 17:
                return True
            else:
                return False
        else:
            return False


class HumanPlayer(Player):

    def wantsscard(self):
        if self.hasspace():
            for c1 in self.hand():
                print(c1)
            print('this means your current score is ', self.gethandvalue(), 'do you want a card?')
            return gamestate.Gamestate.getyesorno()
        else:
            return False
