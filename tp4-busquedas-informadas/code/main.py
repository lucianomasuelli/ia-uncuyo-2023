from enviroment import Enviroment
from agent import Agent

def main():
    env : Enviroment = Enviroment(10)
    env.printMatrix()
    agent : Agent = Agent(env.start, env.goal, env)
    actions = agent.find_path_a_star()
    print(actions)

if __name__ == "__main__":
    main()