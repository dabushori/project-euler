from itertools import count
from math import gcd, ceil, sqrt


def primitive_pythagorean_triples(max_hypotenuse: int | None = None):
    max_m = ceil(sqrt(max_hypotenuse / 2)) if max_hypotenuse is not None else None
    m_values = count(start=2) if max_m is None else range(2, max_m)
    for m in m_values:
        # Make sure m + n is odd
        min_n = 1 if m % 2 == 0 else 2
        for n in range(min_n, m, 2):
            # Make sure gcd(m, n) == 1
            if gcd(m, n) == 1:
                # m > m
                a, b = sorted([2 * m * n, m ** 2 - n ** 2])
                c = m ** 2 + n ** 2
                if c < max_hypotenuse:
                    yield a, b, c
