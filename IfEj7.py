#Ejercicio 7
#Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente.
import math

n = float(input("Ingrese un numero: "))
p = float(input("Ingrese la potencia a la cual sera elevado el numero: "))
r = 0
if p == 0:
	r = 1
elif p < 0:
	r = pow(n,(1/abs(p)))
else:
	r = pow(n,p)
print(f"El resultado es {r}")