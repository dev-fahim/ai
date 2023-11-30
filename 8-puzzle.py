from heapq import heappush, heappop


def manhattan_distance(state, goal):
    distance = 0
    for i in range(1, 9):
        xi, yi = divmod(state.index(i), 3)
        xg, yg = divmod(goal.index(i), 3)
        distance += abs(xi - xg) + abs(yi - yg)
    return distance


def a_star_8_puzzle(start, goal):
    def get_neighbors(state):
        neighbors = []
        index = state.index(0)  # Find the zero (empty space) in the current state
        x, y = divmod(index, 3)

        # Directions the empty space can move
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                neighbor = list(state)
                neighbor[index], neighbor[nx * 3 + ny] = neighbor[nx * 3 + ny], neighbor[index]
                neighbors.append(tuple(neighbor))
        return neighbors

    open_set = [(manhattan_distance(start, goal), start)]
    came_from = {start: None}
    g_score = {start: 0}

    while open_set:
        _, current = heappop(open_set)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for neighbor in get_neighbors(current):
            tentative_g_score = g_score[current] + 1  # All edges have the same cost
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + manhattan_distance(neighbor, goal)
                heappush(open_set, (f_score, neighbor))

    return None


if __name__ == '__main__':
    # Example
    start = (1, 2, 3, 4, 5, 6, 7, 8, 0)  # Representing the board as a tuple
    goal = (1, 2, 3, 4, 5, 6, 0, 7, 8)  # Goal state
    path = a_star_8_puzzle(start, goal)

    for state in path:
        print(state[0:3])
        print(state[3:6])
        print(state[6:9])
        print()
