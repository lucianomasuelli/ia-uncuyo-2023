from csp import Csp, RowsConstraint, DiagonalsConstraint
from backtracking import backtracking_search


# A CSP for the n-queens problem
def main():
    variables = [0, 1, 2, 3, 4, 5, 6, 7]
    domains = {}
    for var in variables:
        domains[var] = [0, 1, 2, 3, 4, 5, 6, 7]
    constraints = [RowsConstraint(variables), DiagonalsConstraint(variables)]
    csp = Csp(variables, domains, constraints)
    result = backtracking_search(csp)
    print(result)
    print(heuristic(result))
    print_board(result)


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
    board = []
    for i in range(8):
        board.append([])
        for j in range(8):
            board[i].append(0)
    for var, value in result.items():
        board[var][value] = 1
    for i in range(8):
        print(board[i])


if __name__ == "__main__":
    main()
