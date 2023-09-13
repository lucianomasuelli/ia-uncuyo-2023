from collections import deque
from enviroment import Enviroment

class Node:
    def __init__(self, parent, state, action):
        self.parent = parent
        self.state = state
        self.action = action

def bfs(start, goal, env:Enviroment):
    count_explored = 0
    node = Node(None, start, None)
    frontier = deque()  # Utilizar append() y popleft() para FIFO
    frontier_states = set()  # Mantener un conjunto de estados en frontier
    frontier.append(node)
    frontier_states.add(node.state)
    explored = set()
    if(goal == node.state):
        return [node.state], count_explored
    while frontier:
        node = frontier.popleft()
        frontier_states.remove(node.state)
        explored.add(node.state)
        count_explored += 1
        if goal == node.state:
            return get_actions(node), count_explored
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
            if env.accept_action(*new_state) and (new_state not in explored) and (new_state not in frontier_states):
                child_node = Node(node, new_state, action)
                frontier.append(child_node)
                frontier_states.add(new_state)


def get_actions(node):
    actions = []
    while node.parent is not None:
        actions.append(node.action)
        node = node.parent
    actions.reverse()  # Invierte la lista para obtener el camino correcto
    return actions