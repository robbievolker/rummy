import random

#Class for each card in the deck. Contains a suit ("Clubs", "Diamonds", "Spades", "Hearts") and a value (1, 2, 3, 4, Jack, Queen etc.) attriubte.
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.hand = []

#Class for creating multiple players.
class Player:

    def __init__(self):
        self.name = self.setName()
        self.score = 0

    def setName(self):
        return input("Please enter your player name!")



def printIntro():
    print("Welcome to Rummy!")
    print("This is a popular card game where you will draw and discard cards in order to complete various runs, which will give you points.")
    print("This game is for 2-6 players!")

#Creating the deck with 1 argument (packNumber). This gives players the option to use a varying number of packs to allow for duplicates (eg. 2 packs would have 2 of each card, 3 packs would have 3 of each card).
#Returns the deck as a list.
def newDeck(packNumber):
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
    #deck = [Card(value, suit) for value in range(1, 14) for suit in suits]
    deck = []
    i = 0
    while(i < packNumber):
        for j in suits:
            for k in values:
                deck.append(Card(k, j))
        i += 1
    random.shuffle(deck)
    return deck

def createPlayers():
    num = int(input("How many players do you want to play with (enter a number between 2-6)? "))
    i = 0
    list = []
    while(i < num):
        list.append(Player())
        i += 1

    return list


#Main function through which the game will run.
def main():

    #Print intro for the game.
    printIntro()

    #Initialise player objects for each player of the game.
    players = createPlayers()
    if(len(players) == 2):
        dealNumber = 10
    elif(len(players) == 3 or len(players) == 4):
        dealNumber = 7
    elif(len(players) == 5 or len(players) == 6):
        dealNumber = 6

    #Ask how many packs of cards player wants to play with.
    packNumber = int(input("How many packs do you want to play with?"))

    #Start turn (return updated list with new player scores).
    #Need to add a condition to check whether or not any player has reached the max score.
    turn(players, dealNumber, packNumber)

    #Check if any player has exceeded the score.

#Logit to simulate a round of the game.
def turn(playersList, dealNumber, packNumber):

    #Create deck and discard pile using newDeck function. Discard pile is an empty list.
    deck = newDeck(packNumber)
    discard = []


if __name__ == "__main__": main()
