import numpy as np


def _get_neighbors(neighbors_matrix, i):
    """
    Get the neighbors of the node i.
    """
    number_of_nodes = neighbors_matrix.shape[0]
    for j in range(number_of_nodes):
        if not np.isnan(neighbors_matrix[i, j]):
            yield j


def _does_path_exists(neighbors_matrix, i, j):
    """
    Check if there exists a path from i to j using BFS.
    """
    nodes_visited = set()
    nodes_to_visit = {i}
    while nodes_to_visit:
        current_node = nodes_to_visit.pop()
        for neighbor in _get_neighbors(neighbors_matrix, current_node):
            if neighbor == j:
                return True
            if neighbor not in nodes_visited:
                nodes_to_visit.add(neighbor)
            nodes_visited.add(current_node)
    return False


def _find_max_redundant_edge(neighbors_matrix: np.ndarray) -> tuple[int, int]|None:
    """
    Find the maximum weighted edge that the removal of it will keep the graph connected (i.e. it is redundant).
    """
    rows, cols = neighbors_matrix.shape
    edges = [
        ((i, j), neighbors_matrix[i, j])
        for i in range(rows) for j in range(i + 1, cols)
        if not np.isnan(neighbors_matrix[i, j])
    ]
    # Iterate the edges from the max weighted edge
    edges.sort(key=lambda edge: edge[1], reverse=True)
    for (i, j), _ in edges:
        new_neighbors_matrix = neighbors_matrix.copy()
        new_neighbors_matrix[i, j] = new_neighbors_matrix[j, i] = np.nan
        # If the edge disconnected the graph, it must have disconnect the 2 nodes it connected before - so it is enough to check them.
        if _does_path_exists(new_neighbors_matrix, i, j):
            # The graph is still connected so the edge is redundant, return it
            return (i, j)
    return None


def find_mst(neighbors_matrix: np.ndarray) -> np.ndarray:
    """
    Use a greedy algo to find an MST (Prim's algorithm).
    The algo removed the max weighted redundant edge until there isn't one.
    """
    mst = neighbors_matrix.copy()
    while edge_to_remove := _find_max_redundant_edge(mst):
        i, j = edge_to_remove
        mst[i, j] = mst[j, i] = np.nan
    return mst
