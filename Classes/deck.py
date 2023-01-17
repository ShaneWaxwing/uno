import random
from Classes.card import Card

class Deck:
    def __init__(self):
        self.cards = []
        self.build_deck()    

    def build_deck(self):
        colors = ['Green', 'red', 'blue', 'yellow']
        values = [1,2,3,4,5,6,7,8,9]

        for color in colors:
            self.cards.append(Card(color, 0))
            for value in values:
                self.cards.append(Card(color, value))
                self.cards.append(Card(color, value))             

        random.shuffle(self.cards)

    def __str__(self):
        return str(self.cards)

    def __repr__(self):
        return str(self.cards)


