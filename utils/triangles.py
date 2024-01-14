from itertools import count
from functools import cache


@cache
def is_triangle_number(number: int) -> int:
    """
    n * (n + 1) // 2 = number
    n^2 + n - 2 * number = 0
    """
    if 1 + 4 * 2 * number < 0:
        # No solution to the equation
        return False
    n1 = (-1 + (1 + 4 * 2 * number) ** 0.5) / 2
    n2 = (-1 - (1 + 4 * 2 * number) ** 0.5) / 2
    return (n1 == int(n1) and n1 > 0) or (n2 == int(n2) and n2 > 0)


def get_triangle_number(n: int) -> int:
    return n * (n + 1) // 2


def get_triangle_numbers_until(upper_limit: int):
    for n in count(start=0):
        number = get_triangle_number(n)
        if number > upper_limit:
            break
        yield number


def get_triangle_numbers(start: int):
    for n in count(start=start):
        yield get_triangle_number(n)
