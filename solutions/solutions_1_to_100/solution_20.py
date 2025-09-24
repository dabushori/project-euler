"""
Challenge 20 of project euler - Factorial Digit Sum

@author Ori Dabush
"""

from math import factorial


INPUT_NUMBER = 100


def solve():
    return sum(list(map(int, str(factorial(INPUT_NUMBER)))))


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
