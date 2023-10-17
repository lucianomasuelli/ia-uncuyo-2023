import random

class Agent:
    def __init__(self, posX, posY):
        self.positionX = posX
        self.positionY = posY
        self.perf = 0
    
    def start(self,env):
        time = 0
        while time < 1000 and self.perf < env.dirt_count:
            clean = random.randint(0,1)
            if clean == 1:
                self.clean(env,self.positionX,self.positionY)
            
            move = random.randint(0,4)

            if move == 0:
                self.up(env)
            elif move == 1:
                self.down(env)
            elif move == 2:
                self.left(env)
            elif move == 3:
                self.right(env)

            time += 1
        print("Unidades de tiempo consumidas: " + str(time))
            
        
    def up(self, enviroment):
        if (enviroment.accept_action(self.positionX, self.positionY+1)):
            self.positionY += 1
            #print("se mueve arriba")

    def down(self, enviroment):
        if (enviroment.accept_action(self.positionX, self.positionY-1)):
            self.positionY -= 1
            #print("se mueve abajo")


    def left(self, enviroment):
        if (enviroment.accept_action(self.positionX-1, self.positionY)):
            self.positionX -= 1
            #print("se mueve hacia la izquierda")

    def right(self, enviroment):
        if (enviroment.accept_action(self.positionX+1, self.positionY)):
            self.positionX += 1
            #print("se mueve hacia la derecha")

    def clean(self, env, posX, posY):
        if env.is_dirty():
            #print("Limpia")
            env.matriz[posX][posY] = 0
            self.perf += 1

            
class Enviroment:
    def __init__(self,sizeX,sizeY,init_posX,init_posY,dirt_rate):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.matriz = []
        self.dirt_count = 0
        for i in range(sizeX):
            fila = []
            for j in range(sizeY):
                num = random.choices([0,1], [1-dirt_rate, dirt_rate])[0]
                fila.append(num)
                self.dirt_count += num
            self.matriz.append(fila)

        self.agent = Agent(init_posX, init_posY)
        self.agent.start(self)

    def is_dirty(self):
        if (self.matriz[self.agent.positionX][self.agent.positionY] == 1):
            return True
        else:
            return False
        
    def accept_action(self, posX, posY):
        if (0 <= posX <= self.sizeX-1 and 0 <= posY <= self.sizeY-1):
            return True
        else:
            return False

    def printMatrix(self):
        for i in self.matriz:
            print(i)

for i in range(10):
    print(i)
    size = 128
    posX = random.randint(0,size-1)
    posY = random.randint(0,size-1)
    env = Enviroment(size,size,posX,posY,0.8)
    print("Cantidad de celdas sucias: " + str(env.dirt_count))
    print("Performance: " + str(env.agent.perf))