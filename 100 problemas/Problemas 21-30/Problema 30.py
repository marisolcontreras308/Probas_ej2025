def calcular_factorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

num = int(input('Ingrese un número para calcular su factorial: '))

resultado = calcular_factorial(num)


print(f'El factorial de {num} es: {resultado}')