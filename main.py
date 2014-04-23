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
    dumb_dummy = g2.create_player('dcpu')

    cardv3 = card.BJCard(1,1)        #here goes 3 of diamonds (value 3)
    cardv10 = card.BJCard(0,8)       #10 of clubs
    cardv10_2 = card.BJCard(3,8)     #10 of spades
    cardv11 = card.BJCard(0,12)      #Ace of clubs
    cardv11_2 = card.BJCard(2,12)    #Ace of hearts


    def test_card_value_01(self):
        print('testcardvalue01')
        bj_card = card.BJCard(0,1)
        self.failUnless(b_card.value() == 3)

    def test_deck_no_repeats(self):
        print('testdecknorepeats')
        d1 = card.BJCard.create_deck(36,1)
        d1 = sorted(d1, key = lambda c1: c1.suit*100 + c1.name)
        has_doubles = False
        for i in range(1,len(d1)):
            has_doubles = has_doubles and d1[i] == d1[i-1]
        self.failIf(has_doubles)

    def test_deck_numcards(self):
        print('testdecknumcards')
        d1 = card.BJCard.create_deck(36,1)
        self.failUnless(len(d1) == 36)

    def test_no_more_cards(self):
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

    def test_more_cards(self):
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

    def test_smart_card_desire(self):
        print('testsmartcarddesire')
        p1 = self.g2.create_player('scpu')
        p1.recieve_card(self.cardv3)
        p1.recieve_card(self.cardv10)
        self.failUnless(p1.has_space())

    def test_bank_card_desire1(self):
        print('testbankcarddesire1')
        b1 = self.g2.create_player('bank')
        b1.recieve_card(self.cardv3)
        b1.recieve_card(self.cardv10)
        self.failUnless(b1.wants_card())

    def test_bank_card_desire_2(self):
        print('testbankcarddesire2')
        b1 = self.g2.create_player('bank')
        b1.recieve_card(self.cardv3)
        b1.recieve_card(self.cardv3)
        b1.recieve_card(self.cardv3)
        b1.recieve_card(self.cardv10)
        self.failIf(b1.wants_card())

    def test_smart_cpu_desire_n(self):
        print('testsmartcpudesire')
        pl = self.g2.create_player('scpu')
        pl.recieve_card(self.cardv10)
        pl.recieve_card(self.cardv10_2)
        self.failIf(pl.wants_card())

    def test_smart_cpu_desire_y(self):
        pl = self.g2.create_player('scpu')
        pl.recieve_card(self.cardv10)
        self.failUnless(pl.wants_card())

    def test_dumb_player(self):
        pl = self.g2.create_player('dcpu')
        t = pl.wants_card()
        t = pl.wants_card()
        t = pl.wants_card()
        t = pl.wants_card()
        self.failUnless(True)

    def test_human_y(self):
        print('testhumany')
        p1 = self.g2.create_player('human')
        print('you better say yes')
        self.failUnless(p1.wants_card())

    def test_human_n(self):
        print('testhumann')
        p1 = self.g2.create_player('human')
        print('you better say no')
        self.failIf(p1.wants_card())

    def test_get_max_1(self):
        print('testgetmax1')
        l1 = [0,0,0,0]
        methmax = utils.get_max_indexes(l1)
        expmax = list(range(len(l1)))
        self.failUnless(methmax == expmax)

    def test_get_max_2(self):
        print('testgetmax2')
        l1 = [0,20,3,20,18]
        methmax = utils.get_max_indexes(l1)
        expmax = [1,3]
        self.failUnless(methmax == expmax)

#    def testgame(self):
#        playgame()

    def test_too_many_cards(self):
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

    def test_get_winners_1(self):

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

    def test_get_winners_2(self):
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

    def test_get_winners_3(self):
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

    def test_get_winners_4(self):

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

    def test_get_winners_5(self):

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

    def test_trump(self):
        test_card = card.DurakCard(3, 8)
        trump = 3
        self.failUnless(test_card.is_trump(trump))

    def test_beat_01(self):
        attack_card = card.DurakCard(3, 8)
        defence_card = card.DurakCard(3, 9)
        self.failUnless(defence_card.beats(attack_card, 1))

    def test_beat_02(self):
        attack_card = card.DurakCard(3, 8)
        defence_card = card.DurakCard(3, 7)
        self.failIf(defence_card.beats(attack_card, 1))

    def test_beat_03(self):
        attack_card = card.DurakCard(3, 8)
        defence_card = card.DurakCard(3, 8)
        self.failIf(defence_card.beats(attack_card, 1))

    def test_beat_04(self):
        attack_card = card.DurakCard(3, 8)
        defence_card = card.DurakCard(1, 6)
        self.failUnless(defence_card.beats(attack_card, 1))

    def test_beat_05(self):
        attack_card = card.DurakCard(3, 8)
        defence_card = card.DurakCard(1, 9)
        self.failIf(defence_card.beats(attack_card, 2))


def maintest():
    unittest.main()

def playgame():
    anothergame = True
    while anothergame:
        game = gamestate.GameStateBJ(NORMALDECK)
        anothergame = game.run_game()

# while True:
#     game = BlackJack(STANDART_DECK)
#     game.run()
#     if not ask_yes_no('Do you want to play again?'):
#         break

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
