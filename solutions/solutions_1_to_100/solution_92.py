"""
Challenge 92 of project euler - Square Digit Chains

@author Ori Dabush
"""

from functools import cache


DESIRED_TARGET = 89
TARGETS = {1, 89}
UPPER_LIMIT = 10_000_000


@cache
def get_target(n: int):
    if n in TARGETS:
        return n
    digits = map(int, str(n))
    return get_target(sum(d ** 2 for d in digits))


def solve():
    return sum(1 for n in range(1, UPPER_LIMIT + 1) if get_target(n) == DESIRED_TARGET)


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
