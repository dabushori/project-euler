"""
Challenge 52 of project euler - Permuted Multiples

@author Ori Dabush
"""

from itertools import count


MULTIPLICANDS = [1, 2, 3, 4, 5, 6]


def solve():
    for number in count(start=1):
        original_digits = sorted(str(number))
        for multiplicand in MULTIPLICANDS:
            if sorted(str(multiplicand * number)) != original_digits:
                break
        else:
            return number


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
