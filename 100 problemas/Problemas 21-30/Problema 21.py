#Convertir una temperatura a distintas escalas
print('Selecciona la figura geométrica para hacer los cálculos:')
print('1.Cilindro')
print('2.Cubo')
print('3.Pirámide')

op1=int(input('Ingrese la opción 1,2 o 3:'))
area=0
vol=0
from math import pi
if op1==1:
    radio = float(input("Introduce el radio de la base de circulo: "))
    h=float(input("Introduce la altura del cilindro: "))
    area=round(pi*(radio)**2,2)
    vol=round(area * h,2)
    print('El área de la base es de:',area ,'u')
    print('El volumen del cuerpo es de:',vol,'u^2')
    
elif op1==2:
    lado= float(input("Introduce la medida de uno de los lados: "))
    area=round(lado**2,2)
    vol=round(lado**3,2)
    print('El área de la base es de:',area ,'u')
    print('El volumen del cuerpo es de:',vol,'u^2')

elif op1==3:
    Lm= float(input("Introduce la medida del lado menor del rectángulo: "))
    Lmay= float(input("Introduce la medida del lado mayor del rectángulo: "))
    h= float(input("Introduce la altura del prisma: "))
    area=round(Lm*Lmay,2)
    vol=round(area*h,2)
    print('El área de la base es de:',area ,'u')
    print('El volumen del cuerpo es de:',vol,'u^2')
    

else:
    base= float(input("Introduce la medida de la base del triángulo: "))
    h= float(input("Introduce la medida de la altura del triángulo: "))
    hp= float(input("Introduce la altura de la pirámide: "))
    area=round((base*h)/2,2)
    vol=round(1/3 *(area),2)
    print('El área de la base es de:',area ,'u')
    print('El volumen del cuerpo es de:',vol,'u^2')
