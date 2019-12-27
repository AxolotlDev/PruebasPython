#Ejercicio 3
#Escribe un programa que lea un número e indique si es par o impar.
print("El programa evaluara si el numero ingresado es par o impar.")
n1 = int(input("Ingrese el numero: "))
rest = n1%2
if rest==0:
	print("El numero es par.")
else:
	print("El numero es impar.")
