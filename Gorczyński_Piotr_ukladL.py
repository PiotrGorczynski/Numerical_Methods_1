import math
import numpy as np


def Gorczyński_Piotr_ukladL(L, b):
    w = np.zeros(len(b))
    for i in range(len(b)):
        w[i] = b[i] / L[i][i]
        for j in range(i + 1, len(L)):
            b[j] = b[j] - w[i] * L[j][i]
    return w

L = [[1,0,0],
     [2,3,0],
     [4,5,5]]

b = [-1,4,1]

print(Gorczyński_Piotr_ukladL(L, b))