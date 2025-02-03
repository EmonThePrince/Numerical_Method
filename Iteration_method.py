class IterationMethod:
    def __init__(self, func, x0, tolerance=1e-6, max_iterations=100):
        self.func = func
        self.x0 = x0
        self.tolerance = tolerance
        self.max_iterations = max_iterations

    def iterate(self):
        x = self.x0
        for i in range(self.max_iterations):
            x_new = self.func(x)
            print(f"Iteration {i+1}: x = {x_new:.6f}")
            if abs(x_new - x) < self.tolerance:
                return x_new
            x = x_new
        raise ValueError("Iteration did not converge within the maximum number of iterations.")


def g(x):
    return (x**2 + 1) / 3  

x0 = float(input("Enter initial guess: "))
method = IterationMethod(g, x0)
root = method.iterate()
print(f"Approximated root: {root:.6f}")
