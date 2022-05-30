from math import *
from pickle import BINFLOAT
import numpy as np
import os
import matplotlib as plt
from functions import *

titulo()



def Euler(t,y,h,N):
    temp=0
    print("Euler")
    print("\nAproximada\n")
    print('y(',y,')=',y)
    temp = t
    temp2 = y
    Errores = float
    for k in range(N):
        y = y+h*f(t,y)
        t = t+h
        print('y(',round(t, 2),')=', round(y, 4))
    print("\nExacta")
    for i in range(N+1):    
        print('y(',round(t, 2),')=',round(f_ex(temp), 4))
        temp = temp + h 
  
    print("\nErrores")
    
    """for j in range(N+1):
        y = y+h*f(t,y)
        y_exacta = f_ex(temp)       
        t = t+h
        temp = temp +h
        Errores = y - y_exacta
        print((j+1),")\t",round(y, 4), "\t\t\t------", round(y_exacta, 4), "\t\t\t\t\t-------", round(Errores, 4))
"""
        
         
    

def Heun(t,y,h,N):
    print("Heun")
    print('y(',y,')=',y)
    temp = t
    temp2 = y
    for k in range(N):
        y0 = y+h*f(t,y)
        y = y+(h/2)*(f(t,y)+f(t, y0))
        t = t+h
        print('y(',round(t, 2),')=', round(y, 4))
    print("\nExacta")
    for i in range(N+1):    
        print(round(f_ex(temp), 4))
        temp = temp + h 

"""h = float(input("Ingrese el valor de h: "))
t = float(input("Ingrese el valor de t: "))
y = float(input("Ingrese el valor de y: "))
N = int(input("Ingrese el rango: "))"""

print("\n")


Euler(1,7,0.4,10)
print("\n")
Heun(1,7,0.4,10)

reinicio()




