"""
Challenge 41 of project euler - Pandigital Prime

@author Ori Dabush
"""

from solutions.utils.primes import is_prime
from solutions.utils.pandigitals import get_pandigital_numbers


def solve():
    for n in range(9, 0, -1):
        pandigital_numbers = sorted(get_pandigital_numbers(n), reverse=True)
        for candidate in pandigital_numbers:
            if is_prime(candidate):
                return candidate


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
