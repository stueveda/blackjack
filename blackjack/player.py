import logging
import blackjack.constants as constants

class Player:
    def __init__(self, id,
                 book_hard=constants.BOOK_STANDARD_HARD,
                 book_soft=constants.BOOK_STANDARD_SOFT,
                 book_splits=constants.BOOK_STANDARD_SPLITS):
        self.id = id
        self.book_hard = book_hard
        self.book_soft = book_soft
        self.book_splits = book_splits
        self.hand = []
        self.funds = 0
        self.bet = 0
        self.round_resolved = False
        self.wins = 0
        self.losses = 0
        self.pushes = 0
        self.blackjacks = 0

    def get_id(self):
        return self.id

    def get_bet(self):
        return self.bet

    def set_bet(self, amount):
        self.funds -= amount
        self.bet = amount
    
    def get_funds(self):
        return self.funds
    
    def add_funds(self, amount):
        self.funds += amount

    def reset_round(self):
        self.hand = []
        self.bet = 0
        self.round_resolved = False

    def add_card(self, card):
        self.hand.append(card)

    def reset_hand(self):
        self.hand = []
    
    def print_hand(self):
        total, soft_aces = self.evaluate_hand()
        logging.debug("{} {}{}".format(self.hand, "S" * soft_aces, total))

    def has_blackjack(self):
        return len(self.hand) == 2 and \
            (self.hand[0] == 'A' and self.hand[1] in ['10', 'J', 'Q', 'K']) or \
            (self.hand[0] in ['10', 'J', 'Q', 'K'] and self.hand[1] == 'A')

    def can_split(self):
        return len(self.hand) == 2 and self.hand[0] == self.hand[1]

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
        else:
            if self.can_split():
                # TODO: implement splitting
                #action = self.book_splits[self.hand[0], dlr_total]
                action = self.book_hard[total][dlr_total]
            elif soft_aces == 1:
                # subtract 11 (value of an A) to get correct row
                action = self.book_soft[total - 11][dlr_total]
            else:
                action = self.book_hard[total][dlr_total]

        logging.debug(action)
        return action

if __name__ == '__main__':
    pass