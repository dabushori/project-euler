"""
Challenge 43 of project euler - Sub-string Divisibility

@author Ori Dabush
"""

from utils.pandigitals import get_pandigital_numbers_in_custom_range


CONSTRAINTS = [
    # (start_index, end_index, divisor)
    (2, 5, 2),
    (3, 6, 3),
    (4, 7, 5),
    (5, 8, 7),
    (6, 9, 11),
    (7, 10, 13),
    (8, 11, 17),
]


def is_substring_divisible(number: str) -> bool:
    for start, end, divisor in CONSTRAINTS:
        # The indexes in constraints are 1-based
        start -= 1
        end -= 1
        if int(number[start:end]) % divisor != 0:
            return False
    return True


def solve():
    return sum(
        int(pandigital)
        for pandigital in get_pandigital_numbers_in_custom_range(0, 9, as_strings=True)
        if is_substring_divisible(pandigital)
    )


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
