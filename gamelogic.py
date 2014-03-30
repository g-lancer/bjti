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
