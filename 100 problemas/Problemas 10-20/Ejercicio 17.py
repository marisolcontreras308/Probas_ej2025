#pila,cola,lista enlazada
pila=list()
def insertarPila(pila, elemento):
    pila.append(elemento)
    return pila


def eliminarPila(pila):
    elementoFinal = pila[len(pila)-1]
    pila.remove(elementoFinal)
    return pila