"""
Challenge 26 of project euler - Reciprocal Cycles

@author Ori Dabush
"""

from utils.decimal_representation import get_recurring_cycle


UPPER_LIMIT = 1000


def solve():
    return max(range(1, UPPER_LIMIT), key=lambda d: get_recurring_cycle(1, d)[1])


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
