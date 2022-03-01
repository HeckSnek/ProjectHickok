class HandBlackjack:
    def __init__(self):
        self.cards = []
        self.total = 0
        self.soft = False
        self.bust = False
    
    def hit (self, card):
        if card.value == 1:
            if (self.total + 11) <= 21:
                self.soft = True
                self.total += 11
            else:
                self.soft = False
                self.total += 1
        elif card.value == 11 or card.value == 12 or card.value == 13:
            self.soft = False
            self.total += 10
        else:
            self.soft = False
            self.total += card.value
        self.cards.append(card)