import math
import numpy as np

def Gorczyński_Piotr_suma_mac(A, B):
    C = np.zeros((len(A),len(A[0])))
    for i in range(len(A)):
        for j in range(len(A[0])):
           C[i][j] = A[i][j]+B[i][j]
    for i in C:
        print(i)


A = [
    [5, 2, 1],
    [3, 6, 2],
    [9, 5, 3]
]

B = [
    [7, 11, 3],
    [4, 4, 7],
    [2, 3, 8]
]

print(Gorczyński_Piotr_suma_mac(A,B))