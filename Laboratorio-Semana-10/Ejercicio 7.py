import random


def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x <= pivote]
        mayores = [x for x in lista[1:] if x > pivote]
        return quicksort(menores) + [pivote] + quicksort(mayores)


def busqueda_binaria(lista, elemento):
    bajo = 0
    alto = len(lista) - 1
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if lista[medio] == elemento:
            return medio  
        elif lista[medio] < elemento:
            bajo = medio + 1
        else:
            alto = medio - 1
    return -1 


def main():
    n = int(input("¿Cuántos números aleatorios deseas generar? "))
    lista = [random.randint(1, 100) for _ in range(n)] 

    
    print("Lista antes de ordenar:")
    print(lista)

    
    lista_ordenada = quicksort(lista)


    print("\nLista después de ordenar:")
    print(lista_ordenada)

    
    elemento = int(input("\nIngresa el número que deseas buscar en la lista: "))
    resultado = busqueda_binaria(lista_ordenada, elemento)

    if resultado != -1:
        print(f"El número {elemento} se encuentra en el índice {resultado}.")
    else:
        print(f"El número {elemento} no se encuentra en la lista.")


if __name__ == "__main__":
    main()
