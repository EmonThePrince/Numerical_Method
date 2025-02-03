

class SimpsonsRule:
    def __init__(self, func, a, b, n= 6):
        self.a = a
        self.b = b
        self.n = n
        self.func = func
        self.h = (b - a) / n
        self.x = [self.a + i*self.h for i in range(n+1)]
        self.y = [self.func(x) for x in self.x]
    def getIntegratedValue(self):
        ans = self.y[0] + self.y[self.n]
        for i in range(1, self.n):
            if i % 2 == 0:
                ans += 2 * self.y[i]
            else:
                ans += 4 * self.y[i]
        ans *= self.h/3
        return ans

def function(x):
    return x**3
s = SimpsonsRule(function, 0.0, 2.0)
print(s.getIntegratedValue()) 
        