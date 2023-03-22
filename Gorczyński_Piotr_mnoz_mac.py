import math
import numpy as np

def Gorczyński_Piotr_mnoz_mac(A,B):
    C = np.zeros((len(A),len(A[0])))

    if(len(A)!=len(B[0])):
        print("Mnożenie niemożliwe.")

    else:
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    C[i][j]=C[i][j]+A[i][k]*B[k][j]

        for i in C:
            print(i)


A = [
    [1, 2, 3],
    [2, 3, 1],
    [3, 2, 1]
]

B = [
    [1, 1, 2],
    [2, 2, 1],
    [1, 2, 1]
]

print(Gorczyński_Piotr_mnoz_mac(A,B))


