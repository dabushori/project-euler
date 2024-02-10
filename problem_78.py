"""
Challenge 78 of project euler - Coin Partitions

@author Ori Dabush
"""

from itertools import count
from functools import cache
from utils.pentagons import get_pentagon_number


DESIRED_DIVISOR = 1_000_000


@cache
def partitions(n: int) -> int:
    if n < 0:
        return 0
    if n <= 1:
        return 1
    sign = 1
    result = 0
    for k in count(start=1):
        pentagon_1, pentagon_2 = get_pentagon_number(k), get_pentagon_number(-k)
        result += sign * (partitions(n - pentagon_1) + partitions(n - pentagon_2))
        if pentagon_2 > n:
            return result
        sign = -sign


def solve():
    """
    This problem is equivalent to the summations count, except that here there's one more solution - the number itself.
    However, this solution is very slow when it reaches big numbers.
    I'll use a formula euler proved that is using pentagonal numbers. The formula is:
    p(n) = sum of (-1) ^ (k - 1) * p(n - g_k), where g_k is the k-th pentagonal number.
    """
    for n in count(start=1):
        if partitions(n) % DESIRED_DIVISOR == 0:
            return n


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
