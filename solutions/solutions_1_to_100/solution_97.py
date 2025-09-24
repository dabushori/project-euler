"""
Challenge 97 of project euler - Large Non-Mersenne Prime

@author Ori Dabush
"""


DESIRED_NUMBER = 28433 * (2 ** 7830457) + 1
DESIRED_PRECISION = 10


def solve():
    return DESIRED_NUMBER % (10 ** DESIRED_PRECISION)


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
