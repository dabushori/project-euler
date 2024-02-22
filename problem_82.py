"""
Challenge 82 of project euler - Path Sum: Three Ways

@author Ori Dabush
"""

from utils.inputs import get_input
from functools import cache
from enum import IntEnum


class Direction(IntEnum):
    NONE = 0
    DOWN = 1
    UP = 2
    RIGHT = 3


@cache
def find_minimal_path_sum_inner(matrix: tuple[tuple[int]], row: int, column: int,
                                last_direction: Direction = Direction.NONE) -> int:
    rows = len(matrix)
    columns = len(matrix[0])
    current_tile = matrix[row][column]
    if column == columns - 1:
        return current_tile
    result = current_tile + find_minimal_path_sum_inner(matrix, row, column + 1, Direction.RIGHT)
    if last_direction != Direction.UP and row != rows - 1:
        result = min(result, current_tile + find_minimal_path_sum_inner(matrix, row + 1, column, Direction.DOWN))
    if last_direction != Direction.DOWN and row != 0:
        result = min(result, current_tile + find_minimal_path_sum_inner(matrix, row - 1, column, Direction.UP))
    return result


def find_minimal_path_sum(matrix: tuple[tuple[int]]) -> int:
    return min(find_minimal_path_sum_inner(matrix, i, 0) for i in range(len(matrix)))


def solve():
    matrix = get_input(82)
    matrix = tuple(tuple(map(int, line.split(','))) for line in matrix.split())
    return find_minimal_path_sum(matrix)


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
