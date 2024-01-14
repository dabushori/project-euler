"""
Challenge 59 of project euler - XOR Decryption

@author Ori Dabush
"""

from itertools import product, batched
from string import ascii_lowercase
from utils.inputs import get_input


def decode(cipher: list[int], key: list[int]) -> list[int]:
    result = []
    for current_cipher in batched(cipher, n=len(key)):
        for c, k in zip(current_cipher, key):
            result.append(c ^ k)
    return result


def solve():
    cipher = list(map(int, get_input(59).split(',')))
    max_space_count, max_plain = 0, None
    for key in product(map(ord, ascii_lowercase), repeat=3):
        plain = ''.join(map(chr, decode(cipher, list(key))))
        # Look for the plain with the most spaces
        if max_space_count < plain.count(' '):
            max_space_count = plain.count(' ')
            max_plain = plain
    return sum(map(ord, max_plain))


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
