"""
Challenge 49 of project euler - Prime Permutations

@author Ori Dabush
"""

from solutions.utils.primes import prime_numbers_until_with_space
from itertools import permutations, product


FOUR_DIGIT_PRIMES = set(prime for prime in prime_numbers_until_with_space(10000) if prime >= 1000)
KNOWN_RESULT = '148748178147'


def solve():
    for prime in FOUR_DIGIT_PRIMES:
        greater_digits_permutations = [
            int(''.join(permutation))
            for permutation in permutations(str(prime))
            if int(''.join(permutation)) > prime
        ]
        for n1, n2 in product(greater_digits_permutations, greater_digits_permutations):
            # We assume prime < n1 < n2
            if n1 >= n2:
                continue
            if {n1, n2}.issubset(FOUR_DIGIT_PRIMES) and n2 - n1 == n1 - prime:
                result = f'{prime}{n1}{n2}'
                if result != KNOWN_RESULT:
                    return result


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
