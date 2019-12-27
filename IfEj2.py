#Ejercicio 2
#Algoritmo que pida un número y diga si es positivo, negativo o 0.

print("El programa evaluara si el numero ingresado es menor, mayor, o igual a 0.")
n1 = float(input("Ingrese el numero: "))
if n1> 0:
	print("El numero es mayor a 0.")
elif n1==0:
	print("El numero es igual a 0.")
else:
	print("El numero es menor a 0 (negativo).")