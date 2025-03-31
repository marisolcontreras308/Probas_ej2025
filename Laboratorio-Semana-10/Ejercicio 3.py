#Gestión de Contactos con Tuplas y Estructuras Anidadas

bandera = True
contador = 1
ListaContactos = list()

def buscarcontacto(identificador):
    # Buscamos el contacto por identificador
    for contacto in ListaContactos:
        if contacto[0].lower() == identificador.lower():  # contact[0] es el identificador
            print(f"Contacto encontrado: {contacto}")
            return
    print("Contacto no encontrado")

def listar_contactos():
    # Listamos los contactos en orden alfabético por el identificador
    if not ListaContactos:
        print("No hay contactos en la agenda.")
        return
    contactos_ordenados = sorted(ListaContactos, key=lambda contacto: contacto[0].lower())  
    print("Lista de contactos ordenada alfabéticamente:")
    for contacto in contactos_ordenados:
        print(f"Identificador: {contacto[0]}, Número: {contacto[1]}, Correo: {contacto[2]}")
#Entramos en un while donde se preentarán las opciones a elegir, el while se romperá cuando el usuario elija n y bandera=false
while bandera:
    op = input(f"Cantidad de contactos: {contador-1} \n ¿Desea agregar un contacto? Presione (S) para agregar, (B) para buscar, (L) para listar, (N) para salir: ")

    if op.lower() == 's':
        # Creamos un nuevo contacto como tupla
        identificador = input(f"Ingrese el identificador de contacto {contador}: ")
        numero = input(f"Ingrese el número de contacto {contador}: ")
        correo = input(f"Ingrese su correo {contador}: ")
        contacto = (identificador, numero, correo)  
        ListaContactos.append(contacto)
        contador += 1
    
    elif op.lower() == 'b':
      
        buscarid = input('Ingrese el identificador del contacto que desea buscar: ')
        buscarcontacto(buscarid)

    elif op.lower() == 'l':
        
        listar_contactos()

    elif op.lower() == 'n':
        print("Saliendo del sistema de contactos.")
        bandera = False  

    else:
        print("Opción no válida. Intente de nuevo.")
