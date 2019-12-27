#Ejercicio 1
#Algoritmo que pida dos números e indique si el primero es mayor que el segundo o no.
print("El programa evaluara si el primer numero ingresado es mayor al segundo.")
n1 = float(input("Ingrese el primer numero: "))
n2 = float(input("Ingrese el segundo numero: "))
if n1> n2:
	print("El primer numero es mayor.")
elif n1==n2:
	print("Ambos numeros son iguales.")
else:
	print("El segundo numero es mayor que el primero.")
	