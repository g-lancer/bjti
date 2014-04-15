__author__ = 'Gl'

import unittest
import card
import gamestate
import player

class BlackjackTest(unittest.TestCase):

#    failg = gamestate.Gamestate(2)  #added just for coverage
    g2 = gamestate.Gamestate(36)
    dumbdummy = g2.createplayer('dcpu')

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

        pltype1 = 'random garbage gives me human'

        handnoneed1 = [self.cardv11_2, self.cardv11]
        handnoneed2 = [self.cardv11_2, self.cardv11, self.cardv3]
        handnoneed3 = [self.cardv10_2, self.cardv10, self.cardv3]
        handnoneed4 = [self.cardv10, self.cardv11]

        pl1 = self.g2.createplayer(pltype1)
        pl2 = self.g2.createplayer(pltype1)
        pl3 = self.g2.createplayer(pltype1)
        pl4 = self.g2.createplayer(pltype1)

        pl1.hand = handnoneed1
        pl2.hand = handnoneed2
        pl3.hand = handnoneed3
        pl4.hand = handnoneed4

        self.g2.announcewinners()

        self.failIf( pl1.hasspace() or pl2.hasspace() or pl3.hasspace() or pl4.hasspace())

    def testmorecards(self):
        print('testmorecards')
#        #lets form a few hands of cards that don't need any more cards

        pltype1 = 'random garbage gives me human'

        handneed1 = [self.cardv11_2]
        handneed2 = [self.cardv11_2, self.cardv3]
        handneed3 = [self.cardv10_2, self.cardv10]
        handneed4 = [self.cardv10, self.cardv3]

        pl1 = self.g2.createplayer(pltype1)
        pl2 = self.g2.createplayer(pltype1)
        pl3 = self.g2.createplayer(pltype1)
        pl4 = self.g2.createplayer(pltype1)

        pl1.hand = handneed1
        pl2.hand = handneed2
        pl3.hand = handneed3
        pl4.hand = handneed4

        self.failUnless(pl1.hasspace() and pl2.hasspace() and pl3.hasspace() and pl3.hasspace())

    def testsmartcarddesire(self):
        print('testsmartcarddesire')
        p1 = self.g2.createplayer('scpu')
        p1.recievecard(self.cardv3)
        p1.recievecard(self.cardv10)
        self.failUnless(p1.hasspace())

    def testbankcarddesire1(self):
        print('testbankcarddesire1')
        b1 = self.g2.createplayer('bank')
        b1.recievecard(self.cardv3)
        b1.recievecard(self.cardv10)
        self.failUnless(b1.wantscard())

    def testbankcarddesire2(self):
        print('testbankcarddesire2')
        b1 = self.g2.createplayer('bank')
        b1.recievecard(self.cardv3)
        b1.recievecard(self.cardv3)
        b1.recievecard(self.cardv3)
        b1.recievecard(self.cardv10)
        self.failIf(b1.wantscard())

    def testsmartcpudesiren(self):
        print('testsmartcpudesire')
        pl = self.g2.createplayer('scpu')
        pl.recievecard(self.cardv10)
        pl.recievecard(self.cardv10_2)
        self.failIf(pl.wantscard())

    def testsmartcpudesirey(self):
        pl = self.g2.createplayer('scpu')
        pl.recievecard(self.cardv10)
        self.failUnless(pl.wantscard())

    def testdumbplayer(self):
        pl = self.g2.createplayer('dcpu')
        t = pl.wantscard()
        t = pl.wantscard()
        t = pl.wantscard()
        t = pl.wantscard()
        self.failUnless(True)

    def testhumany(self):
        print('testhumany')
        p1 = self.g2.createplayer('human')
        print('you better say yes')
        self.failUnless(p1.wantscard())

    def testhumann(self):
        print('testhumann')
        p1 = self.g2.createplayer('human')
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

#    def testgame(self):
#        playgame()

    def testtoomanycards(self):
        print('testtoomanycards')
        hpl = self.g2.createplayer('human')
        dpl = self.g2.createplayer('dcpu')
        spl = self.g2.createplayer('scpu')
        bpl = self.g2.createplayer('bank')

        failhand = [self.cardv10, self.cardv11, self.cardv10_2]

        hpl.hand = failhand
        dpl.hand = failhand
        spl.hand = failhand
        bpl.hand = failhand

        self.failIf(hpl.wantscard() or dpl.wantscard() or spl.wantscard() or bpl.wantscard())



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

#link transfer
#http://portforward.com/english/routers/port_forwarding/Asus/WL-500G/Risk_of_Rain.htm
#http://maps.yandex.ru/?text=%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F%2C%20%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%2C%204-%D1%8F%20%D0%BB%D0%B8%D0%BD%D0%B8%D1%8F%20%D0%92.%D0%9E.%2C%2065&sll=30.275408%2C59.949163&ll=30.275408%2C59.949163&spn=0.052571%2C0.016339&z=15&l=map
