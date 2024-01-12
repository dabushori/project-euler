"""
Challenge 29 of project euler - Distinct Powers

@author Ori Dabush
"""

from itertools import product


A_MIN, A_MAX = 2, 100
B_MIN, B_MAX = 2, 100


def solve():
    return len(set(a ** b for a, b in product(range(A_MIN, A_MAX + 1), range(B_MIN, B_MAX + 1))))


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
