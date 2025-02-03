import random

class FalsePositionMethod:
    def __init__(self, func, precision):
        self.func = func
        self.precision = precision
        self.a = None
        self.b = None
        self.generateInterval()
    
    def generateInterval(self):
        while True:
            self.a, self.b = sorted([random.uniform(-500, 500), random.uniform(-500, 500)])
            if self.func(self.a) * self.func(self.b) <= 0:
                break

    def findRoot(self):
        mid = None
        i = 0
        while True:
            mid = (self.a * self.func(self.b) - self.b * self.func(self.a))/(self.func(self.b)-self.func(self.a))
            if abs(self.func(mid)) < self.precision:
                return mid
            elif self.func(self.a) * self.func(mid) == 0:
                return mid
            elif self.func(self.a) * self.func(mid) < 0:
                self.b = mid
            else:
                self.a = mid
            print(f"step {i}: a = {self.a}, b = {self.b}, mid = {mid}")
            i += 1
    def execute(self):
        print(f"The root of the equation is: {self.findRoot()}")
    
def function(x):
    return x**2 - 9

method = FalsePositionMethod(function, 0.00001)
method.execute()
