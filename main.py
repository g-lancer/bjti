__author__ = 'Gl'

import unittest
import card

class BlackjackTest(unittest.TestCase):

# def test1(self):
# self.failUnless(False)

    def test_cardvalue01(self):
        bjcard = card.BjCard(0,1)
        self.failUnless(bjcard.value() == 3)

    def testdecknorepeats(self):
        d1 = card.BjCard.createdeck(1,1)
        d1 = sorted(d1, key = lambda c1: c1.suit*100 + c1.name)
        hasdoubles = False
        for i in range(1,len(d1)):
            hasdoubles = hasdoubles and d1[i] == d1[i-1]
        self.failIf(hasdoubles)

    def testdecknumcards(self):
        d1 = card.BjCard.createdeck(1,1)
        self.failUnless(len(d1) == 36)


def main():
    unittest.main()


if __name__ == '__main__':
    main()