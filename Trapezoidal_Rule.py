import math

class TrapezoidalRule:
    def __init__(self, func, a, b, n = 6):
        self.func = func
        self.a = a
        self.b = b
        self.n = n
        self.h = (b-a)/n
        self.x = [self.a + i*self.h for i in range(n+1)]
        self.y = [func(x) for x in self.x]

    def getIntegratedValue(self):
        ans = (self.y[0]+self.y[self.n])/2
        for i in range(1, self.n):
            ans += self.y[i]
        ans *= self.h
        return ans
    
def function(x):
    return math.sin(x) - math.log(x) + math.exp(x)

t = TrapezoidalRule(function, 0.2,1.4)
print(t.getIntegratedValue()) 