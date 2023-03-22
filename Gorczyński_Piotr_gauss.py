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


def Gorczyński_Piotr_gauss(A,b):
        L = np.identity(len(A))
        for i in range(len(A)-1):
            for j in range(i + 1, len(A)):
                w = A[j][i] / A[i][i]
                b[j] = b[j] - w * b[i]
                L[j][i] = w
                for k in range(i, len(A)):
                    A[j][k] = A[j][k] - w * A[i][k]
        for i in A:
            print(i)
        print("")

        for j in L:
            print(j)

A=[[2,1,-1],
   [-3,-1,2],
   [-2,1,2]]

b=[8,-11,-3]

print(Gorczyński_Piotr_gauss(A,b))