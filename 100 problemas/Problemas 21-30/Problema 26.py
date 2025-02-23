bandera = True
contador = 1
ListaContactos = list()

while bandera:
    op = input(f"¿Quieres agregar un contacto? (s para sí, cualquier otra tecla para salir) (Contacto {contador}): ")
    
    if op.lower() == 's':
        contacto = dict()
        
       
        identificador = input(f"Ingrese el identificador de contacto {contador}: ")
        numero = input(f"Ingrese el número de contacto {contador}: ")

        
        contacto["Identificador"] = identificador
        contacto["Numero"] = numero
        
        ListaContactos.append(contacto)
        contador += 1  
        
    else:
        bandera = False  


print("\nLista de contactos guardados:")
for idx, contacto in enumerate(ListaContactos, 1):
    print(f"Contacto {idx}: {contacto}")
