from agent import Agent
from enviroment import Enviroment
from multiprocessing import Process
from algorithms.uniform_cost_search import uniformCostSearch

start = (50,6)
goal = (89,66)

env = Enviroment(start,goal,(100,100))
agent = Agent(start,goal,env)

path = agent.find_optimal_path_bfs()
path1 = agent.find_optimal_path_ucs()
path2 = agent.find_optimal_path_dfs()
#env.printMatrix()
print("BFS:")
print(path)
print("UCS:")
print(path1)
print("DFS:")
print(path2)
#agent.move(path)