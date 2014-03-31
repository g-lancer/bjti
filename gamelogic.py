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
