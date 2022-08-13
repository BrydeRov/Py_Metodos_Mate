from math import *
import os

def f(t, y):
    return ((3*y) + (2*t))

def f(t,y,w):
    #return (exp(y,w*2)) + (4*y)    
    return -4 * y

def g(w): 
    return w

def f_ex(t):
    return ((1) * (sin(2*t)) + (sqrt(3)) * cos(2 * t))

def titulo():
    print('\nMétodo de disparo para Valores de Frontera | Javier Camacho & Humberto Orozco\n')
    print("La ecuación es y'' + 4y, y(0) = √3, y(π/6) = √3\n")


def reinicio():
    reinicio = input("¿Desea volver al inicio? S/N: ")
    if(reinicio == "S"):
        os.system("cls")
        os.system("py Metodos.py")
    else:
        exit()