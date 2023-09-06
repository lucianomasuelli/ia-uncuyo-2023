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
    explored = []
    tree.root = node
    if(goal == node.state):
        return node
    while frontier:
        node = frontier.popleft()
        explored.append(node.state)
        if(env.accept_action(node.state[0]-1,node.state[1])): #verifica si la posición de arriba es válida
            child_node = Node(node, (node.state[0]-1,node.state[1]), 'up')
            if (not (child_node.state in explored) and not (child_node in frontier)):
                if(goal == child_node.state):
                    return get_actions(child_node)
                frontier.append(child_node)
        if(env.accept_action(node.state[0]+1,node.state[1])):
            child_node = Node(node, (node.state[0]+1,node.state[1]), 'down')
            if (not (child_node.state in explored) and not (child_node in frontier)):
                if(goal == child_node.state):
                    return get_actions(child_node)
                frontier.append(child_node)
        if(env.accept_action(node.state[0],node.state[1]+1)):
            child_node = Node(node, (node.state[0],node.state[1]+1), 'right')
            if (not (child_node.state in explored) and not (child_node in frontier)):
                if(goal == child_node.state):
                    return get_actions(child_node)
                frontier.append(child_node)
        if(env.accept_action(node.state[0],node.state[1]-1)):
            child_node = Node(node, (node.state[0],node.state[1]-1), 'left')
            if (not (child_node.state in explored) and not (child_node in frontier)):
                if(goal == child_node.state):
                    return get_actions(child_node)
                frontier.append(child_node)


def get_actions(node):
    actions = []
    while node.parent is not None:
        actions.append(node.action)
        node = node.parent
    actions.reverse()  # Invierte la lista para obtener el camino correcto
    return actions