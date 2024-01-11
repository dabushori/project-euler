"""
Challenge 10 of project euler - Summation of Primes

@author Ori Dabush
"""
from utils.primes import prime_numbers_until


UPPER_LIMIT = 2_000_000


def solve():
    return sum(prime_numbers_until(UPPER_LIMIT))


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
