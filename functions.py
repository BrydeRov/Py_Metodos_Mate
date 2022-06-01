import numpy as np
import matplotlib as plt
from math import *
import numpy as np
import os
import math




global t
t = float
global y
y = float
global h
h = float
global N
N = int
global y0
y0 = float
global errorAbs 
errorAbs = float   

def f(t, y):
    func = ((3*y) + (2*t))
    return func

def f_ex(t):
    f_ex = np.exp((3*t) + (pow(t,2)))
    return f_ex

def titulo():
    print('\nMétodo de Heun & Euler | Javier Camacho & Humberto Orozco\n')
    print("La ecuación es f(y,t) | y'= 10 - (t/y)\n")



def reinicio():
    reinicio = input("¿Desea volver al inicio? S/N: ")
    if(reinicio == "S"):
        os.system("cls")
        os.system("py Metodos.py")
    else:
        exit()


