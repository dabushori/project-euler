from itertools import count


def get_heptagonal_number(n: int) -> int:
    return n * (5 * n - 3) // 2


def get_heptagonal_numbers(start: int = 1, end: int | None = None, indexed: bool = False):
    generator = range(start, end) if end is not None else count(start=start)
    for n in generator:
        yield (n, get_heptagonal_number(n)) if indexed else get_heptagonal_number(n)


def get_heptagonal_numbers_until(upper_limit: int):
    for number in get_heptagonal_numbers():
        if number > upper_limit:
            break
        yield number
