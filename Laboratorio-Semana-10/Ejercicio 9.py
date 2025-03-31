#Implementación de múltiples paradigmas


# Paradigma Imperativo:
# Usamos estructuras de control como bucles y condicionales directamente en el bloque principal.
def ejecuta_paradigma_imperativo():
    print("Paradigma Imperativo:")
    suma = 0
    for i in range(1, 6): 
        suma += i
    print("Suma de los primeros 5 números:", suma)

    if suma > 10: 
        print("La suma es mayor que 10.")
    else:
        print("La suma es menor o igual a 10.")

# Paradigma Estructurado:
# Funciones definidas para cálculos.
def ejecuta_paradigma_estructurado():
    print("\nParadigma Estructurado:")
    a = 10
    b = 5
    resultado_suma = sumar(a, b)  
    resultado_resta = restar(a, b) 
    print(f"La suma de {a} y {b} es: {resultado_suma}")
    print(f"La resta de {a} y {b} es: {resultado_resta}")

# Funciones para el paradigma estructurado
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

# Paradigma Modular:
# Aquí no usamos un módulo separado, sino que definimos todo en el mismo archivo.
def ejecuta_paradigma_modular():
    print("\nParadigma Modular:")
    a = 20
    b = 10
    suma = sumar(a, b)
    resta = restar(a, b)
    print(f"Suma (modular): {a} + {b} = {suma}")
    print(f"Resta (modular): {a} - {b} = {resta}")

# Paradigma Orientado a Objetos:
# Definimos clases y objetos en este paradigma.
class Calculadora:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    def suma(self):
        return self.valor1 + self.valor2

    def resta(self):
        return self.valor1 - self.valor2

    def multiplicar(self):
        return self.valor1 * self.valor2

    def dividir(self):
        if self.valor2 != 0:
            return self.valor1 / self.valor2
        else:
            return "Error: División por cero"

def ejecuta_paradigma_orientado_a_objetos():
    print("\nParadigma Orientado a Objetos:")
    calc = Calculadora(15, 5)  
    print("Suma (OOP):", calc.suma())
    print("Resta (OOP):", calc.resta())
    print("Multiplicación (OOP):", calc.multiplicar())
    print("División (OOP):", calc.dividir())

# Ejecución de todos los paradigmas
def ejecutar_programa():
    ejecuta_paradigma_imperativo()
    ejecuta_paradigma_estructurado()
    ejecuta_paradigma_modular()
    ejecuta_paradigma_orientado_a_objetos()

# Llamamos a la función que ejecutará todos los paradigmas
if __name__ == "__main__":
    ejecutar_programa()
