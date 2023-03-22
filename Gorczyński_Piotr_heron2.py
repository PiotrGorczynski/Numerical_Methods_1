import math
import numpy as np

def Gorczyński_Piotr_heron2(a,x):
    wynik = 0
    for i in range(len(a)):
        wynik = a[i]+x*wynik
    return wynik


a = [2,4,5,2]
print(Gorczyński_Piotr_heron2(a,2))




