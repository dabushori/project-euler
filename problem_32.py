"""
Challenge 32 of project euler - Pandigital Products

@author Ori Dabush
"""

from utils.divisors import get_divisors


PRODUCT_UPPER_LIMIT = 10 ** 7
DIGITS = set(map(str, range(1, 10)))


def is_pandigital(string: str):
    return len(string) == len(DIGITS) and set(string) == DIGITS


def solve():
    """
    The multiplicand and multiplier must contain at least one digit, which means the product must have at most 7 digits.
    """
    result = 0
    for product in range(1, PRODUCT_UPPER_LIMIT):
        # Drop the product if it contains 0 or if it contains a duplicate digit
        if '0' in str(product) or len(set(str(product))) != len(str(product)):
            continue
        for multiplicand in get_divisors(product):
            multiplier = product // multiplicand
            if is_pandigital(f"{multiplicand}{multiplier}{product}"):
                result += product
                break
    return result


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
