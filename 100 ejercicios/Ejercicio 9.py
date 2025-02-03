
limite = int(input("Introduce el límite: "))

pares = []
impares = []

for i in range(1, limite + 1):  
    if i % 2 == 0:
        pares.append(i) 
    else:
        impares.append(i)

print("Números pares:", pares)
print("Números impares:", impares)