__author__ = 'Gl'

def get_yes_or_no():
    viableanswers = ['y', 'n']
    answer = ''
    while answer not in viableanswers:
        answer = input('can you please enter y for yes or n for now? \n')
    if answer == 'y':
        return True
    else:
        return False

def get_number(lower_border, upper_border):
    num = lower_border - 1
    while not lower_border <= num < upper_border:
        user_string = input('something from 0 and 9 will do \n')
        if user_string.isnumeric():
            num = int(user_string)
        else:
            print('won\'t do, it\'s not a number')
    return num

def get_max_indexes(list_):
    max_value = max(list_)
    list_of_maximums = []
    for i in range(len(list_)):
        if list_[i] == max_value:
            list_of_maximums.append(i)
    return list_of_maximums

def print_winners(list_of_winners):
    if any(winner.show_type() == 'bank' for winner in list_of_winners)
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