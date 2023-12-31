from enviroment import Enviroment
from queue import LifoQueue

class Node:
    def __init__(self, parent, state, action):
        self.parent = parent
        self.state = state
        self.action = action

    def get_actions(self):
        actions = []
        while self.parent is not None:
            actions.append(self.action)
            self = self.parent
        actions.reverse()  # Invierte la lista para obtener el camino correcto
        return actions

def dfs(start, goal, env:Enviroment):
    count_explored = 0
    node = Node(None, start, None)
    frontier = LifoQueue()  
    frontier_states = set()  # Mantener un conjunto de estados en frontier
    frontier.put(node)
    frontier_states.add(node.state)
    explored = set()
    if(goal == node.state):
        return [node.state], count_explored
    while frontier:
        node = frontier.get()
        frontier_states.remove(node.state)
        explored.add(node.state)
        count_explored += 1
        if goal == node.state:
            return node.get_actions(), count_explored
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
                frontier.put(child_node)
                frontier_states.add(new_state)