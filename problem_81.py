"""
Challenge 81 of project euler - Path Sum: Two Ways

@author Ori Dabush
"""

from utils.inputs import get_input
from functools import cache


@cache
def find_minimal_path_sum(matrix: tuple[tuple[int]]) -> int:
    rows = len(matrix)
    columns = len(matrix[0])
    if rows == 1:
        return sum(matrix[0])
    if columns == 1:
        return sum(row[0] for row in matrix)
    return matrix[0][0] + min(
        find_minimal_path_sum(matrix[1:]),
        find_minimal_path_sum(tuple(row[1:] for row in matrix))
    )


def solve():
    matrix = get_input(81)
    matrix = tuple(tuple(map(int, line.split(','))) for line in matrix.split())
    return find_minimal_path_sum(matrix)


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
