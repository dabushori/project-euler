"""
Challenge 96 of project euler - Su Doku

@author Ori Dabush
"""

from utils.sudoku import solve_board, Board, BOARD_SIDE
from utils.inputs import get_input
import re


GRID_TITLE_REGEX = r"Grid \d+"
TOP_LEFT_COORDINATES = [(0, col) for col in range(BOARD_SIDE)]


def get_top_left_number(board: Board) -> int:
    if not board.is_solved():
        raise ValueError('Board is not solved')
    return int(''.join(str(board[coordinate]) for coordinate in TOP_LEFT_COORDINATES))


def create_board(rows: list[str]) -> Board:
    board = Board()
    for i, row in enumerate(rows):
        for j, value in enumerate(row):
            board[(i, j)] = int(value)
    return board


def solve():
    boards = [create_board(board.strip().split()) for board in re.split(GRID_TITLE_REGEX, get_input(96)) if board]
    solved_boards = [solve_board(board) for board in boards]
    return sum(get_top_left_number(board) for board in solved_boards)


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
