"""
Challenge 76 of project euler - Counting Summations

@author Ori Dabush
"""

from functools import cache


DESIRED_NUMBER = 100


@cache
def summations_count_from_values(n: int, values: tuple[int]) -> int:
    if n == 0:
        return 1
    return sum(
        summations_count_from_values(n - i, tuple(value for value in values if value <= i))
        for i in values
        if i <= n
    )


def summations_count(n: int) -> int:
    return summations_count_from_values(n, tuple(range(1, n)))


def solve():
    return summations_count(DESIRED_NUMBER)


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
