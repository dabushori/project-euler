"""
Challenge 83 of project euler - Path Sum: Four Ways

@author Ori Dabush
"""

from solutions.utils.inputs import get_input
from itertools import product
from math import inf
from collections import defaultdict


def find_minimal_path_sum(matrix: tuple[tuple[int, ...], ...]) -> int:
    """
    An implementation of Dijkstra's algorithm to the shortest path problem.
    The nodes are the matrix tiles and the weight of an edge from m[i,j] to m[k,l] is the value of m[k,l].
    """
    rows, columns = len(matrix), len(matrix[0])
    unvisited_nodes = list(product(range(rows), range(columns)))
    distances = defaultdict(lambda: inf)
    initial_node, target_node = (0, 0), (rows - 1, columns - 1)
    # The initial distance is the value of the initial tile and not 0 because it will be part of the path weight
    distances[initial_node] = matrix[0][0] 
    while target_node in unvisited_nodes and min(unvisited_nodes, key=distances.__getitem__) != inf:
        # Get the node with minimal tentative distance
        current_node = min(unvisited_nodes, key=distances.__getitem__)
        unvisited_nodes.remove(current_node)
        row, column = current_node
        # Update the neighbors if needed
        if row > 0:
            neighbor = (row - 1, column)
            distances[neighbor] = min(distances[neighbor], distances[current_node] + matrix[row - 1][column])
        if row < rows - 1:
            neighbor = (row + 1, column)
            distances[neighbor] = min(distances[neighbor], distances[current_node] + matrix[row + 1][column])
        if column > 0:
            neighbor = (row, column - 1)
            distances[neighbor] = min(distances[neighbor], distances[current_node] + matrix[row][column - 1])
        if column < columns - 1:
            neighbor = (row, column + 1)
            distances[neighbor] = min(distances[neighbor], distances[current_node] + matrix[row][column + 1])
    return int(distances[target_node])


def solve():
    matrix = get_input(83)
    matrix = tuple(tuple(map(int, line.split(','))) for line in matrix.split())
    return find_minimal_path_sum(matrix)


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
