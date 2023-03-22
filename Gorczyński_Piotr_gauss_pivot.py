import math
import numpy as np

def Drukuj(A,L,b):
    for i in A:
        print(i)
    print("")

    for j in L:
        print(j)
    print("")

    print("b:",b)

def Zamień(Z, k):
    for i in range(k, len(Z)):
        if(Z[i]>Z[k]):
            tmp = A[i]
            A[i] = A[k]
            A[k] = tmp

def Gorczyński_Piotr_gauss_pivot(A, b):
    L = np.identity(len(A))
    for i in range(len(A) - 1):
        Zamień(A, i)
        for j in range(i+1, len(A)):
            w = A[j][i] / A[i][i]
            b[j] = b[j] - w * b[i]
            L[j][i] = w
            for n in range(i, len(A)):
                A[j][n] = A[j][n] - w * A[i][n]
    Drukuj(A, L, b)

A=[[2,1,-1],
   [-3,-1,2],
   [-2,1,2]]

b=[8,-11,-3]

print(Gorczyński_Piotr_gauss_pivot(A,b))