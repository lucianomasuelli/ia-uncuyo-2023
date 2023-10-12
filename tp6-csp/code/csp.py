# A CSP for the n-queens problem
class Csp:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def is_consistent(self, var, value, assignment):
        new_assignment = dict(assignment)  # copy assignment
        new_assignment[var] = value
        for constraint in self.constraints:
            if var in constraint.variables:
                if not constraint.is_satisfied(new_assignment):
                    return False
        return True


# A constraint for the n-queens problem
class Constraint:
    def __init__(self, variables):
        self.variables = variables

    def is_satisfied(self, assignment):
        pass


class RowsConstraint(Constraint):
    def __init__(self, variables):
        super().__init__(variables)

    def is_satisfied(self, assignment):
        for var1 in self.variables:
            for var2 in self.variables:
                if var1 != var2:
                    if var1 in assignment and var2 in assignment:
                        # Verifica restricciones de columna
                        if assignment[var1] == assignment[var2]:
                            return False
        return True


class DiagonalsConstraint(Constraint):
    def __init__(self, variables):
        super().__init__(variables)

    def is_satisfied(self, assignment):
        for var1 in self.variables:
            for var2 in self.variables:
                if var1 != var2:
                    if var1 in assignment and var2 in assignment:
                        # Verifica restricciones de diagonal
                        if abs(assignment[var1] - assignment[var2]) == abs(var1 - var2):
                            return False
        return True
