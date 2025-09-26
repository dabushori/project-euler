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



1/x + 1/y = 1/n
(x+y)/xy=1/n
n=xy/(x+y)

We know that:
x|yn
y|xn
n|xy
"""


def count_distinct_solutions(n: int) -> int:
    """
    Count distinct solutions to 1/x + 1/y = 1/n, where x, y and n are positive integers.
    """
    distinct_solutions = 0
    min_possible_x, max_possible_x = n + 1, 2 * n
    print(f'The value of n is {n}')
    for x in range(min_possible_x, max_possible_x + 1):
        y_n, y_d = x*n, x-n
        if y_n % y_d == 0: 
            distinct_solutions += 1
            print(f'1 / {x} + 1 / {y_n//y_d} = 1 / {n}')
    return distinct_solutions


def solve():
    for n in count(1):
        distinct_solutions = count_distinct_solutions(n)
        if n % 1000 == 0:
            print(f'{n}: {distinct_solutions}')
        if distinct_solutions > MIN_SOLUTIONS:
            return n


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
