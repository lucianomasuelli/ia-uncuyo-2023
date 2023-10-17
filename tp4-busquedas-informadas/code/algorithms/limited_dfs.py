from enviroment import Enviroment
from queue import LifoQueue

class Node:
    def __init__(self, parent, state, action, depth):
        self.parent = parent
        self.state = state
        self.action = action
        self.depth = depth
    
    def get_actions(self):
        actions = []
        while self.parent is not None:
            actions.append(self.action)
            self = self.parent
        actions.reverse()  # Invierte la lista para obtener el camino correcto
        return actions

def limited_dfs(start, goal, env, depth_limit):
    node = Node(None, start, None, 0)
    if node.depth > depth_limit:
        return [node.state]

    frontier = LifoQueue()  
    frontier_states = set()  
    frontier.put(node)
    frontier_states.add(node.state)
    explored = set()

    while frontier:
        node = frontier.get()
        frontier_states.remove(node.state)
        explored.add(node.state)

        if goal == node.state:
            return node.get_actions()

        if node.depth < depth_limit:
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
                    child_node = Node(node, new_state, action, node.depth + 1)
                    frontier.put(child_node)
                    frontier_states.add(new_state)

    return None


def recursive_limited_dfs(start, goal, env, depth_limit):
    node = Node(None, start, None, 0)
    visited = set()
    return recursive_limited_dfs_aux(node, goal, env, depth_limit, visited)

def recursive_limited_dfs_aux(node, goal, env, depth_limit, visited):
    if node.depth > depth_limit:
        return None

    if goal == node.state:
        return []
    
    visited.add(node.state)

    for action in ['up', 'down', 'right', 'left']:
        if action == 'up':
            new_state = (node.state[0] - 1, node.state[1])
        elif action == 'down':
            new_state = (node.state[0] + 1, node.state[1])
        elif action == 'right':
            new_state = (node.state[0], node.state[1] + 1)
        elif action == 'left':
            new_state = (node.state[0], node.state[1] - 1)

        if env.accept_action(*new_state):
            child_node = Node(node, new_state, action, node.depth + 1)
            actions = recursive_limited_dfs_aux(child_node, goal, env, depth_limit, visited)
            if actions is not None:
                return [action] + actions
    
    visited.remove(node.state)

    return None