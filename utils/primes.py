from math import ceil
from itertools import count


def is_prime(number: int) -> bool:
    return all(number % factor != 0 for factor in range(2, ceil(number ** 0.5 + 1))) if number >= 2 else False


def get_prime_factors(number):
    if number == 1:
        return []
    for candidate in range(2, number + 1):
        if is_prime(candidate) and number % candidate == 0:
            return [candidate] + get_prime_factors(number // candidate)


def get_first_n_primes(n: int):
    primes_found = 0
    for candidate in count(start=2):
        if primes_found == n:
            break
        if is_prime(candidate):
            primes_found += 1
            yield candidate
