from enviroment import Enviroment
from a_star_search import a_star_search
import random


class Agent:
    def __init__(self, start, goal, env):
        self.position = start
        self.goal = goal
        self.env : Enviroment = env
        self.perf = 0
    
    def find_path_a_star(self):
        actions = a_star_search(self.position,self.goal,self.env)
        return actions

    def up(self):
        self.position = (self.position[0] - 1, self.position[1])

    def down(self):
        self.position = (self.position[0] + 1, self.position[1])

    def left(self):
        self.position = (self.position[0], self.position[1] - 1)

    def right(self):
        self.position = (self.position[0], self.position[1] + 1)

    def move(self, actions):
        for action in actions:
            if(action == "up"):
                self.up()
                if(self.position == self.goal):
                    print("Objetivo alcanzado")
                    return
            if(action == "down"):
                self.down()
                if(self.position == self.goal):
                    print("Objetivo alcanzado")
                    return
            if(action == "left"):
                self.left()
                if(self.position == self.goal):
                    print("Objetivo alcanzado")
                    return
            if(action == "right"):
                self.right()
                if(self.position == self.goal):
                    print("Objetivo alcanzado")
                    return