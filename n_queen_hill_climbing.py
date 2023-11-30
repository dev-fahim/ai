import random


def objective_function(state):
    # Count the number of pairs of queens attacking each other
    attacking_pairs = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            # Check if queens are in the same column or on the same diagonal
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                attacking_pairs += 1
    return attacking_pairs


def get_neighbors(state):
    neighbors = []
    n = len(state)
    for i in range(n):
        for j in range(n):
            if state[i] != j:
                new_neighbor = list(state)
                new_neighbor[i] = j
                neighbors.append(new_neighbor)
    return neighbors


def select_best_neighbor(neighbors):
    best_neighbor = neighbors[0]
    min_attacks = objective_function(best_neighbor)
    for neighbor in neighbors[1:]:
        current_attacks = objective_function(neighbor)
        if current_attacks < min_attacks:
            min_attacks = current_attacks
            best_neighbor = neighbor
    return best_neighbor


def hill_climbing(n):
    initial_state = list(range(n))
    random.shuffle(initial_state)
    current_state = initial_state

    while True:
        neighbors = get_neighbors(current_state)
        next_state = select_best_neighbor(neighbors)

        if objective_function(next_state) >= objective_function(current_state):
            return current_state

        current_state = next_state


if __name__ == '__main__':
    # Example usage
    n = 8  # Number of queens
    solution = hill_climbing(n)
    print("Solution:", solution)
