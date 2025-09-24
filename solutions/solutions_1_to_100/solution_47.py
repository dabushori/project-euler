"""
Challenge 47 of project euler - Distinct Primes Factors

@author Ori Dabush
"""

from solutions.utils.primes import get_prime_factors


CONSECUTIVE_NUMBER_COUNT = 4
DISTINCT_PRIME_FACTORS_COUNT = 4


def solve():
    current_number = 1
    while True:
        for i in reversed(range(CONSECUTIVE_NUMBER_COUNT)):
            if len(set(get_prime_factors(current_number + i))) != DISTINCT_PRIME_FACTORS_COUNT:
                current_number = current_number + i + 1
                break
        else:
            return current_number


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
