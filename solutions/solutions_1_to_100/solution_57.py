"""
Challenge 57 of project euler - Square Root Convergents

@author Ori Dabush
"""

from fractions import Fraction
from functools import cache


UPPER_LIMIT = 1000


@cache
def get_expansion(n: int) -> tuple[int, int]:
    """
    This function returns the n-th expansion (1-based) in the form of (numerator, denominator).
    The expansion is a series which can be described by the formula:
    a_0 = 1.5 = 3 / 2
    a_(n+1) = 1 + 1 / (a_n + 1) = (a_n + 2) / (a_n + 1)
    """
    if n < 1:
        raise ValueError(f'Invalid n: {n}')
    elif n == 1:
        return Fraction(1.5).as_integer_ratio()
    prev_expansion = Fraction(*get_expansion(n - 1))
    return Fraction(prev_expansion + 2, prev_expansion + 1).as_integer_ratio()


def check_expansion(n: int) -> bool:
    numerator, denominator = get_expansion(n)
    return len(str(numerator)) > len(str(denominator))


def solve():
    return len([n for n in range(1, UPPER_LIMIT + 1) if check_expansion(n)])


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
