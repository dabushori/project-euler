"""
Challenge 100 of project euler - Arranged Probability

@author Ori Dabush
"""

from itertools import count
from utils.equations import solve_quadratic_equation, solve_quadratic_equation_and_check
from math import sqrt, floor


LOWER_LIMIT = 10 ** 12
POSSIBLE_TOTAL_DISCS_DIGITS = [0, 1, 5, 6]
SQUARES_POSSIBLE = [0, 1, 4, 5, 6, 9]


def get_possible_total_discs_values():
    """
    We know that n * (n - 1) = 2 * b * (b - 1)
    Let's calculate all the possible values of d * (d - 1):
    0 * 1 % 10 = 0 | 2 * 0 * 1 % 10 = 0 -> Good
    1 * 2 % 10 = 2 | 2 * 1 * 2 % 10 = 4 -> Bad
    2 * 3 % 10 = 6 | 2 * 2 * 3 % 10 = 2 -> Bad
    3 * 4 % 10 = 2 | 2 * 3 * 4 % 10 = 4 -> Bad
    4 * 5 % 10 = 0 | 2 * 4 * 5 % 10 = 0 -> Good
    5 * 6 % 10 = 0 | 2 * 5 * 6 % 10 = 0 -> Good
    6 * 7 % 10 = 2 | 2 * 6 * 7 % 10 = 4 -> Bad
    7 * 8 % 10 = 6 | 2 * 7 * 8 % 10 = 2 -> Bad
    8 * 9 % 10 = 2 | 2 * 8 * 9 % 10 = 4 -> Bad
    9 * 0 % 10 = 0 | 2 * 9 * 0 % 10 = 0 -> Good

    The only values of n which can be both 2 * b * (b - 1) and n * (n - 1) for some value of b are 0, 1, 5, 6.
    This drops 60% of the values to brute force.
    """
    current_number = LOWER_LIMIT
    while True:
        for digit in POSSIBLE_TOTAL_DISCS_DIGITS:
            yield current_number + digit
        current_number += 10



def get_possible_squares(start):
    """
    We know that n * (n - 1) = 2 * b * (b - 1)
    Let's calculate all the possible values of d * (d - 1):
    0 * 1 % 10 = 0 | 2 * 0 * 1 % 10 = 0 -> Good
    1 * 2 % 10 = 2 | 2 * 1 * 2 % 10 = 4 -> Bad
    2 * 3 % 10 = 6 | 2 * 2 * 3 % 10 = 2 -> Bad
    3 * 4 % 10 = 2 | 2 * 3 * 4 % 10 = 4 -> Bad
    4 * 5 % 10 = 0 | 2 * 4 * 5 % 10 = 0 -> Good
    5 * 6 % 10 = 0 | 2 * 5 * 6 % 10 = 0 -> Good
    6 * 7 % 10 = 2 | 2 * 6 * 7 % 10 = 4 -> Bad
    7 * 8 % 10 = 6 | 2 * 7 * 8 % 10 = 2 -> Bad
    8 * 9 % 10 = 2 | 2 * 8 * 9 % 10 = 4 -> Bad
    9 * 0 % 10 = 0 | 2 * 9 * 0 % 10 = 0 -> Good

    The only values of n which can be both 2 * b * (b - 1) and n * (n - 1) for some value of b are 0, 1, 5, 6.
    This drops 60% of the values to brute force.
    """
    current_number = start
    while True:
        for digit in SQUARES_POSSIBLE:
            yield current_number + digit
        current_number += 10


def check_solutions(total_discs: int, solutions: list[float]) -> bool:
    for solution in solutions:
        if 2 * solution * (solution - 1) == total_discs * (total_discs - 1):
            return True
    return False


def solve2():
    """
    n = total discs, b = blue discs

    The probability (b / n) * ((b - 1) / (n-1)) should be 1/2, which means that:
    b ** 2 - b = 0.5 * n * (n - 1)
    we need to find the first n for which b will be an integer
    """
    # for total_discs in get_possible_total_discs_values():
    #     if total_discs % 10_000_000 == 0:
    #         print(total_discs)
    #     solutions = solve_quadratic_equation(1, -1, -0.5 * total_discs * (total_discs - 1))
    #     if solutions and solutions[0].is_integer() and check_solutions(total_discs, solutions):
    #         print(total_discs, solutions)
    #         return total_discs

    min_root = floor(sqrt(1 + 2 * LOWER_LIMIT * (LOWER_LIMIT - 1)))
    for discriminant_sqrt in get_possible_squares(min_root):
        # discriminant_sqrt ** 2 = b ** 2 - 4ac = 1 + 2 * n * (n - 1)
        # We want to find n from discriminant_sqrt
        total_discs = solve_quadratic_equation(2, -2, 1 - discriminant_sqrt ** 2)
        print(total_discs)
        if total_discs and total_discs[0].is_integer():
            n = int(min(total_discs))
            if solve_quadratic_equation_and_check(1, -1, int(-0.5 * n * (n - 1))):
                print(f'n = {n}, b = {solve_quadratic_equation_and_check(1, -1, int(-0.5 * n * (n - 1)))}')
                return n

from utils.triangles import get_triangle_numbers, get_triangle_number


def solve():
    visited_triangles = set()
    current_low_index = int(((LOWER_LIMIT ** 2 + LOWER_LIMIT) / 2) ** 0.5)
    print(f'{current_low_index = }')
    for idx, triangle in get_triangle_numbers(start=LOWER_LIMIT, indexed=True):
        if idx % 1_000_000 == 0:
            print(idx)
        # triangle = n * (n - 1) / 2
        while current_low_index < idx:
            visited_triangles.add(get_triangle_number(current_low_index))
            current_low_index += 1
        target = triangle / 2
        if target in visited_triangles:
            print(triangle, target)
            return idx


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
