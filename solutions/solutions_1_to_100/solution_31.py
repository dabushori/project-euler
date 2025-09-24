"""
Challenge 31 of project euler - Coin Sums

@author Ori Dabush
"""

from functools import cache


WANTED_SUM = 200
COINS = (200, 100, 50, 20, 10, 5, 2, 1)


@cache
def get_coins_options(total_sum: int, available_coins: tuple) -> list[list[int]]:
    available_coins = tuple(sorted(available_coins, reverse=True))
    options = []
    for index, coin in enumerate(available_coins):
        if coin == total_sum:
            options.append([coin])
        elif coin < total_sum:
            options.extend(
                [coin] + option
                for option in get_coins_options(total_sum - coin, available_coins[index:])
            )
    return options


def solve():
    return len(get_coins_options(WANTED_SUM, COINS))


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
