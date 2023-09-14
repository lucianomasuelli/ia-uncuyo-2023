import importlib
from queue import PriorityQueue
from enviroment import Enviroment

class Node:
    def __init__(self, parent, state, action, pathCost):
        self.parent: Node = parent
        self.state = state
        self.action = action
        self.pathCost = pathCost

    def __lt__(self, other):
        return self.pathCost < other.pathCost

    def get_actions(self):
        actions = []
        while self.parent is not None:
            actions.append(self.action)
            self = self.parent
        actions.reverse()  # Invierte la lista para obtener el camino correcto
        return actions
    
def getNode(pq: PriorityQueue, state):
    temp_queue = PriorityQueue()
    target = None
    while not pq.empty():
        item = pq.get()
        if item[1].state == state:
            target = item[1]
        temp_queue.put(item)

    # Restore the elements back to the original queue
    while not temp_queue.empty():
        pq.put(temp_queue.get())

    return target
        
def deleteNode(pq: PriorityQueue, node):
    temp_queue = PriorityQueue()
    while not pq.empty():
        item = pq.get()
        if item[1].state == node.state:
            target = item[1]
        else:
            temp_queue.put(item)

    # Restore the elements back to the original queue
    while not temp_queue.empty():
        pq.put(temp_queue.get())

def a_star_search(start, goal, env:Enviroment):
    frontier = PriorityQueue()
    frontier.put((0, Node(None, start, None, 0)))
    frontier_states = set()
    explored = []
    while not frontier.empty():
        node = frontier.get()[1]
        if node.state == goal:
            return node.get_actions()
        explored.append(node.state)
        for action in ['up', 'down', 'right', 'left']:
            child_state = env.result(node.state, action)
            if (child_state not in explored) and (child_state not in frontier_states) and (env.accept_action(*child_state)):
                child_node = Node(node, child_state, action, node.pathCost + 1)
                frontier.put((child_node.pathCost + env.heuristic(child_state), child_node))
                frontier_states.add(child_state)
            elif child_state in frontier_states:
                child_node = getNode(frontier, child_state) 
                if child_node is not None:
                    if child_node.pathCost > node.pathCost + 1: #Si el costo del camino es menor, se reemplaza
                        child_node.pathCost = node.pathCost + 1 #Se actualiza el costo del camino
                        child_node.parent = node #Se actualiza el padre
                        deleteNode(frontier, child_node) #Se elimina el nodo de la cola
                        frontier.put((child_node.pathCost + env.heuristic(child_state, goal), child_node)) #Se agrega el nodo con el nuevo costo

    return None

