class LagrangeInterpolation:
    def __init__(self, x_values, y_values):
        if len(x_values) != len(y_values):
            raise ValueError("x_values and y_values must have the same length.")
        self.x_values = x_values
        self.y_values = y_values

    def interpolate(self, x):
        result = 0.0
        for i in range(len(self.x_values)):
            term = self.y_values[i]
            for j in range(len(self.x_values)):
                if i != j:
                    term *= (x - self.x_values[j]) / (self.x_values[i] - self.x_values[j])
            result += term
        return result


x_values = list(map(float, input("Enter x values separated by spaces: ").split()))
y_values = list(map(float, input("Enter y values separated by spaces: ").split()))
x_to_interpolate = float(input("Enter the x value to interpolate: "))

lagrange = LagrangeInterpolation(x_values, y_values)
result = lagrange.interpolate(x_to_interpolate)
print(f"Interpolated value at x = {x_to_interpolate}: {result}")