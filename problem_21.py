"""
Challenge 21 of project euler - Amicable Numbers

@author Ori Dabush
"""

from utils.divisors import get_divisors

UPPER_LIMIT = 10000
SUM_OF_PROPER_DIVISORS = {
    number: sum(divisor for divisor in get_divisors(number) if divisor != number)
    for number in range(1, UPPER_LIMIT + 1)
}


def is_amicable_number(number: int) -> bool:
    try:
        return number != SUM_OF_PROPER_DIVISORS[number] and SUM_OF_PROPER_DIVISORS[SUM_OF_PROPER_DIVISORS[number]] == number
    except KeyError:
        return False


def solve():
    return sum(number for number in range(1, UPPER_LIMIT) if is_amicable_number(number))


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
