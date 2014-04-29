__author__ = 'Gl'

import card
import player
import utils


class GameStateBJ():
    MIN_PLAYERS = 0
    MAX_PLAYERS = 7

    def __init__(self, decktype1):
        self.decktype = decktype1
        self.create_list_of_players()
        self.deck = card.BJCard.create_deck(self.decktype,len(self.playerlist))

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
        human_player = self.create_player('human')
        roster = [banker, human_player]
        print('we have 1 banker and one human player here')
        print('tell me how many dumb CPUs you want added to this game')
        dumb_cpu_number = utils.get_number(self.MIN_PLAYERS, self.MAX_PLAYERS)
        for i in range(dumb_cpu_number):
            roster.append(self.create_player('dcpu'))
        print('and now tell me how many smart CPUs you want here')
        smart_cpu_number = utils.get_number(self.MIN_PLAYERS, self.MAX_PLAYERS)
        for i in range(smart_cpu_number):
            roster.append(self.create_player('scpu'))
        self.playerlist = roster

    def give_2_starting_cards(self):
        for pl in self.playerlist:
            pl.recieve_card(self.deck.pop(0))
            pl.recieve_card(self.deck.pop(0))

    def play_rounds(self):
        cards_not_wanted = False
        while not cards_not_wanted:
            cards_not_wanted = True
            for pl in self.playerlist:
                if pl.wants_card():
                    pl.recieve_card(self.deck.pop(0))
                    cards_not_wanted = False

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

class DurakGameState():
    MAX_CARDS = 6
    MIN_PLAYERS = 2
    MAX_PLAYERS = 5

    number_of_decks = 1

    playerlist = []
    active_players = playerlist         #wrong one

    def __init__(self, deck_type):
        self.deck = card.DurakCard.create_deck(deck_type, self.number_of_decks)
        self.playerlist = self.create_list_of_players()
        self.find_trump()
        self.give_starting_cards()
        self.starting_player_index = self.find_lowest_trump_owner()


    def refill_hands(self, starting_player=0):
        player_order = utils.get_cycle(self.active_players, starting_player)

        for pl_num in player_order:
            while len(self.playerlist[pl_num].show_hand()) < self.MAX_CARDS:
                if len(self.deck) > 0:
                    self.playerlist[pl_num].recieve_card(self.deck.pop(0))
                else:
                    print('player ', pl_num, ' tried to take card, but deck is empty now!')
                    break

    def find_trump(self):
        number_of_staring_cards = len(self.playerlist)*6
        if len(self.deck) < number_of_staring_cards:
            print('wtf, we don\'t have cards for everybody')
        elif len(self.deck) == number_of_staring_cards:
            self.trump_card = self.deck[number_of_staring_cards - 1]
            self.trump = self.deck[number_of_staring_cards - 1].tell_suit()
        else:
            self.trump_card = self.deck[number_of_staring_cards]
            self.trump = self.deck[number_of_staring_cards].tell_suit()

    def give_starting_cards(self):
        self.refill_hands()

    def find_lowest_trump_owner(self):
        trumplist = card.DurakCard.trump_roster(self.trump)
        for tr1 in trumplist:
            for pl1 in self.playerlist:
                if tr1 in pl1.show_hand():
                    return self.playerlist.index(pl1)
        print('wtf, no lowest trump?')

    def play_round(self, starting_player):
        attackers = utils.get_cycle(self.active_players, starting_player)
        defender = attackers.pop(1)
        max_number_of_attack_cards = len(self.active_players[defender].showhand()) - 1
        self.playerlist[self.next_move]

        self.active_players[attackers[0]].play_attack()

        while True:
            self.starting_player

