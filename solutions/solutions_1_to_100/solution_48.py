"""
Challenge 48 of project euler - Self Powers

@author Ori Dabush
"""

UPPER_LIMIT = 1000


def solve():
    return str(sum(i ** i for i in range(1, UPPER_LIMIT + 1)))[-10:]


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
