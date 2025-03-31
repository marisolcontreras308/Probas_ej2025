# Manejo de inventarios con listas y diccionarios
inventario = {}

def agregarProducto(nombre, categoria, precio, cantidad):
    producto = {'Nombre': nombre, 'Categoría': categoria, 'Precio': precio, 'Cantidad': cantidad}
    inventario[nombre.lower()] = producto  
    print("Producto '" , nombre , "' agregado al inventario.")

def eliminarProducto(nombre):
    if nombre.lower() in inventario:
        del inventario[nombre.lower()]
        print("Producto '" , nombre , "' eliminado del inventario.")
    else:
         print("Producto '" , nombre , "' no encontrado.")

def buscarProducto(nombre):
    if nombre.lower() in inventario:
        print(inventario[nombre.lower()])
    else:
         print("Producto '" ,nombre , "' no encontrado.")

def productosOrdenadosPorPrecio():
    if not inventario:
        print("El inventario está vacío.")
        return
    productos_ordenados = sorted(inventario.values(), key=lambda producto: producto["Precio"])
    print("Productos ordenados por precio:")
    for producto in productos_ordenados:
        print(producto['Nombre'] , " - Precio: " + str(producto['Precio']) , " - Cantidad: " , str(producto['Cantidad']))


while True:
    print("\nMenú de Inventario:")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Buscar producto")
    print("4. Mostrar productos ordenados por precio")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        nombre = input("Nombre del producto: ")
        categoria = input("Categoría del producto: ")
        precio = float(input("Precio del producto: "))
        cantidad = int(input("Cantidad del producto: "))
        agregarProducto(nombre, categoria, precio, cantidad)
    elif opcion == "2":
        nombre = input("Nombre del producto a eliminar: ")
        eliminarProducto(nombre)
    elif opcion == "3":
        nombre = input("Nombre del producto a buscar: ")
        buscarProducto(nombre)
    elif opcion == "4":
        productosOrdenadosPorPrecio()
    elif opcion == "5":
        print("Saliendo del sistema de inventario.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
