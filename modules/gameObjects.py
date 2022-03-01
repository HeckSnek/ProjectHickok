import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

class Deck:
        def __init__(self, count):
                self.count = count
                cards = []
                #Number of Decks in Play
                for x in range (count):
                        #Suits
                        for y in range (4):
                                #Card Value
                                for z in range (1,14):
                                        cards.append(Card(z,y))
                random.shuffle(cards) #Randomize Card Order
                self.cards = cards

d = Deck(8)
for card in d.cards:
        print(str(card.value)+" "+str(card.suit))