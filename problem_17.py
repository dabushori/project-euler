"""
Challenge 17 of project euler - Number Letter Counts

@author Ori Dabush
"""
from utils.numbers import number_to_words


UPPER_LIMIT = 1000


def letter_count(s: str) -> int:
    return len([letter for letter in s if letter.isalpha()])


def solve():
    return sum(letter_count(number_to_words(number)) for number in range(1, UPPER_LIMIT + 1))


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
