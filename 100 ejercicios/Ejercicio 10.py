#Leer ,escribir y modificar un archivo de texto

#ESCRIBIR ARCHIVO,sobreescribe sobre el archivo
with open ("prueba.txt","w") as variable1:
    print("mensaje de texto sms lol", file=variable1)

# Método 2: con variable

variable2 = open("prueba2.txt","w")

#Si se hace con el método 2, es necesario cerrar la variable
print("Hola mundo desde North Korea", file=variable2)

variable2.close()

#Para leer archivo
with open('prueba.txt', 'r') as archivo:
    contenido = archivo.read()

print(contenido)

'''
CREAR ARCHIVO, crear un archivo nuevo que lanza error si el archivo ya existe
with open ("pruebacrear.txt","x") as variable1:
    print("Creando archivo", file=variable1)

'''