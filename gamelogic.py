__author__ = 'Gl'

import card

class GameLogic():

    @staticmethod
    def gethandvalue(hand):
        val = 0
        for card in hand:
            val = val + card.value()
        return val

    @staticmethod
    def cantakecards(hand):
        val = GameLogic.gethandvalue(hand)
        if val < 21:
            return True
        else:
            return False

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
    def getmaxindexes(list):
        max1 = max(list)
        listofmaximums = []
        for i in range(len(list)):
            if list[i] == max1:
                listofmaximums.append(i)
        return listofmaximums


    @staticmethod
    def getwinners(listofplayers):
        #lets form a list of player points
        scores = []
        for player in listofplayers:
            pscore = GameLogic.gethandvalue(player.showhand())
            if pscore > 22:
                scores.append(0)
            elif pscore == 22:
                if len(player.showhand()) > 2:
                    scores.append(0)
            else:
                scores.append(pscore)

        listofwinners = GameLogic.getmaxindexes(scores)
        if 0 in listofwinners:
            print('ok, bank won this one.')
        else:
            print('hey! we have a winnder(s)')
            for pl in listofwinners:
                print('it is player mumber', pl)
