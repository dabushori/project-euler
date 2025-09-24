"""
Challenge 71 of project euler - Ordered Fractions

@author Ori Dabush
"""

from fractions import Fraction


MIN_D_VALUE = 2
MAX_D_VALUE = 1_000_000
DESIRED_VALUE = Fraction(3, 7)


def solve():
    fractions = []
    for d in range(MIN_D_VALUE, MAX_D_VALUE + 1):
        # Append the fraction closest to DESIRED_VALUE from below
        n = int(d * DESIRED_VALUE)
        f = Fraction(n, d)
        if f == DESIRED_VALUE:
            f = Fraction(n - 1, d)
        fractions.append(f)
    return max(fractions).numerator


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
