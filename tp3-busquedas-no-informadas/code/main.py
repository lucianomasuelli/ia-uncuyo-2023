from agent import Agent
from enviroment import Enviroment
from multiprocessing import Process

start = (8,6)
goal = (9,1)

env = Enviroment(start,goal,(10,10))
agent = Agent(start,goal,env)

path = agent.find_optimal_path_bfs()
#env.printMatrix()
print(path)
#agent.move(path)