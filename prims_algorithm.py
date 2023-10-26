"""
Author: Nicholas Butzke
"""
from math import inf


def prims(beginning_vertex, graph: list[list[int]]):
    """
    Prims Algorithm
    """
    minimum_spanning_tree = [beginning_vertex - 1]
    total_cost = 0

    # setting the edges travling to the beginning vertex to inf
    for vertex in graph:
        vertex[beginning_vertex - 1] = inf

    # only need to find one path to each vertex
    # we started with one vertex in the mst
    # therefore loop n-1 times
    for _ in range(len(graph) - 1):
        optimal_costs = []
        optimal_destinations = []
        for vertex in minimum_spanning_tree:
            # find the cheapest paths from the available vertices
            local_optimum = min(graph[vertex])
            optimal_costs.append(local_optimum)
            optimal_destinations.append(graph[vertex].index(local_optimum))
        # of the shortest paths from each vertex, find the absolute cheapest
        global_optimum = min(optimal_costs)
        # print(global_optimum)  # use this for debugging

        # find the vertex we are traveling to so we can avoid it in the future and add it to the mst
        destination = optimal_destinations[optimal_costs.index(global_optimum)]

        for source in graph:
            source[destination] = inf

        # Add the new vertex and cost to the final output
        minimum_spanning_tree.append(destination)
        total_cost += global_optimum
    return minimum_spanning_tree, total_cost
