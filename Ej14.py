#Ejercicio 14
#Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.

a = float(input("Ingrese el numero 1 : "))
b = float(input("Ingrese el numero 2 : "))
a, b = b, a #Intercambia los valores respectivamente.
print(f" Los valores son Numero 1: {a} y Numero 2: {b}")
