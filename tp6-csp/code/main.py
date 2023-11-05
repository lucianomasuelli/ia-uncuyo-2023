from csp import Csp, RowsConstraint, DiagonalsConstraint
from backtracking import backtracking_search
from forwardchecking import forward_checking_search
import time
import matplotlib.pyplot as plt



def main():
    variables_4 = [0, 1, 2, 3]
    domains_4 = {}
    for var in variables_4:
        domains_4[var] = [0, 1, 2, 3]
    constraints_4 = [RowsConstraint(variables_4), DiagonalsConstraint(variables_4)]
    csp_4 = Csp(variables_4, domains_4, constraints_4)

    variables_8 = [0, 1, 2, 3, 4, 5, 6, 7]
    domains_8 = {}
    for var in variables_8:
        domains_8[var] = [0, 1, 2, 3, 4, 5, 6, 7]
    constraints_8 = [RowsConstraint(variables_8), DiagonalsConstraint(variables_8)]
    csp_8 = Csp(variables_8, domains_8, constraints_8)

    variables_12 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11]
    domains_12 = {}
    for var in variables_12:
        domains_12[var] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11]
    constraints_12 = [RowsConstraint(variables_12), DiagonalsConstraint(variables_12)]
    csp_12 = Csp(variables_12, domains_12, constraints_12)

    variables_15 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11, 12,13,14]
    domains_15 = {}
    for var in variables_15:
        domains_15[var] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11, 12,13,14]
    constraints_15 = [RowsConstraint(variables_15), DiagonalsConstraint(variables_15)]
    csp_15 = Csp(variables_15, domains_15, constraints_15)

    csp_list = [(csp_4, "4 Queens"), (csp_8, "8 Queens"), (csp_12, "12 Queens"), (csp_15, "15 Queens")]

    execution_times_backtracking = []
    execution_times_forward = []
    visited_states_backtracking = []
    visited_states_forward = []

    for csp, name in csp_list:
        start_time = time.time()
        result_backtrack, visited_bt = backtracking_search(csp)
        end_time = time.time()
        execution_times_backtracking.append(end_time - start_time)
        visited_states_backtracking.append(visited_bt)
        print(name + " - Backtracking:")
        print(result_backtrack)
        print("Heuristic: " + str(heuristic(result_backtrack)))
        print("Visited states: " + str(visited_bt))
        print_board(result_backtrack)
        print("Execution time: {:.6f} seconds".format(end_time - start_time))
        print("\n")

        start_time = time.time()
        result_forward, visited_fwd = forward_checking_search(csp)
        end_time = time.time()
        execution_times_forward.append(end_time - start_time)
        visited_states_forward.append(visited_fwd)
        print(name + " - Forward checking:")
        print(result_forward)
        print("Heuristic: " + str(heuristic(result_forward)))
        print("Visited states: " + str(visited_fwd))
        print_board(result_forward)
        print("Execution time: {:.6f} seconds".format(end_time - start_time))
        print("\n")

    # Plot boxplots for execution times and visited states
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))

    # Boxplot para execution times
    axs[0].boxplot([execution_times_backtracking, execution_times_forward])
    axs[0].set_xticks([1, 2])
    axs[0].set_xticklabels(["Backtracking", "Forward checking"])
    axs[0].set_title("Execution times")
    axs[0].set_ylabel("Time (seconds)")

    # Boxplot para visited states
    axs[1].boxplot([visited_states_backtracking, visited_states_forward])
    axs[1].set_xticks([1, 2])
    axs[1].set_xticklabels(["Backtracking", "Forward checking"])
    axs[1].set_title("Visited states")
    axs[1].set_ylabel("States visited")

    plt.show()


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
