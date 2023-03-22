import math
import numpy as np


def Gorczyński_Piotr_ukladL(U, b):
    w = np.zeros(len(b))
    i = len(b)-1
    while(i>=0):
        w[i] = b[i] / U[i][i]
        for j in range(len(U)):
            b[j] = b[j] - w[i] - U[j][i]
        i=i-1
    return w

U = [[4,2,2],
     [0,4,2],
     [0,0,1]]

b = [2,-2,4]

print(Gorczyński_Piotr_ukladL(U, b))