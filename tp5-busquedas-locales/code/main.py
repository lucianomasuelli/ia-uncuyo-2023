from environment import Environment
from algorithms.hill_climbing import hill_climbing
from algorithms.simulated_annealing import simulated_annealing, logarithmic, exponential


def main():
    env = Environment(4)
    start = env.initial_state()
    solution_hill, explored_states_hill = hill_climbing(env, 100, start)
    solution_sim_annealing, explored_states_sim_annealing = simulated_annealing(env, exponential, start)
    #env.plot_board(solution_hill)
    #env.plot_board(solution_sim_annealing)
    print("-----------Hill Climbing------------")
    print("Explored states: ", explored_states_hill)
    print("Solution: ", solution_hill)
    print("Heuristic: ", env.heuristic(solution_hill))
    print("-----------Simulated Annealing------------")
    print("Explored states: ", explored_states_sim_annealing)
    print("Solution: ", solution_sim_annealing)
    print("Heuristic: ", env.heuristic(solution_sim_annealing))


if __name__ == '__main__':
    main()
