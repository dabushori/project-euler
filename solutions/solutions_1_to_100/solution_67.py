"""
Challenge 67 of project euler - Maximum Path Sum II

@author Ori Dabush
"""


from functools import cache
from solutions.utils.inputs import get_input


@cache
def find_max_sum(pyramid: tuple[tuple[int]]) -> int:
    """
    Adding the @cache makes this algorithm a dynamic programming algorithm which makes it way faster.
    """
    if len(pyramid) == 1:
        return pyramid[0][0]
    pyramid_1 = tuple(line[1:] for line in pyramid[1:])
    pyramid_2 = tuple(line[:-1] for line in pyramid[1:])
    return pyramid[0][0] + max(find_max_sum(pyramid_1), find_max_sum(pyramid_2))


def solve():
    pyramid = tuple(tuple(map(int, line.split())) for line in get_input(67).split('\n'))
    return find_max_sum(pyramid)


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
