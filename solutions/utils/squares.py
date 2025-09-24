from itertools import count


def get_square_number(n: int) -> int:
    return n ** 2


def get_square_numbers(start: int = 1, end: int | None = None, indexed: bool = False):
    generator = range(start, end) if end is not None else count(start=start)
    for n in generator:
        yield (n, get_square_number(n)) if indexed else get_square_number(n)


def get_square_numbers_until(upper_limit: int):
    for number in get_square_numbers():
        if number > upper_limit:
            break
        yield number
