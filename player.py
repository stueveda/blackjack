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
        dlr_total = constants.CARD_VALUES[dealer_card]
        
        if total > 21:
            action = 'B'
        # handle hard totals
        elif soft_aces == 0:
            if total >= 17 or \
            (total >= 13 and dlr_total <= 6) or \
            (total == 12 and dlr_total in [4, 5, 6]):
                action = 'S'
            elif total == 11 or \
            (total == 10 and dlr_total < 10) or \
            (total == 9 and dlr_total in [3, 4, 5, 6]):
                action = 'D'
            else:
                action = 'H'
        # handle soft totals
        else:
            if total >= 20 or \
            (total == 19 and dlr_total != 6) or \
            (total == 18 and dlr_total in [7, 8]):
                action = 'S'
            elif (total == 19 and dlr_total == 6) or \
            (total == 18 and dlr_total <= 6) or \
            (total == 17 and dlr_total in [3, 4, 5, 6] or \
            (total in [15, 16] and dlr_total in [4, 5, 6]) or \
            (total in [13, 14] and dlr_total in [5, 6])):
                action = 'D'
            else:
                action = 'H'
        logging.debug(action)
        return action




if __name__ == '__main__':
    pass