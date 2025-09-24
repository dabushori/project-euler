"""
Challenge 100 of project euler - Arranged Probability

@author Ori Dabush
"""

N=2
ELEMENTARY_SOLUTION = (1, 1)
MIN_DISCS=10**12


def solution_to_discs(x, y):
    t = (x + 1) // 2
    b = (y + 1) // 2
    return t, b


def discs_to_solution(t, b):
    x = 2 * t - 1
    y = 2 * b - 1
    return x, y


def _mult(x1, y1, x2, y2, N=N):
    x = x1 * x2 + y1 * y2 * N
    y = y1 * x2 + x1 * y2
    return x, y


def mult(e1, e2): 
    return _mult(*e1, *e2)


def _norm(x, y): 
    return x * x - N * y * y


def norm(e): 
    return _norm(*e)


def solve():
    """
    We need to find b, t such that
    2b(b-1) = t(t-1)
    2(b^2-b) = t^2-t
    2(b^2-b+0.25)-0.5 = t^2-t+0.25-0.25
    2(b-0.5)^2-0.5 = (t-0.5)^2-0.25
    (2t-1)^2-2(2b-1)^2 = -1

    Lets mark
    x = 2t-1, y = 2b-1

    Our equation is
    x^2-2y^2 = -1

    This is a Pal equation, and its solutions are all the elements in Z[sqrt(2)] which their norm is -1.

    If we the elementary solution, we can create all the unit elements with norm of -1 by multplying it with itself squared
    (its norm will be -1 so multiplying it by itself once will give us an element which norm is 1).
    https://gadial.net/2012/08/31/pell_equation/

    I won't implement the algorithm to find the elementary solution - it is (1, 1) for N=2
    """
    start = discs_to_solution(*ELEMENTARY_SOLUTION)
    step = mult(start,start)
    current = start
    while True:
        t, b = solution_to_discs(*current)
        if t > MIN_DISCS:
            return b
        current = mult(current, step)


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
