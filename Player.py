from Deck import Deck

class Player:

    def __init__(self, name : str, cash : int):
        self.name : str = str(name)
        self.hand : list = []
        self.cash : int = cash

    def __str__(self) -> str:
        return str(self.name) + "has $" + str(self.cash)
    
    def __repr__(self):
        total_1, total_2 = [self.sumCards()[i] for i in range(2)]
        if (self.blackJack()):
            print(self.name + " got BlackJack!")
        elif total_1 == total_2 or total_2 > 21:
            print(self.name + "'s hand is: " + str(self.hand) + " with " + str(total_1))
        elif total_1 > 21 and total_2 < 21:
            print(self.name + "'s hand is: " + str(self.hand) + " with " + str(total_1))
        else:
            print(self.name + "'s hand is: " + str(self.hand) + " with " + str(total_1) + " or " + str(total_2))
        return ""


    def dealHand(self, card_deck : Deck) -> bool:
        for i in range(2):
            self.hand.append(card_deck.giveCard())

        return self.blackJack() #true if blackjack

    def sumCards(self) -> int:
        total : list = [0, 0]
        for card in self.hand:
            if(card[1] == 'J' or card[1] == 'Q' or card[1] == 'K' or len(card) == 3):
                total[0] += 10
                total[1] += 10
            elif(card[1] == 'A'):
                total[0] += 11
                total[1] += 1
            else:
                total[0] += int(card[1])
                total[1] += int(card[1])
        
        return total
    
    def hit(self, card_deck : Deck) -> bool:
        self.hand.append(card_deck.giveCard())
        
        return self.sumCards(self) > 21 #returns true if bust

    def blackJack(self) -> bool: #true if blackjack
        return (self.sumCards()[0] == 21
                and len(self.hand[0]) != 3 #checks for 10
                and len(self.hand[1]) != 3)  #checks for 10
    
    def bust(self):
            total_1, total_2 = [self.sumCards[i] for i in range(2)]
            return total_1 > 21 and total_2 > 21 #true if bust
    
    
    
