"""
Challenge 7 of project euler - 10001st Prime

@author Ori Dabush
"""
from solutions.utils.primes import get_first_n_primes


INPUT_NUMBER = 10001


def solve():
    return list(get_first_n_primes(INPUT_NUMBER))[-1]


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
