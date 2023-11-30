from collections import deque


def bfs_shortest_path(graph, start, end):
    # Keep track of explored nodes
    explored = set()
    # Keep track of all the paths to be checked
    queue = deque([[start]])

    # Return path if start is end
    if start == end:
        return [start]

    # Keeps looping until all possible paths have been checked
    while queue:
        # Pop the first path from the queue
        path = queue.popleft()
        # Get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # Go through all neighbour nodes, construct a new path and push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # Return path if neighbour is end
                if neighbour == end:
                    return new_path
            # Mark node as explored
            explored.add(node)

    # In case there's no path between the 2 nodes
    return "No path exists between {} and {}".format(start, end)


if __name__ == '__main__':
    # Example Usage
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    start = 'A'
    end = 'F'
    print(bfs_shortest_path(graph, start, end))  # Returns the shortest path from A to F
