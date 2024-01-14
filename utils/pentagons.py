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


def get_pentagon_numbers(start: int = 1, step: int = 1, indexed: bool = False):
    n = start
    for _ in count():
        yield (n, get_pentagon_number(n)) if indexed else get_pentagon_number(n)
        n += step
