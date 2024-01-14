"""
Challenge 56 of project euler - Powerful Digit Sum

@author Ori Dabush
"""

from itertools import product


A_UPPER_LIMIT = 100
B_UPPER_LIMIT = 100


def digital_sum(number: int) -> int:
    return sum(map(int, str(number)))


def solve():
    return max([digital_sum(a ** b) for a, b in product(range(1, A_UPPER_LIMIT), range(1, B_UPPER_LIMIT))])


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
