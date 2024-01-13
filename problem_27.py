"""
Challenge 27 of project euler - Quadratic Primes

@author Ori Dabush
"""

from math import inf
from utils.primes import prime_numbers_until_with_space, is_prime
from itertools import count


A_MAX = 1000
B_MAX = 1000


def get_formula(a: int, b: int):
    return lambda n: n * (n + a) + b


def calculate_number_of_primes(a: int, b: int) -> int:
    formula = get_formula(a, b)
    for n in count():
        if not is_prime(formula(n)):
            return n


def solve():
    """
    The formula is n^2 + an + b, where |a| < A_MAX, |b| <= B_MAX.
    We know that 'b' must be prime because n = 0 should give us a prime.
    We also know that '1+a+b' must be a prime n = 1 should also give us a prime.
    'b' must be in the range of (0, B_MAX), and 'a' is in (-A_MAX, A_MAX) so 1+a+b is in (1-A_MAX, 1+A_MAX+B_MAX),
    but it is prime which means it is in (0, 1+A_MAX+B_MAX).
    Iterating on the prime numbers in these ranges should be fast enough.
    """
    max_prime_count = -inf
    result = None
    for b in prime_numbers_until_with_space(B_MAX):
        for a_plus_b_plus_1 in prime_numbers_until_with_space(1 + A_MAX + B_MAX):
            a = a_plus_b_plus_1 - 1 - b
            current_prime_count = calculate_number_of_primes(a, b)
            if current_prime_count > max_prime_count:
                max_prime_count = current_prime_count
                result = a * b
    return result


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
