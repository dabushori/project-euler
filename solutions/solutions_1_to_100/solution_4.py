"""
Challenge 4 of project euler - Largest Palindrome Product

@author Ori Dabush
"""
from itertools import product
from solutions.utils.palindrome import is_palindrome


def solve():
    for candidate in sorted([n1 * n2 for n1, n2 in product(range(100, 1000), range(100, 1000))], reverse=True):
        if is_palindrome(candidate):
            return candidate
    raise ValueError('Something is fucked up')


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
