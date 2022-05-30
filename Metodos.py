from math import *
from pickle import BINFLOAT
import numpy as np
import os
import matplotlib as plt
from functions import *

titulo()



def Euler(t,y,h,N):
    print("Euler")
    print('y(',y,')=',y)
    for k in range(N):
        y = y+h*f(t,y)
        t = t+h
        print('y(',round(t, 2),')=', round(y, 4))

def Heun(t,y,h,N):
    print("Heun")
    print('y(',y,')=',y)
    for k in range(N):
        y0 = y+h*f(t,y)
        y = y+(h/2)*(f(t,y)+f(t, y0))
        t = t+h
        HeunFor = 'y(',round(t, 2),')=', round(y, 4)
    for i in range(1):
        for j in range(1):
            print('"Euler\t\t\t\tHeun\t\t\t\tErrorAbs')
        print('')
    for k in range(N):
        for m in range(1):
            print(HeunFor)
        print('')
            

h = float(input("Ingrese el valor de h: "))
t = float(input("Ingrese el valor de t: "))
y = float(input("Ingrese el valor de y: "))
N = int(input("Ingrese el rango: "))

print("\n")


Euler(t,y,h,N)
print("\n")
Heun(t,y,h,N)




