#Contar el numero de consonantes y vocales en una cadena
cadena=input(str('Ingrese una cadena de caracteres:' ))

vocales="aeiouAEIOU"
consonantes="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNOPQRSTVWXYZ"
numvocales = 0
numconsonantes = 0

for caracter in cadena:
    if caracter in vocales:
        numvocales +=1
    elif caracter in consonantes:
        numconsonantes+=1
    
print ('El número de vocales es:',numvocales,' y El número de consonates es:',numconsonantes)
