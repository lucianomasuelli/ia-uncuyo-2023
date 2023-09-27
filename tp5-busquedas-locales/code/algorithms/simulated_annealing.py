import math
import random
from environment import Environment


def simulated_annealing(env: Environment, schedule, start):
    current = start
    i = 0
    h_variation = []
    while True:
        h_variation.append(env.heuristic(current))
        if env.heuristic(current) == 0:
            return current, i, h_variation
        T = schedule(i, env.size)
        if T == 0:
            return current, i, h_variation
        next = random.choice(env.neighbors(current))
        delta_e = env.heuristic(next) - env.heuristic(current)
        if delta_e < 0 or random.uniform(0, 1) < math.exp(-delta_e / T):  # if next is better than current or with probability e^(-delta_e/T)
            current = next
        i += 1


def logarithmic(k):
    return 100 / (1 + k)


def exponential(k,n):
    t0 = 10 * n
    alpha = 0.95
    return t0 * (alpha ** k)
