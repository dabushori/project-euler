"""
Challenge 66 of project euler - Diophantine Equation

@author Ori Dabush
"""

from fractions import Fraction
from utils.sqrt_representation import get_sqrt_representation


D_MAX = 1000


def is_square(n: int) -> bool:
    return float.is_integer(n ** 0.5)


def get_approximated_fraction(n: int) -> Fraction:
    """
    The fraction's index is 0 based
    """
    prefix, cycle = get_sqrt_representation(n)
    prefix, cycle = prefix[0], cycle[:-1] if len(cycle) > 1 else cycle
    result = Fraction(cycle[-1], 1)
    for component in cycle[::-1][1:]:
        result = 1 / result + component
    return prefix + 1 / result


def find_minimal_solution(d: int) -> tuple[int, int] | None:
    if is_square(d):
        return None
    approx_fraction = get_approximated_fraction(d)
    x, y = approx_fraction.numerator, approx_fraction.denominator
    if x ** 2 - d * y ** 2 == 1:
        return x, y
    elif x ** 2 - d * y ** 2 == -1:
        # The solution is (x + sqrt(d) * y) ** 2
        return x ** 2 + d * y ** 2, 2 * x * y
    else:
        raise ValueError("Math gone wrong")


def solve():
    max_x, max_d = 0, None
    for d in range(2, D_MAX + 1):
        solution = find_minimal_solution(d)
        if solution is None:
            continue
        x, y = solution
        if x > max_x:
            max_x, max_d = x, d
    return max_d


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
