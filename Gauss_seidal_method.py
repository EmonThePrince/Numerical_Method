class GaussSeidelSolver:
    def __init__(self, A, b, tolerance=1e-6, max_iterations=100):
        self.A = A
        self.b = b
        self.tolerance = tolerance
        self.max_iterations = max_iterations
        self.n = len(b)  

    def solve(self):
        x = [0.0] * self.n 
        
        for _ in range(self.max_iterations):
            x_new = x.copy()
            
            for i in range(self.n):
                sum1 = sum(self.A[i][j] * x_new[j] for j in range(i))  # Using updated values
                sum1 += sum(self.A[i][j] * x[j] for j in range(i + 1, self.n))  # Using old values
                
                x_new[i] = (self.b[i] - sum1) / self.A[i][i]
            
            # Check for convergence
            if all(abs(x_new[i] - x[i]) < self.tolerance for i in range(self.n)):
                return x_new
            
            x = x_new
        
        raise ValueError("Gauss-Seidel method did not converge within the maximum iterations")

# Example Usage

A = [[2, -1, 0],
     [-1, 2,-1],
     [0, -1, 2]]

b = [7,1,1]

solver = GaussSeidelSolver(A, b)
solution = solver.solve()
print("Solution:", solution)