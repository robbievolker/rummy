from cgitb import handler
import random
ACE = 1
JACK = 11
QUEEN = 12
KING = 13
#Class for each card in the deck. Contains a suit ("Clubs", "Diamonds", "Spades", "Hearts") and a value (1, 2, 3, 4, Jack, Queen etc.) attriubte.
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

def isValidRun(meld):
# A run must contain a sequence of three or more consecutive cards, all of the same suit. Therefore this must check the suit of all the cards are the same and that they are consecutive.

    #Sort the meld in ascending order.
    meld.sort(key=lambda x: x.value)
    print(meld)
    #Establish a base value and suit, this will be used to compare the other elements and determine whether or not the meld is valid.
    value0 = int(meld[0].value) - 1
    suit0 = meld[0].suit

    #Check whether the run is valid.
    for card in meld:
        #Returns false if the suit is not the same.
        if(card.suit != suit0):
            return False
        if(card.value != (value0 + 1)):
            return False
        value0 += 1
    return True

def newDeck(packNumber):
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    values = [ACE, 2, 3, 4, 5, 6, 7, 8, 9, 10, JACK, QUEEN, KING]
    deck = []
    i = 0
    while(i < packNumber):
        for j in suits:
            for k in values:
                deck.append(Card(k, j))
        i += 1
    random.shuffle(deck)
    return deck

def main():
    hand = []
    hand.append(Card(2, "Hearts"))
    hand.append(Card(3, "Hearts"))
    hand.append(Card(4, "Hearts"))

    isValid = isValidRun(hand)
    print(isValid)



if __name__ == "__main__": main()
