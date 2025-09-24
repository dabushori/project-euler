"""
Challenge 61 of project euler - Cyclical Figurate Numbers

@author Ori Dabush
"""

from solutions.utils.triangles import get_triangle_numbers_until
from solutions.utils.squares import get_square_numbers_until
from solutions.utils.pentagons import get_pentagon_numbers_until
from solutions.utils.hexagonals import get_hexagonal_numbers_until
from solutions.utils.heptagonals import get_heptagonal_numbers_until
from solutions.utils.octagonal import get_octagonal_numbers_until


LOWER_LIMIT, UPPER_LIMIT = 1000, 10000
NUMBER_OF_DIGITS_TO_COMPARE = 2


def matching_digits(first_number: int, second_number: int) -> bool:
    return str(first_number)[-NUMBER_OF_DIGITS_TO_COMPARE:] == str(second_number)[:NUMBER_OF_DIGITS_TO_COMPARE]


def _find_cyclical_numbers_helper(remaining_sets: list[list[int]], current_group: list[int]) -> list[int] | None:
    if len(remaining_sets) == 0:
        return current_group
    for set_index, _set in enumerate(remaining_sets):
        for number in _set:
            # Check the current number and the previous one
            if (matching_digits(current_group[-1], number) and
                    # Check the last and first number if this is the last number
                    (len(remaining_sets) != 1 or matching_digits(number, current_group[0]))):
                result = _find_cyclical_numbers_helper(
                    remaining_sets[:set_index] + remaining_sets[set_index + 1:],
                    current_group + [number]
                )
                if result is not None:
                    return result
    return None


def find_cyclical_numbers(number_sets: list[list[int]]):
    if len(number_sets) == 0:
        raise ValueError("No number sets")
    for starting_number in number_sets[0]:
        result = _find_cyclical_numbers_helper(number_sets[1:], [starting_number])
        if result is not None:
            return result
    return None


def solve():
    triangles = [number for number in get_triangle_numbers_until(UPPER_LIMIT) if number >= LOWER_LIMIT]
    squares = [number for number in get_square_numbers_until(UPPER_LIMIT) if number >= LOWER_LIMIT]
    pentagonals = [number for number in get_pentagon_numbers_until(UPPER_LIMIT) if number >= LOWER_LIMIT]
    hexagonals = [number for number in get_hexagonal_numbers_until(UPPER_LIMIT) if number >= LOWER_LIMIT]
    heptagonals = [number for number in get_heptagonal_numbers_until(UPPER_LIMIT) if number >= LOWER_LIMIT]
    octagonals = [number for number in get_octagonal_numbers_until(UPPER_LIMIT) if number >= LOWER_LIMIT]
    number_sets = [triangles, squares, pentagonals, hexagonals, heptagonals, octagonals]
    return sum(find_cyclical_numbers(number_sets))


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
