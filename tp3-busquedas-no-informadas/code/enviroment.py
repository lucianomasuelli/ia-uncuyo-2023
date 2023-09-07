import random

class Enviroment:
    def __init__(self, start, goal, size):
        self.size = size
        self.matriz = []
        obstacle_rate = 0.08
        for i in range(size[0]):
            fila = []
            for j in range(size[1]):
                num = random.choices([0,1], [1-obstacle_rate, obstacle_rate])[0]
                if((i,j) == start):
                    fila.append(2)
                elif((i,j) == goal):
                    fila.append(3)
                else:
                    fila.append(num)
            self.matriz.append(fila)
        
    def accept_action(self, posX, posY):
        if (((0 <= posX <= self.size[0]-1) and (0 <= posY <= self.size[1]-1)) and (self.matriz[posX][posY] != 1)):
            return True
        else:
            return False

    def printMatrix(self):
        for i in self.matriz:
            print(i)