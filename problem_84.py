"""
Challenge 84 of project euler - Monopoly Odds

@author Ori Dabush
"""

from collections import defaultdict
from fractions import Fraction
from functools import cache
from itertools import product


BOARD = [
    "GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3",
    "JAIL", "C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3",
    "FP", "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3",
    "G2J", "G1", "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2",
]
DICE = [4, 4]
assert (len(DICE) == 2 and DICE[0] == DICE[1]), "Invalid dice"
ROUNDS = 100
TILES_COUNT = 3


@cache
def get_dice_odds() -> dict[int, Fraction]:
    assert len(DICE) == 2, "Only 2 dice are supported"
    odds = defaultdict(Fraction)
    for d1, d2 in product(range(1, DICE[0] + 1), range(1, DICE[1] + 1)):
        odds[d1 + d2] += Fraction(1, DICE[0] * DICE[1])
    return odds


def move(tile: int, steps: int) -> int:
    return (tile + steps) % len(BOARD)


def odds_to_stay(tile: int) -> Fraction:
    tile_name = BOARD[tile]
    if tile_name.startswith('CC'):
        return Fraction(2, 16)
    if tile_name.startswith('CH'):
        return Fraction(10, 16)
    if tile_name.startswith('G2J'):
        return Fraction(0, 1)
    return Fraction(1, 1)


def get_next_tile(tile: int, target_name: str) -> int:
    for steps in range(1, len(BOARD) + 1):
        candidate_tile = move(tile, steps)
        candidate_tile_name = BOARD[candidate_tile]
        if candidate_tile_name.startswith(target_name):
            return candidate_tile
    raise ValueError('Broken monopoly')


def get_final_tile_odds(tile: int) -> dict[int, Fraction]:
    tile_name = BOARD[tile]
    if tile_name.startswith('CC'):
        return {
            BOARD.index('GO'): Fraction(1, 16),
            BOARD.index('JAIL'): Fraction(1, 16),
            tile: Fraction(14, 16),
        }
    if tile_name.startswith('CH'):
        return {
            BOARD.index('GO'): Fraction(1, 16),
            BOARD.index('JAIL'): Fraction(1, 16),
            BOARD.index('C1'): Fraction(1, 16),
            BOARD.index('E3'): Fraction(1, 16),
            BOARD.index('H2'): Fraction(1, 16),
            BOARD.index('R1'): Fraction(1, 16),
            get_next_tile(tile, 'R'): Fraction(2, 16),
            get_next_tile(tile, 'U'): Fraction(1, 16),
            move(tile, -3): Fraction(1, 16),
            tile: Fraction(6, 16),
        }
    if tile_name.startswith('G2J'):
        return {BOARD.index('JAIL'): Fraction(1, 1)}
    return {tile: Fraction(1, 1)}


@cache
def odds_for_current_round(current_tile: int) -> defaultdict[int, Fraction]:
    odds_for_jail = Fraction(1, DICE[0]) ** 3
    odds_to_stay_safe = Fraction(1, 1) - odds_for_jail
    result = defaultdict(Fraction, {BOARD.index('JAIL'): odds_for_jail})
    for dice_value, dice_odd in get_dice_odds().items():
        next_tile = move(current_tile, dice_value)
        for final_tile, odd in get_final_tile_odds(next_tile).items():
            result[final_tile] += odds_to_stay_safe * dice_odd * odd
    return result


def solve():
    current_tile = BOARD.index('GO')
    result = defaultdict(Fraction, {current_tile: Fraction(1, 1)})
    for _ in range(ROUNDS):
        for tile, tile_odd in result.copy().items():
            for final_tile, final_tile_odds in odds_for_current_round(tile).items():
                result[final_tile] += tile_odd * final_tile_odds
    common_tiles = sorted(result.keys(), key=result.__getitem__, reverse=True)
    return ''.join(f'{tile:02}' for tile in common_tiles[:TILES_COUNT])


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
