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
    
    
    
class Tree:
    root: None

def uniformCostSearch(start, goal, env:Enviroment):
    node: Node = Node(None, start, None, 1)
    frontier = PriorityQueue() #utilizar append() y popleft() para FIFO
    frontier.put((node.pathCost,node))
    frontier_states = set()
    frontier_states.add(node.state)
    explored = set()
    if(goal == node.state):
        return node
    while frontier:
        _ , node = frontier.get()
        frontier_states.remove(node.state)
        explored.add(node.state)
        if goal == node.state:
            return node.get_actions()
        # Verificar las acciones y agregar nodos hijos
        for action in ['up', 'down', 'right', 'left']:
            if action == 'up':
                new_state = (node.state[0] - 1, node.state[1])
            elif action == 'down':
                new_state = (node.state[0] + 1, node.state[1])
            elif action == 'right':
                new_state = (node.state[0], node.state[1] + 1)
            elif action == 'left':
                new_state = (node.state[0], node.state[1] - 1)
            if node.parent is not None:
                path_cost = node.parent.pathCost + 1
            else:
                path_cost = 1
            child_node:Node = Node(node, new_state, action, path_cost)
            if env.accept_action(*new_state) and (new_state not in explored) and (new_state not in frontier_states):
                frontier.put((child_node.pathCost, child_node))
                frontier_states.add(new_state)
            elif new_state in frontier_states:
                node1 = getNode(frontier,new_state)
                if node1.pathCost > path_cost :
                    deleteNode(frontier,node1)
                    frontier.put((child_node.pathCost, child_node))


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