"""
Challenge 15 of project euler - Lattice Paths

@author Ori Dabush
"""
from math import comb


GRID_ROWS, GRID_COLUMNS = 20, 20


def solve():
    """
    There are only GRID_ROWS * GRID_COLUMNS steps to take, and we need to count the number of options to order them.
    This is equivalent to choosing GRID_ROWS objects out of GRID_ROWS + GRID_COLUMNS, which is equal to:
    (GRID_ROWS + GRID_COLUMNS) choose GRID_ROWS
    """
    return comb(GRID_ROWS + GRID_COLUMNS, GRID_ROWS)


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
