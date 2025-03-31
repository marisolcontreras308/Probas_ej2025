#Ánalisis de texto con diccionarios y conjuntos
def análisisDeTexto(texto):
    #para contar las palabras primero convertimos todas las palabras del texto a minúsculas y después dividimos la cadena en palabras individuales con split
    palabras=texto.lower().split()
    tpalabras=len(palabras)
    palabras_unicas=set(palabras)

    print('El total de palabras es:',tpalabras,'Y las palabras únicas que aparecen son:',palabras_unicas)

    
#Hacemos un diccionario que toma como clave tomas las palabras y como valor las frecuencias
    frecuencia=dict()
    for palabra in palabras:
        frecuencia[palabra]=frecuencia.get(palabra, 0) + 1
        #para encontrar la palabra más frecuente usamos max y key para encontrar la clave que más se repite
        palabra_mas_frecuente = max(frecuencia, key=frecuencia.get)
        #luego ya que tenemos la palabra más frecuente buscamos us valor correspondiente en el diccionario para saver cuantas veces se repite
        frecuencia_maxima = frecuencia[palabra_mas_frecuente]

        #recorremos el diccionario
    for palabra in frecuencia:
           print(palabra,frecuencia[palabra])
    print('La palabra más frecuente es "',palabra_mas_frecuente,'" con',frecuencia_maxima,'apariciones.')
   

texto_usuario = input("Ingrese un texto: ")
análisisDeTexto(texto_usuario)