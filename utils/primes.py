from math import floor
from itertools import count
from functools import cache


@cache
def is_prime(number: int) -> bool:
    return all(number % factor != 0 for factor in range(2, floor(number ** 0.5) + 1)) if number >= 2 else False


@cache
def get_prime_factors(number: int):
    if number == 1:
        return []
    if is_prime(number):
        return [number]
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


def prime_numbers_until_with_space(number: int):
    """
    This function uses Sieve of Eratosthenes which requires an array of number's length
    """
    if number < 2:
        return
    # This array marks 2, ..., number
    numbers = [False] * (number - 1)
    for candidate in range(2, number + 1):
        candidate_index = candidate - 2
        if not numbers[candidate_index]:
            yield candidate
            for index_to_mark in range(candidate_index, len(numbers), candidate):
                numbers[index_to_mark] = True


def prime_numbers_until_no_space(upper_limit: int):
    """
    This function doesn't use any array, but it takes more time
    """
    for candidate in range(2, upper_limit + 1):
        if is_prime(candidate):
            yield candidate


def get_prime_numbers(start: int = 2):
    for candidate in count(start=start):
        if is_prime(candidate):
            yield candidate
