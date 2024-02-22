"""
Challenge 80 of project euler - Square Root Digital Expansion

@author Ori Dabush
"""

from decimal import Decimal, getcontext


NUMBER_COUNT = 100
DIGIT_PRECISION = 100


def sum_decimal_digits(f: Decimal) -> int:
    f = str(f).replace('.', '')
    return sum(map(int, f[:DIGIT_PRECISION]))


def solve():
    getcontext().prec = DIGIT_PRECISION + 1
    result = 0
    for number in range(1, NUMBER_COUNT + 1):
        if Decimal(number).sqrt() == int(Decimal(number).sqrt()):
            continue
        result += sum_decimal_digits(Decimal(number).sqrt())
    return result


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
