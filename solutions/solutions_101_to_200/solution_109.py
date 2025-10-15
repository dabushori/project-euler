"""
Challenge 109 of project euler - Darts

@author Ori Dabush
"""

from dataclasses import dataclass

MULTIPLIER_TO_STR = {
    0: '',
    1: 'S',
    2: 'D',
    3: 'T'
}

@dataclass
class Dart:
    raw_value: int
    multiplier: int

    def value(self):
        return self.multiplier * self.raw_value
    
    def is_zero(self):
        return self.value == 0
    
    def __eq__(self, other):
        return str(self) == str(other)
    
    def __hash__(self):
        return str(self)
    
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return f'{MULTIPLIER_TO_STR[self.multiplier]}{self.raw_value}'

CIRCLE_VALUES = list(range(1, 21))
BULL_VALUE = [25]
POSSIBLE_DART_VALUES_X1 = [Dart(i, 1) for i in CIRCLE_VALUES + BULL_VALUE]
POSSIBLE_DART_VALUES_X2 = [Dart(i, 2) for i in CIRCLE_VALUES + BULL_VALUE]
POSSIBLE_DART_VALUES_X3 = [Dart(i, 3) for i in CIRCLE_VALUES]
ZERO_DART = Dart(0, 0)

class Checkout:
    def __init__(self, *darts):
        self.darts = darts
    
    def __eq__(self, other):
        return self.darts == other.darts or (
            len(self.darts) == 3 and len(other.darts) == 3 and (
                (self.darts[1], self.darts[0], self.darts[2]) == (other.darts[0], other.darts[1], other.darts[2])
            )
        )
    
    def __hash__(self):
        return hash(''.join(sorted(str(d) for d in self.darts)))
    
    def sum(self):
        return sum(d.value() for d in self.darts)
    
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return str(self.darts)

MAXIMAL_CHECKOUT_SUM = 100

def solve():
    possible_checkouts = set()
    for last_dart in POSSIBLE_DART_VALUES_X2:
        # 1 dart checkouts
        possible_checkouts.add(Checkout(last_dart))
        # 2 darts checkouts
        for first_dart in POSSIBLE_DART_VALUES_X1 + POSSIBLE_DART_VALUES_X2 + POSSIBLE_DART_VALUES_X3:
            possible_checkouts.add(Checkout(first_dart, last_dart))
        # 3 darts checkouts
        for first_dart in POSSIBLE_DART_VALUES_X1 + POSSIBLE_DART_VALUES_X2 + POSSIBLE_DART_VALUES_X3:
            for second_dart in POSSIBLE_DART_VALUES_X1 + POSSIBLE_DART_VALUES_X2 + POSSIBLE_DART_VALUES_X3:
                possible_checkouts.add(Checkout(first_dart, second_dart, last_dart))
    # possible_checkouts contains all the possible checkouts, so get what we need
    return len([checkout for checkout in possible_checkouts if checkout.sum() < MAXIMAL_CHECKOUT_SUM])


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
