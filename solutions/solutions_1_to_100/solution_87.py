"""
Challenge 87 of project euler - Prime Power Triples

@author Ori Dabush
"""

from solutions.utils.primes import prime_numbers_until_with_space
from math import ceil, sqrt
from itertools import product


MAX_SUM = 50_000_000


def solve():
    """
    We know that:
    p**2 + q**3 + r**4 <= MAX_SUM

    so we can derive that the primes we will use will be less than sqrt(MAX_SUM).
    """
    numbers = set()
    primes = set(prime_numbers_until_with_space(ceil(sqrt(MAX_SUM))))
    squares = [p**2 for p in primes]
    cubes = [p**3 for p in primes]
    fourths = [p**4 for p in primes]
    for p2, q3, r4 in product(squares, cubes, fourths):
        n = p2 + q3 + r4
        if n <= MAX_SUM:
            numbers.add(n)
    return len(numbers)


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
