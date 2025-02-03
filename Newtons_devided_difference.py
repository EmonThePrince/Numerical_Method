class NewtonsDivided:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n =len(x)
    
    def _calculateTable(self):
        table = [[0*i for i in range(self.n)] for _ in range(self.n)]
        for col in range(0,self.n):
            for row in range(0,self.n-max(0,col-1)):
                if(col == 0):
                    table[row][col] = self.x[row]
                elif(col == 1):
                    table[row][col] = self.y[row]
                else:
                    table[row][col] = (table[row+1][col-1] - table[row][col-1])/(table[row+(col-1)][0] - table[row][0])
        return table
             
    def calculateDivided(self,x):
        table = self._calculateTable()
        factor = 1
        ans = 0
        for i in range(1,self.n):
            ans += factor*table[0][i]
            factor *= (x-table[i-1][0])
        return ans


x = [4,5,7,10,11,13]
y = [48,100,294, 900, 1210,2028]

n = NewtonsDivided(x,y)
for x in n._calculateTable():
    print(x)
print(n.calculateDivided(15))

