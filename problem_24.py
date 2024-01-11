"""
Challenge 24 of project euler - Lexicographic Permutations

@author Ori Dabush
"""

from math import factorial


PERMUTATION_INDEX = 1_000_000


def get_nth_lexicographic_permutation(n: int, digits: list[str]):
    """
    n here is zero based, so we actually pass 999999 to it.
    """
    assert digits == sorted(digits), "The given digits are not sorted"
    if n >= factorial(len(digits)):
        raise ValueError(f"{n} is not a valid permutation index of {digits}")
    if not digits:
        return ''
    first_digit_index = n // factorial(len(digits) - 1)
    reminder = n % factorial(len(digits) - 1)
    first_digit = digits[first_digit_index]
    new_digits = digits[:first_digit_index] + digits[first_digit_index + 1:]
    print(first_digit, reminder, first_digit)
    return first_digit + get_nth_lexicographic_permutation(reminder, new_digits)


def solve():
    return get_nth_lexicographic_permutation(PERMUTATION_INDEX - 1, list(map(str, range(10))))


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
