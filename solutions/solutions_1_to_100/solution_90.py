"""
Challenge 90 of project euler - Cube Digit Pairs

@author Ori Dabush
"""

from itertools import combinations, product


SQUARES = [tuple(map(int, f'{x ** 2:02}')) for x in range(1, 10)]


def is_good_arrangement(a1: set[int], a2: set[int]) -> bool:
    for d1, d2 in SQUARES:
        if not ((d1 in a1 and d2 in a2) or (d1 in a2 and d2 in a1)):
            return False
    return True


def solve():
    """
    There are very few options for digits arrangement, so might as well brute force.
    """
    result = 0
    for a1, a2 in product(list(combinations(range(10), 6)), repeat=2):
        a1, a2 = set(a1), set(a2)
        if 6 in a1 or 9 in a1:
            a1 = a1.union({6, 9})
        if 6 in a2 or 9 in a2:
            a2 = a2.union({6, 9})
        if is_good_arrangement(a1, a2):
            result += 1
    # Divide by 2 because of duplicates
    return result // 2


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
