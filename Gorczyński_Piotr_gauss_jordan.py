import math
import numpy as np
def Gorczyński_Piotr_gauss_jordan(A,b):
    for i in range(len(A)-1):
        for j in range(i+1,len(A)):
            w = A[j][i]/A[i][i]
            b[j] = b[j] - w*b[i]
            for k in range(i, len(A)):
                A[j][k] = A[j][k] - w*A[i][k]

    for i in range(len(A)-1,0,-1):
        for j in range(i-1,-1,-1):
            w = A[j][i]/A[i][i]
            b[j] = b[j] - w*b[i]
            for k in range(len(A)-1,0,-1):
                A[j][k] = A[j][k] - w*A[i][k]




    for i in A:
        print(i)

    print("\nb:",b)

A=[[2,3,-1],
   [1,4,2],
   [5,-4,4]]

b=[4,10,2]
print(Gorczyński_Piotr_gauss_jordan(A,b))