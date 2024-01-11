"""
Challenge 12 of project euler - Highly Divisible Triangular Number

@author Ori Dabush
"""
from itertools import count
from utils.divisors import get_divisors


NUMBER_OF_DIVISORS = 500


def get_triangle_number(n: int) -> int:
    return n * (n + 1) // 2


def solve():
    for number in count(start=2):
        triangle_number = get_triangle_number(number)
        if len(list(get_divisors(triangle_number))) > NUMBER_OF_DIVISORS:
            return triangle_number


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
