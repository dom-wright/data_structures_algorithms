'''
Graph search - iterative
'''


from collections import deque


def iterative_search(graph, start_vertex, target_value):

    path = [start_vertex]
    vertex_and_path = [start_vertex, path]
    queue = deque()
    queue.append(vertex_and_path)
    visited = set()

    while queue:
        current_vertex_and_path = queue.pop()
        current_vertex, path = current_vertex_and_path
        visited.add(current_vertex)
        print(f"Testing path {path}")
        if current_vertex == target_value:
            return path

        for neighbor in graph[current_vertex]:
            if neighbor in visited:
                continue
            new_path = path[:]
            new_path.append(neighbor)
            new_vertex_and_path = [neighbor, new_path]
            queue.appendleft(new_vertex_and_path)
            # for depth-first, change to append.


the_most_dangerous_graph = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['lava', 'bees', 'lasers']),
    'piranhas': set(['lava', 'crocodiles']),
    'bees': set(['sharks']),
    'lasers': set(['sharks', 'crocodiles']),
    'crocodiles': set(['piranhas', 'lasers'])
}

print(iterative_search(the_most_dangerous_graph, "crocodiles", "bees"))
