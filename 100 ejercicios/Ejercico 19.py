#Numeros aleatorios con distintas distribuciones
from random import randint

listap=list()
listan=list()
elementos=int(input("Introduce la cantidad de elementos:"))
for cont in range(-elementos,elementos):
    if cont <0:
        listan.append(randint(-100,0))
    elif cont>0:
        listap.append(randint(1,100))
    else:
        listap.append(randint(0,1))
 
#Combinar lista

#Forma 1    
listaCompleta = listan + listap

print(listaCompleta)
#Forma2
listap.extend(listan)
print(listap)