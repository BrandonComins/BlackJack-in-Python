from Deck import deck
from Player import player
from CustomErrors import InvalidPlayerError

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
        players.append(player(i))
    
    return players

if __name__ == "__main__":
    deck_of_cards = deck()
    getPlayers()