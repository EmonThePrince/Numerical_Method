class RungeKutta:
    def __init__(self, func, x0, y0, n = 2, h = 0.1):
        self.h = h
        self.func = func
        self.x = [x0 + i*self.h for i in range(n+1)]
        self.y = [y0]

        
        self.n = len(self.x)
        
    def run(self):
        for i in range(self.n-1):
            k1 = self.h*self.func(self.x[i], self.y[i])
            k2 = self.h*self.func(self.x[i] + 0.5*self.h, self.y[i]+k1/2)
            k3 = self.h*self.func(self.x[i] + 0.5*self.h, self.y[i]+k2/2)
            k4 = self.h*self.func(self.x[i] + self.h, self.y[i]+k3)
            self.y.append(self.y[i] + (k1 + 2*k2 + 2*k3 + k4)/6)
        return self.y
    
def function(x,y):
    return x + y**2
r = RungeKutta(function, 0, 1)
print(r.run())