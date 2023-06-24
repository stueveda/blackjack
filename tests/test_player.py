import unittest
import blackjack.constants as constants, blackjack.player as player

class TestPlayer(unittest.TestCase):
    def test_player(self):
        pass

if __name__ == '__main__':
    p = player.Player(1)

    assert p.get_id() == 1

    p.set_bet(10)
    assert p.get_bet() == 10
    assert p.get_funds() == -10
    p.set_bet(5)
    assert p.get_bet() == 5
    assert p.get_funds() == -15
    p.add_funds(20)
    assert p.get_funds() == 5

    # test various cards to see if they evaluate correctly
    assert p.evaluate_hand() == (0, 0)
    p.add_card("2")
    assert p.evaluate_hand() == (2, 0)
    p.add_card("3")
    assert p.evaluate_hand() == (5, 0)
    p.add_card("3")
    assert p.evaluate_hand() == (8, 0)
    p.add_card("10")
    assert p.evaluate_hand() == (18, 0)
    p.add_card("J")
    assert p.evaluate_hand() == (28, 0)
    p.add_card("Q")
    assert p.evaluate_hand() == (38, 0)
    p.add_card("K")
    assert p.evaluate_hand() == (48, 0)

    p.reset_hand()
    assert p.evaluate_hand() == (0, 0)
    
    # Test Aces
    p.add_card("A")
    assert p.evaluate_hand() == (11, 1)
    p.add_card("A")
    assert p.evaluate_hand() == (12, 1)
    p.add_card("2")
    assert p.evaluate_hand() == (14, 1)
    p.add_card("5")
    assert p.evaluate_hand() == (19, 1)
    p.add_card("K")
    assert p.evaluate_hand() == (19, 0)
