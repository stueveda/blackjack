CARD_VALUES = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11,
}

STANDARD_DECK = [
    "2","2","2","2",
    "3","3","3","3",
    "4","4","4","4",
    "5","5","5","5",
    "6","6","6","6",
    "7","7","7","7",
    "8","8","8","8",
    "9","9","9","9",
    "10","10","10","10",
    "J","J","J","J",
    "Q","Q","Q","Q",
    "K","K","K","K",
    "A","A","A","A"
]

# TODO: find an implementation of a book that I like.

# Book refers to the action a player takes based on their
# hand and the dealer's showing card
# the 2-D matrix represents the player's hand total as the row index,
# and the dealer's total as the column index.
# e.g. player hand = [3, 7], dealer card = 6 ====> row 10, col 6
# note - the matrix is zero-indexed, thus the first two rows
# and first column of each row will have not have a
# usable action (denoted 'X')

BOOK_STANDARD_HARD = [
    # 0    1    2    3    4    5    6    7    8    9    10   A
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], # 0
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], # 1
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], # 2
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], # 3
    ['X', 'X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], # 4
    ['X', 'X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], # 5
    ['X', 'X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], # 6
    ['X', 'X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], # 7
    ['X', 'X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], # 8
    ['X', 'X', 'H', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H'], # 9
    ['X', 'X', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'H', 'H'], # 10
    ['X', 'X', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D'], # 11
    ['X', 'X', 'H', 'H', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'], # 12
    ['X', 'X', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'], # 13
    ['X', 'X', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'], # 14
    ['X', 'X', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'], # 15
    ['X', 'X', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'], # 16
    ['X', 'X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'], # 17
    ['X', 'X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'], # 18
    ['X', 'X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'], # 19
    ['X', 'X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'], # 20
    ['X', 'X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']  # 21
]

# Soft books are indexed on row by the card accomapnying the Ace,
# and indexed on column by the dealer's card.
# e.g. [A, 7] Vs dealer 4 = row 7, col 4

BOOK_STANDARD_SOFT = [
    # 0    1    2    3    4    5    6    7    8    9   10    A
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], # A A
    ['X', 'X', 'H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H', 'H'], # A 2
    ['X', 'X', 'H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H', 'H'], # A 3
    ['X', 'X', 'H', 'H', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H'], # A 4
    ['X', 'X', 'H', 'H', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H'], # A 5
    ['X', 'X', 'H', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H'], # A 6
    ['X', 'X', 'D', 'D', 'D', 'D', 'D', 'S', 'S', 'H', 'H', 'H'], # A 7
    ['X', 'X', 'S', 'S', 'S', 'S', 'D', 'S', 'S', 'S', 'S', 'S'], # A 8
    ['X', 'X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'], # A 9
    ['X', 'X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']  # A 10
]

BOOK_STANDARD_SPLITS = [
    # 0    1     2     3     4     5     6     7     8     9    10     A
    ['X', 'X',  'X',  'X',  'X',  'X',  'X',  'X',  'X',  'X',  'X' , 'X' ],
    ['X', 'X',  'Sp', 'Sp', 'Sp', 'Sp', 'Sp', 'Sp', 'Sp', 'Sp', 'Sp', 'Sp'], # A A
    ['X', 'X',  'Sp', 'Sp', 'Sp', 'Sp', 'Sp', 'H',  'H',  'H',  'H' , 'H' ], # 2 2
    ['X', 'X',  'Sp', 'Sp', 'Sp', 'Sp', 'Sp', 'H',  'H',  'H',  'H' , 'H' ], # 3 3
    ['X', 'X',  'H',  'H',  'H',  'Sp', 'Sp', 'H',  'H',  'H',  'H' , 'H' ], # 4 4
    ['X', 'X',  'D',  'D',  'D',  'D',  'D',  'D',  'D',  'D',  'H' , 'H' ], # 5 5
    ['X', 'X',  'Sp', 'Sp', 'Sp', 'Sp', 'H',  'H',  'H',  'H',  'H' , 'H' ], # 6 6
    ['X', 'X',  'Sp', 'Sp', 'Sp', 'Sp', 'Sp', 'Sp', 'H',  'H',  'H' , 'H' ], # 7 7
    ['X', 'X',  'Sp', 'Sp', 'Sp', 'Sp', 'Sp', 'Sp', 'Sp', 'Sp', 'Sp', 'Sp'], # 8 8
    ['X', 'X',  'Sp', 'Sp', 'Sp', 'Sp', 'Sp', 'S',  'Sp', 'Sp', 'S' , 'S' ], # 9 9
    ['X', 'X',  'S',  'S',  'S',  'S',  'S',  'S',  'S',  'S',  'S' , 'S' ]  # 10 10
]




BOOK_NO_DOUBLES_HARD = [
    # 0    1    2    3    4    5    6    7    8    9    10   A
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], # 0
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], # 1
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], # 2
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], # 3
    ['X', 'X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], # 4
    ['X', 'X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], # 5
    ['X', 'X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], # 6
    ['X', 'X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], # 7
    ['X', 'X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], # 8
    ['X', 'X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], # 9
    ['X', 'X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], # 10
    ['X', 'X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], # 11
    ['X', 'X', 'H', 'H', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'], # 12
    ['X', 'X', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'], # 13
    ['X', 'X', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'], # 14
    ['X', 'X', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'], # 15
    ['X', 'X', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'], # 16
    ['X', 'X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'], # 17
    ['X', 'X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'], # 18
    ['X', 'X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'], # 19
    ['X', 'X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'], # 20
    ['X', 'X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']  # 21
]

BOOK_NO_DOUBLES_SOFT = [
    # 0    1    2    3    4    5    6    7    8    9   10    A
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], # A A
    ['X', 'X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], # A 2
    ['X', 'X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], # A 3
    ['X', 'X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], # A 4
    ['X', 'X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], # A 5
    ['X', 'X', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], # A 6
    ['X', 'X', 'H', 'H', 'H', 'H', 'H', 'S', 'S', 'H', 'H', 'H'], # A 7
    ['X', 'X', 'S', 'S', 'S', 'S', 'H', 'S', 'S', 'S', 'S', 'S'], # A 8
    ['X', 'X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'], # A 9
    ['X', 'X', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']  # A 10
]

BOOK_NO_DOUBLES_SPLITS = [
    # 0    1     2     3     4     5     6     7     8     9    10     A
    ['X', 'X',  'X',  'X',  'X',  'X',  'X',  'X',  'X',  'X',  'X' , 'X' ],
    ['X', 'X',  'Sp', 'Sp', 'Sp', 'Sp', 'Sp', 'Sp', 'Sp', 'Sp', 'Sp', 'Sp'], # A A
    ['X', 'X',  'Sp', 'Sp', 'Sp', 'Sp', 'Sp', 'H',  'H',  'H',  'H' , 'H' ], # 2 2
    ['X', 'X',  'Sp', 'Sp', 'Sp', 'Sp', 'Sp', 'H',  'H',  'H',  'H' , 'H' ], # 3 3
    ['X', 'X',  'H',  'H',  'H',  'Sp', 'Sp', 'H',  'H',  'H',  'H' , 'H' ], # 4 4
    ['X', 'X',  'H',  'H',  'H',  'H',  'H',  'H',  'H',  'H',  'H' , 'H' ], # 5 5
    ['X', 'X',  'Sp', 'Sp', 'Sp', 'Sp', 'H',  'H',  'H',  'H',  'H' , 'H' ], # 6 6
    ['X', 'X',  'Sp', 'Sp', 'Sp', 'Sp', 'Sp', 'Sp', 'H',  'H',  'H' , 'H' ], # 7 7
    ['X', 'X',  'Sp', 'Sp', 'Sp', 'Sp', 'Sp', 'Sp', 'Sp', 'Sp', 'Sp', 'Sp'], # 8 8
    ['X', 'X',  'Sp', 'Sp', 'Sp', 'Sp', 'Sp', 'S',  'Sp', 'Sp', 'S' , 'S' ], # 9 9
    ['X', 'X',  'S',  'S',  'S',  'S',  'S',  'S',  'S',  'S',  'S' , 'S' ]  # 10 10
]