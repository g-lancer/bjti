__author__ = 'Gl'

class BjCard():
    suits = ['clubs', 'diamonds', 'hearts', 'spades']
    names = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    values = [2, 3, 4, 5, 6, 7, 8, 0, 10, 2, 3, 4, 11]

    def __init__(self, suit, name):
        self.suit = suit
        self.name = name

    def print(self):
        print(self.names[self.name], 'of ', self.suits[self.suit],', value ', self.values[self.name])
        return



    def gamevalue(self):
        return self.values[self.name]