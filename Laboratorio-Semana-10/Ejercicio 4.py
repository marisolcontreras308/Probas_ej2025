#Calculadora de estadísticas
import math


def calculo(*args):
   
    def promedio(nums):
        return sum(nums) / len(nums)

    def mediana(nums):
        sorted_nums = sorted(nums)
        n = len(sorted_nums)
        if n % 2 == 0:
            return (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2
        else:
            return sorted_nums[n // 2]


    def desviacionEstandar(nums, mean):
        return math.sqrt(sum((x - mean) ** 2 for x in nums) / len(nums))

    media = promedio(args)
    median = mediana(args)
    de = desviacionEstandar(args, media)

    return {'Promedio': media,'Mediana': median,'Desviación estándar': de}

numeros = list(map(float, input("Ingrese una lista de números separados por espacio: ").split()))


resultados = calculo(*numeros)


print("Resultados:")
print(f"Promedio: {resultados['Promedio']}")
print(f"Mediana: {resultados['Mediana']}")
print(f"Desviación estándar: {resultados['Desviación estándar']}")
