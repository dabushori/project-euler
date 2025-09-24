"""
Challenge 23 of project euler - Non-Abundant Sums

@author Ori Dabush
"""

from solutions.utils.divisors import get_divisors
from itertools import product


UPPER_LIMIT = 28123


def sum_of_proper_divisors(number: int) -> int:
    return sum(divisor for divisor in get_divisors(number) if divisor != number)


def is_abundant(number: int) -> bool:
    return sum_of_proper_divisors(number) > number


def solve():
    abundant_numbers = [number for number in range(1, UPPER_LIMIT) if is_abundant(number)]
    # The numbers which can be expressed as the sum of 2 abundant numbers
    two_abundant_numbers_sums = set(
        number_1 + number_2
        for number_1, number_2 in product(abundant_numbers, abundant_numbers)
    )
    # Calculate the sum of those who cannot be expressed as the sum of abundant numbers by calculating the complementary
    # set of the set of the number who can be expressed as the sum of 2 abundant numbers
    return sum(set(range(1, UPPER_LIMIT)) - two_abundant_numbers_sums)


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
