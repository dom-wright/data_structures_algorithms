'''
Dijkstra's algorithm

Dijkstra's algorithm computes the shortest distance from a given vertex to every other vertex in the graph, returning a dictionary of the results.

Process:
- Instantiate a dictionary that will eventually map vertices to their distance from the start vertex.
- Assign the start vertex a distance of 0 in a min heap (0 to itself).
- Assign every other vertex a distance of infinity in a min heap
- Remove the vertex with the smallest distance from the min heap and set that to the current vertex
- For the current vertex, consider all of its adjacent vertices and calculate the distance to them as (distance to current vertex) + (edge weight of current vertex to all adjacent vertices).
- If this new distance is less than the current distance recorded for that destination vertex, replace the current distance.
- Repeat the last two steps until the heap is empty, and all min-distances have been calculated.
- After the heap is empty, return the distances.

Runtime:
The runtime is O (E+V)log V
e - edges 
v - vertices
log V - as the heap will reduce the number of routes when a faster route is found.
'''

from heapq import heappop, heappush
from math import inf

graph = {
    'A': [('B', 10), ('C', 3)],
    'C': [('D', 2)],
    'D': [('E', 10)],
    'E': [('A', 7)],
    'B': [('C', 3), ('D', 2)]
}


def dijkstras(graph, start):
    distances = {}

    for vertex in graph:
        distances[vertex] = inf

    distances[start] = 0
    vertices_to_explore = [(0, start)]

    while vertices_to_explore:
        current_distance, current_vertex = heappop(vertices_to_explore)

        for neighbor, edge_weight in graph[current_vertex]:
            new_distance = current_distance + edge_weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heappush(vertices_to_explore, (new_distance, neighbor))

    return distances


distances_from_d = dijkstras(graph, 'D')
print("\n\nShortest Distances: {0}".format(distances_from_d))
