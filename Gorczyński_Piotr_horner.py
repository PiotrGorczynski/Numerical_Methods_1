import math
import numpy as np

def Gorczyński_Piotr_horner(a,c):
    w = np.zeros(len(a))
    w[0] = 0
    for i in range(len(a)):
        w[i] = a[i] + w[i-1]*c
    return w

a = [4, 2, 1, 3]
c = 2
print(Gorczyński_Piotr_horner(a, c))