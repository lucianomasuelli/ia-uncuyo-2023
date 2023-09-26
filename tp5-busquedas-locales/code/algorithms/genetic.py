from environment import Environment
import random


def genetic(environment: Environment, population_size: int, iterations: int, mutation_rate: float):
    """
    Algoritmo genético para resolver el problema de las n-reinas.

    :param environment: Entorno en el que se ejecuta el algoritmo.
    :param population_size: Tamaño de la población.
    :param iterations: Cantidad de iteraciones.
    :param mutation_rate: Tasa de mutación.
    :return: Mejor solución encontrada.
    """
    population = get_population(environment, population_size)
    sum_fitness, best_state = get_population_fitness(environment, population)
    elite_size = int(population_size * 0.1)

    if fitness(environment, best_state) == 0:
        return best_state, 0

    i = 0
    while iterations > 0:
        selected = selection(environment, population, sum_fitness)
        new_population = crossover(selected)
        new_population = mutate(new_population, mutation_rate)
        offspring = sorted(new_population, key=lambda x: fitness(environment, x))[:population_size - elite_size]
        elites = sorted(population, key=lambda x: fitness(environment, x))[:elite_size]  # selecciono los mejores estados
        new_population = elites + offspring
        sum_fitness, best_state = get_population_fitness(environment, new_population)

        if fitness(environment, best_state) == 0:
            return best_state, i

        population = new_population
        iterations -= 1
        i += 1
    return best_state, i


def get_population_fitness(environment: Environment, population):
    sum_fitness = 0
    best_fitness = 100000
    best_state = None
    for state in population:
        state_fitness = fitness(environment, state)
        sum_fitness += state_fitness
        if state_fitness < best_fitness:
            best_fitness = state_fitness
            best_state = state
    return sum_fitness, best_state


def get_population(environment: Environment, population_size: int):
    population = []
    for i in range(population_size):
        population.append(environment.random_state())
    return population


def fitness(environment: Environment, state):
    return environment.heuristic(state)


def selection(environment: Environment, population, sum_fitness):
    selected = []
    for state in population:
        pr = fitness(environment, state) / sum_fitness
        if random.random() < pr:  # selecciono el estado con probabilidad pr
            selected.append(state)
    return selected


def crossover(selected):
    new_population = []
    for i in range(len(selected)):
        for j in range(len(selected)):
            if i != j:
                new_population.append(crossover_states(selected[i], selected[j]))
    return new_population


def crossover_states(state1, state2):
    cross_point = int(len(state1)/2)
    new_state = []
    if random.random() < 0.5:
        for i in range(len(state1)):
            if i < cross_point:
                new_state.append(state1[i])
            else:
                new_state.append(state2[i])
    else:
        for i in range(len(state1)):
            if i < cross_point:
                new_state.append(state2[i])
            else:
                new_state.append(state1[i])
    return new_state


def mutate(population, mutation_rate):
    new_population = []
    for state in population:
        for i in range(len(state)):
            if random.random() < mutation_rate:
                state[i] = random.randint(0, len(state) - 1)
        new_population.append(state)
    return new_population



