"""
Challenge 69 of project euler - Totient Maximum

@author Ori Dabush
"""

from solutions.utils.primes import prime_numbers_until_with_space


MAX_VALUE = 1_000_000


def solve():
    """
    Assuming n = (p1 ** k1) * ... * (pm ** km) (prime factorization)
    phi(n) = n * (1 - 1 / p1) * ... * (1 - 1 / pm) = n * ((p1 - 1) / p1) * ... * ((pm - 1) / pm)

    That means that
    n / phi(n) = (p1 / (p1 - 1)) * ... * (pm / (pm - 1))

    p / (p - 1) is greater as p is lower, so we know that n which will give the maximum value will be the
    multiplication of as much lowest primes as possible.
    """
    n = 1
    for prime in prime_numbers_until_with_space(MAX_VALUE):
        if n * prime > MAX_VALUE:
            return n
        n *= prime


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
