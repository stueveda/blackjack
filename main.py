import game, logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING)
    num_players = 3
    num_decks = 4
    g = game.Game(num_players, num_decks)
    for i in range(10000):
        g.play_round()
    g.print_stats()