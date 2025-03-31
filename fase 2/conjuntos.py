conjuntos={1,2,3,4}
conjuntos.add(5)
print(conjuntos)

conjunto3=conjuntos.copy()
print(conjunto3)

conjunto2=[3,4,5,6]
print(conjuntos.difference(conjunto2))
print(conjuntos.intersection(conjunto2))

print(conjuntos.isdisjoint(conjunto2))

conjuntos.pop()
print(conjuntos)