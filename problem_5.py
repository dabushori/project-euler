"""
Challenge 5 of project euler - Smallest Multiple

@author Ori Dabush
"""
from math import lcm


NUMBER_COUNT = 20


def solve():
    return lcm(*range(1, NUMBER_COUNT + 1))


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
