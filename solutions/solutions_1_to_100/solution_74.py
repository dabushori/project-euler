"""
Challenge 74 of project euler - Digit Factorial Chains

@author Ori Dabush
"""

from math import factorial


MIN_VALUE = 1
MAX_VALUE = 1_000_000
DESIRED_LOOP_LENGTH = 60
DIGITS_FACTORIAL = {str(digit): factorial(digit) for digit in range(0, 10)}


def sum_factorials_of_digits(n: int) -> int:
    return sum(DIGITS_FACTORIAL[digit] for digit in str(n))


def factorial_non_repeating_length(n: int) -> int:
    results = []
    while True:
        results.append(n)
        n = sum_factorials_of_digits(n)
        if n in results:
            return len(results)


def solve():
    return len([n for n in range(MIN_VALUE, MAX_VALUE) if factorial_non_repeating_length(n) == DESIRED_LOOP_LENGTH])


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
