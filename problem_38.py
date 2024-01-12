"""
Challenge 38 of project euler - Pandigital Multiples

@author Ori Dabush
"""

from itertools import count


DIGITS = set(map(str, range(1, 10)))
PRODUCT_UPPER_LIMIT = 10 ** 9
MULTIPLICAND_UPPER_LIMIT = 10 ** 4


def is_one_to_nine_pandigital_number(number: int) -> bool:
    number = str(number)
    return len(number) == len(DIGITS) and set(number) == DIGITS


def calculate_concatenated_product(number: int, n: int) -> int:
    return int(''.join(str(number * i) for i in range(1, n + 1)))


def solve():
    """
    We can stop at 10 ** 4 because if the multiplicand will have 5 or more digits the product will
    have at least 10 digits.
    """
    max_result = 0
    for multiplicand in range(1, MULTIPLICAND_UPPER_LIMIT):
        for n in count(start=2):
            product = calculate_concatenated_product(multiplicand, n)
            if product >= PRODUCT_UPPER_LIMIT:
                break
            if is_one_to_nine_pandigital_number(product):
                max_result = max(max_result, product)
    return max_result


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
