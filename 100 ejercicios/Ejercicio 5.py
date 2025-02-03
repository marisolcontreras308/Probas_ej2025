#Verificar si un número es primo
num=int(input('Ingresa un número'))
if num <= 1:
    print('No es un número primo')
else:
    
    es_primo = True
    
    for i in range(2, num):  
        if num % i == 0:
            es_primo = False  
            break 

    if es_primo:
        print('Es un número primo')
    else:
        print('No es un número primo')