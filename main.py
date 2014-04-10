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

    def testnomorecards(self):
#        #lets form a few hands of cards that don't need any more cards

        handnoneed1 = [self.cardv11_2, self.cardv11]
        handnoneed2 = [self.cardv11_2, self.cardv11, self.cardv3]
        handnoneed3 = [self.cardv10_2, self.cardv10, self.cardv3]
        handnoneed4 = [self.cardv10, self.cardv11]

        self.failIf(gamestate.Gamestate.cantakecards(handnoneed1) or gamestate.Gamestate.cantakecards(handnoneed2)
                    or gamestate.Gamestate.cantakecards(handnoneed3) or gamestate.Gamestate.cantakecards(handnoneed4))

    def testmorecards(self):
#        #lets form a few hands of cards that don't need any more cards

        handnoneed1 = [self.cardv11_2]
        handnoneed2 = [self.cardv11_2, self.cardv3]
        handnoneed3 = [self.cardv10_2, self.cardv10]
        handnoneed4 = [self.cardv10, self.cardv3]

        self.failUnless(gamestate.Gamestate.cantakecards(handnoneed1) and gamestate.Gamestate.cantakecards(handnoneed2)
                    and gamestate.Gamestate.cantakecards(handnoneed3) and gamestate.Gamestate.cantakecards(handnoneed4))

    def testsmartcarddesire(self):
        p1 = player.Player.createplayer('scpu')
        p1.recievecard(self.cardv3)
        p1.recievecard(self.cardv10)
        self.failUnless(p1.wantscard(1))

    def testbankcarddesire(self):
        b1 = player.Player.createplayer('bank')
        b1.recievecard(self.cardv3)
        b1.recievecard(self.cardv10)
        self.failUnless(b1.wantscard())

    def testhuman(self):
        p1 = player.Player.createplayer('human')
        print('you better say yes')
        self.failUnless(p1.wantscard())

    def testgetmax1(self):
        l1 = [0,0,0,0]
        methmax = gamestate.Gamestate.getmaxindexes(l1)
        expmax = list(range(len(l1)))
        self.failUnless(methmax == expmax)

    def testgetmax2(self):
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
        print('ok, game\'s over, od you want another one?')
        anothergame = gamestate.Gamestate.getyesorno()
        print('...')

if __name__ == '__main__':
    playgame()

