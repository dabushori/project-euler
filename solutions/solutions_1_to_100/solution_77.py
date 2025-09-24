"""
Challenge 77 of project euler - Prime Summations

@author Ori Dabush
"""

from solutions.utils.primes import get_first_n_primes
from functools import cache


DESIRED_PRIME_SUMMATIONS_COUNT = 5000


@cache
def prime_summations_count_from_values(n: int, values: tuple[int]) -> int:
    if n == 0:
        return 1
    return sum(
        prime_summations_count_from_values(n - i, tuple(value for value in values if value <= i))
        for i in values
        if i <= n
    )


def solve():
    # There will not be more than DESIRED_PRIME_SUMMATIONS_COUNT used in the combinations for sure
    first_primes = tuple(get_first_n_primes(DESIRED_PRIME_SUMMATIONS_COUNT))
    n = 1
    while prime_summations_count_from_values(n, first_primes) <= DESIRED_PRIME_SUMMATIONS_COUNT:
        n += 1
    return n


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
