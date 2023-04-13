from Player import Player
from Deck import Deck

class Dealer(Player):
    
    def __init__(self):
        super().__init__("Dealer", 100000)
    
    def showHand(self):
        print('Dealer hand is: [' + '■, ' + str(self.hand[1]) + ']')
    

    def hit(self, card_deck : Deck) -> bool:
        self.hand.append(card_deck.giveCard())
        total_1, total_2 = [self.sumCards()[i] for i in range(2)]
        
        return (total_1 == 16, total_2 == 16, self.bust())  # true if player busts