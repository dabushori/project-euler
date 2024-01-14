"""
Challenge 46 of project euler - Goldbach's Other Conjecture

@author Ori Dabush
"""

from itertools import count
from math import ceil
from utils.primes import is_prime, prime_numbers_until_with_space


def check_goldbach_conjecture(number: int) -> bool:
    for prime in prime_numbers_until_with_space(number):
        for square in range(1, ceil((number - prime) ** 0.5)):
            if prime + 2 * square ** 2 == number:
                return True
    return False


def solve():
    for number in count():
        number = 2 * number + 1
        if is_prime(number) or number == 1:
            continue
        if not check_goldbach_conjecture(number):
            return number


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
