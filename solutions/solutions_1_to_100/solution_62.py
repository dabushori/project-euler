"""
Challenge 62 of project euler - Cubic Permutations

@author Ori Dabush
"""

from itertools import count


DESIRED_PERMUTATION_COUNT = 5


def is_permutation_with_zeros(number_1: int, number_2: int) -> bool:
    return sorted(str(number_1).replace('0', '')) == sorted(str(number_2).replace('0', ''))


def is_permutation(number_1: int, number_2: int) -> bool:
    return sorted(str(number_1)) == sorted(str(number_2))


def number_of_digits(number: int) -> int:
    return len(str(number))


def solve():
    for current_number_of_digits in count():
        start_number = int((10 ** (current_number_of_digits - 1)) ** (1 / 3) + 1)
        end_number = int((10 ** current_number_of_digits) ** (1 / 3))
        candidates = {n ** 3 for n in range(start_number, end_number)}
        while len(candidates) > 0:
            candidate = candidates.pop()
            permutations = {candidate}
            for permutation in list(candidates.copy()):
                if is_permutation(candidate, permutation):
                    candidates.remove(permutation)
                    permutations.add(permutation)
            if len(permutations) == DESIRED_PERMUTATION_COUNT:
                return min(permutations)


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
