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
        print('something from ', lower_border, ' and ', upper_border, ' will do')
        user_string = input()
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

def get_cycle(array_to_cycle, start_num):
    final_order = []
    for i in range(start_num, start_num + len(array_to_cycle)):
        if i < len(array_to_cycle):
            final_order.append(array_to_cycle[i])
        else:
            final_order.append(i - len(array_to_cycle))
    return final_order
