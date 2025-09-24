"""
Challenge 42 of project euler - Coded Triangle Numbers

@author Ori Dabush
"""

from solutions.utils.inputs import get_input
from solutions.utils.triangles import get_triangle_numbers_until


def get_letters_sum(word: str) -> int:
    if not word.isalpha():
        raise ValueError(f"{word} is not an alphabetical word")
    return sum(ord(letter) - ord('a') + 1 for letter in word.lower())


def solve():
    words = [name.strip('"') for name in get_input(42).split(',')]
    max_words_length = max(map(len, words))
    max_triangle_number = ord('z') * max_words_length
    triangle_numbers = list(get_triangle_numbers_until(max_triangle_number))
    return len([word for word in words if get_letters_sum(word) in triangle_numbers])


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
