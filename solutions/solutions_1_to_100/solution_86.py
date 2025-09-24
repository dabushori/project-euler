"""
Challenge 86 of project euler - Cuboid Route

@author Ori Dabush
"""

from collections import defaultdict
from itertools import count
from math import sqrt, ceil
from solutions.utils.pythagorean_triples import primitive_pythagorean_triples


INITIAL_M_VALUE = 100
INITIAL_NUMBER_OF_CUBOIDS = 2060
DESIRED_NUMBER_OF_CUBOIDS = 1_000_000
MAX_M_VALUE_GUESS = 2000


def get_shortest_path(a: int, b: int, c: int) -> float:
    """
    This function assumes that a >= b >= c
    """
    return sqrt((b + c) ** 2 + a ** 2)


def solve_slow():
    """
    Assuming the edges of the cuboid are a, b and c, the shortest linear path from S to F must be 2 hypotenuses of 2
    right triangles, which edges are the cuboid's edges.
    There are 3 ways to create such triangles:
    1. first triangles legs are 'a' and 'x', second triangle legs are 'b - x' and 'c'.
    2. first triangles legs are 'c' and 'x', second triangle legs are 'a - x' and 'b'.
    3. first triangles legs are 'b' and 'x', second triangle legs are 'c - x' and 'a'.

    After applying some math (calculating the hypotenuses of the triangles and finding x that minimizes the sum of them)
    we get that on each case:
    1. 'x = ab / (a + c)'
    2. 'x = ca / (b + c)'
    3. 'x = bc / (a + b)'

    From these solutions we can see that the path length for each of these solutions is:
    1. 'sqrt((a + c) ** 2 + b ** 2)'
    2. 'sqrt((b + c) ** 2 + a ** 2)'
    3. 'sqrt((a + b) ** 2 + c ** 2)'

    We can see that the solutions are sqrt(a ** 2 + b ** 2 + c ** 2 + 2xy), where x, y are 2 edges of the cuboid.
    We can derive from that the minimal path is when x and y the 2 minimal edges of the cuboid.
    """
    number_of_cuboids = INITIAL_NUMBER_OF_CUBOIDS
    values = []
    for M in count(start=INITIAL_M_VALUE):
        print(M, number_of_cuboids)
        # 'a = M', 1 <= b <= c < M
        a = M
        for b in range(1, M + 1):
            for c in range(1, b + 1):
                # M = a > b >= c
                if get_shortest_path(a, b, c).is_integer():
                    values.append((a, b, c))
                    number_of_cuboids += 1
        if number_of_cuboids >= DESIRED_NUMBER_OF_CUBOIDS:
            # from pprint import pprint
            # pprint(values)
            return M


def find_m_value(max_m: int) -> int | None:
    """
    Instead of iterating on every value of a, b and c, iterate only on pythagorean triples (x, y, z)
    and count the number of ways to split x or y to be a + b. The minimum path will be z.
    """
    results = defaultdict(int)
    for a, b, c in primitive_pythagorean_triples(6 * max_m):
        for k in count(start=1):
            ka, kb, kc = k * a, k * b, k * c
            if kb > 3 * max_m:
                break
            # Number of ways to split 'a' into the 2 short edges of the cuboid
            results[kb] += ceil((ka - 1) / 2)
            # Number of ways to split 'b' into the 2 short edges of the cuboid
            if kb <= 2 * ka:
                results[ka] += ceil(((kb - 1) - 2 * (min(ka, kb - ka) - 1)) / 2)
    accumulated_m_values = defaultdict(int)
    for m in range(1, max_m):
        accumulated_m_values[m] = accumulated_m_values[m - 1] + results[m]
    m_values_over_desired_value = [m for m, value in accumulated_m_values.items() if value >= DESIRED_NUMBER_OF_CUBOIDS]
    return min(m_values_over_desired_value) if m_values_over_desired_value else None


def solve():
    max_m_guess = 1
    while True:
        m = find_m_value(max_m_guess)
        if m is not None:
            return m
        max_m_guess *= 2


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
