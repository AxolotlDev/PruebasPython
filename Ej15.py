#Ejercicio 15
#Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. Ejemplo, si se introduce 23 que muestre 32.

n1 = int(input("Ingrese un numero de dos cifras: "))
n1 = int(str(n1)[::-1])#Convierto el numero a String, invierto el orden de la cadena con "[::-1]" y luego vuelvo a pasarlo a int.
print(n1)