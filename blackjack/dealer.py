import logging
import blackjack.constants as constants, blackjack.player as player

class Dealer(player.Player):
    
    def pick_action(self, dealer_card=None):
        # return the action to take based on the current hand and ruleset
        action = None
        total = sum(constants.CARD_VALUES[c] for c in self.hand)
        # determine the number of soft aces in hand
        soft_aces = self.hand.count('A')
        while soft_aces > 0 and total > 21:
            total -= 10
            soft_aces -= 1
        
        if total > 21:
            action = 'B'
        # handle hard totals
        elif soft_aces == 0:
            if total < 17:
                action = 'H'
            else:
                action = 'S'
        # handle soft totals
        else:
            if total <= 17:
                action = 'H'
            else:
                action = 'S'
        logging.debug(action)
        return action