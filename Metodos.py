import math
from functions import *

titulo()

def Euler(t,y,h,N):
    print("Euler")
    print("\nAproximada\n")
    t_exacta = t

    for k in range(N+1):
        print(k+1,")\t",'y(',round(t, 4),')=', round(y, 4))
        funcion_exacta = f_ex(t_exacta)
        ErrorAbsoluto = abs(funcion_exacta - y)
        ErrorRelativo = ((ErrorAbsoluto) / (abs(funcion_exacta)))              
        print(
            "\t\t\t==========", '\t\t\ty(',round(t_exacta, 2),')=',round(funcion_exacta, 4),
            "\t\t\t==========\t\t", ErrorAbsoluto,
            "\t\t\t==========\t\t\t", ErrorRelativo
            )
        y = y+h*f(t,y)
        t = t+h  
        t_exacta = t_exacta + h
        
         
def Heun(t, y,w, h,N):
    print("Heun\n")
    t_exacta = t

    for k in range(N):
        print('y(',round(t, 2),')=', round(y, 4))
        funcion_exacta = f_ex(t_exacta)
        ErrorAbsoluto = abs(funcion_exacta - y)
        ErrorRelativo = (ErrorAbsoluto / (abs(funcion_exacta)))
        y0 = y+h*g(w)
        w0 = w+h*f(t ,y, w)
        y = y + (h/2) * (g(w) + g(w0))
        w = w + (h/2)*(f(t + h, y0, w0) + f(t, y, w))
        t = t+h       
        print(
            "\t\t\t==========", '\t\t\ty(',round(t_exacta, 2),')=',round(funcion_exacta, 4),
            "\t\t\t==========\t\t\t", ErrorAbsoluto,
            "\t\t\t==========\t\t\t", ErrorRelativo
            )
        t_exacta = t_exacta + h

def Heun(t0, tf, y0, yf, N):
    print("Heun\n")
    t_exacta = t0
    t = t0
    y = y0
    h = (tf - t0) / N
    
    w1 = Heunxd(t0,tf,y0, yf, N, 12)
    w2 = Heunxd(t0,tf,y0, yf, N, -12)

    w = Heunxd(t0,tf,y0, yf, N, 12 + ((-12 - 12) / (w2 - w1)) * (yf - w1))
    print(w)

    for k in range(N):
        print('y(',round(t, 2),')=', round(y, 4), end="")
        funcion_exacta = f_ex(t_exacta)
        ErrorAbsoluto = abs(funcion_exacta - y)
        ErrorRelativo = (ErrorAbsoluto / (abs(funcion_exacta)))
        ya = y+h*g(w)
        wa = w+h*f(t ,y, w)
        y = y + (h/2) * (g(w) + g(wa))
        w = w + (h/2)*(f(t + h, ya, wa) + f(t, y, w))
        t = t + h
        print(
            "\t\t\t==========", '\t\t\ty(',round(t_exacta, 2),')=',round(funcion_exacta, 4),
            "\t\t\t==========\t\t\t", ErrorAbsoluto,
            "\t\t\t==========\t\t\t", ErrorRelativo
            , "\n")
        t_exacta = t_exacta + h

    
def Heunxd(t0, tf, y0, yf, N, w):
    t_exacta = t0
    t = t0
    y = y0
    h = (tf - t0) / N

    for k in range(N):
        funcion_exacta = f_ex(t_exacta)
        ErrorAbsoluto = abs(funcion_exacta - y)
        ErrorRelativo = (ErrorAbsoluto / (abs(funcion_exacta)))
        ya = y+h*g(w)
        wa = w+h*f(t ,y, w)
        y = y + (h/2) * (g(w) + g(wa))
        w = w + (h/2)*(f(t + h, ya, wa) + f(t, y, w))
        t = t + h
        t_exacta = t_exacta + h

    return y



print("\n")


print("\n")

Heun(0, math.pi / 6, math.sqrt(3), math.sqrt(3), 10)
#    t0,  tf,            y0,           yf,        n

reinicio()