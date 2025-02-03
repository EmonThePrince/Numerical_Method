def gauss_jordan_elimination(A, b=None):
    n = len(A)
    
    if b is not None:
        for i in range(n):
            A[i].append(b[i])
    
    for i in range(n):
        if A[i][i] == 0:
            for j in range(i + 1, n):
                if A[j][i] != 0:
                    A[i], A[j] = A[j], A[i]
                    break
        
        pivot = A[i][i]
        for k in range(len(A[i])):
            A[i][k] /= pivot
        
        for j in range(n):
            if i != j:
                factor = A[j][i]
                for k in range(len(A[j])):
                    A[j][k] -= factor * A[i][k]
        
    
    if b is not None:
        return [row[-1] for row in A]
    else:
        return [row[:-1] for row in A]

# Example usage
A = [[2, -1, 1], [1, 3, 2], [1, -1, 2]]
b = [8, 13, 7]
x = gauss_jordan_elimination(A, b)
print(A)
print("Solution:", x)
