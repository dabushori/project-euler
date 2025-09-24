"""
Challenge 22 of project euler - Names Scores

@author Ori Dabush
"""

from solutions.utils.inputs import get_input


def alphabetical_value(string: str) -> int:
    if not string.isalpha():
        raise ValueError(f"{string} is not alphabetical")
    return sum(ord(letter) - ord('a') + 1 for letter in string.lower())


def solve():
    names = sorted([name.strip('"') for name in get_input(22).split(',')])
    return sum(index * alphabetical_value(name) for index, name in enumerate(names, start=1))


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
