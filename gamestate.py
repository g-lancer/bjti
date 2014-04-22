__author__ = 'Gl'

import card
import player
import utils

MIN_PLAYERS = 0
MAX_PLAYERS = 7

class GameStateBJ():

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
        dumbcpunumber = utils.get_number(MIN_PLAYERS, MAX_PLAYERS)
        for i in range(dumbcpunumber):
            roster.append(self.create_player('dcpu'))
        print('and now tell me how many smart CPUs you want here')
        smartcpunumber = utils.get_number(MIN_PLAYERS, MAX_PLAYERS)
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
        list_of_winners = utils.get_max_indexes(scores)
        return list_of_winners

    def print_winners(self, list_of_winners):
        if any(self.playerlist[winner].show_type() == 'bank' for winner in list_of_winners):
            print('ok, bank won this one.')
        else:
            print('hey! we have a winner(s)')
            for pl_num in list_of_winners:
                print('it\'s player number ', pl_num)
                print('it\'s ', self.playerlist[pl_num].show_type())
            if self.playerlist[list_of_winners[0]].get_hand_value() > 21:      #I don't like this 0 here
                #this is fail (it's int -_-)
                print('double ace!')
            else:
                print('score is ', self.playerlist[list_of_winners[0]].get_hand_value())

    def run_game(self):
        self.give_2_starting_cards()
        self.play_rounds()
        winners = self.get_leaders()
        self.print_winners(winners)
        print('ok, game\'s over, do you want another one?')
        print('...')
        return utils.get_yes_or_no()
