__author__ = 'Gl'

import unittest
import card
import gamestate
import utils

#lets have some constants
NORMALDECK = 36

class BlackjackTest(unittest.TestCase):
#    failg = gamestate.GameStateBJ(2)  #added just for coverage
    g2 = gamestate.GameStateBJ(NORMALDECK)
    dumbdummy = g2.create_player('dcpu')

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
        d1 = card.BjCard.create_deck(36,1)
        d1 = sorted(d1, key = lambda c1: c1.suit*100 + c1.name)
        hasdoubles = False
        for i in range(1,len(d1)):
            hasdoubles = hasdoubles and d1[i] == d1[i-1]
        self.failIf(hasdoubles)

    def testdecknumcards(self):
        print('testdecknumcards')
        d1 = card.BjCard.create_deck(36,1)
        self.failUnless(len(d1) == 36)

    def testnomorecards(self):
        print('testnomorecards')
#        #lets form a few hands of cards that don't need any more cards

        pltype1 = 'random garbage gives me human'

        handnoneed1 = [self.cardv11_2, self.cardv11]
        handnoneed2 = [self.cardv11_2, self.cardv11, self.cardv3]
        handnoneed3 = [self.cardv10_2, self.cardv10, self.cardv3]
        handnoneed4 = [self.cardv10, self.cardv11]

        pl1 = self.g2.create_player(pltype1)
        pl2 = self.g2.create_player(pltype1)
        pl3 = self.g2.create_player(pltype1)
        pl4 = self.g2.create_player(pltype1)

        pl1.hand = handnoneed1
        pl2.hand = handnoneed2
        pl3.hand = handnoneed3
        pl4.hand = handnoneed4

        self.g2.get_leaders()

        self.failIf( pl1.has_space() or pl2.has_space() or pl3.has_space() or pl4.has_space())

    def testmorecards(self):
        print('testmorecards')
#        #lets form a few hands of cards that don't need any more cards

        pltype1 = 'random garbage gives me human'

        handneed1 = [self.cardv11_2]
        handneed2 = [self.cardv11_2, self.cardv3]
        handneed3 = [self.cardv10_2, self.cardv10]
        handneed4 = [self.cardv10, self.cardv3]

        pl1 = self.g2.create_player(pltype1)
        pl2 = self.g2.create_player(pltype1)
        pl3 = self.g2.create_player(pltype1)
        pl4 = self.g2.create_player(pltype1)

        pl1.hand = handneed1
        pl2.hand = handneed2
        pl3.hand = handneed3
        pl4.hand = handneed4

        self.failUnless(pl1.has_space() and pl2.has_space() and pl3.has_space() and pl3.has_space())

    def testsmartcarddesire(self):
        print('testsmartcarddesire')
        p1 = self.g2.create_player('scpu')
        p1.recieve_card(self.cardv3)
        p1.recieve_card(self.cardv10)
        self.failUnless(p1.has_space())

    def testbankcarddesire1(self):
        print('testbankcarddesire1')
        b1 = self.g2.create_player('bank')
        b1.recieve_card(self.cardv3)
        b1.recieve_card(self.cardv10)
        self.failUnless(b1.wants_card())

    def testbankcarddesire2(self):
        print('testbankcarddesire2')
        b1 = self.g2.create_player('bank')
        b1.recieve_card(self.cardv3)
        b1.recieve_card(self.cardv3)
        b1.recieve_card(self.cardv3)
        b1.recieve_card(self.cardv10)
        self.failIf(b1.wants_card())

    def testsmartcpudesiren(self):
        print('testsmartcpudesire')
        pl = self.g2.create_player('scpu')
        pl.recieve_card(self.cardv10)
        pl.recieve_card(self.cardv10_2)
        self.failIf(pl.wants_card())

    def testsmartcpudesirey(self):
        pl = self.g2.create_player('scpu')
        pl.recieve_card(self.cardv10)
        self.failUnless(pl.wants_card())

    def testdumbplayer(self):
        pl = self.g2.create_player('dcpu')
        t = pl.wants_card()
        t = pl.wants_card()
        t = pl.wants_card()
        t = pl.wants_card()
        self.failUnless(True)

    def testhumany(self):
        print('testhumany')
        p1 = self.g2.create_player('human')
        print('you better say yes')
        self.failUnless(p1.wants_card())

    def testhumann(self):
        print('testhumann')
        p1 = self.g2.create_player('human')
        print('you better say no')
        self.failIf(p1.wants_card())

    def testgetmax1(self):
        print('testgetmax1')
        l1 = [0,0,0,0]
        methmax = utils.get_max_indexes(l1)
        expmax = list(range(len(l1)))
        self.failUnless(methmax == expmax)

    def testgetmax2(self):
        print('testgetmax2')
        l1 = [0,20,3,20,18]
        methmax = utils.get_max_indexes(l1)
        expmax = [1,3]
        self.failUnless(methmax == expmax)

