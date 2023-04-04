from Deck import deck

class player:

    def __init__(self, name : str):
        self.name : str = name
        self.hand : list = []
        self.cash : int = 1000

    def __str__(self) -> str:
        return self.name + "has $" + self.cash


    def dealHand(self, card_deck : deck) -> bool:
        for i in range(2):
            self.hand.append(card_deck.giveCard())

        return self.blackJack() #true if blackjack

    def sumCards(self) -> int:
        total : int = 0
        for card in self.hand:
            total += int(card[0])
        
        return total
    
    def hit(self, card_deck : deck) -> bool:
        self.hand.append(card_deck.giveCard())
        
        return self.sumCards(self) > 21 #returns true if bust

    def blackJack(self) -> bool: #true if blackjack
        return (self.sumCards == 21
                and int(self.hand[0][0]) != 10 
                and int(self.hand[-1][0] != 10))  
    
