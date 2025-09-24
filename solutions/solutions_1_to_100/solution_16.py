"""
Challenge 16 of project euler - Power Digit Sum

@author Ori Dabush
"""


INPUT_NUMBER = 2 ** 1000


def solve():
    return sum(map(int, str(INPUT_NUMBER)))


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
