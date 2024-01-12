"""
Challenge 36 of project euler - Double-base Palindromes

@author Ori Dabush
"""

from utils.palindrome import is_palindrome


UPPER_LIMIT = 1_000_000


def binary_representation(number: int) -> str:
    return bin(number).replace("0b", "")


def solve():
    return sum(
        number
        for number in range(UPPER_LIMIT)
        if is_palindrome(str(number)) and is_palindrome(binary_representation(number))
    )


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
