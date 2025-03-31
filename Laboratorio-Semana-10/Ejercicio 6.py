# Clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, año, precio):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio

    def info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Precio: {self.precio}")

# Subclase Automovil
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, precio, num_puertas):
        
        super().__init__(marca, modelo, año, precio)
        self.num_puertas = num_puertas

    def info(self):
        
        super().info()
    
        print(f"Número de puertas: {self.num_puertas}")


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, precio, cilindrada):
        super().__init__(marca, modelo, año, precio)
        self.cilindrada = cilindrada

    def info (self):
       
        super().info()
        
        print(f"Cilindrada: {self.cilindrada} cc")

# Crear instancias de los vehículos
auto = Automovil("Nissan", "Centra", 2025,400000, 4)
moto = Motocicleta("Vento", "Crossmax", 2025, 34000, 689)

# Mostrar la información de los vehículos
print("Información del Automóvil:")
auto.info()
print("\nInformación de la Motocicleta:")
moto.info()
