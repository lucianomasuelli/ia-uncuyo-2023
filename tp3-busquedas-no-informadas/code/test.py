from agent import Agent
from enviroment import Enviroment

env = Enviroment(10)
agent = Agent(env.start, env.goal, env)

#pathUCS = agent.find_optimal_path_ucs()
#pathBFS = agent.find_optimal_path_bfs()
#pathDFS = agent.find_optimal_path_dfs()
pathDFSLimited = agent.find_optimal_path_limited_dfs(10)
#pathDFSRecursive = agent.find_optimal_path_recursive_limited_dfs(10)
env.printMatrix()
#print(pathUCS)
#print(pathBFS)
#print(pathDFS)
print(pathDFSLimited)
