class NewtonInterpolation:
    def __init__(self, x_values, y_values):
        if len(x_values) != len(y_values):
            raise ValueError("x_values and y_values must have the same length.")
        self.x_values = x_values
        self.y_values = y_values
        self.n = len(x_values)
        self.forward_diff_table = self._compute_forward_differences()
        self.backward_diff_table = self._compute_backward_differences()

    def _compute_forward_differences(self):
        table = [[0] * self.n for _ in range(self.n)]
        for i in range(self.n):
            table[i][0] = self.y_values[i]
        for j in range(1, self.n):
            for i in range(self.n - j):
                table[i][j] = table[i + 1][j - 1] - table[i][j - 1]
        return table

    def _compute_backward_differences(self):
        table = [[0] * self.n for _ in range(self.n)]
        for i in range(self.n):
            table[i][0] = self.y_values[i]
        for j in range(1, self.n):
            for i in range(self.n - 1, j - 1, -1):
                table[i][j] = table[i][j - 1] - table[i - 1][j - 1]
        return table

    def forward_interpolate(self, x):
        h = self.x_values[1] - self.x_values[0]
        p = (x - self.x_values[0]) / h
        result = self.y_values[0]
        factorial = 1
        product_term = 1
        
        for i in range(1, self.n):
            factorial *= i
            product_term *= (p - (i - 1))
            result += (self.forward_diff_table[0][i] * product_term) / factorial
        
        return result

    def backward_interpolate(self, x):
        h = self.x_values[1] - self.x_values[0]
        p = (x - self.x_values[-1]) / h
        result = self.y_values[-1]
        factorial = 1
        product_term = 1
        
        for i in range(1, self.n):
            factorial *= i
            product_term *= (p + (i - 1))
            result += (self.backward_diff_table[-1][i] * product_term) / factorial
        
        return result


x_values = list(map(float, input("Enter x values separated by spaces: ").split()))
y_values = list(map(float, input("Enter y values separated by spaces: ").split()))
x_to_interpolate = float(input("Enter the x value to interpolate: "))

newton_interp = NewtonInterpolation(x_values, y_values)
forward_result = newton_interp.forward_interpolate(x_to_interpolate)
backward_result = newton_interp.backward_interpolate(x_to_interpolate)

print(f"Forward Interpolation result at x = {x_to_interpolate}: {forward_result}")
print(f"Backward Interpolation result at x = {x_to_interpolate}: {backward_result}")
