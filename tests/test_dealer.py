import unittest
import blackjack.constants as constants, blackjack.dealer as dealer

class TestPlayer(unittest.TestCase):
    def test_player(self):
        pass

if __name__ == '__main__':
    d = dealer.Dealer(1)

    assert d.get_id() == 1

    # test various cards to see if they evaluate correctly
    assert d.evaluate_hand() == (0, 0)
    assert d.pick_action() == 'H'

    d.add_card("2")
    assert d.evaluate_hand() == (2, 0)
    assert d.pick_action() == 'H'

    d.add_card("3")
    assert d.evaluate_hand() == (5, 0)
    assert d.pick_action() == 'H'

    d.add_card("3")
    assert d.evaluate_hand() == (8, 0)
    assert d.pick_action() == 'H'

    d.add_card("10")
    assert d.evaluate_hand() == (18, 0)
    assert d.pick_action() == 'S'

    d.add_card("J")
    assert d.evaluate_hand() == (28, 0)
    assert d.pick_action() == 'B'

    d.add_card("Q")
    assert d.evaluate_hand() == (38, 0)
    assert d.pick_action() == 'B'

    d.add_card("K")
    assert d.evaluate_hand() == (48, 0)
    assert d.pick_action() == 'B'

    d.reset_hand()
    assert d.evaluate_hand() == (0, 0)
    assert d.pick_action() == 'H'
    
    # Test Aces
    d.add_card("A")
    assert d.evaluate_hand() == (11, 1)
    assert d.pick_action() == 'H'

    d.add_card("A")
    assert d.evaluate_hand() == (12, 1)
    assert d.pick_action() == 'H'

    d.add_card("2")
    assert d.evaluate_hand() == (14, 1)
    assert d.pick_action() == 'H'

    d.add_card("5")
    assert d.evaluate_hand() == (19, 1)
    assert d.pick_action() == 'S'

    d.add_card("K")
    assert d.evaluate_hand() == (19, 0)
    assert d.pick_action() == 'S'
