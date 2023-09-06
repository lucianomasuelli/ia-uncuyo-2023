from enviroment import Enviroment
import random
from algorithms.bfs import bfs


class Agent:
    def __init__(self, start, goal, env):
        self.position = start
        self.goal = goal
        self.env : Enviroment = env
        self.perf = 0

    def goal_test(self, pos):
        if(pos == self.goal_pos):
            return True
        return False
    
    def find_optimal_path_bfs(self):
        actions = bfs(self.position,self.goal,self.env)
        return actions

    def up(self, enviroment):
        if (enviroment.accept_action(self.positionX, self.positionY+1)):
            self.positionY += 1
            self.clean(enviroment)
            #print("se mueve arriba")

    def down(self, enviroment):
        if (enviroment.accept_action(self.positionX, self.positionY-1)):
            self.positionY -= 1
            self.clean(enviroment)
            #print("se mueve abajo")


    def left(self, enviroment):
        if (enviroment.accept_action(self.positionX-1, self.positionY)):
            self.positionX -= 1
            self.clean(enviroment)
            #print("se mueve hacia la izquierda")

    def right(self, enviroment):
        if (enviroment.accept_action(self.positionX+1, self.positionY)):
            self.positionX += 1
            self.clean(enviroment)
           # print("se mueve hacia la derecha")

    def clean(self, env):
        if env.is_dirty(self.positionX, self.positionY):
           # print("Limpia")
            env.matriz[self.positionX][self.positionY] = 0
            self.perf += 1
