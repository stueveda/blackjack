import logging
import blackjack.constants as constants
import blackjack.player as player
import blackjack.game as game

if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING)
    players = [player.Player(1),
               player.Player(2, constants.BOOK_NO_DOUBLES_HARD,
                                constants.BOOK_NO_DOUBLES_SOFT,
                                constants.BOOK_NO_DOUBLES_SPLITS)]
    num_decks = 5
    g = game.Game(players, num_decks)
    for i in range(100000):
        g.play_round()
    g.print_stats()