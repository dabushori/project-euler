"""
Challenge 72 of project euler - Counting Fractions

@author Ori Dabush
"""

from utils.primes import prime_numbers_until_with_space
from fractions import Fraction
from collections import defaultdict


MIN_D_VALUE = 2
MAX_D_VALUE = 1_000_000


def solve():
    """
    For a given value of d, the number of reduced proper fractions with their denominator being d is phi(d).
    """
    phi_over_n_dict = defaultdict(lambda: Fraction(1, 1))
    for prime in prime_numbers_until_with_space(MAX_D_VALUE + 1):
        for i in range(prime, MAX_D_VALUE + 1, prime):
            phi_over_n_dict[i] *= Fraction(prime - 1, prime)
    return sum(phi_over_n * n for n, phi_over_n in phi_over_n_dict.items())


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
