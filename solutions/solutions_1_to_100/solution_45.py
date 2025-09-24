"""
Challenge 45 of project euler - Triangular, Pentagonal, and Hexagonal

@author Ori Dabush
"""

from solutions.utils.triangles import is_triangle_number
from solutions.utils.pentagons import is_pentagon_number
from solutions.utils.hexagonals import get_hexagonal_numbers


KNOWN_HEXAGONAL_INDEX = 143


def solve():
    for number in get_hexagonal_numbers(start=KNOWN_HEXAGONAL_INDEX + 1):
        if is_triangle_number(number) and is_pentagon_number(number):
            return number


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
