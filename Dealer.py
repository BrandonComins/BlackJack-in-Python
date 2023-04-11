from Player import Player
from Deck import Deck
class Dealer(Player):
    
    def __init__(self):
        super().__init__("Dealer", 100000)
    
    def showHand(self):
        print('Dealer hand is: [' + '■, ' + str(self.hand[1]) + ']')
    

    