import random

#Class for each card in the deck. Contains a suit ("Clubs", "Diamonds", "Spades", "Hearts") and a value (1, 2, 3, 4, Jack, Queen etc.) attriubte.
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


def main():
    play = wantToPlay()
    while(play == True):

        #Print introductory message.
        printIntro()

        #Create deck (from list of card objects).
        deck = newDeck()


        #Players turn, returns the total value of player's hand as an integer. All turn logic takes place during the player function.
        print(len(deck))
        player = playerTurn(deck)
        #Immediately call final score function if player score is over 21.

        #Dealer's turn, returns the total value of the dealer's hand as an integer. All turn logic takes place during the dealer function.
        print("")
        print("Now it's the dealer's turn!")
        dealer = dealerTurn(deck)

        #Compare scores and determine a winner.
        finalResult(player, dealer)


        #Ask user if they want to play again.
        play = wantToPlay()


#Establishes whether or not the player wants to play. Returns True or False.
def wantToPlay():
    value = input("Do you want to play Blackjack? (Y/N)")
    if(value == "Y" or value == "y"):
        return True
    elif(value == "N" or value == "n"):
        return False
    else:
        print("Please restart the game and enter either y or n")
        return False

#Intro message printed to console explaining th game.
def printIntro():
        print("Welcome to Blackjack!")
        print("This is a popular casino game where the objective is to get as close to the number 21 as possible with the value of your cards. If you go over 21, you're bust!")
        print("You will go first and then the dealer will go second.")
        print("An Ace is worth either 1 or 11. Picture cards are worth 10 each.")
        print("Good luck, and have fun!")
        print("")
        print("")

#Returns True or False depending on whether or not the player wants to draw another card.
def hitOrStick():
    value = input("Do you want to hit or stick? (Y/N)")
    if(value == "Y" or value == "y"):
        return True
    elif(value == "N" or value == "n"):
        return False
    else:
        print("Please input Y or N.")

#Creates a new deck using a nested loop. Creates a card of each value for each suit and returns a list of objects.
def newDeck():

    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
    #deck = [Card(value, suit) for value in range(1, 14) for suit in suits]
    deck = []

    for i in suits:
        for j in values:
            deck.append(Card(j, i))
    random.shuffle(deck)
    return deck

#Evaluates the score of a hand.
def evalHand(hand):
    playerCount = 0
    print("Hand contains:")
    for card in hand:
        if(card.value == "King" or card.value == "Jack" or card.value == "Queen"):
            playerCount += 10
        elif(card.value == "Ace"):
            if(playerCount + 11 > 21):
                playerCount += 1
            else:
                playerCount += 11
        else:
            playerCount += card.value
        print(str(card.value)  + " of " + str(card.suit))
    print("")
    print("The total value is: " + str(playerCount))
    print("")

    return playerCount

#Function for the player's turn. Appends two cards and evaluates hand to start. Player then can choose to hit or stick. Returns an integer which is the player's score.
def playerTurn(deck):
    hand = []
    while(len(hand) < 2):
        hand.append(deck.pop())
    playerCount = evalHand(hand)
    hit = hitOrStick()
    while(hit == True):
        hand.append(deck.pop())
        playerCount = evalHand(hand)
        if(playerCount > 21):
            print("Bust! You lose!")
            quit()
        hit = hitOrStick()
    return playerCount

#Dealer turn. Dealer logic is set to always draw as long as the value is less than 17 (16 or lower). Returns an integer which is the dealer's score.
def dealerTurn(deck):
    hand = []
    dealerCount = 0
    while(len(hand) < 2):
        hand.append(deck.pop())
    dealerCount = evalHand(hand)
    while(dealerCount < 17):
        hand.append(deck.pop())
        dealerCount = evalHand(hand)
        if(dealerCount > 21):
            print("The house went bust! You win!")
            quit()
    return dealerCount

#Prints final result.
def finalResult(playerScore, dealerScore):
    if(playerScore > dealerScore):
        print("You won!")
        print("Your score was: " + str(playerScore))
        print("The house's score was: " + str(dealerScore))
    elif(dealerScore > playerScore):
        print("Bad luck, the house won!")
        print("Your score was: " + str(playerScore))
        print("The house's score was: " + str(dealerScore))
    else:
        print("It's a draw!")
        print("Your score was: " + str(playerScore))
        print("The house's score was: " + str(dealerScore))

if __name__ == "__main__": main()
