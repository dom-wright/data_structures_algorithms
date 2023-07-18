'''
Vertices & Graphs

A graph is a non-linear data structure that consists of a set of vertices (also known as nodes) and a set of edges that connect these vertices. It is an abstraction that represents relationships or connections between different entities.
'''

from random import randrange


class Vertex:

    def __init__(self, value):
        self.value = value
        self.edges = {}

    def add_edge(self, vertex, weight=0):
        self.edges[vertex] = weight

    def get_edges(self):
        return list(self.edges)


class Graph:

    def __init__(self, directed=False):
        self.graph_dict = {}
        self.directed = directed

    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex, weight=0):
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(
                from_vertex.value, weight)

    def find_path(self, start_vertex, end_vertex):
        start = [start_vertex]
        seen = {}
        while len(start) > 0:
            current_vertex = start.pop(0)
            seen[current_vertex] = True
            print("Visiting " + current_vertex)
            if current_vertex == end_vertex:
                return True
            else:
                vertices_to_visit = set(
                    self.graph_dict[current_vertex].get_edges())
                # this next step will ensure vertices that have been tested are excluded.
                start += [vertex for vertex in vertices_to_visit if vertex not in seen]
        return False


def print_graph(graph):

    # loops through vertexes in graph and shows which vertexes they are linked to.
    for vertex in graph.graph_dict:
        print("")
        print(vertex + " connected to")
        vertex_neighbors = graph.graph_dict[vertex].edges
        if len(vertex_neighbors) == 0:
            print("No edges!")
        for adjacent_vertex in vertex_neighbors:
            print("=> " + adjacent_vertex)


def build_graph(directed):

    g = Graph(directed)
    vertices = []

    # create and add vertexes to graph, and a separate list that will contain references to the vertexes.
    for val in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        vertex = Vertex(val)
        vertices.append(vertex)
        g.add_vertex(vertex)

    # create random edges between vertexes.
    for v in range(len(vertices)):
        v_idx = randrange(0, len(vertices) - 1)
        v1 = vertices[v_idx]
        v_idx = randrange(0, len(vertices) - 1)
        v2 = vertices[v_idx]
        g.add_edge(v1, v2, randrange(1, 10))

    print_graph(g)
    return g


my_graph = build_graph(False)
