from Deck import Deck
from Player import Player
from Dealer import Dealer
from CustomErrors import *

def getPlayers() -> list:
    while True:
        try:
            number_of_players : int = int(input("Enter the amount of players (1-4): "))
            print()
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



def takeTurn(player : Player, deck : Deck):
    if(player.name != "Dealer"):
        choice = 0
        while (True):
            try:
                choice = int(input(" 1. hit \n 2. stay \n Your move: "))
                if choice == 1:
                    outcomes = player.hit(deck)
                    repr(player)
                    if outcomes[2]:
                        print('\n' + str(player.name) + " busted!")
                        break
                    elif outcomes[0] or outcomes[1]:
                        print()
                        break
                elif choice == 2:
                    repr(player)
                    print('\n' + str(player.name) + " stays!")
                    print()
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Bad input, must be 1 or 2")
                continue
    else:
        dealerTurn(player, deck)
        
def dealerTurn(dealer : Player, deck : Deck):
    repr(dealer)
    while(True):
        if(dealer.sumCards()[0] < 16 and dealer.sumCards()[1] < 16):
            if(dealer.hit(deck)[2]):
                print("Dealer busts!")
                repr(dealer)
                break
            repr(dealer)
        else:
            repr(dealer)
            break
    


def setUpGame(players : list, deck : Deck):
    players.append(Dealer())
    for player in players:
        player.dealHand(deck)

        if player.name != "Dealer":
            repr(player)
   
    players[-1].showHand()


def playGame(players: list, deck : Deck):
    setUpGame(players, deck)
    for player in players:
        if not player.blackJack():
            print('\n' + str(player.name) + "'s turn!")
            takeTurn(player, deck)
        else:
            print(player.name, "got Black Jack!")
            repr(player)
        

if __name__ == "__main__":
    deck_of_cards = Deck()
    playGame(getPlayers(), deck_of_cards)

