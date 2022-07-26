
from matplotlib import pyplot as plt
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

"""a = float(input("Ingrese el valor de a: "))
   b = float(input("Ingrese el valor de b: "))
   h = 
"""

print("\n")


print("\n")
Heun(0, 0, 1, 0.05, 10)
#    t, y, yd, h, n

reinicio()




