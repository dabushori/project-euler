"""
Challenge 30 of project euler - Digit Fifth Powers

@author Ori Dabush
"""

WANTED_POWER = 5
UPPER_LIMIT = 10 ** 6


def sum_of_digits_powers(number: int, power: int) -> int:
    # An optimization to avoid calculating the powers of the digits every time
    powers = {digit: digit ** power for digit in range(10)}
    return sum(powers[digit] for digit in map(int, str(number)))


def solve():
    """
    We know that the sum of the digits of n is lower than k * (9 ** 5) where k is the number of digits in n.
    We also know that the n is greater than 10 ** (k - 1).
    We can skip the cases where k * (9 ** 5) < 10 ** (k - 1) because then:
    sum of digits <= k * (9 ** 5) < 10 ** (k - 1) <= n.
    These condition holds where k > 6, which means it is enough to check the numbers until 10 ** k.
    """
    return sum(number for number in range(10, UPPER_LIMIT) if sum_of_digits_powers(number, WANTED_POWER) == number)


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
