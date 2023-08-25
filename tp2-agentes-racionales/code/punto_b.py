import random

class Agent:
    def __init__(self, posX, posY):
        self.positionX = posX
        self.positionY = posY
        
    def up(self, enviroment):
        if (enviroment.accept_action(self.positionX, self.positionY+1)):
            self.positionY += 1
            print("se mueve arriba")
        else:
            print("no es posible")

    def down(self, enviroment):
        if (enviroment.accept_action(self.positionX, self.positionY-1)):
            self.positionY -= 1
            print("se mueve abajo")
        else:
            print("no es posible")

    def left(self, enviroment):
        if (enviroment.accept_action(self.positionX-1, self.positionY)):
            self.positionX -= 1
            print("se mueve hacia la izquierda")
        else:
            print("no es posible")

    def right(self, enviroment):
        if (enviroment.accept_action(self.positionX+1, self.positionY)):
            self.positionX += 1
            print("se mueve hacia la derecha")
        else:
            print("no es posible")

            
class Enviroment:
    def __init__(self,sizeX,sizeY,init_posX,init_posY):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.agent = Agent(init_posX, init_posY)
        self.matriz = []
        for _ in range(sizeX):
            fila = random.choices([0,1],[0.7,0.3], k=sizeY) #devuelve una lista con k elementos que pueden ser 0 o 1, con probabilidades 0.7 y 0.3 respectivamente.
            self.matriz.append(fila)
    
    def is_dirty(self):
        if (self.matriz[self.agent.positionX][self.agent.positionY] == 1):
            return True
        else:
            return False
        
    def accept_action(self, posX, posY):
        if (0 <= posX <= self.sizeX and 0 <= posY <= self.sizeY):
            return True
        else:
            return False

    def printMatrix(self):
        for i in self.matriz:
            print(i)

env = Enviroment(10,10,4,2)
env.printMatrix()
env.agent.up(env)