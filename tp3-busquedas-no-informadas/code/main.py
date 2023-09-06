from agent import Agent
from enviroment import Enviroment

start = (2,2)
goal = (6,9)

env = Enviroment(start,goal,(10,10))
agent = Agent(start,goal,env)
path = agent.find_optimal_path_bfs()
env.printMatrix()
print(path)