import logging, time
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
    num_rounds = 100000
    g = game.Game(players, num_decks)
    logging.info("starting simulation of {} rounds".format(num_rounds))
    simulation_start_time = time.time()
    for i in range(num_rounds):
        g.play_round()
        if i % 100000 == 0:
            logging.info("{} rounds played".format(i))
    logging.info("time elapsed: {:.2f} seconds".format(time.time() - simulation_start_time))
    g.print_stats()