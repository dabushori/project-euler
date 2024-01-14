"""
Challenge 51 of project euler - Prime Digit Replacements

@author Ori Dabush
"""

from collections import Counter
from itertools import combinations
from utils.primes import get_prime_numbers, is_prime


INITIAL_PRIME = 56003
DESIRED_NUMBER_OF_PRIMES = 8
DIGITS = list(range(10))
DIGITS_WITHOUT_ZERO = list(range(1, 10))
REPLACEMENT_CHARACTER = '*'


def generate_pattern(prime: int, indexes_to_replace: set[int]) -> str:
    return ''.join(
        REPLACEMENT_CHARACTER if index in indexes_to_replace else char
        for index, char in enumerate(str(prime))
    )


def get_number_of_primes(pattern: str) -> int:
    digits = DIGITS
    if pattern.startswith(REPLACEMENT_CHARACTER):
        digits = DIGITS_WITHOUT_ZERO
    return len([digit for digit in digits if is_prime(int(pattern.replace(REPLACEMENT_CHARACTER, str(digit))))])


def solve():
    for prime in get_prime_numbers(start=INITIAL_PRIME):
        counter = Counter(str(prime))
        for digit, number_of_occurrences in counter.items():
            indexes = {index for index, char in enumerate(str(prime)) if char == digit}
            for number_of_replaces in range(1, number_of_occurrences + 1):
                for indexes_to_replace in combinations(indexes, number_of_replaces):
                    pattern = generate_pattern(prime, indexes_to_replace)
                    number_of_primes = get_number_of_primes(pattern)
                    if number_of_primes == DESIRED_NUMBER_OF_PRIMES:
                        return prime


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
