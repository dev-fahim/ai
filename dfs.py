from collections import deque


def iterative_dfs(graph, start, end):
    stack = deque([(start, [start])])
    visited = set()

    while stack:
        print(visited)
        vertex, path = stack.pop()
        if vertex == end:
            return path
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph[vertex]:
                stack.append((neighbor, path + [neighbor]))

    return None


# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': [],
}

if __name__ == '__main__':
    # Find path
    path = iterative_dfs(graph, 'A', 'E')
    print(path)
