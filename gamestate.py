__author__ = 'Gl'

import card
import player

class Gamestate():

    def __init__(self, decktype1):
        self.decktype = decktype1
        self.createlistofplayers()
        self.deck = card.BjCard.createdeck(self.decktype,len(self.playerlist))


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
        #print('hey, can you give me a number?')
        while not 0 <= num1 < 10:
            str1 = input('something from 0 and 9 will do \n')
            if str1.isnumeric():
                num1 = int(str1)
            else:
                print('won\'t do, it\'s not a number')
        return num1

    @staticmethod
    def getmaxindexes(list1):
        max1 = max(list1)
        listofmaximums = []
        for i in range(len(list1)):
            if list1[i] == max1:
                listofmaximums.append(i)
        return listofmaximums

    @staticmethod
    def printwinners(listofwinners):
        if 0 in listofwinners:
            print('ok, bank won this one.')
        else:
            print('hey! we have a winner(s)')
            for pl in listofwinners:
                if pl == 1:
                    print('hey, our human won!!')
                print('it is player mumber', pl)
            if listofwinners[0].gethandvalue() > 21:      #I don't like this 0 here
                #this is fail (it's int -_-)
                print('double ace!')
            else:
                print('score is ', listofwinners[0].gethandvalue())

    def createplayer(self,playertype):
        if playertype == 'dcpu':
            p = player.DumbCPUPlayer()
        elif playertype == 'scpu':
            p = player.SmartCPUPlayer(self.decktype)
        elif playertype == 'bank':
            p = player.Bank17()
        else:
            p = player.HumanPlayer()
        return p

    def createlistofplayers(self):
        banker = self.createplayer('bank')
        humanplayer = self.createplayer('human')
        roster = [banker, humanplayer]
        print('we have 1 banker and one human player here')
        print('tell me how many dumb CPUs you want added to this game')
        dumbcpunumber = Gamestate.getnumber()
        for i in range(dumbcpunumber):
            roster.append(self.createplayer('dcpu'))
        print('and now tell me how many smart CPUs you want here')
        smartcpunumber = Gamestate.getnumber()
        for i in range(smartcpunumber):
            roster.append(self.createplayer('scpu'))
        self.playerlist = roster

    def give2startingcards(self):
        for pl in self.playerlist:
            pl.recievecard(self.deck.pop(0))
            pl.recievecard(self.deck.pop(0))

    def playrounds(self):
        cardsnotwanted = False
        while not cardsnotwanted:
            cardsnotwanted = True
            for pl in self.playerlist:
                if pl.wantscard():
                    pl.recievecard(self.deck.pop(0))
                    cardsnotwanted = False

    def getwinners(self):
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

        print(scores)

        listofwinners = Gamestate.getmaxindexes(scores)
        return listofwinners

#http://habrahabr.ru/company/stratoplan/blog/218217/
#don't boterh, just link transfer