from environment import Environment
from algorithms.hill_climbing import hill_climbing
from algorithms.simulated_annealing import simulated_annealing, logarithmic, exponential
from algorithms.genetic import genetic


def main():
    env = Environment(8)
    start = env.initial_state()
    solution_hill, explored_states_hill = hill_climbing(env, 100, start)
    solution_sim_annealing, explored_states_sim_annealing = simulated_annealing(env, exponential, start)
    solution_genetic, explored_states_genetic = genetic(env, 100, 10000, 0.1)

    print("-----------Hill Climbing------------")
    print("Explored states: ", explored_states_hill)
    print("Solution: ", solution_hill)
    print("Heuristic: ", env.heuristic(solution_hill))
    print("-----------Simulated Annealing------------")
    print("Explored states: ", explored_states_sim_annealing)
    print("Solution: ", solution_sim_annealing)
    print("Heuristic: ", env.heuristic(solution_sim_annealing))
    print("-----------Genetic------------")
    print("Explored states: ", explored_states_genetic)
    print("Solution: ", solution_genetic)
    print("Heuristic: ", env.heuristic(solution_genetic))

    env.plot_board(solution_hill)
    env.plot_board(solution_sim_annealing)
    env.plot_board(solution_genetic)

if __name__ == '__main__':
    main()
