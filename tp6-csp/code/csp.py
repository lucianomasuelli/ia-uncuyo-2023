

# A CSP for the n-queens problem
class Csp:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def is_consistent(self, var, value, assignment):
        for constraint in self.constraints:
            if var in constraint.variables:
                if not constraint.is_satisfied(assignment):
                    return False
        return True