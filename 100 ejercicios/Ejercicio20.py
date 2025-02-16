#Busqueda lineal y binaria

#Lista
num = int(input("Introduce un número a buscar del 1 al 8: "))
 
listaCompleta =(1,2,3,4,5,6,7,8)
#Búsqueda lineal

for itm in listaCompleta:
    if itm == num:
        print("El numero se encontraba en la posición ", listaCompleta.index(itm))
        break 
            
 #Búsqueda binaria

izquierda = 0
derecha = len(listaCompleta) - 1
encontrado = False

while izquierda <= derecha:
    medio = (izquierda + derecha) // 2  

    if listaCompleta[medio] == num: 
        print(f"El número {num} se encuentra en la posición {medio}")
        encontrado = True
        break
    elif listaCompleta[medio] < num:  
        izquierda = medio + 1
    else:  
        derecha = medio - 1