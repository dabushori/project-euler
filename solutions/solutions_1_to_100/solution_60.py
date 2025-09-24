"""
Challenge 60 of project euler - Prime Pair Sets

@author Ori Dabush
"""

from itertools import combinations
from solutions.utils.primes import get_prime_numbers, prime_numbers_until_with_space, is_prime


GROUP_SIZE = 5


def check_concatenating_primes(prime_1: int, prime_2: int) -> bool:
    return is_prime(int(f'{prime_1}{prime_2}')) and is_prime(int(f'{prime_2}{prime_1}'))


def solve():
    prime_pairs = set()
    for prime in get_prime_numbers():
        current_prime_pairs = [
            p for p in prime_numbers_until_with_space(prime - 1)
            if check_concatenating_primes(prime, p)
        ]
        # Check if there exists a subset of GROUP_SIZE-1 primes that are pairs with each other
        for primes in combinations(current_prime_pairs, GROUP_SIZE - 1):
            for prime_1, prime_2 in combinations(primes, 2):
                if not check_concatenating_primes(prime_1, prime_2):
                    break
            else:
                return prime + sum(primes)
        prime_pairs.update({(prime, other) for other in current_prime_pairs})


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
