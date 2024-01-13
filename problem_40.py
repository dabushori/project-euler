"""
Challenge 40 of project euler - Champernowne's Constant

@author Ori Dabush
"""

from itertools import count
from functools import reduce
from operator import mul


DIGITS_INDEXES = [10 ** i for i in range(7)]


def get_number_of_digits(digit_index: int) -> tuple[int, int]:
    """
    Returns (range_start_index, number_of_digits)
    """
    if digit_index < 10:
        return 0, 1
    current_index = 10
    for n in count(start=2):
        next_current_index = current_index + n * 9 * (10 ** (n - 1))
        if next_current_index > digit_index:
            return current_index, n
        current_index = next_current_index


def get_digits_value(digit_index: int) -> int:
    range_start_index, number_of_digits = get_number_of_digits(digit_index)
    range_start_value = 10 ** (number_of_digits - 1) if number_of_digits > 1 else 0
    number = range_start_value + (digit_index - range_start_index) // number_of_digits
    digit_index_in_number = (digit_index - range_start_index) % number_of_digits
    return int(str(number)[digit_index_in_number])


def solve():
    return reduce(mul, [get_digits_value(index) for index in DIGITS_INDEXES], 1)


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
