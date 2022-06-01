
from functions import *

titulo()



def Euler(t,y,h,N):
    temp=0
    print("Euler")
    print("\nAproximada\n")
    y_exacta = y
    t_exacta = t

    for k in range(N):
        print('y(',round(t, 2),')=', round(y, 4))
        funcion_exacta = f_ex(t_exacta)
        ErrorAbsoluto = abs(y - funcion_exacta)
        ErrorRelativo = 100*(ErrorAbsoluto/(abs(funcion_exacta)))
        y = y+h*f(t,y)
        t = t+h        
        print(
            "\t\t\t==========", '\t\t\ty(',round(t_exacta, 2),')=',round(funcion_exacta, 4),
            "\t\t\t==========\t\t", ErrorAbsoluto,
            "\t\t\t==========\t\t\t", ErrorRelativo
            )
        t_exacta = t_exacta + h
        
         
def Heun(t,y,h,N):
    print("Heun\n")
    y_exacta = y
    t_exacta = t

    for k in range(N):
        print('y(',round(t, 2),')=', round(y, 4))
        funcion_exacta = f_ex(t_exacta)
        ErrorAbsoluto = abs(y - funcion_exacta)
        ErrorRelativo = 100*(ErrorAbsoluto/(abs(funcion_exacta)))
        y0 = y+h*f(t,y)
        y = y+(h/2)*(f(t,y)+f(t, y0))
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


Euler(0,2/9,0.05,100)
print("\n")
Heun(0,2/9,0.05,100)

reinicio()




