"""
Run's Prim's Algorithm

Author: Nicholas Butzke
"""
from math import inf
import numpy as np
from prims_algorithm import prims


def main():
    """
    Main wrapper functions
    """
    graph_1 = [
        # 1   2    3    4    5    6   7   8    9    10
        [inf, 32, inf, 17, inf, inf, inf, inf, inf, inf],  # 1
        [32, inf, inf, inf, 45, inf, inf, inf, inf, inf],  # 2
        [inf, inf, inf, 18, inf, inf, 5, inf, inf, inf],  # 3
        [17, inf, 18, inf, 10, inf, inf, 3, inf, inf],  # 4
        [inf, 45, inf, 10, inf, 28, inf, inf, 25, inf],  # 5
        [inf, inf, inf, inf, 28, inf, inf, inf, inf, 6],  # 6
        [inf, inf, 5, inf, inf, inf, inf, 59, inf, inf],  # 7
        [inf, inf, inf, 3, inf, inf, 59, inf, 4, inf],  # 8
        [inf, inf, inf, inf, 25, inf, inf, 4, inf, 12],  # 9
        [inf, inf, inf, inf, inf, 6, inf, inf, 12, inf],  # 10
    ]
    graph_2 = [
        [inf, inf, 72, 50, 90, 35],
        [inf, inf, 71, 70, 73, 75],
        [72, 71, inf, inf, 77, 90],
        [50, 70, inf, inf, 60, 40],
        [90, 73, 77, 60, inf, 80],
        [35, 75, 90, 40, 80, inf],
    ]
    minimum_spanning_tree, total_cost = prims(4, graph_2)
    numpy_mst = np.array(minimum_spanning_tree)
    print(f"Minimum spanning tree: {numpy_mst + 1}")
    print(f"Total cost: {total_cost}")


if __name__ == "__main__":
    main()
