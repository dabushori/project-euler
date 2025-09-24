"""
Challenge 105 of project euler - Special Subset Sums: Testing

@author Ori Dabush
"""

from solutions.utils.inputs import get_input
from solutions.utils.special_sum_set import is_special_sum_set


def solve():
    sets = [list(map(int, line.strip().split(','))) for line in get_input(105).split('\n')]
    return sum(sum(s) for s in sets if is_special_sum_set(s))


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
