"""
Challenge 64 of project euler - Odd Period Square Roots

@author Ori Dabush
"""

from utils.sqrt_representation import get_sqrt_representation


UPPER_LIMIT = 10000


def solve():
    result = 0
    for n in range(1, UPPER_LIMIT + 1):
        prefix, cycle = get_sqrt_representation(n)
        if len(cycle) % 2 == 1:
            result += 1
    return result


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
