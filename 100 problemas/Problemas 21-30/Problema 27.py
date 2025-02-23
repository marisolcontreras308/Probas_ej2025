print("Bienvenido al conversor de unidades")
print("Elige la categoría de unidades a convertir:")
print("1. Longitud")
print("2. Masa")


categoria = input("Elige una opción (1/2): ")

if categoria == "1":
    print("\nCategoría de Longitud:")
    print("1. Metros a Kilómetros")
    print("2. Kilómetros a Metros")
    print("3. Centímetros a Metros")
    opl = input("Elige una opción (1/2/3): ")

    cantidad = float(input("Introduce la cantidad que deseas convertir: "))

    if opl == "1":
        resultado = cantidad / 1000 
        print(cantidad, "metros son", resultado, "kilómetros.")
    elif opl == "2":
        resultado = cantidad * 1000  # Kilómetros a Metros
        print(cantidad, "kilómetros son",resultado, "metros.")
    elif opl == "3":
        resultado = cantidad / 100  # Centímetros a Metros
        print(cantidad, "centímetros son",resultado, "metros.")
    else:
        print("Opción no válida.")

elif categoria == "2":
    print("\nCategoría de Masa:")
    print("1. Gramos a Kilogramos")
    print("2. Kilogramos a Gramos")
    opm = input("Elige una opción (1/2): ")

    cantidad = float(input("Introduce la cantidad que deseas convertir: "))

    if opm == "1":
        resultado = cantidad / 1000  
        print(cantidad, "gramos son", resultado, "kilogramos.")
    elif opm == "2":
        resultado = cantidad * 1000  
        print(cantidad, "kilogramos son", resultado, "gramos.")
    else:
        print("Opción no válida.")


else:
    print("Categoría no válida.")
