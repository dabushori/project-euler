"""
Challenge 68 of project euler - Magic 5-gon Ring

@author Ori Dabush
"""

from itertools import combinations, permutations


MAX_NUMBER = 10
NUMBERS = set(range(1, MAX_NUMBER + 1))
GROUPS_COUNT = MAX_NUMBER // 2


def ordered_combinations(iterable, r):
    for combination in combinations(iterable, r):
        yield from permutations(combination)


def solve():
    solutions = []
    for inner_numbers in ordered_combinations(list(NUMBERS), GROUPS_COUNT):
        for outer_numbers in permutations(list(NUMBERS - set(inner_numbers))):
            groups = [
                # Every 2 neighbor numbers and the outer number in offset 'offset' from idx
                (
                    outer_numbers[idx % len(outer_numbers)],
                    inner_numbers[idx],
                    inner_numbers[(idx + 1) % len(inner_numbers)],
                )
                for idx in range(len(inner_numbers))
            ]
            min_group_index = groups.index(min(groups, key=lambda group: group[0]))
            """
            The groups are sorted non-clockwise, start from the minimal outer, sort them from the minimal first
            number clockwise
            """
            groups = groups[min_group_index:] + groups[:min_group_index]
            if len({sum(group) for group in groups}) == 1 and groups not in solutions:
                solutions.append(groups)
    numbers = [''.join(''.join(map(str, group)) for group in solution) for solution in solutions]
    return max(numbers)


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
