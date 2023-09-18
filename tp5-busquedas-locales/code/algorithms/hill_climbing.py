from environment import Environment


def hillClimbing(env: Environment, maxIterations):  # calculates a solution for the n-queens problem using hill climbing
    current = env.initialState()
    i = 0
    while i < maxIterations:
        current_heuristic = env.heuristic(current)
        if current_heuristic == 0:
            return current, i
        else:
            neighbor = env.bestNeighbor(current)
            neighbor_heuristic = env.heuristic(neighbor)
            if neighbor_heuristic < current_heuristic:
                current = neighbor
            else:
                return current, i
        i += 1
    return current, i
