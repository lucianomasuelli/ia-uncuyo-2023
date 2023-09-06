from agent import Agent
from enviroment import Enviroment

start = (2,2)
goal = (68,8)

env = Enviroment(start,goal,(100,100))
agent = Agent(start,goal,env)
path = agent.find_optimal_path_bfs()
#env.printMatrix()
print(path)
#agent.move(path)