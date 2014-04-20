__author__ = 'Gl'

import card
import player
import utils

class GameState():

    def __init__(self, decktype1):
        self.decktype = decktype1
        self.create_list_of_players()
        self.deck = card.BjCard.create_deck(self.decktype,len(self.playerlist))

    def create_player(self,playertype):
        if playertype == 'dcpu':
            p = player.DumbCPUPlayer()
        elif playertype == 'scpu':
            p = player.SmartCPUPlayer(self.decktype)
        elif playertype == 'bank':
            p = player.Bank17()
        else:
            p = player.HumanPlayer()
        return p

    def create_list_of_players(self):
        banker = self.create_player('bank')
        humanplayer = self.create_player('human')
        roster = [banker, humanplayer]
        print('we have 1 banker and one human player here')
        print('tell me how many dumb CPUs you want added to this game')
        dumbcpunumber = utils.get_number()
        for i in range(dumbcpunumber):
            roster.append(self.create_player('dcpu'))
        print('and now tell me how many smart CPUs you want here')
        smartcpunumber = utils.get_number()
        for i in range(smartcpunumber):
            roster.append(self.create_player('scpu'))
        self.playerlist = roster

    def give_2_starting_cards(self):
        for pl in self.playerlist:
            pl.recieve_card(self.deck.pop(0))
            pl.recieve_card(self.deck.pop(0))

    def play_rounds(self):
        cardsnotwanted = False
        while not cardsnotwanted:
            cardsnotwanted = True
            for pl in self.playerlist:
                if pl.wants_card():
                    pl.recieve_card(self.deck.pop(0))
                    cardsnotwanted = False

    def get_leaders(self):
        #lets form a list of player points
        scores = []
        for player in self.playerlist:
            pscore = player.get_hand_value()
            if pscore > 22:
                scores.append(0)
            elif pscore == 22:
                if len(player.show_hand()) > 2:
                    scores.append(0)
                else:
                    scores.append(pscore)
            else:
                scores.append(pscore)
        listofwinners = utils.get_max_indexes(scores)
        return listofwinners

    def run_game(self):
        self.give_2_starting_cards()
        self.play_rounds()
        winners = self.get_leaders()
        utils.print_winners(winners)
        print('ok, game\'s over, do you want another one?')
        anothergame = utils.get_yes_or_no()
        print('...')

#http://habrahabr.ru/company/stratoplan/blog/218217/
#don't boterh, just link transfer