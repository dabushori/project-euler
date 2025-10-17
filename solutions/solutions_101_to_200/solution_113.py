"""
Challenge 113 of project euler - Non-bouncy Numbers

@author Ori Dabush
"""

import math
from functools import cache


TARGET_NUMBER = 10 ** 100


@cache
def count_increasing_numbers(num_digits, digits, include_zeros=True):
    if num_digits == 1:
        if not include_zeros and (0 in digits):
            return len(digits) - 1
        return len(digits)
    increasing_numbers = 0
    for first_digit in digits:
        if not include_zeros and first_digit == 0: continue
        increasing_numbers += count_increasing_numbers(num_digits - 1, tuple(d for d in digits if d >= first_digit))
    return increasing_numbers


@cache
def count_decreasing_numbers(num_digits, digits, include_zeros=True):
    if num_digits == 1:
        if not include_zeros and (0 in digits):
            return len(digits) - 1
        return len(digits)
    decreasing_numbers = 0
    for first_digit in digits:
        if not include_zeros and first_digit == 0: continue
        decreasing_numbers += count_decreasing_numbers(num_digits - 1, tuple(d for d in digits if d <= first_digit))
    return decreasing_numbers


def solve():
    """
    Instead of trying to optimize counting bouncy numbers, I can count the non bouncy numbers - which must be increasing or decreasing.
    I do it recursively (easier implementation).
    """
    max_number_of_digits = math.floor(math.log10(TARGET_NUMBER)) + 1
    increasing = sum(count_increasing_numbers(n, digits=tuple(range(10)), include_zeros=False) for n in range(1, max_number_of_digits))
    decreasing = sum(count_decreasing_numbers(n, digits=tuple(range(10)), include_zeros=False) for n in range(1, max_number_of_digits))
    # The only numbers which are both increasing and decreasing are the numbers which are made up with 1 digit.
    # For every number of digits there are 9 of them
    # There is also 0 which is counted only once for all the digit numbers (as 00 and 0 are the same), but it is not counted in the functions above
    both_increasing_and_decreasing = 9 * (max_number_of_digits - 1)
    return increasing + decreasing - both_increasing_and_decreasing


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
