"""
Challenge 37 of project euler - Truncatable Primes

@author Ori Dabush
"""

from solutions.utils.primes import is_prime, get_prime_numbers


TRIVIAL_EXAMPLES = {2, 3, 5, 7}
TRUNCATABLE_PRIMES_COUNT = 11


def is_truncatable_prime(number: int) -> bool:
    number = str(number)
    for index in range(len(number)):
        if not is_prime(int(number[index:])) or not is_prime(int(number[:index + 1])):
            return False
    return True


def solve():
    result = 0
    primes_counter = 0
    for prime in get_prime_numbers():
        if primes_counter == TRUNCATABLE_PRIMES_COUNT:
            break
        if prime in TRIVIAL_EXAMPLES:
            continue
        if is_truncatable_prime(prime):
            result += prime
            primes_counter += 1
    return result


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
