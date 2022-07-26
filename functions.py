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
e=2.718281 

def f(t, y):
    return ((3*y) + (2*t))

def f(t,y,w):
    return (2 * exp(t)) - (2 * w) - y    

def g(w): 
    return w

def f_ex(t):
    return ((-1/2) * (exp(-t)) + (1/2) * t * (exp(-t)) + exp(t)) /2

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


