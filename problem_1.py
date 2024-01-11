"""
Challenge 1 of project euler - Multiples of 3 or 5

@author Ori Dabush
"""


def solve():
    return sum(number for number in range(1000) if number % 3 == 0 or number % 5 == 0)


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
