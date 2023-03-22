import math
import numpy as np
def Gorczyński_Piotr_heron(a,x,eps):
    while abs(a-math.pow(x,2))>eps:
        x = 0.5*(x+a/x)
    return x



print(Gorczyński_Piotr_heron(24,4,0.001))