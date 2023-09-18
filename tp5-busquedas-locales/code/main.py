from environment import Environment
from algorithms.hill_climbing import hillClimbing


def main():
    env = Environment(8)
    solution, exploredStates = hillClimbing(env, 100)
    #env.printBoard(solution)
    env.plot_board(solution)
    print("Explored states: ", exploredStates)
    print(solution)
    print("Heuristic: ", env.heuristic(solution))


if __name__ == '__main__':
    main()
