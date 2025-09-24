"""
Challenge 75 of project euler - Singular Integer Right Triangles

@author Ori Dabush
"""

from math import gcd
from collections import defaultdict


MAX_VALUE = 1500000


def solve():
    """
    By Euclid's formula all primitive Pythagorean triples can be generated from integers m > n > 0 where:
    * m + n is odd
    * gcd(m, n) = 1
    We can find all the L values of primitive triples. Then, we check all their multiple and count all the L values
    which are multiple of exactly 1 primitive L value.
    """
    primitive_l_values = []
    for m in range(2, MAX_VALUE):
        # Make sure m + n is odd
        min_n = 1 if m % 2 == 0 else 2
        for n in range(min_n, m, 2):
            # Make sure L doesn't exceed the max value
            if 2 * m * (m + n) > MAX_VALUE:
                break
            # Make sure gcd(m, n) == 1
            if gcd(m, n) == 1:
                primitive_l_values.append(2 * m * (m + n))
    l_counts = defaultdict(int)
    for primitive_l in primitive_l_values:
        for l_multiple in range(primitive_l, MAX_VALUE, primitive_l):
            l_counts[l_multiple] += 1
    return len([l_count for l_count in l_counts.values() if l_count == 1])


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
