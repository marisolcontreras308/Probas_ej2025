a = int(input("Introduce el primer término de la serie (a): "))
d = int(input("Introduce la diferencia común entre los términos (d): "))
n = int(input("Introduce el número de términos (n): "))


Suma = (n / 2) * (2 * a + (n - 1) * d)

print("La suma de los primeros",n,"términos de la serie es" ,Suma)