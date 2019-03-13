import random

class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return 'SUIT: {} VALUE: {}'.format(self.suit, self.value)

class Deck(object):
    deck = []
    def __init__(self):
        self.createDeck()

    def createDeck(self):
        suits = ['spade', 'heart', 'club', 'diamond']
        for suit in suits:
            for value in range(2,15):
                self.deck.append(Card(suit, value))
    
    def __str__(self):
        return 'cards in deck: {}'.format(len(self.deck))

    def Deal(self, numOfCards):
        dealt = []
        for i in range(numOfCards):
            index = random.randint(0,len(self.deck) - 1)
            dealt.append(self.deck.pop(index))
        return dealt

class Player(object):
    hand = []
    def __init__(self, name, deckObject):
        self.name = name
        self.deckObject = deckObject

    def add(self, numOfCards):
        addCards = self.deckObject.Deal(numOfCards)
        for card in addCards:
            print card
            self.hand.append(card)

    def __str__(self):
        for card in self.hand:
            print card

ourDeck = Deck()
print ourDeck
ourDeck.Deal(3)
print ourDeck
jim = Player('jim', ourDeck)
jim.add(3)
print jim