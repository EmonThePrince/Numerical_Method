class NewtonRaphsonSolver:
    def __init__(self, function, derivative, initial_guess, tolerance=1e-6, max_iterations=100):
        self.f = function
        self.df = derivative
        self.x = initial_guess
        self.tolerance = tolerance
        self.max_iterations = max_iterations
    
    def solve(self):
        for _ in range(self.max_iterations):
            f_x = self.f(self.x)
            df_x = self.df(self.x)
            
            if df_x == 0:
                raise ValueError("Derivative is zero. Newton-Raphson method fails.")
            
            x_new = self.x - f_x / df_x
            
            # Check for convergence
            if abs(x_new - self.x) < self.tolerance:
                return x_new
            
            self.x = x_new
        
        raise ValueError("Newton-Raphson method did not converge within the maximum iterations")

# Example Usage
def func(x):
    return x**2 - 4  # Example: f(x) = x^2 - 4 (roots: ±2)

def dfunc(x):
    return 2*x  # Derivative: f'(x) = 2x

solver = NewtonRaphsonSolver(func, dfunc, initial_guess=3.0)
root = solver.solve()
print("Root:", root)
