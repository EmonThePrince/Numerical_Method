class GaussElimination:
    def __init__(self, A, B):
        """
        Initializes the coefficient matrix A and constant matrix B.
        """
        self.A = [row[:] for row in A]  # Deep copy of A
        self.B = B[:]
        self.n = len(A)

    def forward_elimination(self):
        """Performs forward elimination to convert the system into an upper triangular matrix."""
        for i in range(self.n):
            # Partial Pivoting: Swap rows if pivot is zero
            max_row = i
            for j in range(i + 1, self.n):
                if abs(self.A[j][i]) > abs(self.A[max_row][i]):
                    max_row = j
            if max_row != i:
                self.A[i], self.A[max_row] = self.A[max_row], self.A[i]
                self.B[i], self.B[max_row] = self.B[max_row], self.B[i]

            # Make elements below the pivot zero
            for j in range(i + 1, self.n):
                if self.A[i][i] == 0:
                    raise ValueError("Mathematical Error: Division by zero.")
                factor = self.A[j][i] / self.A[i][i]
                for k in range(i, self.n):
                    self.A[j][k] -= factor * self.A[i][k]
                self.B[j] -= factor * self.B[i]

    def back_substitution(self):
        """Performs back substitution to find the solution vector X."""
        X = [0] * self.n
        for i in range(self.n - 1, -1, -1):
            sum_ax = sum(self.A[i][j] * X[j] for j in range(i + 1, self.n))
            X[i] = (self.B[i] - sum_ax) / self.A[i][i]
        return X

    def solve(self):
        """Solves the system using Gaussian Elimination."""
        self.forward_elimination()
        return self.back_substitution()

# Example usage
A = [[1, 1, 1], 
     [4, 2, 1], 
     [9, 3, 1]]

B = [4, 0, 12]

solver = GaussElimination(A, B)
solution = solver.solve()
print("Solution:", solution)
