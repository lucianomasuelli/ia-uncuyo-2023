from csp import Csp, RowsConstraint, DiagonalsConstraint
from backtracking import backtracking_search
from forwardchecking import forward_checking_search


# A CSP for the n-queens problem
def main():
    variables = [0, 1, 2, 3, 4, 5, 6, 7]
    domains = {}
    for var in variables:
        domains[var] = [0, 1, 2, 3, 4, 5, 6, 7]
    constraints = [RowsConstraint(variables), DiagonalsConstraint(variables)]
    csp = Csp(variables, domains, constraints)
    result_backtrack = backtracking_search(csp)
    result_forward = forward_checking_search(csp)
    print("Backtracking:")
    print(result_backtrack)
    print("Heuristic: " + str(heuristic(result_backtrack)))
    print_board(result_backtrack)
    print("Forward checking:")
    print(result_forward)
    print("Heuristic: " + str(heuristic(result_forward)))
    print_board(result_forward)


def heuristic(result):
    h = 0
    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            if result[i] == result[j]:  # same row
                h += 1
            offset = j - i
            if result[i] == result[j] - offset or result[i] == result[j] + offset:  # same diagonal
                h += 1
    return h

def print_board(result):
    length = len(result)
    ordered = sorted(result.items())
    board = []
    for i in range(length):
        board.append([])
        for j in range(length):
            board[i].append(0)
    for (var, value) in ordered:
        board[value][var] = 1
    for i in range(length):
        print(board[i])


if __name__ == "__main__":
    main()
