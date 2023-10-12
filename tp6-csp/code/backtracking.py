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
    min_var = None
    for var in csp.variables:
        if var not in assignment:
            var_mrv = mrv(var, assignment, csp)
            if var_mrv < min_mrv:
                min_mrv = var_mrv
                min_var = var
    return min_var


def mrv(var, assignment, csp):  # minimum remaining values
    count = 0
    for value in csp.domains[var]:
        if csp.is_consistent(var, value, assignment):
            count += 1
    return count


def order_domain_values(var, assignment, csp):
    least_constraining_values = []
    for value in csp.domains[var]:
        least_constraining_values.append((value, constraining_value(var, value, assignment, csp)))
    least_constraining_values.sort(key=lambda x: x[1])  # sort by least constraining value
    return [value[0] for value in least_constraining_values]  # return only the values


def constraining_value(var, value, assignment,  csp):  # constraining value
    count = 0
    for constraint in csp.constraints:
        if var in constraint.variables:
            for other_var, other_value in assignment.items():
                if other_var in constraint.variables:
                    if not constraint.is_satisfied({var: value, other_var: other_value}):
                        count += 1
    return count
