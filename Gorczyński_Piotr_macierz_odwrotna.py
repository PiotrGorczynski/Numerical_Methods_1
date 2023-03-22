import math
import numpy as np
def Gorczyński_Piotr_macierz_odwrotna(A):
    for i in range(len(A)-1):
        for j in range(i+1,len(A)):
            w = A[j][i]/A[i][i]
            for k in range(i, len(A)):
                A[j][k] = A[j][k] - w * A[i][k]
                b[j][k] = b[j][k] - w * b[i][k]


    for i in range(len(A)-1,0,-1):
        for j in range(i-1,-1,-1):
            w = A[j][i]/A[i][i]
            for k in range(len(A)-1,0,-1):
                A[j][k] = A[j][k] - w * A[i][k]
                b[j][k] = b[j][k] - w * b[i][k]


    for i in b:
        print(i)


A=[[2,3,-1],
   [1,4,2],
   [5,-4,4]]

b = [[1,0,0],
     [0,1,0],
     [0,0,1]]
print(Gorczyński_Piotr_macierz_odwrotna(A))
