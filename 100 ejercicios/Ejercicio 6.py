#Interés compuesto
cap=float(input('Ingrese el monto de depósito inicial: '))
int=float(input('Ingrese la tasa de interés anual (solo el número): '))
tiempo=float(input('Ingrese el tiempo en años: '))
periodo=float(input('Ingresa el número de veces que se capitaliza el interés al año (mensual=12, anual=1, semestral=2  etc.):'))
int=int/100
intc=float(0)
intc=cap*(1+int/periodo)**(periodo*tiempo)-cap
print('El monto con interés compuesto es :',round(intc,2))
