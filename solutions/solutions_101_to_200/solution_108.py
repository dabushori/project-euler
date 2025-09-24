"""
Challenge 108 of project euler - Diophantine Reciprocals I

@author Ori Dabush
"""

from itertools import count


MIN_SOLUTIONS = 1000


"""
1/x + 1/y = 1/n
(x+y)/xy = 1/n
ny + nx = xy
n = xy/(x+y)

1/y = 1/n - 1/x = (x - n) / xn
y = xn / (x - n)
"""


def count_distinct_solutions(n: int) -> int:
    """
    Count distinct solutions to 1/x + 1/y = 1/n, where x, y and n are positive integers.
    """
    distinct_solutions = 0
    for factor in count(2):
        # y = x * n / (x - n) = n * factor * n / (n * factor - n) = factor * n / (factor - 1)
        y_nominator = factor * n
        y_denominator = factor - 1
        y = y_nominator // y_denominator
        if y <= n:
            break
        if y_nominator % y_denominator == 0:
            y = y_nominator // y_denominator
            distinct_solutions += 1
    return distinct_solutions


def solve():
    for n in range(2, 100):
        print(f'count_distinct_solutions({n}) = {count_distinct_solutions(n)}')
    # for n in count(1):
    #     distinct_solutions = count_distinct_solutions(n)
    #     print(f'{n}: {distinct_solutions}')
    #     if distinct_solutions > MIN_SOLUTIONS:
    #         return n


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
