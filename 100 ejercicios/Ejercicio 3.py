num=int(input('Ingrese un número para calcular su factorial: '))
resultado=1
for i in range (1, num+1):
    resultado*=i

print('El factorial de ',num,' es: ', resultado)