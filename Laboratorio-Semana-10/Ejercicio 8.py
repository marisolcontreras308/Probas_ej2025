#Implementación de mergesort
def mergesort(lista):
    if len(lista) > 1:
        # Encuentra el punto medio de la lista
        medio = len(lista) // 2
        izquierda = lista[:medio] 
        derecha = lista[medio:]   

        # Llamada recursiva para ordenar las sublistas
        mergesort(izquierda)
        mergesort(derecha)

        # Inicialización de los índices para las sublistas
        i = j = k = 0

        # Mezcla las dos sublistas ordenadas
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        # Si quedan elementos en la sublista izquierda
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        # Si quedan elementos en la sublista derecha
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1


numeros = input("Ingrese los números separados por espacio: ").split()
lista = [int(num) for num in numeros]  

print("Lista antes de ordenar:")
print(lista)

mergesort(lista)

print("\nLista después de ordenar:")
print(lista)