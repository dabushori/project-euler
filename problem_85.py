"""
Challenge 85 of project euler - Counting Rectangles

@author Ori Dabush
"""

from math import ceil, inf


DESIRED_VALUE = 2_000_000


def number_of_rectangles(width: int, height: int) -> int:
    """
    The number of rectangles in a rectangle of (width, height) is equal to:
    sum(i * j for i in range(1, width + 1) for j in range(1, height + 1))

    After some math, this sum is equal to:
    0.25 * (width * (width + 1) * height * (height + 1))
    """
    return (width * (width + 1) * height * (height + 1)) // 4


def solve():
    """
    We know that (width * height) ** 2 // 4 <= DESIRED_VALUE, so height * width <= (4 * DESIRED_VALUE) ** 0.5.
    If we assume height <= width, we can see in particular that height <= width <= (4 * DESIRED_VALUE) ** 0.5.
    That gives us an upper limit.
    """
    area, closest_rectangles_count = inf, inf
    for width in range(1, ceil((4 * DESIRED_VALUE) ** 0.5) + 1):
        for height in range(1, width + 1):
            rectangles_count = number_of_rectangles(width, height)
            if abs(rectangles_count - DESIRED_VALUE) <= abs(closest_rectangles_count - DESIRED_VALUE):
                closest_rectangles_count = rectangles_count
                area = width * height
    return area


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
