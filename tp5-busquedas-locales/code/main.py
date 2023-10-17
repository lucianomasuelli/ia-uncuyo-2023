from environment import Environment
from algorithms.hill_climbing import hill_climbing
from algorithms.simulated_annealing import simulated_annealing, exponential
from algorithms.genetic import genetic
import csv
import time
import matplotlib.pyplot as plt


def main():
    num_trials = 30
    results_hill = []
    results_sim_annealing = []
    results_genetic = []
    num_explored_hill = []
    num_explored_sim_annealing = []
    num_explored_genetic = []
    count_solution_hill = 0
    count_solution_sim_annealing = 0
    count_solution_genetic = 0
    results = []
    execution_time_hill = []
    execution_time_sim_annealing = []
    execution_time_genetic = []
    h_variation_hill_1 = []
    h_variation_sim_annealing_1 = []
    h_variation_genetic_1 = []

    for i in range(num_trials):
        env = Environment(10)
        start = env.initial_state()

        # run algorithms
        start_time_hill = time.time()
        solution_hill, explored_states_hill, h_variation_hill = hill_climbing(env, 100, start)
        end_time_hill = time.time()

        start_time_sim_annealing = time.time()
        solution_sim_annealing, explored_states_sim_annealing, h_variation_sim_annealing = simulated_annealing(env, exponential, start)
        end_time_sim_annealing = time.time()

        start_time_genetic = time.time()
        solution_genetic, explored_states_genetic, h_variation_genetic = genetic(env, 500, 10000, 0.1)
        end_time_genetic = time.time()

        # save results
        results_hill.append(env.heuristic(solution_hill))
        results_sim_annealing.append(env.heuristic(solution_sim_annealing))
        results_genetic.append(env.heuristic(solution_genetic))
        num_explored_states = [explored_states_hill, explored_states_sim_annealing, explored_states_genetic]
        num_explored_hill.append(explored_states_hill)
        num_explored_sim_annealing.append(explored_states_sim_annealing)
        num_explored_genetic.append(explored_states_genetic)

        # check if solution was found
        found_solution_hill = env.heuristic(solution_hill) == 0
        found_solution_sim_annealing = env.heuristic(solution_sim_annealing) == 0
        found_solution_genetic = env.heuristic(solution_genetic) == 0
        found_solutions = [found_solution_hill, found_solution_sim_annealing, found_solution_genetic]
        if found_solution_hill:
            count_solution_hill += 1
            execution_time_hill.append(end_time_hill - start_time_hill)
        if found_solution_sim_annealing:
            count_solution_sim_annealing += 1
            execution_time_sim_annealing.append(end_time_sim_annealing - start_time_sim_annealing)
        if found_solution_genetic:
            count_solution_genetic += 1
            execution_time_genetic.append(end_time_genetic - start_time_genetic)

        if i == int((num_trials-1) / 2):
            h_variation_hill_1 = h_variation_hill
            h_variation_sim_annealing_1 = h_variation_sim_annealing
            h_variation_genetic_1 = h_variation_genetic

        # Guardar resultados
        for j, algorithm in enumerate(['Hill Climbing', 'Simulated Annealing', 'Genetic']):
            results.append({
                'Algorithm_name': algorithm,
                'env_n': i + 1,
                'states_n': num_explored_states[j],
                'solution_found': found_solutions[j]
            })

    # Calculate mean and standard deviation
    mean_states_explored_hill = sum(num_explored_hill) / num_trials
    std_dev_states_explored_hill = (sum([(x - mean_states_explored_hill) ** 2 for x in num_explored_hill]) / num_trials) ** 0.5
    mean_execution_time_hill = sum(execution_time_hill) / num_trials
    std_dev_execution_time_hill = (sum([(x - mean_execution_time_hill) ** 2 for x in execution_time_hill]) / num_trials) ** 0.5
    percentage_solution_hill = count_solution_hill / num_trials

    mean_states_explored_sim_annealing = sum(num_explored_sim_annealing) / num_trials
    std_dev_states_explored_sim_annealing = (sum([(x - mean_states_explored_sim_annealing) ** 2 for x in num_explored_sim_annealing]) / num_trials) ** 0.5
    mean_execution_time_sim_annealing = sum(execution_time_sim_annealing) / num_trials
    std_dev_execution_time_sim_annealing = (sum([(x - mean_execution_time_sim_annealing) ** 2 for x in execution_time_sim_annealing]) / num_trials) ** 0.5
    percentage_solution_sim_annealing = count_solution_sim_annealing / num_trials

    mean_states_explored_genetic = sum(num_explored_genetic) / num_trials
    std_dev_states_explored_genetic = (sum([(x - mean_states_explored_genetic) ** 2 for x in num_explored_genetic]) / num_trials) ** 0.5
    mean_execution_time_genetic = sum(execution_time_genetic) / num_trials
    std_dev_execution_time_genetic = (sum([(x - mean_execution_time_genetic) ** 2 for x in execution_time_genetic]) / num_trials) ** 0.5
    percentage_solution_genetic = count_solution_genetic / num_trials

    # Guardar resultados en archivo csv
    with open('results.csv', 'w', newline='') as csvfile:
        fieldnames = ['Algorithm_name', 'env_n', 'states_n', 'solution_found']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print("-----------Hill Climbing------------")
    print("Mean states explored in Hill Climbing: ", mean_states_explored_hill)
    print("Standard deviation of states explored in Hill Climbing: ", std_dev_states_explored_hill)
    print("Mean execution time in Hill Climbing: ", mean_execution_time_hill)
    print("Standard deviation of execution time in Hill Climbing: ", std_dev_execution_time_hill)
    print("Percentage of solutions found in Hill Climbing: ", percentage_solution_hill)
    print("-----------Simulated Annealing------------")
    print("Mean states explored in Simulated Annealing: ", mean_states_explored_sim_annealing)
    print("Standard deviation of states explored in Simulated Annealing: ", std_dev_states_explored_sim_annealing)
    print("Mean execution time in Simulated Annealing: ", mean_execution_time_sim_annealing)
    print("Standard deviation of execution time in Simulated Annealing: ", std_dev_execution_time_sim_annealing)
    print("Percentage of solutions found in Simulated Annealing: ", percentage_solution_sim_annealing)
    print("-----------Genetic------------")
    print("Mean states explored in Genetic: ", mean_states_explored_genetic)
    print("Standard deviation of states explored in Genetic: ", std_dev_states_explored_genetic)
    print("Mean execution time in Genetic: ", mean_execution_time_genetic)
    print("Standard deviation of execution time in Genetic: ", std_dev_execution_time_genetic)
    print("Percentage of solutions found in Genetic: ", percentage_solution_genetic)

    # Execution time boxplot

    plt.boxplot([execution_time_hill, execution_time_sim_annealing, execution_time_genetic],
                labels=['Hill Climbing', 'Simulated Annealing', 'Genetic'],
                showfliers=True)
    plt.ylabel('Execution time (s)')
    plt.xlabel('Algorithm')
    plt.title('Execution time boxplot')
    plt.show()

    # Explored states boxplot
    #plt.boxplot([num_explored_hill, num_explored_sim_annealing, num_explored_genetic], labels=['Hill Climbing', 'Simulated Annealing', 'Genetic'])
    #plt.ylabel('Explored states')
    #plt.xlabel('Algorithm')
    #plt.title('Explored states boxplot')
    #plt.show()

    # Heuristic variation plot
    plt.plot(h_variation_hill_1, label='Hill Climbing')
    plt.xlabel('Iteration')
    plt.ylabel('Heuristic')
    plt.title('Heuristic variation plot (Hill Climbing)')
    plt.show()

    plt.plot(h_variation_sim_annealing_1, label='Simulated Annealing')
    plt.plot(h_variation_genetic_1, label='Genetic')
    plt.legend()
    plt.xlabel('Iteration')
    plt.ylabel('Heuristic')
    plt.title('Heuristic variation plot')
    plt.show()

if __name__ == '__main__':
    main()
