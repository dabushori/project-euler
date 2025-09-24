"""
Challenge 104 of project euler - Pandigital Fibonacci Ends

@author Ori Dabush
"""

from solutions.utils.fibonacci import fibonacci_from_index
from solutions.utils.pandigitals import is_one_to_nine_pandigital
from math import log10, ceil


def solve():
    for idx, n in fibonacci_from_index(2749, return_indexes=True):
        first = n % 10**9
        if not is_one_to_nine_pandigital(first):
            continue
        number_of_digits = ceil(log10(n))
        last = n // (10**(number_of_digits - 9))
        if is_one_to_nine_pandigital(last):
            return idx


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
