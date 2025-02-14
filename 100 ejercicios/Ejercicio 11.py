#Verificar si una cadena es un palíndromo

frase=str(input("Ingrese la frase para verificar si es un palíndromo"))
frase = frase.replace(" ", "").lower()
reverso = ""
for i in range(len(frase) - 1, -1, -1):
        reverso += frase[i]
    
    
if frase==reverso:
        print("Es un palíndromo")
else:
        print('No es un palíndromo')