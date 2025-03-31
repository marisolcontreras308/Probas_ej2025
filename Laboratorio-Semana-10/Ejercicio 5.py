#Módulo para conversión de unidades
import conversor
bandera=True

while bandera:
    print("Seleccione la conversión que desea realizar:")
    print("1. Kilómetros a millas")
    print("2. Celsius a Fahrenheit")
    print("3. Litros a galones")
    print("4. Salir")

    opcion = input("Ingrese el número de la opción: ")

    if opcion == "1":
        km = float(input("Ingrese los kilómetros: "))
        millas = conversor.km_a_millas(km)  
        print(f"{km} kilómetros son {millas} millas.")
    
    elif opcion == "2":
        celsius = float(input("Ingrese la temperatura en Celsius: "))
        fahrenheit = conversor.celsius_a_fahrenheit(celsius)  
        print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")
    
    elif opcion == "3":
        litros = float(input("Ingrese la cantidad de litros: "))
        galones = conversor.litros_a_galones(litros)

    elif opcion == "4":
        
         bandera=False
        
    else:
         print("Opción no válida. Intente de nuevo.")