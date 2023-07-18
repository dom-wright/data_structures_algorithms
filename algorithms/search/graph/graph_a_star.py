'''
A* algorithm

Similar concept to Dijkstra's algorithm, but used when there is a target vertex in mind (avoids routes that shouldn't be considered). It is considered a greedy algorithm, as it doesn't check every route, rather uses a form of intuition to check only the likely routes. 

Heuristic:
It does this using a heuristic, which is a practical approach for finding approximate solutions to complex problems. Heuristics are based on experience, intuition, or common sense, and are designed to guide the search for a solution by efficiently exploring the problem space. They are often tailored to specific problem domains and take advantage of domain-specific knowledge or constraints.

Example:
Two commonly used distance-related heuristics are the Manhattan and Euclidian heuristics:
Manhattan - grid-based, the heuristic is calculated by summing the x and y coordinates (as diagonal movement is not possible)
Euclidean - calculates the straight line distance using coordinates and the pythagorean formula.

Runtime:
The runtime of A* is O(b^d).
b - branching factor (average number of edges per vertex in graph
d - depth of the goal vertex.
In the worst case, we would look at all of the edges in the direction of the goal vertex until we reach the goal vertex.
'''


from math import inf, sqrt
from heapq import heappop, heappush
from data.manhattan_graph import manhattan_graph, penn_station, grand_central_station
from data.euclidean_graph import euclidean_graph, bengaluru, jaipur


# Manhattan Heuristic:
def heuristic(start, target):
    x_distance = abs(start.position[0] - target.position[0])
    y_distance = abs(start.position[1] - target.position[1])
    return x_distance + y_distance


# Euclidean Heuristic:
def heuristic(start, target):
    x_distance = abs(start.position[0] - target.position[0])
    y_distance = abs(start.position[1] - target.position[1])
    return sqrt(x_distance * x_distance + y_distance * y_distance)


def a_star(graph, start, target):
    print("Starting A* algorithm!")
    count = 0
    paths_and_distances = {}
    for vertex in graph:
        paths_and_distances[vertex] = [inf, [start.name]]

    paths_and_distances[start][0] = 0
    vertices_to_explore = [(0, start)]
    while vertices_to_explore and paths_and_distances[target][0] == inf:
        current_distance, current_vertex = heappop(vertices_to_explore)
        for neighbor, edge_weight in graph[current_vertex]:
            new_distance = current_distance + \
                edge_weight + heuristic(neighbor, target)
            new_path = paths_and_distances[current_vertex][1] + [neighbor.name]

            if new_distance < paths_and_distances[neighbor][0]:
                paths_and_distances[neighbor][0] = new_distance
                paths_and_distances[neighbor][1] = new_path
                heappush(vertices_to_explore, (new_distance, neighbor))
                count += 1
                print("At " + vertices_to_explore[0][1].name)

    print(
        f"Found a path from {start.name} to {target.name} in {count} steps: {paths_and_distances[target][1]}")

    return paths_and_distances[target][1]


a_star(manhattan_graph, penn_station, grand_central_station)
a_star(euclidean_graph, bengaluru, jaipur)
