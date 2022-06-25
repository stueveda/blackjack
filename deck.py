import constants, random

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


if __name__ == '__main__':
    d = Deck()

    assert d.count() == 0
    assert not d.peek()
    assert not d.draw()
    
    d.add_cards('A')
    assert d.count() == 1
    assert d.peek() == 'A'
    assert d.draw() == 'A'
    assert d.count() == 0

    d.add_cards(constants.STANDARD_DECK)
    assert d.count() == 52
    assert d.peek()
    assert d.draw()
    assert d.count() == 51
    d.empty_deck()
    assert d.count() == 0