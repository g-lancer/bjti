__author__ = 'Gl'

import unittest
import card
import gamestate
import player

class BlackjackTest(unittest.TestCase):

# def test1(self):
# self.failUnless(False)

#lets have a bunch of cards here

    cardv3 = card.BjCard(1,1)        #here goes 3 of diamonds (value 3)
    cardv10 = card.BjCard(0,8)       #10 of clubs
    cardv10_2 = card.BjCard(3,8)     #10 of spades
    cardv11 = card.BjCard(0,12)      #Ace of clubs
    cardv11_2 = card.BjCard(2,12)    #Ace of hearts


    def testcardvalue01(self):
        print('testcardvalue01')
        bjcard = card.BjCard(0,1)
        self.failUnless(bjcard.value() == 3)

    def testdecknorepeats(self):
        print('testdecknorepeats')
        d1 = card.BjCard.createdeck(36,1)
        d1 = sorted(d1, key = lambda c1: c1.suit*100 + c1.name)
        hasdoubles = False
        for i in range(1,len(d1)):
            hasdoubles = hasdoubles and d1[i] == d1[i-1]
        self.failIf(hasdoubles)

    def testdecknumcards(self):
        print('testdecknumcards')
        d1 = card.BjCard.createdeck(36,1)
        self.failUnless(len(d1) == 36)

    def testnomorecards(self):
        print('testnomorecards')
#        #lets form a few hands of cards that don't need any more cards

        g1 = gamestate.Gamestate(36)
        pltype1 = 'random garbage gives me human'

        handnoneed1 = [self.cardv11_2, self.cardv11]
        handnoneed2 = [self.cardv11_2, self.cardv11, self.cardv3]
        handnoneed3 = [self.cardv10_2, self.cardv10, self.cardv3]
        handnoneed4 = [self.cardv10, self.cardv11]

        pl1 = g1.createplayer(pltype1)
        pl2 = g1.createplayer(pltype1)
        pl3 = g1.createplayer(pltype1)
        pl4 = g1.createplayer(pltype1)

        pl1.hand = handnoneed1
        pl2.hand = handnoneed2
        pl3.hand = handnoneed3
        pl4.hand = handnoneed4

        self.failIf( pl1.hasspace() or pl2.hasspace() or pl3.hasspace() or pl4.hasspace())

    def testmorecards(self):
        print('testmorecards')
#        #lets form a few hands of cards that don't need any more cards

        g1 = gamestate.Gamestate(36)
        pltype1 = 'random garbage gives me human'

        handneed1 = [self.cardv11_2]
        handneed2 = [self.cardv11_2, self.cardv3]
        handneed3 = [self.cardv10_2, self.cardv10]
        handneed4 = [self.cardv10, self.cardv3]

        pl1 = g1.createplayer(pltype1)
        pl2 = g1.createplayer(pltype1)
        pl3 = g1.createplayer(pltype1)
        pl4 = g1.createplayer(pltype1)

        pl1.hand = handneed1
        pl2.hand = handneed2
        pl3.hand = handneed3
        pl4.hand = handneed4

        self.failUnless(pl1.hasspace() and pl2.hasspace() and pl3.hasspace() and pl3.hasspace())

    def testsmartcarddesire(self):
        print('testsmartcarddesire')
        g1 = gamestate.Gamestate(36)
        p1 = g1.createplayer('scpu')
        p1.recievecard(self.cardv3)
        p1.recievecard(self.cardv10)
        self.failUnless(p1.hasspace())

    def testbankcarddesire1(self):
        print('testbankcarddesire1')
        g1 = gamestate.Gamestate(36)
        b1 = g1.createplayer('bank')
        b1.recievecard(self.cardv3)
        b1.recievecard(self.cardv10)
        self.failUnless(b1.wantscard())

    def testbankcarddesire2(self):
        print('testbankcarddesire2')
        g1 = gamestate.Gamestate(36)
        b1 = g1.createplayer('bank')
        b1.recievecard(self.cardv3)
        b1.recievecard(self.cardv3)
        b1.recievecard(self.cardv3)
        b1.recievecard(self.cardv10)
        print(b1.hand)
        print(b1.gethandvalue())
        self.failIf(b1.wantscard())

    def testhumany(self):
        print('testhumany')
        g1 = gamestate.Gamestate(36)
        p1 = g1.createplayer('human')
        print('you better say yes')
        self.failUnless(p1.wantscard())

    def testhumann(self):
        print('testhumann')
        g1 = gamestate.Gamestate(36)
        p1 = g1.createplayer('human')
        print('you better say no')
        self.failIf(p1.wantscard())

    def testgetmax1(self):
        print('testgetmax1')
        l1 = [0,0,0,0]
        methmax = gamestate.Gamestate.getmaxindexes(l1)
        expmax = list(range(len(l1)))
        self.failUnless(methmax == expmax)

    def testgetmax2(self):
        print('testgetmax2')
        l1 = [0,20,3,20,18]
        methmax = gamestate.Gamestate.getmaxindexes(l1)
        expmax = [1,3]
        self.failUnless(methmax == expmax)



def maintest():
    unittest.main()

def playgame():
    anothergame = True
    while anothergame:
        game1 = gamestate.Gamestate(36)
        game1.give2startingcards()
        game1.playrounds()
        game1.announcewinners()
        print('ok, game\'s over, do you want another one?')
        anothergame = gamestate.Gamestate.getyesorno()
        print('...')

if __name__ == '__main__':
    maintest()

