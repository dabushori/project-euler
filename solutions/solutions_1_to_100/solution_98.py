"""
Challenge 98 of project euler - Anagramic Squares

@author Ori Dabush
"""

from collections import defaultdict
from itertools import takewhile, count, combinations
from solutions.utils.inputs import get_input


SQUARES = []


def find_anagrams(words: list[str]) -> list[list[str]]:
    anagrams = defaultdict(list)
    for word in words:
        # Collect words by the letters in them
        anagrams[''.join(sorted(word))].append(word)
    return [anagram for anagram in anagrams.values() if len(anagram) > 1]


def to_pairs(anagrams: list[list[str]]) -> list[list[str]]:
    result = []
    for anagram in anagrams:
        if len(anagram) == 2:
            result.append(anagram)
        else:
            result.extend(combinations(anagram, 2))
    return result


def initialize_squares(max_word_length: int):
    global SQUARES
    upper_limit = 10 ** (max_word_length - 1)
    squares_iterator = map(lambda x: x**2, count(start=1))
    SQUARES = list(takewhile(lambda x: x < upper_limit, squares_iterator))


def check_anagramic_square(square_word: str, square: int, other_word: str) -> bool:
    letter_values = {}
    for letter, digit in zip(square_word, str(square)):
        if any(_digit == digit for _letter, _digit in letter_values.items() if _letter != letter):
            return False
        if letter not in letter_values:
            letter_values[letter] = digit
        elif letter_values[letter] != digit:
            return False
    translation_table = str.maketrans(letter_values)
    other_square = int(other_word.translate(translation_table))
    if other_square not in SQUARES or len(str(other_square)) != len(other_word):
        return False
    return True


def is_anagramic_square(anagram: list[str], square: int) -> bool:
    if len(anagram) != 2:
        raise ValueError('Supporting only pairs of anagrams')
    if len(anagram[0]) != len(str(square)):
        return False
    # Try assign square to anagram[0] and to anagram[1]
    return (check_anagramic_square(anagram[0], square, anagram[1]) or
            check_anagramic_square(anagram[1], square, anagram[0]))


def find_largest_anagramic_squares(anagram: list[str]) -> int:
    for square in reversed(SQUARES):
        if is_anagramic_square(anagram, square):
            return square
    return -1


def solve():
    words = [word.strip('"') for word in get_input(98).split(',')]
    anagrams = to_pairs(find_anagrams(words))
    initialize_squares(max(map(len, [anagram[0] for anagram in anagrams])))

    return max(find_largest_anagramic_squares(anagram) for anagram in anagrams)


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
