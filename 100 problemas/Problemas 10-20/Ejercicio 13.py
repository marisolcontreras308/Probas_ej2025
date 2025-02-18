#Convertir una temperatura a distintas escalas
print('Selecciona la escala de temperatura de origen:')
print('1.Celcius')
print('2.Farenheit')
print('3.Kelvin')

op1=int(input('Ingrese la opción 1,2 o 3:'))
temperatura=0
if op1==1:
    temperatura = float(input("Introduce la temperatura en Celsius: "))
    
    print('La temperatura son:',temperatura + 273.15,'K°')
    print('La temperatura son:',temperatura * 9/5 + 32,'F°')
    
elif op1==2:
    temperatura = float(input("Introduce la temperatura en Farenheit: "))
    print('La temperatura son:',(temperatura - 32) * 5/9,'C°')
    print('La temperatura son:',(temperatura - 32) * 5/9 + 273.15,'K°')

else:
    temperatura = float(input("Introduce la temperatura en Kelvin: "))
    print('La temperatura son:',temperatura - 273.15,'C°')
    print('La temperatura son:',(temperatura - 273.15) * 9/5 + 32,'F°')
