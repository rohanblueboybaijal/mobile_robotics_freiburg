import numpy as np 
import math

def isOrthogonal(Q):
    n = Q.shape[0]
    M = Q@Q.T
    I = np.identity(n)
    flag = True
    for i in range(n):
        for j in range(n):
            flag = np.isclose(I[i][j], M[i][j])
            if not flag:
                return False
    
    return True


A = np.array([[2,2,-1],[2,-1,2],[-1,2,2]])
A = A/3
check = isOrthogonal(A)
print(check)