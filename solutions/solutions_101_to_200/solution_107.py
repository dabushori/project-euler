"""
Challenge 107 of project euler - Minimal Network

@author Ori Dabush
"""

from solutions.utils.inputs import get_input_file_path
import numpy as np
from solutions.utils.mst import find_mst


def solve():
    input_file_path = get_input_file_path(107)
    neighbors_matrix = np.genfromtxt(input_file_path, delimiter=',', dtype=float, missing_values='-', filling_values=np.nan)
    original_graph_weight = np.nansum(np.triu(neighbors_matrix))
    mst = find_mst(neighbors_matrix)
    mst_graph_weight = np.nansum(np.triu(mst))
    return int(original_graph_weight - mst_graph_weight)


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
