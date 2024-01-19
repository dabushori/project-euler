"""
Challenge 65 of project euler - Convergents of e

@author Ori Dabush
"""


from fractions import Fraction


DIGIT_INDEX = 100


def get_representation_of_e_at(n: int):
    """
    The representation's index is 0 based
    """
    if n == 0:
        return 2
    if n % 3 == 2:
        return ((n // 3) + 1) * 2
    return 1


def get_e_fraction(n: int):
    """
    The fraction's index is 0 based
    """
    result = Fraction(get_representation_of_e_at(n), 1)
    for i in reversed(range(n)):
        result = 1 / result + get_representation_of_e_at(i)
    return result


def sum_digits(number: int) -> int:
    return sum(map(int, str(number)))


def solve():
    # Zero based index
    return sum_digits(get_e_fraction(DIGIT_INDEX - 1).numerator)


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
