from environment import Environment


def hill_climbing(env: Environment, maxIterations, start):  # calculates a solution for the n-queens problem using hill climbing
    current = start
    i = 0
    h_variaton = []
    while i < maxIterations:
        current_heuristic = env.heuristic(current)
        h_variaton.append(current_heuristic)
        if current_heuristic == 0:
            return current, i, h_variaton
        else:
            neighbor = env.best_neighbor(current)
            neighbor_heuristic = env.heuristic(neighbor)
            if neighbor_heuristic < current_heuristic:
                current = neighbor
            else:
                return current, i, h_variaton
        i += 1
    return current, i, h_variaton
