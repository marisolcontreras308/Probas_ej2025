#Resolver ecuaciones cuadráticas
print("Ingresa los valores para resolver la ecuación de la forma ax^2 + bx + c = 0")
a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingresa el valor de c: "))
import math
solucion1 = (-b + math.sqrt(b**2-4*a*c)) / (2*a)
solucion2 = (-b - math.sqrt(b**2-4*a*c)) / (2*a)

print('La soluciones son',solucion1,'y',solucion2)
    