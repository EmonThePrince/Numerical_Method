class LinearCurveFitting:
    def __init__(self, x_values, y_values):
        if len(x_values) != len(y_values):
            raise ValueError("x_values and y_values must have the same length.")
        self.x_values = x_values
        self.y_values = y_values
        self.n = len(x_values)
        self.slope, self.intercept = self._compute_coefficients()

    def _compute_coefficients(self):
        n = self.n
        sum_x = sum(self.x_values)
        sum_y = sum(self.y_values)
        sum_xx = sum(x * x for x in self.x_values)
        sum_xy = sum(x * y for x, y in zip(self.x_values, self.y_values))
        
        denominator = n * sum_xx - sum_x ** 2
        if denominator == 0:
            raise ValueError("Cannot compute linear regression, check your input data.")
        
        slope = (n * sum_xy - sum_x * sum_y) / denominator
        intercept = (sum_y - slope * sum_x) / n
        return slope, intercept

    def predict(self, x):
        return self.slope * x + self.intercept

x_values = list(map(float, input("Enter x values separated by spaces: ").split()))
y_values = list(map(float, input("Enter y values separated by spaces: ").split()))
x_to_predict = float(input("Enter the x value to predict y: "))

linear_fit = LinearCurveFitting(x_values, y_values)
predicted_y = linear_fit.predict(x_to_predict)

print(f"Equation of line: y = {linear_fit.slope:.4f}x + {linear_fit.intercept:.4f}")
print(f"Predicted y value at x = {x_to_predict}: {predicted_y:.4f}")