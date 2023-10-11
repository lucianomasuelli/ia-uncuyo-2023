from csp import Csp


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


def select_unassigned_variable(assignment, csp):
    min_mrv = 100000
    for var in csp.variables:
        var_mrv = mrv(var, assignment, csp)
        if var_mrv < min_mrv:
            min_mrv = var_mrv
    return min_mrv


def mrv(var, assignment, csp):
    if var in assignment:
        return 100000
    else:
        return len(csp.domains[var])


def order_domain_values(var, assignment, csp):
    least_constraining_values = []
    for value in csp.domains[var]:
        least_constraining_values.append((value, lcv(var, value, assignment, csp)))
    least_constraining_values.sort(key=lambda x: x[1])  # sort by least constraining value
    return [value[0] for value in least_constraining_values]  # return only the values


def lcv(var, value, csp):
    count = 0
    for constraint in csp.constraints:
        if var in constraint.variables:
            for other_var in constraint.variables:
                if other_var != var:
                    for other_value in csp.domains[other_var]:
                        if not constraint.is_satisfied({var: value, other_var: other_value}):
                            count += 1
    return count
