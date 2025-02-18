#Par, impar o múltiplo
num=int(input("Ingrese un número: "))
if num%2 == 0:
    print('El número es par')
else:
    print ('El número es impar')
rango=num
multiplos=[]
for i in range(1,rango+1):
    if num% i ==0 :
        multiplos.append(i)
print(num, 'es múltiplo de:',multiplos)