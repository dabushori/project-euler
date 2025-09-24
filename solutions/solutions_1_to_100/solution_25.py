"""
Challenge 25 of project euler - 1000-digit Fibonacci Number

@author Ori Dabush
"""

from solutions.utils.fibonacci import fibonacci_from


NUMBER_OF_DIGITS = 1000
LOWER_LIMIT = 10 ** (NUMBER_OF_DIGITS - 1)


def solve():
    index, _ = next(fibonacci_from(LOWER_LIMIT, return_indexes=True))
    return index


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
