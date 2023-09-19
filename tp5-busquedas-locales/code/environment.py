import random
import matplotlib.pyplot as plt


class Environment:
    def __init__(self, size):
        self.size = size
        self.board = []

    def heuristic(self, state):
        h = 0
        for i in range(len(state)):
            for j in range(i+1, len(state)):
                if state[i] == state[j]: # same row
                    h += 1
                offset = j - i
                if state[i] == state[j] - offset or state[i] == state[j] + offset: # same diagonal
                    h += 1
        return h

    def initial_state(self):
        for i in range(self.size):
            num = random.randint(0, self.size - 1)
            self.board.append(num)
        return self.board

    def best_neighbor(self, state): #returns the neighbor with the lowest heuristic
        bestNeighbor = state
        bestHeuristic = self.heuristic(state)
        for i in range(len(state)):
            for j in range(len(state)):
                if i != j:
                    newState = list(state)
                    newState[i] = j
                    h = self.heuristic(newState)
                    if h < bestHeuristic:
                        bestNeighbor = newState
                        bestHeuristic = h
        return bestNeighbor

    def neighbors(self, state):
        neighbors = []
        for i in range(len(state)):
            for j in range(len(state)):
                if i != j:
                    newState = list(state)
                    newState[i] = j  # change the queen in row i to column j
                    neighbors.append(newState)
        return neighbors


    def plot_board(self,state):
        n = len(state)
        board = [[(i + j) % 2 for i in range(n)] for j in range(n)]

        for i in range(n):
            board[state[i]][i] = 2  # Mark queen positions

        plt.imshow(board, cmap="binary") # Create a colored game board
        ax = plt.gca() # Get the current axis

        for i in range(n):
            for j in range(n):
                if board[i][j] == 2:
                    rect = plt.Rectangle((j-0.5, i-0.5), 1, 1, fill=True, color='red')
                    ax.add_patch(rect)

        plt.xticks([])
        plt.yticks([])
        plt.show()