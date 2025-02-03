#Secuencia Fibonacci
a=int(0)
b=int(1)
rango=int(input('¿Cuántos términos desea generar?: '))
secuencia=[0]*rango
for i in range (rango):
    secuencia[i]=a
    temp=a
    a=b
    b=temp+b

print(secuencia)
