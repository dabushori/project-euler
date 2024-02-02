"""
Challenge 73 of project euler - Counting Fractions in a Range

@author Ori Dabush
"""

from math import ceil, floor, gcd
from fractions import Fraction


MIN_D_VALUE = 2
MAX_D_VALUE = 12000
RANGE_MIN = Fraction(1, 3)
RANGE_MAX = Fraction(1, 2)


def solve():
    count = 0
    for d in range(MIN_D_VALUE, MAX_D_VALUE + 1):
        # Count all the reduced proper fractions in (RANGE_MIN, RANGE_MAX) which d is their denominator.
        min_n = floor(d * RANGE_MIN + 1)
        max_n = ceil(d * RANGE_MAX - 1)
        count += len([n for n in range(min_n, max_n + 1) if gcd(n, d) == 1])
    return count


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
