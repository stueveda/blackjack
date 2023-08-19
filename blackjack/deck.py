import random
import blackjack.constants as constants

class Deck:
    def __init__(self):
        self.cards = []
    
    def draw(self):
        return self.cards.pop() if self.cards else None

    def peek(self):
        return self.cards[-1] if self.cards else None

    def shuffle(self):
        random.shuffle(self.cards)

    def count(self):
        return len(self.cards)

    def empty_deck(self):
        self.cards = []

    def add_cards(self, new_cards):
        self.cards.extend(new_cards)

    def __len__(self):
        return len(self.cards)