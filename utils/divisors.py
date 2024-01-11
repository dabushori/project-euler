from math import floor


def get_divisors(number: int):
    if number <= 0:
        raise ValueError('Invalid number')
    for candidate in range(1, floor(number ** 0.5) + 1):
        if number % candidate == 0:
            yield candidate
            other_candidate = number // candidate
            if other_candidate != candidate:
                yield other_candidate
