"""
Challenge 6 of project euler - Sum Square Difference

@author Ori Dabush
"""

NUMBER_COUNT = 100


def get_sum_of_squares(number: int) -> int:
    # 1 ** 2 + 2 ** 2 + ... + n ** 2 = n * (n + 1) * (2n + 1) / 6
    return (number * (number + 1) * (2 * number + 1)) // 6


def solve():
    sum_of_squares = get_sum_of_squares(NUMBER_COUNT)
    square_of_sum = sum(range(1, NUMBER_COUNT + 1)) ** 2
    return square_of_sum - sum_of_squares


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
