import random

class Agent:
    def __init__(self, posX, posY):
        self.positionX = posX
        self.positionY = posY
        self.perf = 0
        
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

    def think(self,env):
        time = 0
        self.clean(env)
        while time < 1000 and self.perf < env.dirt_count:
            if env.is_dirty(self.positionX, self.positionY+1):
                self.up(env)
            elif env.is_dirty(self.positionX, self.positionY-1):
                self.down(env)
            elif env.is_dirty(self.positionX+1, self.positionY):
                self.right(env)
            elif env.is_dirty(self.positionX-1, self.positionY):
                self.left(env)
            else:
                move = random.randint(0,3)
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
            
class Enviroment:
    def __init__(self,sizeX,sizeY,init_posX,init_posY,dirt_rate):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.matriz = []
        self.dirt_count = 0
        for _ in range(sizeX):
            fila = []
            for _ in range(sizeY):
                num = random.choices([0,1], [1-dirt_rate, dirt_rate])[0]
                fila.append(num)
                self.dirt_count += num
            self.matriz.append(fila)

        self.agent = Agent(init_posX, init_posY)
        self.agent.think(self)
    
    def is_dirty(self, posX, posY):
        if self.accept_action(posX,posY):
            if (self.matriz[posX][posY] == 1):
                return True
            else:
                return False
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