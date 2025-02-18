#Encontrar el mayor entre tres números dados
num1=float(input('Ingrese el primer número:'))
num2=float(input('Ingrese el segundo número:'))
num3=float(input('Ingrese el tercer número:'))
nummayor=0

if num1>num2:
    nummayor=num1
    if num1>num3:
        nummayor=num1
elif num2>num3:
    nummayor=num2
else:
    nummayor=num3

print('El número mayor es',nummayor)