import constants, dealer, deck, logging, player

class Game:
    def __init__(self, num_players, num_decks):
        self.dealer = dealer.Dealer(0)
        self.players = [player.Player(i + 1) for i in range(num_players)]
        self.num_decks = num_decks
        self.deck = deck.Deck()
        self.running_count = 0
        self.round_number = 0

    def refresh_deck(self):
        self.deck.empty_deck()
        for _ in range(self.num_decks):
            self.deck.add_cards(constants.STANDARD_DECK)
        self.deck.shuffle()
    
    def deal_cards(self):
        for _ in range(2):
            for plr in self.players:
                plr.hand.append(self.deck.draw())
            self.dealer.hand.append(self.deck.draw())

    def evaluate_blackjacks(self):
        dealer_blackjack = self.dealer.has_blackjack()
        if dealer_blackjack:
            logging.debug('dealer blackjack')
        for plr in self.players:
            if plr.has_blackjack():
                logging.debug('player blackjack')
                if not dealer_blackjack:
                    plr.add_funds(plr.bet * 2.5)
                    plr.wins += 1
                else:
                    plr.pushes += 1
                plr.round_resolved = True
                plr.blackjacks += 1
            elif dealer_blackjack:
                plr.round_resolved = True
                plr.losses += 1
        
    def play_hand(self, plr, dealer_card=None):
        plr.print_hand()
        action = plr.pick_action(dealer_card)
        while action not in ['B', 'S', 'D']:
            plr.hand.append(self.deck.draw())
            plr.print_hand()
            action = plr.pick_action(dealer_card)
        if action == 'D':
            plr.add_funds(plr.bet)
            plr.set_bet(plr.bet * 2)
            plr.hand.append(self.deck.draw())
            plr.print_hand()

    def play_round(self):
        self.round_number += 1
        logging.debug('--------------- ROUND {} ----------------'.format(self.round_number))
        if self.deck.count() < (self.num_decks * 52 // 5):
            logging.debug('Refreshing Deck')
            self.refresh_deck()
        
        for plr in self.players:
            plr.set_bet(1)
        
        self.deal_cards()
        logging.debug('Dealer card: {}'.format(self.dealer.hand[0]))
        for plr in self.players:
            logging.debug("Player {}".format(plr.get_id()))
            plr.print_hand()
        
        self.evaluate_blackjacks()
        
        # play each player's hand in order
        for plr in self.players:
            if not plr.round_resolved:
                logging.debug('Player {} is playing'.format(plr.get_id()))
                self.play_hand(plr, self.dealer.hand[0])
        logging.debug('dealer is playing')
        self.play_hand(self.dealer)
        
        # evaluate hands and settle bets
        logging.debug("evaluating hands")
        dlr_total = self.dealer.evaluate_hand()[0]
        for plr in self.players:
            plr_total = plr.evaluate_hand()[0]
            if plr_total > 21:
                logging.debug("player {} busted! {}".format(plr.get_id(), plr_total))
                plr.losses += 1
            if plr_total <= 21 and not plr.round_resolved:
                if (dlr_total > 21 or plr_total > dlr_total):
                    logging.debug("player {} wins! {} - {}".format(plr.get_id(), plr_total, dlr_total))
                    plr.add_funds(plr.bet * 2)
                    plr.wins += 1
                elif plr_total == dlr_total:
                    logging.debug("player {} pushes! {} - {}".format(plr.get_id(), plr_total, dlr_total))
                    plr.add_funds(plr.bet)
                    plr.pushes += 1
                elif plr_total < dlr_total:
                    logging.debug("player {} loses! {} - {}".format(plr.get_id(), plr_total, dlr_total))
                    plr.losses += 1

        # reset all players
        for plr in self.players:
            plr.reset_round()
        self.dealer.reset_round()

    def print_stats(self):
        print('Rounds played: {}'.format(self.round_number))
        for plr in self.players:
            print('Player {} | Funds: {} | Record: {}-{}-{} | {} BJ'.format(plr.get_id(), plr.funds,
                                                                            plr.wins, plr.losses, plr.pushes,
                                                                            plr.blackjacks))