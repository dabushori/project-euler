"""
Challenge 3 of project euler - Largest Prime Factor

@author Ori Dabush
"""
from utils.primes import get_prime_factors


INPUT_NUMBER = 600851475143


def solve():
    return max(get_prime_factors(INPUT_NUMBER))


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
