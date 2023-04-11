from Deck import Deck
from Player import Player
from Dealer import Dealer
from CustomErrors import *

def getPlayers() -> list:
    while True:
        try:
            number_of_players : int = int(input("Enter the amount of players (1-4): "))
             
            if not(1 <= number_of_players <= 4):
                raise InvalidPlayerError 
        except ValueError:
            print("Must input a number (1-4)")
            continue
        except InvalidPlayerError:
            print("Not a valid player amount, (1-4)")            
            continue
        
        break
    
    players : list = []
    for i in range(number_of_players):
        players.append(Player(i, 1000))
    
    return players



def takeTurn(player : Player):
    choice = 0
    while (not player.bust or choice == 2):
        choice = int(input("1. hit\n2.stay"))
        if choice == 1:
            player.hit()
        elif choice == 2:
            break
        else:
            print("Bad input, must be 1 or 2")
            continue

    


def playGame(players : list, deck : Deck):
    players.append(Dealer())
    for player in players:
        player.dealHand(deck)

        if player.name != "Dealer":
            repr(player)
   
    players[-1].showHand()







if __name__ == "__main__":
    deck_of_cards = Deck()
    playGame(getPlayers(), deck_of_cards)

