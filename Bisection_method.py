import random

class BisectionMethod:
    def __init__(self, func, precision):
        self.func = func
        self.precision = precision
        self.a = None
        self.b = None
        self._generate_interval()

    def _generate_interval(self):
        while True:
            self.a, self.b = sorted([random.uniform(-500, 500), random.uniform(-500, 500)])
            if self.func(self.a) * self.func(self.b) <= 0:
                break

    def find_root(self):
        while (self.b - self.a) / 2 > self.precision:
            mid = (self.a + self.b) / 2
            print(f"Midpoint: {mid}")
            if self.func(mid) == 0:
                return mid
            elif self.func(self.a) * self.func(mid) < 0:
                self.b = mid
            else:
                self.a = mid
        return (self.a + self.b) / 2



def function(x):
    return x**3 - x**2 + 2


precision = float(input("Enter the precision point: "))
bisection = BisectionMethod(function, precision)
root = bisection.find_root()
print(f"The root is: {root}")
