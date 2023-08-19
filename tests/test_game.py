import unittest
import blackjack.constants as constants
import blackjack.game as game
import blackjack.player as player
import blackjack.dealer as dealer

class TestGame(unittest.TestCase):
    def test_game(self):
        pass

if __name__ == '__main__':
    players = [player.Player(1),
               player.Player(2, constants.BOOK_NO_DOUBLES_HARD,
                                constants.BOOK_NO_DOUBLES_SOFT,
                                constants.BOOK_NO_DOUBLES_SPLITS)]
    num_decks = 5
    g = game.Game(players, num_decks)

    assert len(g.players) == 2
    assert g.num_decks == num_decks
    assert len(g.deck) == 52 * num_decks
    assert g.round_number == 0