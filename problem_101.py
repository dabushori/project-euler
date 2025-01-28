"""
Challenge 101 of project euler - Optimum Polynomial

@author Ori Dabush
"""

import numpy as np


POLY_DEGREE = 10
def u(n):
    return sum((-n) ** i for i in range(POLY_DEGREE + 1))


def find_op(degree):
    """
    I will find the OP by solving a system of `degree` linear equations. I will do it using numpy. 
    Ax = b, where x = (a_1, ..., a_degree) are the OP coefficients, b = (u(1), ..., u(n)) are the actual value of the original polynomial
    and A_ij = i ** (j - 1) [1 <= i, j <= n].
    I will find x by calculating inverse(A) * b
    """
    A = np.array([
        [n ** i for i in range(degree)]
        for n in range(1, degree + 1)
    ])
    b = np.array([u(n) for n in range(1, degree + 1)])
    return np.rint(np.matmul(np.linalg.inv(A), b))


def find_fit(degree):
    op = find_op(degree)
    for n in range(1, POLY_DEGREE + 2):
        op_value = np.dot(op, [n ** i for i in range(degree)])
        real_value = u(n)
        if op_value != real_value:
            return op_value
    raise Exception("Hasn't found FIT")


def solve():
    return sum(find_fit(d) for d in range(1, POLY_DEGREE + 1))


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
