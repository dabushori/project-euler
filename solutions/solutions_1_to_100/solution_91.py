"""
Challenge 91 of project euler - Right Triangles with Integer Coordinates

@author Ori Dabush
"""

from fractions import Fraction
from itertools import product


MAX_COORDINATES = 50


def count_right_triangles(x_p: int, y_p: int):
    """
    The slope of P is 'y_p / x_p'. It is guaranteed that it won't be 0 or undefined because x_p, y_p != 0.
    We assume that OP is one of the legs because if OQ was one of the legs it is symmetric.
    We assume that OP is perpendicular to PQ and not to OQ because the only case where it can be perpendicular to OQ is
    if they were both on the axes, otherwise OQ will be completely out of the range.
    """
    assert x_p != 0 and y_p != 0, "Invalid coordinates"
    op_slope = Fraction(y_p, x_p)
    # They are perpendicular so the slopes product is -1
    pq_slope = -1 / op_slope
    result = 0
    # Iterate on every x value and calculate the y value of Q
    for x_q in range(MAX_COORDINATES + 1):
        if x_q == x_p:
            continue
        # y - y_1 = m * (x - x_1)
        y_q = pq_slope * (x_q - x_p) + y_p
        # Count this option only if the y of Q is an integer in the range
        if 0 <= y_q <= MAX_COORDINATES and y_q.is_integer():
            result += 1
    return result


def solve():
    # Count all the options for P to be on x and y axes (OQ and OP can both be legs only in this case)
    result = 3 * (MAX_COORDINATES ** 2)
    # Count all the options for P to not be on x and y axes (x, y >= 1)
    for x1, y1 in product(range(1, MAX_COORDINATES + 1), repeat=2):
        result += count_right_triangles(x1, y1)
    return result


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
