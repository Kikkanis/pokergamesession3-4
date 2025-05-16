"This script simulates 5-card poker hands to estimate the probability of drawing a straight.
"It defines a Hand class to evaluate hand types such as flush, full house, and straight.
"Each hand is dealt from a freshly shuffled standard deck.
"The simulation continues until a straight is found or a max limit is reached.

from deck import Deck, Card

class Hand:
    def __init__(self, deck):
        cards = []
        for i in range(5):
            cards.append(deck.deal())
        self._cards = cards

    @property
    def cards(self):
        return self._cards


    def __str__(self):
        return str(self.cards)

    @property
    def is_flush(self):
        for card in self.cards[1:]:
            if self.cards[0].suit != card.suit:
                return False
            return True

while True:
    deck = Deck()
    deck.shuffle()
    hand = Hand(deck)
    if hand.is_flush:
        print(hand)
        break
