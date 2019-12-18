#Ejercicio 4
#Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.
import math

a = int(input("Ingrese primer numero: "))
b = int(input("Ingrese segundo numero: "))
sum = (a+b)
rest = (a-b)
mult= (a*b)
div = (a/b)
rest = (a%b)
pot = math.pow(a,b)
print(f"Siendo {a} y {b} los numeros elegidos, poniendolos en orden respectivamente, se obtienen los siguientes resultados" + '\n' + f"Suma {sum}" + "\n" + f"Resta {rest}" + "\n" + f"Multiplicacion {mult}" + "\n" + f"Division {div}" + "\n" + f"Resto {rest}")