"""
Challenge 14 of project euler - Longest Collatz Sequence

@author Ori Dabush
"""
from functools import cache


UPPER_LIMIT = 1_000_000


@cache
def get_collatz_sequence_length(start: int):
    if start == 1:
        return 1
    if start % 2 == 0:
        next_element = start // 2
    else:
        next_element = 3 * start + 1
    return 1 + get_collatz_sequence_length(next_element)


def solve():
    return max(range(1, UPPER_LIMIT), key=lambda number: get_collatz_sequence_length(number))


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
