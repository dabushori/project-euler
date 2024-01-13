from itertools import count


def get_triangle_number(n: int) -> int:
    return n * (n + 1) // 2


def get_triangle_numbers_until(upper_limit: int):
    for n in count(start=0):
        number = get_triangle_number(n)
        if number > upper_limit:
            break
        yield number
