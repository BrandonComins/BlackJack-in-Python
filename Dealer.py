from Player import player
from Deck import deck
class dealer(player):
    
    def __init__(self):
        super().__init__(self, "Dealer")
        self.cash = 100000000

    