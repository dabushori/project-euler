"""
Challenge 53 of project euler - Combinatoric Selections

@author Ori Dabush
"""

from math import comb


N_LOWER_LIMIT, N_UPPER_LIMIT = 1, 100
COMPARED_VALUE = 1_000_000


def solve():
    """
    This problem can be very optimized, but this is not necessary as these are small numbers.
    """
    result = 0
    for n in range(N_LOWER_LIMIT, N_UPPER_LIMIT + 1):
        for r in range(n + 1):
            if comb(n, r) > COMPARED_VALUE:
                result += 1
    return result


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
