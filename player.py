import constants, logging

class Player:
    def __init__(self, id):
        self.id = id
        self.hand = []
        self.funds = 0
        self.bet = 0
        self.round_resolved = False
        self.wins = 0
        self.losses = 0
        self.pushes = 0
        self.blackjacks = 0

    def has_blackjack(self):
        return len(self.hand) == 2 and \
            (self.hand[0] == 'A' and self.hand[1] in ['J', 'Q', 'K']) or \
            (self.hand[0] in ['J', 'Q', 'K'] and self.hand[1] == 'A')

    def add_funds(self, amount):
        self.funds += amount

    def reset_round(self):
        self.hand = []
        self.bet = 0
        self.round_resolved = False

    def set_bet(self, amount):
        self.funds -= amount
        self.bet = amount

    def get_id(self):
        return self.id

    def get_bet(self):
        return self.bet
    
    def print_hand(self):
        total, soft_aces = self.evaluate_hand()
        logging.debug("{} {}{}".format(self.hand, "S" * soft_aces, total))

    def evaluate_hand(self):
        # returns a tuple of (hand_value, # of remaining soft aces)
        total = sum(constants.CARD_VALUES[c] for c in self.hand)
        # determine the number of soft aces in hand
        soft_aces = self.hand.count('A')
        while soft_aces > 0 and total > 21:
            total -= 10
            soft_aces -= 1
        return (total, soft_aces)

    def pick_action(self, dealer_card):
        # return which action to take based on the current hand and ruleset
        action = None
        total, soft_aces = self.evaluate_hand()
        
        if total > 21:
            action = 'B'
        # handle hard totals
        elif soft_aces == 0:
            if total >= 17:
                action = 'S'
            elif total >= 13 and constants.CARD_VALUES[dealer_card] <= 6:
                action = 'S'
            elif total == 12 and constants.CARD_VALUES[dealer_card] in [4, 5, 6]:
                action = 'S'
            else:
                action = 'H'
        # handle soft totals
        else:
            if total >= 19:
                action = 'S'
            elif total >= 18 and constants.CARD_VALUES[dealer_card] <= 8:
                action = 'S'
            else:
                action = 'H'
        logging.debug(action)
        return action




if __name__ == '__main__':
    pass