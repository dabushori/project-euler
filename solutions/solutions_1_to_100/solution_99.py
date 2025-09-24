"""
Challenge 99 of project euler - Largest Exponential

@author Ori Dabush
"""

from math import log10
from solutions.utils.inputs import get_input


def solve():
    """
    b1 ** e1 < b2 ** e2 <==> log10(b1 ** e1) < log10(b2 ** e2) <==> e1 * log10(b1) < e2 * log10(b2)
    """
    pairs = [tuple(map(int, line.split(','))) for line in get_input(99).split()]
    values = [exponent * log10(base) for idx, (base, exponent) in enumerate(pairs)]
    return max(range(len(pairs)), key=values.__getitem__) + 1  # The indexes are 1-based


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
