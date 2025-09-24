"""
Challenge 70 of project euler - Totient Permutation

@author Ori Dabush
"""

from collections import defaultdict
from solutions.utils.primes import prime_numbers_until_with_space
from fractions import Fraction


MIN_VALUE = 2
MAX_VALUE = 10 ** 7


def is_permutation(number_1: int, number_2: int) -> bool:
    return sorted(str(number_1)) == sorted(str(number_2))


def solve():
    """
    n / phi(n) = (p1 / (p1 - 1)) * ... * (pm / (pm - 1))
    """
    n_over_phi_dict = defaultdict(lambda: Fraction(1, 1))
    for prime in prime_numbers_until_with_space(MAX_VALUE):
        for i in range(prime, MAX_VALUE, prime):
            n_over_phi_dict[i] *= Fraction(prime, prime - 1)
    # Find the min value of n / n_over_phi, starting from MIN_VALUE, only if phi(n) is a permutation of n
    return min(
        ((n, n_over_phi) for n, n_over_phi in n_over_phi_dict.items() if is_permutation(n, int(n / n_over_phi))), 
        key=lambda x: x[0] / x[1]
    )[0]


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
