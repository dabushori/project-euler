"""
Challenge 34 of project euler - Digit Factorials

@author Ori Dabush
"""

from math import factorial


LOWER_LIMIT, UPPER_LIMIT = 10, 10 ** 7
FACTORIALS = {digit: factorial(digit) for digit in range(10)}


def sum_digits_factorials(number: int) -> int:
    return sum(FACTORIALS[digit] for digit in map(int, str(number)))


def solve():
    """
    We again need to limit the range of numbers we search in.
    We know that the sum of the digits' factorials of n must be <= 9! * k where k is the number of digits in n.
    We also know that n >= 10 ** (k - 1).
    It means that if 10 ** (k - 1) > 9! * k, n can't be equal to the sum of its digits' factorials.
    That inequality holds for every k > 7, so we can limit our search to numbers with at most 7 digits.
    """
    return sum(number for number in range(LOWER_LIMIT, UPPER_LIMIT) if sum_digits_factorials(number) == number)


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
