from copy import deepcopy


BOARD_SIDE = 3
BOARD_SIZE = BOARD_SIDE ** 2
INITIAL_TILE_VALUE = 0
POSSIBLE_VALUES = set(range(1, BOARD_SIZE + 1))


def iterate_row(row: int):
    for col in range(BOARD_SIZE):
        yield row, col


def iterate_col(col: int):
    for row in range(BOARD_SIZE):
        yield row, col


def iterate_box(coordinate_in_box: tuple[int, int]):
    row, col = coordinate_in_box
    row, col = row - row % BOARD_SIDE, col - col % BOARD_SIDE
    for i in range(BOARD_SIDE):
        for j in range(BOARD_SIDE):
            yield row + i, col + j


class Board(dict[tuple[int, int], int | set[int]]):
    def get_values_in_row(self, row: int) -> set[int]:
        return {self[coordinates] for coordinates in iterate_row(row)} - {INITIAL_TILE_VALUE}

    def get_values_in_col(self, col: int) -> set[int]:
        return {self[coordinates] for coordinates in iterate_col(col)} - {INITIAL_TILE_VALUE}

    def get_values_in_box(self, coordinate_in_box: tuple[int, int]) -> set[int]:
        return {self[coordinates] for coordinates in iterate_box(coordinate_in_box)} - {INITIAL_TILE_VALUE}

    def get_possible_values_in_row(self, row: int) -> set[int]:
        possible_values = set()
        for coordinates in iterate_row(row):
            values = self[coordinates]
            if type(values) is set:
                possible_values.update(values)
        return possible_values - {INITIAL_TILE_VALUE}

    def get_possible_values_in_col(self, col: int) -> set[int]:
        possible_values = set()
        for coordinates in iterate_col(col):
            values = self[coordinates]
            if type(values) is set:
                possible_values.update(values)
        return possible_values - {INITIAL_TILE_VALUE}

    def get_possible_values_in_box(self, coordinate_in_box: tuple[int, int]):
        possible_values = set()
        for coordinates in iterate_box(coordinate_in_box):
            values = self[coordinates]
            if type(values) is set:
                possible_values.update(values)
        return possible_values - {INITIAL_TILE_VALUE}

    def set_value(self, coordinates: tuple[int, int], value: int):
        """
        Set a value and remove it from the row, column and box.
        """
        row, col = coordinates
        # Remove the value from other undetermined tiles
        for i, j in iterate_row(row):
            if type(self[i, j]) is set and value in self[i, j]:
                self[i, j].remove(value)
        for i, j in iterate_col(col):
            if type(self[i, j]) is set and value in self[i, j]:
                self[i, j].remove(value)
        for i, j in iterate_box((row, col)):
            if type(self[i, j]) is set and value in self[i, j]:
                self[i, j].remove(value)
        self[row, col] = value

    def is_solved(self):
        return all(type(value) is int for value in self.values())

    def is_unsolvable(self):
        return any(type(value) is set and len(value) == 0 for value in self.values())


def _phase1(helper_board: Board) -> bool:
    """
    Place the tiles with only one option for a value
    """
    has_board_changed = False
    while True:
        for coordinates, value in helper_board.items():
            if type(value) is set and len(value) == 1:
                has_board_changed = True
                helper_board.set_value(coordinates, value.pop())
                break
        else:
            return has_board_changed


def _phase2_on_tile(helper_board: Board, coordinates: tuple[int, int]) -> bool:
    row, col = coordinates
    possible_values = helper_board[coordinates]
    if type(possible_values) is not set:
        return False
    for value in possible_values.copy():
        # Remove the value from the current tile so the get_value_in_* functions will get the other values
        possible_values.remove(value)
        # If this value is only in this tile in the current row, column or box, set it
        if (value not in helper_board.get_possible_values_in_row(row)
                or value not in helper_board.get_possible_values_in_col(col)
                or value not in helper_board.get_possible_values_in_box((row, col))):
            helper_board.set_value((row, col), value)
            break
        # Add the value back
        possible_values.add(value)
    else:
        # If no value was set
        return False
    return True


def _phase2(helper_board: Board) -> bool:
    """
    Look at every row, column and box and see if there's a value which can be only in 1 tile
    """
    has_board_changed = False
    while True:
        for coordinates in helper_board:
            if _phase2_on_tile(helper_board, coordinates):
                has_board_changed = True
                break
        else:
            return has_board_changed


def _final_phase(helper_board: Board) -> Board | None:
    """
    Brute force the first non-determined tile value and recursively solve the board
    """
    for (row, col), possible_values in helper_board.items():
        # Find the first non-determined tile and brute force its values
        if type(possible_values) is not set:
            continue
        # Try each value of the tile, if the board is solved - return it
        for value in possible_values:
            board_copy = deepcopy(helper_board)
            board_copy.set_value((row, col), value)
            solution = _solve_helper_board(board_copy)
            if solution is not None:
                return solution
        # Return None if no solution was found
        return None


def _solve_helper_board(helper_board: Board) -> Board | None:
    has_board_changed = True
    # Try phases 1 and 2 until the board is unsolvable or hasn't changed
    while has_board_changed:
        if helper_board.is_unsolvable():
            return None
        has_board_changed = _phase1(helper_board) or _phase2(helper_board)
    # If the board hasn't changed in phases 1 and 2, try brute forcing a value and continue recursively
    if not helper_board.is_solved():
        return _final_phase(helper_board)
    return helper_board


def solve_board(board: Board) -> Board:
    helper_board = Board(board.copy())
    # Create the options for every tile
    for (i, j), value in board.items():
        if value == INITIAL_TILE_VALUE:
            helper_board[i, j] = (POSSIBLE_VALUES -
                                  board.get_values_in_row(i) -
                                  board.get_values_in_col(j) -
                                  board.get_values_in_box((i, j)))
            if len(helper_board[i, j]) == 0:
                raise ValueError("Unsolvable board")
    solution = _solve_helper_board(helper_board)
    if solution is None:
        raise ValueError("Unsolvable board")
    return solution
