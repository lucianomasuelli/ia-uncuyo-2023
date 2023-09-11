from agent import Agent
from enviroment import Enviroment
from multiprocessing import Process
from algorithms.uniform_cost_search import uniformCostSearch

start = (1,6)
goal = (88,18)

env = Enviroment(start,goal,(100,100))
agent = Agent(start,goal,env)

path = agent.find_optimal_path_bfs()
path1 = agent.find_optimal_path_ucs()
#env.printMatrix()
print(path)
print(path1)
#agent.move(path)