"""
Challenge 35 of project euler - Circular Primes

@author Ori Dabush
"""

from utils.primes import prime_numbers_until_with_space


UPPER_LIMIT = 1_000_000
PRIMES_UNTIL_LIMIT = set(prime_numbers_until_with_space(UPPER_LIMIT))


def is_circular_prime(number: int) -> bool:
    number = str(number)
    for index in range(len(number)):
        if int(number[index:] + number[:index]) not in PRIMES_UNTIL_LIMIT:
            return False
    return True


def solve():
    return len([prime for prime in PRIMES_UNTIL_LIMIT if is_circular_prime(prime)])


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
