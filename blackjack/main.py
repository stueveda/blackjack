import logging
import blackjack.game as game

if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING)
    num_players = 3
    num_decks = 5
    g = game.Game(num_players, num_decks)
    for i in range(100000):
        g.play_round()
    g.print_stats()