"""
Challenge 2 of project euler - Even Fibonacci Numbers

@author Ori Dabush
"""
from solutions.utils.fibonacci import fibonacci_until


UPPER_LIMIT = 4_000_000


def solve():
    return sum(element for element in fibonacci_until(UPPER_LIMIT) if element % 2 == 0)


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
