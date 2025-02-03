import matplotlib.pyplot as plt

# Define the differential equation dy/dx = f(x, y)
def f(x, y):
    return 2*x 

# Euler's method implementation
class EulerMethod:
    def __init__(self, x0, y0, h, n):
        self.x0 = x0
        self.y0 = y0
        self.h = h
        self.n = n

    def run(self):
        x = self.x0
        y = self.y0
        results = [(x, y)]
        for _ in range(self.n):
            y = y + self.h * f(x, y)
            x = x + self.h
            results.append((x, y))
        return results

# Initial conditions
x0 = 1   # Initial x
y0 = 1   # Initial y
h = 0.01  # Step size
n = 100   # Number of steps


e = EulerMethod(x0,y0,h,n)

# Solve using Euler's method
solution = e.run()

# Extract x and y values for plotting
x_vals, y_vals = zip(*solution)

# Plot the solution
plt.plot(x_vals, y_vals, marker='o', label="Euler's Method")
plt.xlabel('x')
plt.ylabel('y')
plt.title("Solution of dy/dx = 2x using Euler's Method")
plt.legend()
plt.grid()
plt.show()

# Print results
for x, y in solution:
    print(f"x = {x:.2f}, y = {y:.4f}")
