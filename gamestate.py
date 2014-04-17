__author__ = 'Gl'

import card
import player

class GameState():

    def __init__(self, decktype1):
        self.decktype = decktype1
        self.create_list_of_players()
        self.deck = card.BjCard.create_deck(self.decktype,len(self.playerlist))


    @staticmethod
    def get_yes_or_no():
        viableanswers = ['y', 'n']
        answer = ''
        while answer not in viableanswers:
            answer = input('can you please enter y for yes or n for now? \n')
        if answer == 'y':
            return True
        else:
            return False

    @staticmethod
    def get_number():
        num1 = -1
        #print('hey, can you give me a number?')
        while not 0 <= num1 < 10:
            str1 = input('something from 0 and 9 will do \n')
            if str1.isnumeric():
                num1 = int(str1)
            else:
                print('won\'t do, it\'s not a number')
        return num1

    @staticmethod
    def get_max_indexes(list1):
        max1 = max(list1)
        listofmaximums = []
        for i in range(len(list1)):
            if list1[i] == max1:
                listofmaximums.append(i)
        return listofmaximums

    @staticmethod
    def print_winners(listofwinners):
        if 0 in listofwinners:
            print('ok, bank won this one.')
        else:
            print('hey! we have a winner(s)')
            for pl in listofwinners:
                if pl == 1:
                    print('hey, our human won!!')
                print('it is player mumber', pl)
            if listofwinners[0].get_hand_value() > 21:      #I don't like this 0 here
                #this is fail (it's int -_-)
                print('double ace!')
            else:
                print('score is ', listofwinners[0].get_hand_value())

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
        dumbcpunumber = GameState.get_number()
        for i in range(dumbcpunumber):
            roster.append(self.create_player('dcpu'))
        print('and now tell me how many smart CPUs you want here')
        smartcpunumber = GameState.get_number()
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
        listofwinners = GameState.get_max_indexes(scores)
        return listofwinners

#http://habrahabr.ru/company/stratoplan/blog/218217/
#don't boterh, just link transfer