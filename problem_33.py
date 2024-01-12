"""
Challenge 33 of project euler - Digit Cancelling Fractions

@author Ori Dabush
"""

from fractions import Fraction


LOWER_LIMIT, UPPER_LIMIT = 10, 100


def is_trivial_example(numerator: int, denominator: int) -> bool:
    return numerator % 10 == 0 and denominator % 10 == 0


def is_digit_cancelling_fraction(numerator: int, denominator: int) -> bool:
    if is_trivial_example(numerator, denominator):
        return False
    fraction = Fraction(numerator, denominator)
    numerator_1, numerator_2 = numerator // 10, numerator % 10
    denominator_1, denominator_2 = denominator // 10, denominator % 10
    if denominator_1 != 0:
        if numerator_1 == denominator_2 and fraction == Fraction(numerator_2, denominator_1):
            return True
        if numerator_2 == denominator_2 and fraction == Fraction(numerator_1, denominator_1):
            return True
    if denominator_2 != 0:
        if numerator_1 == denominator_1 and fraction == Fraction(numerator_2, denominator_2):
            return True
        if numerator_2 == denominator_1 and fraction == Fraction(numerator_1, denominator_2):
            return True
    return False


def solve():
    result = 1
    for denominator in range(LOWER_LIMIT, UPPER_LIMIT):
        for numerator in range(LOWER_LIMIT, denominator):
            if is_digit_cancelling_fraction(numerator, denominator):
                result *= Fraction(numerator, denominator)
    return result.denominator


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
