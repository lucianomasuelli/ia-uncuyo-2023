from collections import deque
from enviroment import Enviroment

class Node:
    def __init__(self, parent, state, action):
        self.parent = parent
        self.state = state
        self.action = action

class BFSTree:
    root: None

def bfs(start, goal, env:Enviroment):
    tree = BFSTree
    node = Node(None, start, None)
    frontier = deque() #utilizar append() y popleft() para FIFO
    frontier.append(node)
    explored = set()
    tree.root = node
    if(goal == node.state):
        return node
    while frontier:
        node = frontier.popleft()
        explored.add(node.state)
        if goal == node.state:
            return get_actions(node)
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
            if env.accept_action(*new_state) and new_state not in explored:
                child_node = Node(node, new_state, action)
                frontier.append(child_node)


def get_actions(node):
    actions = []
    while node.parent is not None:
        actions.append(node.action)
        node = node.parent
    actions.reverse()  # Invierte la lista para obtener el camino correcto
    return actions