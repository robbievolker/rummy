import random

#Class for each card in the deck. Contains a suit ("Clubs", "Diamonds", "Spades", "Hearts") and a value (1, 2, 3, 4, Jack, Queen etc.) attriubte.
class Card:
    def __init__(self, value, suit,):
        self.value = value
        self.suit = suit

#Class for creating multiple players.
class Player:

    def __init__(self):
        self.name = self.setName()
        self.score = 0
        self.hand = []
        self.table = []
        self.out = False

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

#Logic to simulate a round of the game.
def round(playersList, dealNumber, packNumber):

    #Create deck and discard pile using newDeck function. Discard pile is an empty list.
    deck = newDeck(packNumber)
    discard = []
    #When a player is out of cards this will change to True and the round will get ready to end.
    playerOut = False

    #Deal cards to players (based on the number specified in dealNumber).
    for player in playersList:
        while(len(player.hand) < dealNumber):
            player.hand.append(deck.pop())

    #While player isn't out, iterate over players and let them make their turn.
    while(playerOut == False):
        for player in playersList:
            viewHand(player)
            #Check if deck is empty. If so, discard pile becomes the new deck and shuffle.
            if(len(deck) == 0):
                deck = discard
                discard = []
                deck.shuffle()

            #Phase 1 of a turn, pick up from either the stock or the discard pile.

            #Check if there are any cards in the discard pile. If not, player must pick up from deck.
            if(len(discard) == 0):
                print("There are no cards in the discard pile, therefore you must draw from the deck.")
                player.hand.append(deck.pop())
            else:
                print(str(discard[len(discard) - 1].value) + " of " + discard[len(discard) - 1].suit + " is on the top of the discard pile.")
                stockOrDiscard = stockOrDiscard()
                if (stockOrDiscard == 1):
                    player.hand.append(deck.pop())
                elif (stockOrDiscard == 2):
                    player.hand.append(discard.pop())

            #Phase 2 of a turn, choose to meld or lay-off.
            choice = int(chooseMeldOrLay())
            meldOrLay(player, choice)

            #Phase 3 of a turn, discard one card from the player's hand.

            #Check if player is out of cards, if so set the round to end and the scoring to take place within this if statement.
            if(player.out == True):
                playerOut = True

#Potential helper function for the options available to each player during their turn.
def turn():
    pass

#Helper function to view a player's hand
def viewHand(player):
    i = 1
    for card in player.hand:
        print(str(i) + ": " + str(card.value) + " of " + card.suit)
        i += 1

#Gives player the option to pick up from the stock or discard pile.
def stockOrDiscard():
    print("Pick up from either the deck or discard pile.")
    print("Input 1 to pick up from the deck, or 2 for the discard pile")
    choice = input()

    return choice

#Gives player the option to do a meld or lay-off.
def chooseMeldOrLay():
    print("You can either meld or lay-off!")
    print("Input 1 to meld, or 2 to lay-off! If you can't do either this turn, input 3.")
    choice = input()
    return choice

#Helper function for player to play their cards onto the table.
def meldOrLay(player, choice):
    if(choice == 1):
        viewHand(player)
        #Get players choice for cards to meld. Split into an array of numbers and then iterate through them and add those cards to the table meld.
        print("What cards would you like to play as a meld (input the numbers separated by a comma (,) for the cards you wish to play eg. 1, 2, 4): ")
        cards = str(input())
        cards = [x.strip() for x in cards.split(",")] #Strip whitespace and split on commas to create list of numbers
        meld = []
        for num in cards:
            meld.append(player.hand[int(num)]) #Add the cards in the player's hand to the meld array.
        #Check if the meld is valid.
        if(isValidMeld(meld) == True):
            pass
        else:
            print("The cards you have selected are invalid. Please try again.")
    elif(choice == 2):
        pass
    else:
        pass

#Checks to see if the meld is valid.
def isValidMeld(meld):
    value0 = meld[0].value
    suit0 = meld[0].suit
    for card in meld:
        if(card.suit != suit0):
            return False
    return True

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
    round(players, dealNumber, packNumber)

    #Check if any player has exceeded the score.




if __name__ == "__main__": main()
