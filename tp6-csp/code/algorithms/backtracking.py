from ../csp import Csp


def backtracking_search(csp: Csp):
    return recursive_backtracking({}, csp)

def recursive_backtracking(assignment, csp):
    if len(assignment) == len(csp.variables):
        return assignment
    var = select_unassigned_variable(assignment, csp)
    for value in order_domain_values(var, assignment, csp):
        if csp.is_consistent(var, value, assignment):
            assignment[var] = value
            result = recursive_backtracking(assignment, csp)
            if result is not None:
                return result
            del assignment[var]
    return None