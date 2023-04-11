from random import randint

class Deck:
    def __init__(self):
        self.suits = ['♠', '♦', '♥', '♣']
        self.numbers = (['A', '2', '3', '4', '5', '6' , '7' , '8' ,
                     '9', '10', 'J', 'Q', 'K'])
        self.cards = []
        
        for suit in self.suits:
            for number in self.numbers:
                self.cards.append(suit + number)
        
    def __str__(self):
        return str(self.cards)

    def giveCard(self):
        return self.cards.pop(randint(0, len(self.cards) - 1))

    def shuffle(self):
        self.__init__()
    

