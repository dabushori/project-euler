from itertools import count


def get_hexagonal_number(n: int) -> int:
    return n * (2 * n - 1)


def get_hexagonal_numbers(start: int):
    for n in count(start=start):
        yield get_hexagonal_number(n)
