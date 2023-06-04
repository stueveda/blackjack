import unittest
import blackjack.constants as constants, blackjack.deck as deck

class TestDeck(unittest.TestCase):
    def test_deck(self):
        pass

if __name__ == '__main__':
    d = deck.Deck()

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