#    def testgame(self):
#        playgame()

    def testtoomanycards(self):
        print('testtoomanycards')
        hpl = self.g2.create_player('human')
        dpl = self.g2.create_player('dcpu')
        spl = self.g2.create_player('scpu')
        bpl = self.g2.create_player('bank')

        failhand = [self.cardv10, self.cardv11, self.cardv10_2]

        hpl.hand = failhand
        dpl.hand = failhand
        spl.hand = failhand
        bpl.hand = failhand

        self.failIf(hpl.wants_card() or dpl.wants_card()
                    or spl.wants_card() or bpl.wants_card())

    def testgetwinners1(self):

        pltype1 = 'random garbage gives me human'

        handneed1 = [self.cardv11_2]
        handneed2 = [self.cardv11_2, self.cardv3]
        handneed3 = [self.cardv10_2, self.cardv10]
        handneed4 = [self.cardv10, self.cardv3]

        pl1 = self.g2.create_player(pltype1)
        pl2 = self.g2.create_player(pltype1)
        pl3 = self.g2.create_player(pltype1)
        pl4 = self.g2.create_player(pltype1)

        pl1.hand = handneed1
        pl2.hand = handneed2
        pl3.hand = handneed3
        pl4.hand = handneed4

        self.g2.playerlist = [pl1, pl2, pl3, pl4]

        self.failUnless(self.g2.get_leaders() == [2])

    def testgetwinners2(self):
        print('testgetwinners2')

        pltype1 = 'random garbage gives me human'

        handneed1 = [self.cardv11_2,self.cardv11]
        handneed2 = [self.cardv11_2, self.cardv3]
        handneed3 = [self.cardv10_2, self.cardv10]
        handneed4 = [self.cardv10, self.cardv3]

        pl1 = self.g2.create_player(pltype1)
        pl2 = self.g2.create_player(pltype1)
        pl3 = self.g2.create_player(pltype1)
        pl4 = self.g2.create_player(pltype1)

        pl1.hand = handneed1
        pl2.hand = handneed2
        pl3.hand = handneed3
        pl4.hand = handneed4

        self.g2.playerlist = [pl1, pl2, pl3, pl4]
        self.failUnless(self.g2.get_leaders() == [0])

    def testgetwinners3(self):
        print('testgetwinners3')

        pltype1 = 'random garbage gives me human'

        handneed1 = [self.cardv11_2,self.cardv10]
        handneed2 = [self.cardv11_2, self.cardv11]
        handneed3 = [self.cardv10_2, self.cardv10]
        handneed4 = [self.cardv10, self.cardv3]

        pl1 = self.g2.create_player(pltype1)
        pl2 = self.g2.create_player(pltype1)
        pl3 = self.g2.create_player(pltype1)
        pl4 = self.g2.create_player(pltype1)

        pl1.hand = handneed1
        pl2.hand = handneed2
        pl3.hand = handneed3
        pl4.hand = handneed4

        self.g2.playerlist = [pl1, pl2, pl3, pl4]

        self.failUnless(self.g2.get_leaders() == [1])

    def testgetwinners4(self):

        pltype1 = 'random garbage gives me human'

        handneed1 = [self.cardv11_2]
        handneed2 = [self.cardv11_2, self.cardv3]
        handneed3 = [self.cardv11, self.cardv3]
        handneed4 = [self.cardv10, self.cardv3]

        pl1 = self.g2.create_player(pltype1)
        pl2 = self.g2.create_player(pltype1)
        pl3 = self.g2.create_player(pltype1)
        pl4 = self.g2.create_player(pltype1)

        pl1.hand = handneed1
        pl2.hand = handneed2
        pl3.hand = handneed3
        pl4.hand = handneed4

        self.g2.playerlist = [pl1, pl2, pl3, pl4]

        self.failUnless(self.g2.get_leaders() == [1,2])

    def testgetwinners5(self):

        pltype1 = 'random garbage gives me human'

        handneed1 = [self.cardv11, self.cardv3]
        handneed2 = [self.cardv11_2, self.cardv3]
        handneed3 = [self.cardv11, self.cardv3]
        handneed4 = [self.cardv10, self.cardv3]

        pl1 = self.g2.create_player(pltype1)
        pl2 = self.g2.create_player(pltype1)
        pl3 = self.g2.create_player(pltype1)
        pl4 = self.g2.create_player(pltype1)

        pl1.hand = handneed1
        pl2.hand = handneed2
        pl3.hand = handneed3
        pl4.hand = handneed4

        self.g2.playerlist = [pl1, pl2, pl3, pl4]
        self.failUnless(self.g2.get_leaders() == [0,1,2])

class DurakTest(unittest.TestCase):
    def test_beat(self, attack_card, defence_card):
        self.failUnless(defence_card.beats(attack_card))

def maintest():
    unittest.main()

def playgame():
    anothergame = True
    while anothergame:
        game = gamestate.GameStateBJ(NORMALDECK)
        anothergame = game.run_game()

if __name__ == '__main__':
    playgame()

#link transfer
#http://guildwarstemple.com/dragontimer/events.php?serverKey=207&langKey=en
#http://gw2sched.azurewebsites.net/
#https://www.guildwars2.com/en/news/the-megaserver-system-world-bosses-and-events/
#http://habrahabr.ru/company/stratoplan/blog/218217/
#http://www.imdb.com/title/tt1843230/


# Durak analytics
#
#gamestate.__init__(self):
# match_counter = 0
#
# game.create_deck()
#
# game.give_players_cards(self)
# game.select_trump             (may be needs to be put into give cards)
# game.select_1st_player        (may ditch this

#game.play()                 (play rounds?)
# while len(active_players > 1):
#  game.select_next_player()
#  game.attack_round()
#   game.play_attack_card
#  game.give_cards()
#
#  game.announce_fool(self)
# match_counter += 1
#
#
#
#
#
#
#
#
#
#
#
#
