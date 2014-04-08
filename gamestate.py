__author__ = 'Gl'

import card
import player

class Gamestate():

    def __init__(self, decktype)
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