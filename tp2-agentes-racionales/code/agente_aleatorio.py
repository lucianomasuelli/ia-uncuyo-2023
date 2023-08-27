import random

class Agent:
    def __init__(self, posX, posY):
        self.positionX = posX
        self.positionY = posY
        self.perf = 0
        
    def up(self, enviroment):
        if (enviroment.accept_action(self.positionX, self.positionY+1)):
            self.positionY += 1
            self.clean(enviroment, self.positionX, self.positionY)
            print("se mueve arriba")

    def down(self, enviroment):
        if (enviroment.accept_action(self.positionX, self.positionY-1)):
            self.positionY -= 1
            self.clean(enviroment, self.positionX, self.positionY)
            print("se mueve abajo")


    def left(self, enviroment):
        if (enviroment.accept_action(self.positionX-1, self.positionY)):
            self.positionX -= 1
            self.clean(enviroment, self.positionX, self.positionY)
            print("se mueve hacia la izquierda")

    def right(self, enviroment):
        if (enviroment.accept_action(self.positionX+1, self.positionY)):
            self.positionX += 1
            self.clean(enviroment, self.positionX, self.positionY)
            print("se mueve hacia la derecha")

    def clean(self, env, posX, posY):
        if env.is_dirty():
            print("Limpia")
            env.matriz[posX][posY] = 0
            self.perf += 1

            
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


env = Enviroment(100,100,0,0)
#env.printMatrix()
for i in range(50):
    move = random.randint(0,3)
    if move == 0:
        env.agent.up(env)
    elif move == 1:
        env.agent.down(env)
    elif move == 2:
        env.agent.left(env)
    elif move == 3:
        env.agent.right(env)
print("Performance: " + str(env.agent.perf))
#env.printMatrix()