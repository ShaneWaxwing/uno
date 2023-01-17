class Card:
    def __init__(self, color, number):
        self.color = color
        self.number = number

    def __str__(self):
        return self.color + " " + str(self.number)

    def __repr__(self):
        return self.color + " " + str(self.number)