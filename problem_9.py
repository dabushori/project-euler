"""
Challenge 9 of project euler - Special Pythagorean Triplet

@author Ori Dabush
"""
from itertools import product


SUM_OF_TRIPLET = 1000


def solve():
    """
    we want a < b < c where:
    1. a + b + c = 1000
    2. a**2 + b**2 = c**2

    from 1 we get:
    c = 1000 - a - b

    which means:
    a**2 + b**2 = (1000 - a - b)**2
    a**2 + b**2 = a**2 + 2ab - 2000a + b**2 - 2000b + 1000000
    2ab - 2000a - 2000b + 1000000 = 0

    we know that a, b, c > 0, so a, b ,c < 1000
    """
    for a, b in product(range(1, SUM_OF_TRIPLET), range(1, SUM_OF_TRIPLET)):
        if 2 * a * b - 2000 * a - 2000 * b + 1000000 == 0:
            c = int((a ** 2 + b ** 2) ** 0.5)
            return a * b * c


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
