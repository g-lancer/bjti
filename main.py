__author__ = 'Gl'

import unittest
import card

class BlackjackTest(unittest.TestCase):

#    def test1(self):
#        self.failUnless(False)

    def test_card_value_01(self):
        bjcard = card.BjCard(0,0)
        self.failUnless(bjcard.gamevalue() == 2)

def main():
    unittest.main()


if __name__ == '__main__':
    main()