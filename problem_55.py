"""
Challenge 55 of project euler - Lychrel Numbers

@author Ori Dabush
"""

from utils.palindrome import is_palindrome


MAX_ITERATIONS = 50
UPPER_LIMIT = 10_000


def is_lychrel_number(number: int) -> bool:
    for _ in range(MAX_ITERATIONS):
        number = number + int(str(number)[::-1])
        if is_palindrome(number):
            return False
    return True


def solve():
    return len([number for number in range(1, UPPER_LIMIT) if is_lychrel_number(number)])


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
