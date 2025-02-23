# Sistema Bancario
saldo = input("Ingresa tu saldo inicial")

print("Bienvenido a tu cuenta bancaria")
print("Tu saldo inicial es:",saldo, "unidades.")

while True:
    print("\nOpciones disponibles:")
    print("1. Depositar dinero")
    print("2. Retirar dinero")
    print("3. Consultar saldo")
    print("4. Salir")
    
    opcion = input("Elige una opción (1/2/3/4): ")

    if opcion == "1":
        
        cantidad = float(input("¿Cuánto deseas depositar? "))
        if cantidad > 0:
            saldo += cantidad
            print("Has depositado",cantidad, "unidades. Tu saldo actual es:",saldo, "unidades.")
        else:
            print("Por favor ingresa una cantidad válida mayor que 0.")
    
    elif opcion == "2":
        
        cantidad = float(input("¿Cuánto deseas retirar? "))
        if cantidad > 0:
            if cantidad <= saldo:
                saldo -= cantidad
                print("Has retirado",cantidad, "unidades. Tu saldo actual es:", saldo ,"unidades.")
            else:
                print("No tienes suficiente saldo para realizar esta operación.")
        else:
            print("Por favor ingresa una cantidad válida mayor que 0.")
    
    elif opcion == "3":
       
        print("Tu saldo actual es:" ,saldo, "unidades.")
    
    elif opcion == "4":
        
        print( "¡Hasta luego!")
        break
    
    else:
        print("Opción no válida, por favor elige una opción entre 1 y 4.")
