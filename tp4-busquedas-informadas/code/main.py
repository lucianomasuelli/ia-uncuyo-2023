from agent import Agent
from environment import Environment
import numpy as np
import matplotlib.pyplot as plt


def run_algorithm(agent:Agent):
    len_paths = []
    num_explored_list = []
    path01, num_exploredBFS = agent.find_optimal_path_bfs()
    path02, num_exploredDFS = agent.find_optimal_path_dfs()
    path03, num_exploredUCS = agent.find_optimal_path_ucs()
    path04, num_exploredAStar = agent.find_path_a_star()

    len_paths.append(len(path01))
    len_paths.append(len(path02))
    len_paths.append(len(path03))
    len_paths.append(len(path04))
    num_explored_list.append(num_exploredBFS)
    num_explored_list.append(num_exploredDFS)
    num_explored_list.append(num_exploredUCS)
    num_explored_list.append(num_exploredAStar)

    return len_paths, num_explored_list

def main():
    num_trials = 30
    resultsBFS = []
    resultsDFS = []
    resultsUCS = []
    resultsAStar = []
    numExploredBFS = []
    numExploredDFS = []
    numExploredUCS = []
    numExploredAStar = []
    results = []

    for _ in range(num_trials):
        env = Environment(100)
        agent = Agent(env.start, env.goal, env)
        num_states_path, num_states_explored = run_algorithm(agent)
        resultsBFS.append(num_states_path[0])
        resultsDFS.append(num_states_path[1])
        resultsUCS.append(num_states_path[2])
        resultsAStar.append(num_states_path[3])
        numExploredBFS.append(num_states_explored[0])
        numExploredDFS.append(num_states_explored[1])
        numExploredUCS.append(num_states_explored[2])
        numExploredAStar.append(num_states_explored[3])

        # Guardar resultados
        for i, algorithm in enumerate(['BFS', 'DFS', 'UCS', 'A*']):
            results.append({
                'Algorithm_name': algorithm,
                'env_n': _ + 1,
                'estates_n': num_states_path[i],
                'solution_found': num_states_path[i] > 0
            })

    # Calculate mean and standard deviation
    mean_states_explored_bfs = np.mean(numExploredBFS)
    std_dev_states_explored_bfs = np.std(numExploredBFS)

    mean_states_explored_dfs = np.mean(numExploredDFS)
    std_dev_states_explored_dfs = np.std(numExploredDFS)

    mean_states_explored_ucs = np.mean(numExploredUCS)
    std_dev_states_explored_ucs = np.std(numExploredUCS)

    mean_states_explored_star = np.mean(numExploredAStar)
    std_dev_states_explored_star = np.std(numExploredAStar)


    # Print results
    print("---------------BFS-----------------")
    print(f"Mean states explored in BFS: {mean_states_explored_bfs}")
    print(f"Standard deviation of states explored in BFS: {std_dev_states_explored_bfs}")
    print("---------------DFS-----------------")
    print(f"Mean states explored in DFS: {mean_states_explored_dfs}")
    print(f"Standard deviation of states explored in DFS: {std_dev_states_explored_dfs}")
    print("---------------UCS-----------------")
    print(f"Mean states explored in UCS: {mean_states_explored_ucs}")
    print(f"Standard deviation of states explored in UCS: {std_dev_states_explored_ucs}")
    print("---------------A*-----------------")
    print(f"Mean states explored in A*: {mean_states_explored_star}")
    print(f"Standard deviation of states explored in A*: {std_dev_states_explored_star}")

    # Create subplots
    fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(15, 5))

    # Create boxplots for each algorithm
    axes[0].boxplot(numExploredBFS, showfliers=True)
    axes[0].set_title('BFS')
    axes[1].boxplot(numExploredDFS, showfliers=True)
    axes[1].set_title('DFS')
    axes[2].boxplot(numExploredUCS, showfliers=True)
    axes[2].set_title('UCS')
    axes[3].boxplot(numExploredAStar, showfliers=True)
    axes[3].set_title('A*')

    # Add titles and labels
    for ax in axes:
        ax.set_xlabel('Algorithm')
        ax.set_ylabel('Number of States Explored')

    # Customize x-axis labels
    plt.setp(axes, xticks=[1], xticklabels=[''])

    # Adjust layout
    plt.tight_layout()

    # Show the plots
    plt.show()


if __name__ == "__main__":
    main()
