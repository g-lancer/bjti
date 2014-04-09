__author__ = 'Gl'

import card
import player

class Gamestate():

    def __init__(self, decktype):
        self.decktype = decktype
        self.playerlist = player.Player.createlistofplayers()
        self.deck = card.BjCard.createdeck(decktype,len(playerlist))

    @staticmethod
    def getyesorno():
        viableanswers = ['y', 'n']
        answer = ''
        while answer not in viableanswers:
            answer = input('can you please enter y for yes or n for now? \n')
        if answer == 'y':
            return True
        else:
            return False

    @staticmethod
    def getnumber():
        num1 = -1
        print('hey, can you give me a number?')
        while not 0 <= num1 < 10:
            str1 = input('something from 0 and 9 will do')
            if str1.isnumeric():
                num1 = int(str1)
            else:
                print('won\'t do,it\'s not a number')
        return num1

    @staticmethod
    def getmaxindexes(list):
        max1 = max(list)
        listofmaximums = []
        for i in range(len(list)):
            if list[i] == max1:
                listofmaximums.append(i)
        return listofmaximums

    def createplayer(self,playertype):
        if playertype == 'dcpu':
            p = player.Player.DumbCPUPlayer()
        elif playertype == 'scpu':
            p = player.Player.SmartCPUPlayer()
        elif playertype == 'bank':
            p = player.Player.Bank17(self.decktype)
        else:
        p = HumanPlayer()
        return p

    def createlistofplayers(self):
        banker = player.Player.createplayer('bank')
        humanplayer = player.Player.createplayer('human')
        roster = [banker, humanplayer]
        print('we have 1 banker and one human player here')
        print('tell me how many dumb CPUs you want added to this game')
        dumbcpunumber = Gamestate.getnumber()
        for i in range(dumbcpunumber):
            roster.append(player.Player.createplayer('dcpu'))
        print('and now tell me how many smart CPUs you want here')
        smartcpunumber = Gamestate.getnumber()
        for i in range(smartcpunumber):
            roster.append(player.Player.createplayer('scpu'))
        self.playerlist = roster

    def give2startingcards(self):
        for pl in self.playerlist:
            pl.recievecard(self.deck.pop(0))
            pl.recievecard(self.deck.pop(0))

    def playrounds():
        cardsnotwanted = False
        while not cardsnotwanted:
            for pl in self.playerlist:
                if pl.wantscard():
                    pl.recievecard(self.deck.pop(0))

    def announcewinners(self):
        #lets form a list of player points
        scores = []
        for player in self.playerlist:
            pscore = player.gethandvalue()
            if pscore > 22:
                scores.append(0)
            elif pscore == 22:
                if len(player.showhand()) > 2:
                    scores.append(0)
            else:
                scores.append(pscore)

        listofwinners = Gamestate.getmaxindexes(scores)
        if 0 in listofwinners:
            print('ok, bank won this one.')
        else:
            print('hey! we have a winnder(s)')
            for pl in listofwinners:
                print('it is player mumber', pl)

#http://habrahabr.ru/company/stratoplan/blog/218217/
#don't boterh, just link transfer