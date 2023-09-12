from agent import Agent
from enviroment import Enviroment
import numpy as np
import matplotlib.pyplot as plt
import csv


def run_algorithm(agent:Agent):
    len_paths = []
    path01 = agent.find_optimal_path_bfs()
    path02 = agent.find_optimal_path_dfs()
    path03 = agent.find_optimal_path_ucs()
    len_paths.append(len(path01))
    len_paths.append(len(path02))
    len_paths.append(len(path03))

    return len_paths

def main():
    num_trials = 30
    resultsBFS = []
    resultsDFS = []
    resultsUCS = []
    results = []

    for _ in range(num_trials):
        env = Enviroment(50)
        agent = Agent(env.start, env.goal, env)
        num_states_explored = run_algorithm(agent)
        resultsBFS.append(num_states_explored[0])
        resultsDFS.append(num_states_explored[1])
        resultsUCS.append(num_states_explored[2])

        # Guardar resultados
        for i, algorithm in enumerate(['BFS', 'DFS', 'UCS']):
            results.append({
                'Algorithm_name': algorithm,
                'env_n': _ + 1,
                'estates_n': num_states_explored[i],
                'solution_found': num_states_explored[i] > 0
            })

    # Calculate mean and standard deviation
    mean_states_explored_bfs = np.mean(resultsBFS)
    std_dev_states_explored_bfs = np.std(resultsBFS)

    mean_states_explored_dfs = np.mean(resultsDFS)
    std_dev_states_explored_dfs = np.std(resultsDFS)

    mean_states_explored_ucs = np.mean(resultsUCS)
    std_dev_states_explored_ucs = np.std(resultsUCS)

    # Guardar resultados en un archivo CSV
    with open('no-informada-results.csv', 'w', newline='') as csvfile:
        fieldnames = ['Algorithm_name', 'env_n', 'estates_n', 'solution_found']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in results:
            writer.writerow(row)

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

    # Create subplots
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))

    # Create boxplots for each algorithm
    axes[0].boxplot(resultsBFS, showfliers=True)
    axes[0].set_title('BFS')
    axes[1].boxplot(resultsDFS, showfliers=True)
    axes[1].set_title('DFS')
    axes[2].boxplot(resultsUCS, showfliers=True)
    axes[2].set_title('UCS')

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
