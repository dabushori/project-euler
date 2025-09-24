"""
Challenge 94 of project euler - Almost Equilateral Triangles

@author Ori Dabush
"""

from math import sqrt


MAX_PERIMETER = 1_000_000_000


def solve():
    """
    The height is equal to:
    sqrt((3 * x + 1) * (x - 1) / 4) on the case of x, x, x + 1
    sqrt((3 * x - 1) * (x + 1) / 4) on the case of x, x, x - 1

    These values can be integral only if x is odd.
    So I brute forced all the odd values and checked if the square root is an integer.
    """
    result = 0
    for x in range(3, MAX_PERIMETER // 3 + 1, 2):
        # Try x, x, x + 1
        non_squared_part = (3 * x + 1) * (x - 1)
        square_root_value = sqrt(non_squared_part)
        if square_root_value.is_integer() and int(square_root_value) ** 2 == non_squared_part:
            result += 3 * x + 1
        # Try x, x, x - 1
        non_squared_part = (3 * x - 1) * (x + 1)
        square_root_value = sqrt(non_squared_part)
        if square_root_value.is_integer() and int(square_root_value) ** 2 == non_squared_part:
            result += 3 * x - 1
    return result


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
