from itertools import count
from functools import cache


@cache
def is_pentagon_number(number: int) -> bool:
    """
    n * (3n - 1) / 2 = number
    3n^2 - n - 2 * number = 0
    """
    if 1 + 4 * 3 * 2 * number < 0:
        # No solution to the equation
        return False
    n1 = (1 + (1 + 4 * 3 * 2 * number) ** 0.5) / (2 * 3)
    n2 = (1 - (1 + 4 * 3 * 2 * number) ** 0.5) / (2 * 3)
    return (n1 == int(n1) and n1 > 0) or (n2 == int(n2) and n2 > 0)


def get_pentagon_number(n: int) -> int:
    return n * (3 * n - 1) // 2


def get_pentagon_numbers(start: int = 1, end: int | None = None, indexed: bool = False):
    generator = range(start, end) if end is not None else count(start=start)
    for n in generator:
        yield (n, get_pentagon_number(n)) if indexed else get_pentagon_number(n)


def get_pentagon_numbers_until(upper_limit: int):
    for number in get_pentagon_numbers():
        if number > upper_limit:
            break
        yield number
