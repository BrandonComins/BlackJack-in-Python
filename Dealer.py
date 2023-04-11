from Player import Player

class Dealer(Player):
    
    def __init__(self):
        super().__init__("Dealer", 100000)
    
    def showHand(self):
        print('Dealer hand is: [' + '■, ' + str(self.hand[1]) + ']')
    

    